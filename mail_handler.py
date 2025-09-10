#!/usr/bin/env python3
"""
Simple Mail Handler Service
A basic email processing and sending service for web applications.
"""

import smtplib
import email
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Third-party imports
import requests
from jinja2 import Template
from flask import Flask, request, jsonify

app = Flask(__name__)

class MailHandler:
    """Handles email operations including sending, processing, and templating."""
    
    def __init__(self, smtp_server='localhost', smtp_port=587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        
    def send_email(self, from_addr, to_addr, subject, body, smtp_user=None, smtp_pass=None):
        """Send an email using SMTP."""
        try:
            msg = MIMEMultipart()
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            
            text = msg.as_string()
            server.sendmail(from_addr, to_addr, text)
            server.quit()
            
            return {"status": "success", "message": "Email sent successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def process_template(self, template_string, context):
        """Process email template using Jinja2."""
        template = Template(template_string)
        return template.render(**context)
    
    def fetch_email_data(self, url):
        """Fetch email data from external API."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def process_email_attachment(self, file_path):
        """Process email attachments (basic file handling)."""
        try:
            # Basic file processing - just verify file exists and get size
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                return {
                    "processed": True,
                    "file_path": file_path,
                    "size": file_size
                }
            return {"processed": False, "error": "File not found"}
        except Exception as e:
            return {"processed": False, "error": str(e)}

@app.route('/send_mail', methods=['POST'])
def send_mail_endpoint():
    """Flask endpoint to send emails via POST request."""
    data = request.get_json()
    
    if not data or not all(k in data for k in ['from', 'to', 'subject', 'body']):
        return jsonify({"error": "Missing required fields"}), 400
    
    mail_handler = MailHandler()
    result = mail_handler.send_email(
        data['from'], 
        data['to'], 
        data['subject'], 
        data['body'],
        data.get('smtp_user'),
        data.get('smtp_pass')
    )
    
    return jsonify(result)

@app.route('/process_template', methods=['POST'])
def process_template_endpoint():
    """Flask endpoint to process email templates."""
    data = request.get_json()
    
    if not data or 'template' not in data:
        return jsonify({"error": "Missing template"}), 400
    
    mail_handler = MailHandler()
    context = data.get('context', {})
    
    try:
        processed = mail_handler.process_template(data['template'], context)
        return jsonify({"processed_template": processed})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fetch_mail_data', methods=['GET'])
def fetch_mail_data_endpoint():
    """Flask endpoint to fetch email data from external sources."""
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400
    
    mail_handler = MailHandler()
    data = mail_handler.fetch_email_data(url)
    
    return jsonify(data)

def main():
    """Main function to demonstrate mail handling capabilities."""
    print("Simple Mail Handler Service")
    print("===========================")
    
    # Initialize mail handler
    mail_handler = MailHandler()
    
    # Example template processing
    template = "Hello {{name}}, your order #{{order_id}} has been {{status}}."
    context = {
        "name": "John Doe",
        "order_id": "12345",
        "status": "shipped"
    }
    
    processed_email = mail_handler.process_template(template, context)
    print(f"Processed template: {processed_email}")
    
    print("\nMail service ready. Run 'python mail_handler.py server' to start web server.")
    print("Available endpoints:")
    print("  POST /send_mail - Send emails")
    print("  POST /process_template - Process email templates")
    print("  GET /fetch_mail_data?url=<url> - Fetch external email data")

if __name__ == "__main__":
    if len(os.sys.argv) > 1 and os.sys.argv[1] == "server":
        # Run Flask development server
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        # Run demo
        main()