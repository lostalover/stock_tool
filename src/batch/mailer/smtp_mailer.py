from collections import namedtuple
import smtplib
from email.mime.text import MIMEText


class SmtpReportPublisher():
    _END_POINT = namedtuple("EndPoint", "host port")
    GOOGLE = _END_POINT("smtp.gmail.com", 587)
    LIVE = _END_POINT("smtp.live.com", 587)
    OUTLOOK = _END_POINT("smtp.office365.com", 587)

    def __init__(self, end_point: _END_POINT, username: str, password: str):
        self.smtp = None
        self.host = end_point.host
        self.port = end_point.port
        self.username = username
        self.password = password

    def _connect(self) -> bool:
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
            self._connect()
        from_addr = self.username
        self.smtp.sendmail(from_addr, to_addr, msg.as_string())
        return True

    def __del__(self):
        if self.smtp:
            self.smtp.quit()
