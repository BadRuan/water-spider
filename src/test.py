from test.tdenginetool import TestTDengineTool
import unittest


if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suit = test_loader.loadTestsFromTestCase(TestTDengineTool)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suit)
