import unittest
from lib.gettoken import *
from testCase.basecase import BaseCase

localReadConfig = readConfig.ReadConfig()

class TestgetStockList(BaseCase):
    global baseurl
    baseurl = localReadConfig.get_http('baseurl')
    @classmethod
    def setUpClass(cls):
        cls.data_list = get_loginxls("test_user_data.xlsx", "getstocklist")

    def test_getstocklist_jurisdiction(self):
        case_data = get_data(self.data_list, "test_getstocklist")
        if not case_data:
            print("数据不存在")
        url = baseurl + case_data.get('url')
        bearer = case_data.get('bearer')
        access_token = gettoken()
        authorization = bearer + access_token
        header = eval(case_data.get('header'))
        header['Authorization'] = authorization
        # print("a:", header)
        # print("b", gettoken())
        res = requests.post(url=url, headers=header)
        x = json.loads(res.content)
        # print(x)
        # print(res.status_code)
        expect_res = case_data.get('expect_res')
        info = x['returnInfo']['logInfo']
        log_case_info('test_getstocklist_jurisdiction', url, header, expect_res, res.status_code,info)
        #logging.info("测试用例：{}".format('getpassword'))
        self.assertEqual(res.status_code, expect_res)

    def test_getstocklist_normal(self):
        # case_data = get_data(self.data_list, "test_getstocklist")
        # if not case_data:
        #     print("数据不存在")
        # url = baseurl + case_data.get('url')
        # bearer = case_data.get('bearer')
        # access_token = gethyytoken()
        # authorization = bearer + access_token
        # header = eval(case_data.get('header'))
        # header['Authorization'] = authorization
        # # print("a:", header)
        # # print("b", gettoken())
        # res = requests.post(url=url, headers=header)
        # x = json.loads(res.content)
        # # print(x)
        # # print(res.status_code)
        # expect_res = case_data.get('expect_res')
        # info = x['returnInfo']['logInfo']
        # log_case_info('test_getstocklist_normal', url, header, expect_res, res.status_code,info)
        # #logging.info("测试用例：{}".format('getpassword'))
        # self.assertEqual(res.status_code, expect_res)
        """有权限"""
        case_data = self.get_case_data("test_getstocklist_normal")
        self.send_request(case_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)