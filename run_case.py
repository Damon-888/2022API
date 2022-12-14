import unittest
from HTMLTestRunner import HTMLTestRunner
from  api.base import Base

test_report = 'test_report.html'


if __name__ == '__main__':
    base = Base()
    base.login()

    suite = unittest.TestLoader().discover('cases',pattern='test*.py')

    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='标题测试报告',description='简化版')
        runner.run(suite)