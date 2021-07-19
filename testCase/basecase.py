import unittest
import requests
import json
from basecommon.common import *
from lib.case_log import *
from lib.gettoken import *
import readConfig

localReadConfig = readConfig.ReadConfig()
class BaseCase(unittest.TestCase):
    global baseurl
    baseurl = localReadConfig.get_http('baseurl')
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = get_loginxls(readConfig.data_file, cls.__name__)
    def get_case_data(self, casename):
        return get_data(self.data_list, casename)
    def send_request(self, case_data):
        case_name = case_data.get('casename')
        url = baseurl + case_data.get('url')
        bearer = case_data.get('bearer')
        access_token = gethyytoken()
        authorization = bearer + access_token
        args = case_data.get('args')
        headers = eval(case_data.get('header'))
        headers['Authorization'] = authorization
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        # if method.upper() == 'GET':  # GET类型请求
        #     res = requests.get(url=url, params=json.loads(args))
        #
        # elif data_type.upper() == 'FORM':  # 表单格式请求
        #     res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
        #     log_case_info(case_name, url, args, expect_res, res.text)
        #     self.assertEqual(res.text, expect_res)
        # else:
        res = requests.post(url=url, headers=headers)  # JSON格式请求
        x = json.loads(res.content)
        info = x['returnInfo']['logInfo']
        log_case_info(case_name, url, args, expect_res, res.status_code, info)
        self.assertEqual(res.status_code, expect_res)


if __name__ == "__main__":
    unittest.main()