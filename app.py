from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from src.services.service import send_email,get_emails
app = Flask(__name__)

# Set your Outlook email credentials
outlook_email = "adm@dhyey.com"
outlook_password = "Gay84688"

# API to send an email
@app.route('/send_email', methods=['POST'])
def api_send_email():
    data = request.get_json()
    subject = data.get('subject')
    message = data.get('message')
    to_email = data.get('to_email')

    if not (subject and message and to_email):
        return jsonify({"status": "error", "message": "Missing required parameters."}), 400

    result = send_email(subject, message, to_email)
    return jsonify(result)

# API to get emails (dummy implementation)
# API to get emails
@app.route('/get_emails', methods=['GET'])
def api_get_emails():
    result = get_emails()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
