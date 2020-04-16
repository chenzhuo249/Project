from django.core.mail import send_mail
from  django.conf import settings
from dadashop12.celery import app


@app.task
def send_active_email_async(email_address, v_url):
    """
    发送激活邮件
    :param email_address: 收件方邮箱地址
    :param v_url: 激活地址
    """
    subject = "卓卓商城激活邮件"
    html_msg = f"""
    <p>尊敬的用户您好</p>
    <p>请点击此连接激活您的账户(3天内有效):</p>
    <p><a href="{v_url}" target="_blank">点击激活</a></p>
    """
    send_mail(subject=subject, html_message=html_msg, from_email=settings.EMAIL_HOST_USER, recipient_list=[email_address], message="?")
