from lib.getpassword import *

def gettoken():
    data_list = get_loginxls("test_user_data.xlsx", "login")

    case_data = get_data(data_list, "test_login")
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
    tt = json.loads(res.content)
    token = tt['returnData']['bisData']['jwt']['access_token']
    return token

def gethyytoken():
    data_list = get_loginxls("test_user_data.xlsx", "login")

    case_data = get_data(data_list, "test_login_wrong")
    url = case_data.get('url')
    loginId = case_data.get('loginid')
    header = eval(case_data.get('header'))
    password = getpassword_nozero()
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
    tt = json.loads(res.content)
    token = tt['returnData']['bisData']['jwt']['access_token']
    return token

if __name__ == '__main__':
    gettoken()
    gethyytoken()