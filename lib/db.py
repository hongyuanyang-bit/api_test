# import cx_Oracle

from basecommon.configDB import MyDB

#
# conn = cx_Oracle.connect('falk/falk@10.84.162.189:1521/appmkt')
#
# cur = conn.cursor()
#
# cur.execute("select * from tconversation where CONVERSATION_NAME = 'hyy'")
#
# result = cur.fetchall()
# print(result)
#
# cur.execute("delete from tconversation where CONVERSATION_NAME = 'hyy'")
# conn.commit()
# cur.close()
# conn.close()

db = MyDB()
if db.check_user("hyy"):
    db.del_user("hyy")