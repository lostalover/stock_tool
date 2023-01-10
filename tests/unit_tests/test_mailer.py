import unittest
from unittest.mock import patch
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
        with patch("smtplib.SMTP") as smtp:
            instance = smtp.return_value

            to_address = "rabbit_trader@outlook.com"
            success = self.mailer.send(to_address, "title", "message body")

            self.assertTrue(success)
            self.assertTrue(instance.sendmail.called)
            self.assertEqual(instance.sendmail.call_count, 1)
            self.assertEqual(instance.sendmail.mock_calls[0][1][0],
                             self.mailer.username)
            self.assertEqual(instance.sendmail.mock_calls[0][1][1], to_address)
