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
Новое заявка на консультацию № <b>{data['id']}</b>!
Имя пользователя: <b>{data['username']}</b>
Куда ответить: <b>{data['type_of_contact']}</b>
Контакт пользователя: <b>{data['contact']}</b>
Сообщение: <b>{data['message']}</b>
Название дома: <b>{data['house_name']}</b>
<a href="{SITE_DOMAIN}/{ADMIN_URL}/products/consultationrequest/{data['id']}/change/">Посмотреть в панели администратора</a>
"""
    send_message_to_admin(message, admin_id)
