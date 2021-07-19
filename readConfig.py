import os
import codecs
import configparser
import time
from optparse import OptionParser

today = time.strftime('%Y%m%d', time.localtime())
#now = time.strftime('%Y%m%d_%H%M%S', time.localtime())#到秒
now = time.strftime('%Y%m%d', time.localtime())

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
testPatn = os.path.join(proDir, 'testCase', 'case')
comPath = os.path.join(proDir, 'basecommon')
report_file = os.path.join(proDir, 'result', 'report_{}.html'.format(now))
log_file = os.path.join(proDir, 'result', 'log_{}.txt'.format(today))
data_file = os.path.join(proDir, 'testFile', 'test_user_data.xlsx')
testlist_file = os.path.join(proDir, 'testCase', 'testlist.txt')

senf_email_after_run = False

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value


    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return  value


    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


