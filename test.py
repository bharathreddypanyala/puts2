import main
import unittest

class MyTestCalculator(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            rv =  self.app.get('/add?A=2&B=5')
            self.assertEqual(b'7.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_addfloat(self):
            rv =  self.app.get('/add?A=2.3&B=3.3')
            self.assertEqual(b'5.6',rv.data)
        def test_addfraction(self):
            rv =  self.app.get('/add?A=2/3&B=3/3')
            self.assertNotEqual(b'1.667',rv.data)
        def test_addnegativeint(self):
            rv =  self.app.get('/add?A=2.3&B=-3.3')
            self.assertEqual(b'-1.0', rv.data)


if __name__ == '__main__':
    unittest.main()
