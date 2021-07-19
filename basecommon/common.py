import os
from xlrd import open_workbook
# from xml.etree import ElementTree as ElemenTree
# from basecommon.Log import MyLog as Log
import readConfig
# import basecommon.configHttp as configHttp

# localConfigHttp = configHttp.ConfigHttp()
# log = Log.get_log()
# logger = log.get_logger()

#从excel文件中读取测试用例
def get_loginxls(xls_name, sheet_name):
    cls = []
    #get xls file's path
    xlsPath = os.path.join(readConfig.proDir, "testFile", xls_name)
    #open xls file
    file = open_workbook(xlsPath)
    #get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    header = sheet.row_values(0)  # 获取标题行数据
    #get one sheet's rows
    nrows = sheet.nrows
    for i in range(1, nrows):
         d = dict(zip(header, sheet.row_values(i)))
         cls.append(d)
    return cls

def get_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['casename']:
            return case_data



# #从xml文件中读取sql语句
# database = {}
# def set_xml():
#     if len(database) == 0:
#         sql_path = os.path.join(readConfig.proDir, "testFile", "SQL.xml")
#         tree = ElemenTree.parse(sql_path)
#         for db in tree.findall("database"):
#             db_name = db.get("name")
#             #print(db_name)
#             table = {}
#             for tb in db.getchildren():
#                 table_name = tb.get("name")
#                 #print(table_name)
#                 sql = {}
#                 for data in tb.getchildren():
#                     sql_id = data.get("id")
#                     #print(sql_id)
#                     sql[sql_id] = data.text
#                 table[table_name] = sql
#             database[db_name] = table
#
#
# def get_xml_dict(database_name, table_name):
#     set_xml()
#     database_dict = database.get(database_name).get(table_name)
#     return database_dict
#
# def get_sql(database_name, table_name, sql_id):
#     db = get_xml_dict(database_name, table_name)
#     sql = db.get(sql_id)
#     return sql
#
if __name__ == '__main__':
    data_list = get_loginxls("test_user_data.xlsx", "login")
    case_data = get_data(data_list, "test_login")
    print(case_data)