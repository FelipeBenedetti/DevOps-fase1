import unittest
import sys
import os


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from app import app  


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        """Testa se o endpoint de saúde retorna status 200 e informações corretas."""
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["version"], "1.0.0")

    def test_home_endpoint(self):
        """Testa se o endpoint principal retorna status 200 e mensagem de boas-vindas."""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("endpoints", data)


if __name__ == "__main__":
    unittest.main()
