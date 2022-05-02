import unittest
from app.models import sources

Source = sources.Source

class sourceTest(unittest.TestCase):
    """To test the behaviour of the source class"""
    
    def setUp(self):
        self.new_source = Source('source_1','myNews','all the news worldwide', 'http://source.com')
        
    def test_source_instance(self):
        self.assertTrue(source_instance(self.new_source, Source))
        
if __name__ == '__main__':
    unittest.main()