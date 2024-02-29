import smtplib
import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
from email.parser import BytesParser
from email.mime.text import MIMEText
# Set your Outlook email credentials
outlook_email = "adm@dhyey.com"
outlook_password = "Gay84688"

# Function to send an email
def send_email(subject, message, to_email):
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(outlook_email, outlook_password)

            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = outlook_email
            msg["To"] = to_email

            server.sendmail(outlook_email, to_email, msg.as_string())
            return {"status": "success", "message": "Email sent successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Error sending email: {e}"}

    
# Function to get emails using IMAP
def get_emails():
    try:
        mail = imaplib.IMAP4_SSL("outlook.office365.com")
        mail.login(outlook_email, outlook_password)
        mail.select("inbox")

        _, data = mail.search(None, "ALL")
        email_ids = data[0].split()

        emails = []
        for email_id in email_ids:
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            msg = BytesParser().parsebytes(msg_data[0][1])
            
            email_info = {
                "subject": decode_header(msg["Subject"])[0][0],
                "from": msg["From"],
                "date": parsedate_to_datetime(msg["Date"]).strftime("%Y-%m-%d %H:%M:%S")
            }

            emails.append(email_info)

        mail.logout()
        return {"status": "success", "emails": emails}
    except Exception as e:
        return {"status": "error", "message": f"Error retrieving emails: {e}"}