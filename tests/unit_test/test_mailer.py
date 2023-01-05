import unittest
from src.batch.mailer.smtp_mailer import SmtpMailer, Host


class TestMailer(unittest.TestCase):
    def setUp(self):
        self.mailer = SmtpMailer(Host.GOOGLE, "seungminyi95@gmail.com", "rrcbtegenmfxonko")

    def test_connect(self):
        is_success1 = self.mailer.connect()
        is_success2 = self.mailer.connect()
        self.assertTrue(is_success1)
        self.assertFalse(is_success2)

    def test_send(self):
        success = self.mailer.send("seungminyi95@gmail.com", "title", "body")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()
