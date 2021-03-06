import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import sys
# sys.path.append(readConfig.comPath)
from lib.case_log import *
from email.header import Header

localReadConfig = readConfig.ReadConfig()

#
def send_emial(report_file):
    global host, user, password, from_user, to_user, smtp
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))
    host = localReadConfig.get_email("mail_host")
    user = localReadConfig.get_email("mail_user")
    password = localReadConfig.get_email("mail_pass")#授权码，非邮箱密码
    from_user = localReadConfig.get_email("mail_from")
    to_user = localReadConfig.get_email("mail_to")
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = Header('接口测试报告', 'utf-8')#主题
    att1 = MIMEText(open(report_file,'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="report.html"'
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(host)
        # smtp = smtplib.SMTP
        # smtp.connect(host, 25)
        smtp.login(user, password)
        smtp.sendmail(from_user, to_user, msg.as_string())
        logging.info("邮件发送完成")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()


# class Email:
#     def __init__(self):
#         global host, user, password, port, sender, title, content
#         host = localReadConfig.get_email("mail_host")
#         user = localReadConfig.get_email("mail_user")
#         password = localReadConfig.get_email("mail_pass")
#         port = localReadConfig.get_email("mail_port")
#         sender = localReadConfig.get_email("sender")
#         title = localReadConfig.get_email("subject")
#         content = localReadConfig.get_email("content")
#         self.value = localReadConfig.get_email("receiver")
#         self.receiver = []
#         # get receiver list
#         for n in str(self.value).split("/"):
#             self.receiver.append(n)
#         # defined email subject
#         date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.subject = title + " " + date
#         self.log = MyLog.get_log()
#         self.logger = self.log.get_logger()
#         self.msg = MIMEMultipart('mixed')
#
#     def config_header(self):
#         self.msg['subject'] = self.subject
#         self.msg['from'] = sender
#         self.msg['to'] = ";".join(self.receiver)
#
#     def config_content(self):
#         content_plain = MIMEText(content, 'plain', 'utf-8')
#         self.msg.attach(content_plain)
#
#     def config_file(self):
#         # if the file content is not null, then config the email file
#         if self.check_file():
#
#             reportpath = self.log.get_result_path()
#             zippath = os.path.join(readConfig.proDir, "result", "test.zip")
#             # zip file
#             files = glob.glob(reportpath + '\*')
#             f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
#             for file in files:
#                 f.write(file)
#             f.close()
#
#             reportfile = open(zippath, 'rb').read()
#             filehtml = MIMEText(reportfile, 'base64', 'utf-8')
#             filehtml['Content-Type'] = 'application/octet-stream'
#             filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
#             self.msg.attach(filehtml)
#
#     def check_file(self):
#         reportpath = self.log.get_report_path()
#         if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
#             return True
#         else:
#             return False
#
#     def send_email(self):
#         self.config_header()
#         self.config_content()
#         self.config_file()
#         try:
#             smtp = smtplib.SMTP()
#             smtp.connect(host)
#             smtp.login(user, password)
#             smtp.sendmail(sender, self.receiver, self.msg.as_string())
#             smtp.quit()
#             self.logger.info("The test report has send to developer by email.")
#         except Exception as ex:
#             self.logger.error(str(ex))
#
# class MyEmail:
#     email = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_email():
#
#         if MyEmail.email is None:
#             MyEmail.mutex.acquire()
#             MyEmail.email = Email()
#             MyEmail.mutex.release()
#         return MyEmail.email
#
#
if __name__ == "__main__":
    send_emial()