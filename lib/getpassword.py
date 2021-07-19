import requests
from basecommon.common import *
from lib.case_log import *


def getpassword_zero():
    data_list = get_loginxls("test_user_data.xlsx", "password")
    case_data = get_data(data_list, "test_login")
    if not case_data:
        print("数据不存在")
    url = case_data.get('url')
    data = case_data.get('data')
    header = eval(case_data.get('header'))
    res = requests.post(url=url, data=data, headers=header)
    #print(res.status_code)
    tt = json.loads(res.content)
    password = tt['returnData']['bisData']
    #print("密码是：", password)
    return password
def getpassword_nozero():
    data_list = get_loginxls("test_user_data.xlsx", "password")
    case_data = get_data(data_list, "test_login_nozero")
    if not case_data:
        print("数据不存在")
    url = case_data.get('url')
    data = case_data.get('data')
    header = eval(case_data.get('header'))
    res = requests.post(url=url, data=data, headers=header)
    # print(res.status_code)
    tt = json.loads(res.content)
    password = tt['returnData']['bisData']
    # print("密码是：", password)
    return password

if __name__ == '__main__':
    getpassword_zero()
    getpassword_nozero()