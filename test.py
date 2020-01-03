import main
import unittest

class MyTestCalculator(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        

        def test_subint(self):
            rv =  self.app.get('/sub?A=2&B=5')
            self.assertEqual(b'-3.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_subfloat(self):
            rv =  self.app.get('/sub?A=2.3&B=3.3')
            self.assertEqual(b'-1.0', rv.data)
        def test_subfraction(self):
            rv =  self.app.get('/sub?A=2/3&B=3/3')
            self.assertNotEqual(b'-0.333', rv.data)
        def test_subnegativeinteger(self):
            rv =  self.app.get('/sub?A=2.3&B=-3.3')
            self.assertEqual(b'5.6', rv.data)

        

if __name__ == '__main__':
    unittest.main()
