import unittest
from unittest.mock import MagicMock, Mock

from src.controller import scheduling, config


class SchedulingTest(unittest.TestCase):
    def setUp(self):
        self.scheduling = scheduling
        mock = Mock()
        mock.total.return_value = 3
        self.scheduling.Service = mock

        self.client = config.app.test_client()
        self.response_get = self.client.get('/api/scheduling')

    def test_get(self):
        """ Check response of get scheduling is 200 ok """
        self.assertEqual(200, self.response_get.status_code)

    def test_json_response(self):
        """ Check response json result object, the get call request  """
        json_data = self.response_get.get_json()
        print(json_data)
        assert 'teste' in json_data
        self.assertEqual(3, json_data['teste'])
        # assert 3 in json_data['teste']

    def test_content_type(self):
        """ Check content type, the get call request """
        self.assertIn('application/json', self.response_get.content_type)


if __name__ == '__main__':
    unittest.main()
