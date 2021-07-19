import unittest
from testCase.case.test_alogin import TestUserLogin
from testCase.case.test_getstkocklist import TestgetStockList
import readConfig
#
smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_user_login_normal'), TestgetStockList('test_getstocklist_normal')])

# def get_suite(suite_name):
#     return globals().get(suite_name)

# if __name__ == "__main__":
#     print(run_suit())
