import unittest
from src.batch.mailer.smtp_mailer import SmtpReportPublisher


class TestMailer(unittest.TestCase):
    def setUp(self):
        self.mailer = SmtpReportPublisher(SmtpReportPublisher.OUTLOOK,
                                          "rabbit_trader@outlook.com",
                                          "foqltxmfpdlej1!@")

    def test_connect(self):
        is_success1 = self.mailer._connect()
        is_success2 = self.mailer._connect()
        self.assertTrue(is_success1)
        self.assertFalse(is_success2)

    def test_send(self):
        success = self.mailer.send("rabbit_trader@outlook.com", "title", "message body")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()
