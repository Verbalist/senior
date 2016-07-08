import unittest
from unittest.result import TestResult

# class A(object):
#     def b(self):


# def sampleTestResult(self):
#     print('1')
#     result = unittest.result.TestResult()
#     result.stopTestRun = lambda self: print('stop')
#     return result


class GoFraudTest(unittest.TestCase):

    inited = False

    def defaultTestResult(self):

        class MyTestResult(TestResult):
            def startTestRun(self):
                print('first solo start')

            def stopTestRun(self):
                print('last solo finish')

        return MyTestResult()

    # @classmethod
    # def setUpClass(cls):
    #     if not GoFraudTest.inited:
    #         cls.inited = True

        # self._outcome.stopTestRun = lambda self, test: print('stop')

    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')
    #     print(cls.countTestCases())


class ATest(GoFraudTest):

    def test_1(self):
        assert 1 == 1


class BTest(GoFraudTest):

    def test_2(self):
        assert 1 == 1

    def test_3(self):
        assert 1 == 1

if __name__ == '__main__':
    unittest.main()
