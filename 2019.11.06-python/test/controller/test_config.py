import unittest

from src.controller import config


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.client = config.app.test_client()
        self.response = self.client.get('/')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se a nossa home retorna a string "ok"
    def test_html_string_response(self):
        self.assertEqual("Server talk scheduling up", self.response.data.decode('utf-8'))

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)


if __name__ == '__main__':
    unittest.main()
