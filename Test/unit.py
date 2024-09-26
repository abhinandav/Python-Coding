import unittest

def sum(a,b):
    return a+b


class TestClass(unittest.TestCase):
    def setUp(self):
        print('setup called')
        self.a=10
        self.b=20
    def test_fn1(self):
        print('test1 called')
        #Arrange 
        # a=10
        # b=20

        #Act
        result=sum(self.a,self.b)

        #Assert
        self.assertEqual(result,self.a+self.b)

    def test_fn2(self):
        print('test2 called')
        # #Arrange 
        # a=10
        # b=20

        #Act
        result=sum(self.b,self.a)

        #Assert
        self.assertEqual(result,self.a+self.b)



if __name__=='__main__':
    unittest.main()