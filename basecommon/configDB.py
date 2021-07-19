#import pymysql
import cx_Oracle
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()

class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    # config = {
    #     'host': str(host),
    #     'user': username,
    #     'passwd': password,
    #     'port': int(port),
    #     'db': database
    # } #连接mysql
    config = username+"/"+password+"@"+host+":"+port+"/"+database
    #print(config)

    # def __init__(self):
    #     # self.log = Log.get_log()
    #     # self.logger = self.log.get_logger()
    #     self.db = None
    #     self.cursor = None

    def __init__(self):
        self.db = cx_Oracle.connect(config)  # 建立链接
        self.cursor = self.db.cursor()  # 建立游标
        print("Connect DB successfully")


    # def connectDB(self):
    #     # try:
    #     #     #connect to DB
    #     #     self.db = pymysql.connect(**config)
    #     #     #create cuesor
    #     #     self.cursor = self.db.cursor()
    #     #     print("Connect DB successfully")
    #     # except ConnectionError as ex:
    #     #     self.logger.error(str(ex))
    #     self.db = pymysql.connect(**config)#建立链接
    #     self.cursor = self.db.cursor()#建立游标
    #     print("Connect DB successfully")

    # def __del__(self):
    #     self.cursor.close()
    #     self.db.close()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query("select * from tconversation where CONVERSATION_NAME = '{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.exec("delete from tconversation where CONVERSATION_NAME = '{}'".format(name))

    # def executeSQL(self, sql, params):
    #     self.connectDB()
    #     #executing sql
    #     self.cursor.execute(sql, params)
    #     # executing by committing to DB
    #     self.db.commit()
    #     return self.cursor

    # def get_all(self, cursor):
    #     value = cursor.fetchall()
    #     return value
    #
    # def get_one(self, cursor):
    #     value = cursor.fetchone()
    #     return value

    def closeDB(self):
        self.db.close()
        print("Database closed")