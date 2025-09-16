# Fake SMTP Server for Credential Capture (PASSBACK HACK)

A Python-based fake SMTP server designed to capture and decode SMTP credentials during security testing, specifically useful for demonstrating passback attacks against network devices like printers.

## Overview

This Python script creates a fake SMTP server that listens on port 587 and captures authentication credentials sent by clients. It's particularly useful for demonstrating SMTP passback attacks where devices like printers are configured to use malicious SMTP servers, allowing attackers to capture credentials in base64 format and decode them to plain text.

## Features

- Listens on SMTP port 587 for incoming connections
- Handles standard SMTP commands (HELO, EHLO, AUTH, MAIL FROM, RCPT TO, DATA, QUIT)
- Captures and automatically decodes base64-encoded credentials
- Supports both LOGIN and PLAIN authentication methods
- Displays email content sent through the server
- Properly handles SMTP command sequences and responses

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.x installed
3. No additional dependencies required (uses only standard library modules)

## Usage

1. Run the script with Python:
2. The server will start listening on all interfaces (0.0.0.0) on port 587:
[+] Fake SMTP Server listening on port 587...
3. Configure a device (like a printer) to use your machine's IP address as the SMTP server
4. When the device attempts to send email, the server will capture and display the credentials:
[+]  Connection received from: ('192.168.1.100', 51234)
CLIENT: EHLO printer.example.com
CLIENT: AUTH LOGIN
AUTH User: dXNlcm5hbWU= -> username
AUTH Pass: cGFzc3dvcmQ= -> password



## How It Works

The script mimics a real SMTP server by:
1. Responding to SMTP commands with appropriate responses
2. Sending base64-encoded challenges for authentication (Username: and Password:)
3. Capturing the base64-encoded credentials from the client
4. Decoding them to plain text using Python's base64 module
5. Displaying both the encoded and decoded values for analysis

## Disclaimer

**This tool is provided for educational and security testing purposes only. The author is not responsible for any misuse or damage caused by this program. Always ensure you have proper authorization before testing any network or system.**

- Use only on networks you own or have explicit permission to test
- Do not use this tool for any malicious activities
- Understanding attack techniques helps in building better defenses
- Compliance with local laws and regulations is your responsibility

## Responsible Use

This tool is intended for:
- Security professionals testing their own systems
- Educational demonstrations of SMTP security vulnerabilities
- Penetration testing with proper authorization
- Research purposes in controlled environments

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Example Output
[+] Fake SMTP Server listening on port 587...
[+] Connection received from: ('192.168.1.50', 49162)  
CLIENT: EHLO OfficeJet-Pro-8500  
CLIENT: AUTH LOGIN  
AUTH User: YWRtaW5pc3RyYXRvcg== -> administrator  
AUTH Pass: UCFzNHcwcmQxMjM= -> Ps4w0rd123  
CLIENT: MAIL FROM:printer@office.local  
CLIENT: RCPT TO:admin@company.com  
CLIENT: DATA  
EMAIL DATA:  
Subject: Toner Low Alert
