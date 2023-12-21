import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(sender_email, sender_name, receiver_email, subject, message):
    try:
        # 配置SMTP服务器
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'your_username'
        smtp_password = 'your_password'

        # 创建邮件内容
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # 连接SMTP服务器并发送邮件
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败:', str(e))

# 调用发送邮件函数
send_email('sender@example.com', 'Sender Name', 'receiver@example.com', 'Test Email', 'This is a test email.')
