/**
 * Node.js Mail Service
 * A mail handling service built with Node.js using various third-party libraries
 * This application demonstrates email processing, template rendering, and API integration
 */

const express = require('express');
const nodemailer = require('nodemailer');
const axios = require('axios');
const _ = require('lodash');
const helmet = require('helmet');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));
app.use(helmet());
app.use(cors());

// File upload configuration
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadDir = './uploads';
        if (!fs.existsSync(uploadDir)) {
            fs.mkdirSync(uploadDir);
        }
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + '-' + file.originalname);
    }
});

const upload = multer({ storage: storage });

class MailService {
    constructor() {
        this.transporter = null;
        this.setupTransporter();
    }

    setupTransporter() {
        // Setup nodemailer transporter (configuration would come from env vars in production)
        this.transporter = nodemailer.createTransporter({
            host: process.env.SMTP_HOST || 'localhost',
            port: process.env.SMTP_PORT || 587,
            secure: false,
            auth: {
                user: process.env.SMTP_USER || '',
                pass: process.env.SMTP_PASS || ''
            }
        });
    }

    async sendEmail(emailData) {
        try {
            const mailOptions = {
                from: emailData.from,
                to: emailData.to,
                subject: emailData.subject,
                text: emailData.text,
                html: emailData.html,
                attachments: emailData.attachments || []
            };

            const result = await this.transporter.sendMail(mailOptions);
            return { success: true, messageId: result.messageId };
        } catch (error) {
            console.error('Email sending failed:', error);
            return { success: false, error: error.message };
        }
    }

    processTemplate(template, data) {
        // Simple template processing using lodash template
        const compiled = _.template(template);
        return compiled(data);
    }

    async fetchExternalData(url) {
        try {
            const response = await axios.get(url, {
                timeout: 5000,
                headers: {
                    'User-Agent': 'MailService/1.0'
                }
            });
            return response.data;
        } catch (error) {
            console.error('Failed to fetch external data:', error.message);
            throw new Error('External data fetch failed');
        }
    }

    validateEmailData(data) {
        const required = ['from', 'to', 'subject'];
        const missing = required.filter(field => !data[field]);
        
        if (missing.length > 0) {
            throw new Error(`Missing required fields: ${missing.join(', ')}`);
        }

        // Email validation using lodash
        if (!_.isString(data.from) || !data.from.includes('@')) {
            throw new Error('Invalid from email address');
        }

        if (!_.isString(data.to) || !data.to.includes('@')) {
            throw new Error('Invalid to email address');
        }

        return true;
    }
}

const mailService = new MailService();

// API Routes

/**
 * Send email endpoint
 */
app.post('/api/send-email', async (req, res) => {
    try {
        mailService.validateEmailData(req.body);
        const result = await mailService.sendEmail(req.body);
        
        if (result.success) {
            res.json({ 
                message: 'Email sent successfully', 
                messageId: result.messageId 
            });
        } else {
            res.status(500).json({ error: result.error });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

/**
 * Process email template endpoint
 */
app.post('/api/process-template', (req, res) => {
    try {
        const { template, data } = req.body;
        
        if (!template) {
            return res.status(400).json({ error: 'Template is required' });
        }

        const processed = mailService.processTemplate(template, data || {});
        res.json({ processedTemplate: processed });
    } catch (error) {
        res.status(500).json({ error: 'Template processing failed' });
    }
});

/**
 * Fetch external email data endpoint
 */
app.get('/api/fetch-data', async (req, res) => {
    try {
        const { url } = req.query;
        
        if (!url) {
            return res.status(400).json({ error: 'URL parameter is required' });
        }

        const data = await mailService.fetchExternalData(url);
        res.json({ data: data });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * Upload email attachment endpoint
 */
app.post('/api/upload-attachment', upload.single('attachment'), (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({ error: 'No file uploaded' });
        }

        const fileInfo = {
            filename: req.file.filename,
            originalName: req.file.originalname,
            size: req.file.size,
            mimetype: req.file.mimetype,
            path: req.file.path
        };

        res.json({ 
            message: 'File uploaded successfully', 
            file: fileInfo 
        });
    } catch (error) {
        res.status(500).json({ error: 'File upload failed' });
    }
});

/**
 * Health check endpoint
 */
app.get('/health', (req, res) => {
    res.json({ 
        status: 'OK', 
        timestamp: new Date().toISOString(),
        service: 'Mail Service'
    });
});

/**
 * Get service info endpoint
 */
app.get('/api/info', (req, res) => {
    res.json({
        service: 'Node.js Mail Service',
        version: '1.0.0',
        endpoints: [
            'POST /api/send-email',
            'POST /api/process-template', 
            'GET /api/fetch-data',
            'POST /api/upload-attachment',
            'GET /health'
        ]
    });
});

// Error handling middleware
app.use((error, req, res, next) => {
    console.error('Unhandled error:', error);
    res.status(500).json({ error: 'Internal server error' });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Mail Service running on port ${PORT}`);
    console.log(`Health check available at: http://localhost:${PORT}/health`);
    console.log(`API info available at: http://localhost:${PORT}/api/info`);
});

module.exports = app;