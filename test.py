import main
import unittest

class MyTestCalculator(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        

        def test_divint(self):
            rv =  self.app.get('/div?A=2&B=5')
            self.assertEqual(b'0.4', rv.data)
            self.assertNotEqual(b'0.0256',rv.data)
        def test_divfloat(self):
            rv =  self.app.get('/div?A=2.3&B=3.3')
            self.assertEqual(b'0.697', rv.data)
        def test_divfraction(self):
            rv =  self.app.get('/div?A=2/3&B=3/3')
            self.assertNotEqual(b'0.667', rv.data)
        def test_divnegativeinteger(self):
            rv =  self.app.get('/div?A=2.3&B=-3.3')
            self.assertEqual(b'-0.697', rv.data)
        def test_zerodiv(self):
            rv = self.app.get('/div?A=1/0&B=1')
            self.assertEqual(b'None',rv.data)

if __name__ == '__main__':
    unittest.main()
