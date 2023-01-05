from enum import Enum
import smtplib
from email.mime.text import MIMEText


class Host(Enum):
    GOOGLE = ("smtp.gmail.com", 587)
    LIVE = ("smtp.live.com", 587)
    OUTLOOK = ("smtp.office365.com", 587)


class SmtpMailer():
    def __init__(self, host: Host, username: str, password: str = ''):
        self.smtp = None
        self.host = host.value[0]
        self.port = host.value[1]
        self.username = username
        self.password = password

    def connect(self) -> bool:
        if self.smtp:
            return False
        self.smtp = smtplib.SMTP(self.host, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.username, self.password)
        return True

    def send(self, to_addr: str, title: str, body: str) -> bool:
        msg = MIMEText(body.encode('utf-8'), 'html', 'utf-8')
        msg['Subject'] = title
        msg['To'] = to_addr
        msg['From'] = self.username
        if self.smtp is None:
            self.connect()
        from_addr = self.username
        self.smtp.sendmail(from_addr, to_addr, msg.as_string())
        return True

    def __del__(self):
        if self.smtp:
            self.smtp.quit()
