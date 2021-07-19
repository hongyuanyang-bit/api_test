import logging
from datetime import datetime
import time
import threading
import os
import readConfig


# class Log:
#     def __init__(self):
#         global logPath, resultPath, proDir
#         proDir = readConfig.proDir
#         resultPath = os.path.join(proDir, "result")
#
#         #creat result file if it doesn't exist
#         if not os.path.exists(resultPath):
#             os.mkdir(resultPath)
#
#         #defined test result file name by localtime
#         logPath = os.path.join(resultPath, str(datetime.now(), time.strftime("%Y%m%d%H%M%S")))
#
#         #creat test result file if it doesn't exit
#         if not os.path.exists(logPath):
#             os.mkdir(logPath)
#
#         #define logger
#         self.logger = logging.getLogger()
#
#         #define log level
#         self.logger.setLevel(logging.INFO)
#
#         #define handler
#         handler = logging.FileHandler(os.path.join(logPath,"output.log"))
#         #define formatter
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         #define formatter
#         handler.setFormatter(formatter)
#         #add handler
#         self.logger.addHandler(handler)
#
#
# class MyLog:
#     log = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_log():
#         if MyLog.log is None:
#             MyLog.mutex.acquire()
#             MyLog.log = Log()
#             MyLog.mutex.release()
#
#         return MyLog.log

logpath = readConfig.log_file
logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=logpath,  # 日志输出文件
                    filemode='a')  # 追加模式



# if __name__ == '__main__':
#     logging.info("hello")