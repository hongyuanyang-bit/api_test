
import json
from basecommon.Log import *
import readConfig

def log_case_info(case_name, url, data,expect_res, res_text,loginfo):
    if isinstance(data, dict):
        data = json.dumps(data,ensure_ascii=False)
    # logging.basicConfig(level=logging.DEBUG,  # log level
    #                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    #                     # log格式
    #                     datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
    #                     filename='log.txt',  # 日志输出文件
    #                     filemode='a')  # 追加模式
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))
    logging.info("返回：{}".format(loginfo))