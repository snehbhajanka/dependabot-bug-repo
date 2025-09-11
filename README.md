# Simple Mail Handler Service

A basic Python-based email processing service built with Flask. This service provides functionality for sending emails, processing templates, and handling email-related operations through a web API.

## Features

- **Email Sending**: Send emails via SMTP with authentication support
- **Template Processing**: Dynamic email content using Jinja2 templates
- **External Data Integration**: Fetch data from external APIs for email content
- **Image Processing**: Basic image handling for email attachments
- **REST API**: Simple HTTP endpoints for all mail operations

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage

### Run Demo
```bash
python mail_handler.py
```

### Start Web Server
```bash
python mail_handler.py server
```

The server will start on `http://localhost:5000`

## API Endpoints

- `POST /send_mail` - Send emails
- `POST /process_template` - Process email templates with dynamic content
- `GET /fetch_mail_data?url=<url>` - Fetch external data for emails

## Example Usage

### Send an Email
```bash
curl -X POST http://localhost:5000/send_mail \
  -H "Content-Type: application/json" \
  -d '{
    "from": "sender@example.com",
    "to": "recipient@example.com", 
    "subject": "Test Email",
    "body": "Hello, this is a test email!"
  }'
```

### Process a Template
```bash
curl -X POST http://localhost:5000/process_template \
  -H "Content-Type: application/json" \
  -d '{
    "template": "Hello {{name}}, welcome to {{service}}!",
    "context": {
      "name": "John",
      "service": "Mail Handler"
    }
  }'
```

## Dependencies

- **Flask**: Web framework for the REST API (≥3.0.2 for security)
- **Jinja2**: Template engine for dynamic email content (≥3.1.2)
- **requests**: HTTP library for external API calls (≥2.25.1)

## Security

This project uses Flask ≥3.0.2 which includes fixes for:
- CVE-2023-30861: Flask session cookie disclosure vulnerability due to missing Vary: Cookie header

## License

ISC