import main
import unittest

class MyTestCalculator(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        

        def test_mulint(self):
            rv =  self.app.get('/mul?A=2&B=5')
            self.assertEqual(b'10.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=2.3&B=3.3')
            self.assertEqual(b'7.59', rv.data)
        def test_mulfraction(self):
            rv =  self.app.get('/mul?A=2/3&B=3/3')
            self.assertNotEqual(b'0.667', rv.data)
        def test_mulnegativeinteger(self):
            rv =  self.app.get('/mul?A=2.3&B=-3.3')
            self.assertEqual(b'-7.59', rv.data)

        

if __name__ == '__main__':
    unittest.main()
