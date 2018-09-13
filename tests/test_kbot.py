import unittest
import kbot.py

class TestSlackbot(unittest.TestCase):

    def test_auth(self):
        self.assertEqual(slack_client.api_call("auth.test").get("ok"), True)


    def test_handle_command('choc','DCR9ET3FD'):
        self.assertTrue(':choclate:')


if __name__ == '__main__':
    unittest.main()