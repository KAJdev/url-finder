import url_finder
import unittest

class Test(unittest.TestCase):
    def test_no_url(self):
        self.assertEqual(url_finder.get_urls("Hello World"), [])
    
    def test_one_url(self):
        self.assertEqual(url_finder.get_urls("Hello World http://www.google.com"), ["http://www.google.com"])

    def test_two_url(self):
        self.assertEqual(url_finder.get_urls("Hello World http://www.google.com http://www.yahoo.com"), ["http://www.google.com", "http://www.yahoo.com"])

    def test_three_url(self):
        self.assertEqual(url_finder.get_urls(
            "Hello World http://www.google.com http://www.yahoo.com http://www.cnn.com"),
            ["http://www.google.com", "http://www.yahoo.com", "http://www.cnn.com"]
        )

    def test_close_url(self):
        self.assertEqual(url_finder.get_urls("Hello World https://test.test.com/ http://www.google.com/"), ["https://test.test.com", "http://www.google.com"])

    def test_newline_url(self):
        self.assertEqual(url_finder.get_urls("Hello World https://test.test.com/\nhttp://www.google.com/"), ["https://test.test.com", "http://www.google.com"])

    def test_real_message(self):
        self.assertEqual(url_finder.get_urls(
            "bigbeans.solutions is false positive. it's owned by discord, and redirects to https://sex.com b bigbeans.solutions example.com skefjnsknjef.com ksjefksjnef.com"),
            ["https://bigbeans.solutions", "https://sex.com", "https://bigbeans.solutions", "https://example.com", "https://skefjnsknjef.com", "https://ksjefksjnef.com"])

if __name__ == '__main__':
    unittest.main()

