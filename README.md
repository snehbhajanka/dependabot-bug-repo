# Dependabot Vulnerability Test Repository

This repository contains intentionally vulnerable mail handling applications to demonstrate Dependabot's security alert capabilities. The applications use outdated versions of popular libraries with known security vulnerabilities.

## ⚠️ Security Notice

**This repository contains intentionally vulnerable dependencies for testing purposes only. Do not use this code in production environments.**

## Applications

### 1. Python Mail Handler (`mail_handler.py`)

A Python-based email processing application using Flask that demonstrates:
- Email sending via SMTP
- Template processing with Jinja2
- External API data fetching with requests
- Image processing for email attachments
- Flask web endpoints for mail operations

**Key vulnerable dependencies:**
- `requests==2.25.1` - HTTP library with known vulnerabilities
- `Jinja2==2.11.3` - Template engine with XSS vulnerabilities  
- `Flask==1.1.4` - Web framework with security issues
- `urllib3==1.26.4` - HTTP client with vulnerabilities
- `Pillow==8.1.2` - Image processing library with security flaws

### 2. Node.js Mail Service (`mail_service.js`)

A Node.js/Express-based mail service that provides:
- RESTful API for email operations
- File upload handling for attachments
- Template processing with lodash
- External data fetching with axios
- CORS and security middleware

**Key vulnerable dependencies:**
- `axios==0.21.1` - HTTP client with security vulnerabilities
- `lodash==4.17.19` - Utility library with prototype pollution issues
- `express==4.17.1` - Web framework with known security issues
- `multer==1.4.2` - File upload middleware with vulnerabilities

## Usage

### Python Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run demo
python mail_handler.py

# Run Flask server
python mail_handler.py server
```

### Node.js Application

```bash
# Install dependencies
npm install

# Run the service
npm start

# Run in development mode
npm run dev
```

## API Endpoints

### Python Flask Server (Port 5000)

- `POST /send_mail` - Send emails
- `POST /process_template` - Process email templates
- `GET /fetch_mail_data?url=<url>` - Fetch external email data

### Node.js Express Server (Port 3000)

- `POST /api/send-email` - Send emails
- `POST /api/process-template` - Process email templates
- `GET /api/fetch-data?url=<url>` - Fetch external data
- `POST /api/upload-attachment` - Upload email attachments
- `GET /health` - Health check
- `GET /api/info` - Service information

## Dependabot Configuration

Dependabot is configured via `.github/dependabot.yml` to monitor both Python (`pip`) and Node.js (`npm`) dependencies daily. It will automatically create pull requests for vulnerable package updates.

## Expected Vulnerabilities

This repository should trigger Dependabot alerts for various CVEs including but not limited to:
- CVE-2021-33503 (urllib3)
- CVE-2021-23337 (lodash)  
- CVE-2021-32052 (Django - if added)
- Various prototype pollution and XSS vulnerabilities

## License

ISC - For testing purposes only