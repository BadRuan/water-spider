from unittest import TestCase
from utils.config_loader import Config


class TestLoadConfig(TestCase):

    def test_load_config(self):
        config = Config("dev").value
        self.assertEqual(config["mode"], "dev")
