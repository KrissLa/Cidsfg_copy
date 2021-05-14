import requests
from loguru import logger

from config.settings import TG_BOT_TOKEN, TG_ADMIN_ID, SITE_DOMAIN, ADMIN_URL


def send_message_to_admin(message, admin_id=TG_ADMIN_ID):
    """ Отправляем сообщение в телеграм"""

    response = requests.get(
        f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={admin_id}&text={message}&parse_mode=HTML',
        data={'key': 'value'})
    logger.info(response)
    logger.info(response.json())


def send_notification(data, admin_id=TG_ADMIN_ID):
    """Отправляем уведомление о новой заявке на консультацию """
    message = f"""
Новое заявка на консультацию № {data['id']}!
Имя пользователя: {data['username']}
E-mail пользователя: {data['email']}
Номер телефона пользователя: {data['phone_number']}
Сообщение: {data['message']}
Название дома: {data['house_name']}
<a href="{SITE_DOMAIN}/{ADMIN_URL}/products/consultationrequest/{data['id']}/change/">Посмотреть в панели администратора</a>
"""
    send_message_to_admin(message, admin_id)
