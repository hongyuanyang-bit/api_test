import unittest
from basecommon.HTMLTestReportCN import HTMLTestRunner
import os
import readConfig as readConfig
import unittest
import readConfig
from basecommon.Log import *
from basecommon.configEmail import *
from testCase.suite.test_suites import *
#--coding:GBK --


# def set_case_list(self):
# #     fb = open(self.caseListFile)
# #     for value in fb.readlines():
# #         data = str(value)
# #         if data != '' and not data.startswith("#"):
# #             self.caseList.append(data.replace("\n", ""))
# #     fb.close()
# #
# #
# # def set_case_suite(self):
# #     self.set_case_list()
# #     test_suite = unittest.TestSuite()
# #     suite_model = []
# #
# #     for case in self.caseList:
# #         case_file = os.path.join(readConfig.proDir, "testCase")
# #         print(case_file)
# #         case_name = case.split("/")[-1]
# #         print(case_name + ".py")
# #         discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
# #         suite_model.append(discover)
# #
# #     if len(suite_model) > 0:
# #         for suite in suite_model:
# #             for test_name in suite:
# #                 test_suite.addTest(test_name)
# #     else:
# #         return None
# #     return test_suite
# #
# #
# # def run(self):
# #     try:
# #         suit = self.set_case_suite()
# #         if suit is not None:
# #             logger.info("********TEST START********")
# #             fp = open(resultPath, 'wb')
# #             runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
# #             runner.run(suit)
# #         else:
# #             logger.info("Have no case to test.")
# #     except Exception as ex:
# #         logger.error(str(ex))
# #     finally:
# #         logger.info("*********TEST END*********")
# #         # send test report by email
# #         if int(on_off) == 0:
# #             self.email.send_email()
# #         elif int(on_off) == 1:
# #             logger.info("Doesn't send report email to developer.")
# #         else:
# #             logger.info("Unknow state.")
def discover():
    return unittest.defaultTestLoader.discover(readConfig.testPatn)


def collect():

    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)

    _collect(discover())
    return suite

def makesuite_by_testlist(testlist_file):
    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]

    suite = unittest.TestSuite()
    all_cases = collect()
    for case in all_cases:
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite

def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suite.addTest(case)

    return suite

def collect():   # 由于使用discover() 组装的TestSuite是按文件夹目录多级嵌套的，我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
    suite = unittest.TestSuite()

    def _collect(tests):   # 递归，如果下级元素还是TestSuite则继续往下找
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)  # 如果下级元素是TestCase，则添加到TestSuite中

    _collect(discover())
    return suite


def run(suit):
    logging.info("============测试开始===========")

    with open(readConfig.report_file, "wb") as f:
        HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suit)
    if readConfig.senf_email_after_run:
        send_emial(readConfig.report_file)
    logging.info("===================测试结束===================")

#只列出用例不执行
def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time()-t0))


def run_all():
    run(discover())

#跑指定用例
def run_suite(suit):
    run(suit)

#按testlist用例列表运行
def run_by_testlist():
    run(makesuite_by_testlist(readConfig.testlist_file))
    #print(makesuite_by_testlist(readConfig.testlist_file))

def run_by_tag(tag):
    run(makesuite_by_tag(tag))

def main():
    # run_all()
    # run_suite(smoke_suite)
    #run_by_testlist()
    # makesuite_by_testlist(readConfig.testlist_file)
    #run_by_tag("有权限")
    collect_only()


if __name__ == '__main__':
    main()