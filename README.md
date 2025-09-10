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

- **Flask**: Web framework for the REST API
- **Jinja2**: Template engine for dynamic email content
- **requests**: HTTP library for external API calls
- **Pillow**: Image processing for email attachments

## License

ISC