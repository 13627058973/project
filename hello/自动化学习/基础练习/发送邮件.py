# coding:utf-8
import smtplib
from email.mime.text import MIMEText  # MIMETest()定义邮件正文
from email.header import Header  # Header()定义邮件标题
from email.mime.multipart import MIMEMultipart  # 邮件附件
from email.mime.base import MIMEBase
from email import encoders

#  -----1，跟发件相关的参数------
smtpserver = 'smtp.qq.com'  # 发送服务器
port = 465  # 端口
sender = '1269357308@qq.com'  # 账号
psw = 'iryymvusssjsifce'  # 密码
receiver = ['953561304@qq.com', '1269357308@qq.com']  # 接收人的QQ

#  ------2，编辑邮件的内容（正文发送）
'''
subject = "python邮件测试"   # 主题
content = "阿昌渣渣"         # 正文
msg = MIMEText(content)
msg['subject'] = subject
msg['sender'] = sender
msg['receiver'] = receiver
'''

# -------2，编辑邮件的内容（附件发送）------
subject = 'python附件测试'
file_path = 'result.html'
with open(file_path, 'rb') as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg['sender'] = sender  # 发件人
msg['receiver'] = ';'.join(receiver)  # 收件人
msg['subject'] = subject  # 主题

# 正文
body = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(body)

# 附件
att = MIMEText(mail_body, 'base64', 'utf-8')
att['content-Type'] = 'application/octet-stream'
att['content-Disposition'] = 'attachment;filename="test1_report.html"'
msg.attach(att)
try:
    # 以QQ邮箱为主
    stmp = smtplib.SMTP_SSL("smtp.qq.com", 465)    # 连服务器
    stmp.login(sender, psw)                        # 登录

except:
    # 不需要加授权，如163邮箱
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)        # 连服务器
    smtp.login(sender, psw)
stmp.sendmail(sender, receiver, msg.as_string())   # 发送
smtp.quit()  # 关闭
