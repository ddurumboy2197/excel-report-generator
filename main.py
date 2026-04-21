import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from logging.handlers import RotatingFileHandler

# Error Reporting to File + Email
class ErrorReporter:
    def __init__(self, email, password, recipient):
        self.email = email
        self.password = password
        self.recipient = recipient

    def send_email(self, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.recipient
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, self.recipient, text)
        server.quit()

    def log_to_file(self, message):
        logger = logging.getLogger('error_logger')
        logger.setLevel(logging.ERROR)

        handler = RotatingFileHandler('error.log', maxBytes=1000000, backupCount=5)
        handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.error(message)

def main():
    email = 'your_email@gmail.com'
    password = 'your_password'
    recipient = 'recipient_email@gmail.com'

    reporter = ErrorReporter(email, password, recipient)

    try:
        # Simulate an error
        x = 1 / 0
    except Exception as e:
        reporter.log_to_file(str(e))
        reporter.send_email('Error Report', str(e))

if __name__ == '__main__':
    main()
```

Kodda quyidagilar mavjud:

1. `ErrorReporter` klassi: bu klass email va logga xatoliklar yuborish uchun mo'ljallangan.
2. `send_email` metodi: bu metod emailga xatoliklar yuborish uchun mo'ljallangan.
3. `log_to_file` metodi: bu metod logga xatoliklar yuborish uchun mo'ljallangan.
4. `main` funksiyasi: bu funksiyada xatolikni simulyatsiya qilish uchun mo'ljallangan.
5. `if __name__ == '__main__':` qismi: bu qismda kodni boshlash uchun mo'ljallangan.
