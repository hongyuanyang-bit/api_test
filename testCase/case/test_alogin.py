import unittest
from lib.getpassword import *
from basecommon.common import *
from lib.case_log import *
import requests

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = get_loginxls("test_user_data.xlsx", "login")

    def test_user_login_normal(self):
        case_data = get_data(self.data_list, "test_login")
        if not case_data:
            logging.error("数据不存在")
        url = case_data.get('url')
        loginId = case_data.get('loginid')
        header = eval(case_data.get('header'))
        password = getpassword_zero()
        data = json.dumps(
        {
            "appParam": {
                "loginId": loginId,
                "passWord": password
            },
            "dataParam": {}
        }
        )
        res = requests.post(url=url, data=data, headers=header)
        #print(res.status_code)
        expect_res = case_data.get('expect_res')
        x = json.loads(res.content)
        logInfo = x['returnInfo']['logInfo']
        log_case_info('test_user_login_normal', url, data, expect_res, res.status_code,logInfo)
        #logging.info("测试用例：{}".format('getpassword'))
        #print(json.loads(res.content))
        self.assertEqual(res.status_code, expect_res)
        #tt = json.loads(res.content)
        # #token = tt['returnData']['bisData']['jwt']['access_token']
        # globals()["token"] = tt['returnData']['bisData']['jwt']['access_token']
        #print(globals()["token"])

        #return token
    def test_user_login_wrong(self):
        case_data = get_data(self.data_list, "test_login_wrong")
        if not case_data:
            logging.error("数据不存在")
        url = case_data.get('url')
        loginId = case_data.get('loginid')
        header = eval(case_data.get('header'))
        password = getpassword_zero()
        data = json.dumps(
            {
                "appParam": {
                    "loginId": loginId,
                    "passWord": password
                },
                "dataParam": {}
            }
        )
        res = requests.post(url=url, data=data, headers=header)
        expect_res = case_data.get('expect_res')
        x = json.loads(res.content)
        logInfo = x['returnInfo']['logInfo']
        log_case_info('test_user_login_wrong', url, data, expect_res, res.status_code, logInfo)
        print(json.loads(res.content))
        self.assertEqual(res.status_code, expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2)