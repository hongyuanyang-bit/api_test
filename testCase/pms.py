import requests
import json


def decryptPassword():
    url = "http://10.88.60.225:9997/um/api/sys/user/decryptPassword"
    data = json.dumps({
        "appParam": {
        "id": "0"
        },
    "dataParam": {}
    })
    header = {
        "sysParam": json.dumps({"sysID":"2"}),
        "Content-Type":"application/json"
    }
    res = requests.post(url=url,data=data,headers=header)
    #print(res.text)
    tt = json.loads(res.content)
    password = tt['returnData']['bisData']
    #print(tt['returnData']['bisData'])
    return password

def login():
    url = "http://10.88.60.225:9997/um/api/sys/user/login"
    t=decryptPassword()
    #print("lllll:",t)
    data = json.dumps(
        {
            "appParam": {
                "loginId": "hzm",
                "passWord": decryptPassword()
            },
            "dataParam": {}
        }
    )
    header = {
        "sysParam": json.dumps({"sysID": "2"}),
        "Content-Type": "application/json"
    }
    res = requests.post(url=url, data=data, headers=header)
    #print(res.text)
    x = json.loads(res.content)
    token = x['returnData']['bisData']['jwt']['access_token']
    #print(token)
    return token

def getstocklist():
    url = "http://10.88.60.225:9993/pms/api/sys/fundHolding/getStockList"
    bearer = "Bearer "
    access_token = login()
    authorization = bearer + access_token
    #print(authorization)
    header = {
        "Authorization": authorization,
        "sysParam": json.dumps({"sysID": "2"}),
        "Content-Type": "application/json"
    }
    res = requests.post(url=url,headers=header)
    x = json.loads(res.content)
    #print(authorization)
    print(x)


# def getFuturesList():
#     url = "http://10.88.60.225:9993/pms/api/sys/fundHolding/getFuturesList"
#     bearer = "Bearer "
#     access_token = login()
#     authorization = bearer + access_token
#     header = {
#         "Authorization": authorization,
#         "sysParam": json.dumps({"sysID": "2"}),
#         "Content-Type": "application/json"
#     }
#     res = requests.post(url=url,headers=header)
#     x = json.loads(res.content)
#     print(authorization)
#     print(x)
#
#
# def getCodeInfo():
#     url = "http://10.88.60.225:9993/pms/api/sys/fundHolding/getCodeInfo"
#     bearer = "Bearer "
#     access_token = login()
#     authorization = bearer + access_token
#     header = {
#         "Authorization": authorization,
#         "sysParam": json.dumps({"sysID": "2"}),
#         "Content-Type": "application/json"
#     }
#     res = requests.post(url=url,headers=header)
#     x = json.loads(res.content)
#     print(authorization)
#     print(x)
#
#
# def getUserMenuList():
#     url = "http://10.88.60.225:9997/um/api/sys/permission/getUserMenuList"
#     bearer = "Bearer "
#     access_token = login()
#     authorization = bearer + access_token
#     header = {
#         "Authorization": authorization,
#         "sysParam": json.dumps({"sysID": "2"}),
#         "Content-Type": "application/json"
#     }
#     res = requests.post(url=url,headers=header)
#     x = json.loads(res.content)
#     print(authorization)
#     print(x)
#
# def getInstructionTodo():
#     url = "http://10.88.60.225:9993/pms/api/sys/instructionApproval/getInstructionTodo"
#     bearer = "Bearer "
#     access_token = login()
#     authorization = bearer + access_token
#     header = {
#         "Authorization": authorization,
#         "sysParam": json.dumps({"sysID": "2"}),
#         "Content-Type": "application/json"
#     }
#     res = requests.post(url=url,headers=header)
#     x = json.loads(res.content)
#     print(authorization)
#     print(x)


if __name__ == '__main__':
    #decryptPassword()
    login()
    getstocklist()