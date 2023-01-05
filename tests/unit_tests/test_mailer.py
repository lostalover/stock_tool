import unittest
from src.batch.mailer.smtp_mailer import SmtpMailer, Host


class TestMailer(unittest.TestCase):
    def setUp(self):
        self.mailer = SmtpMailer(Host.OUTLOOK, "rabbit_trader@outlook.com", "foqltxmfpdlej1!@")

    def test_connect(self):
        is_success1 = self.mailer.connect()
        is_success2 = self.mailer.connect()
        self.assertTrue(is_success1)
        self.assertFalse(is_success2)

    def test_send(self):
        success = self.mailer.send("rabbit_trader@outlook.com", "title", "message body")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()
