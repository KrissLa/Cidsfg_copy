import requests
from loguru import logger

from config.settings import TG_BOT_TOKEN, TG_ADMIN_ID


def send_message_to_admin(message):
    """ Отправляем сообщение в телеграм"""

    response = requests.get(
        f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={TG_ADMIN_ID}&text={message}&parse_mode=HTML',
        data={'key': 'value'})
    logger.info(response)
    logger.info(response.json())


def send_notification(data):
    """Отправляем уведомление о новом заказе"""
    message = f"""
Новый заказ № {data['id']}!
Имя пользователя: {data['username']}
Номер телефона: {data['phone_number']}"""
    send_message_to_admin(message)
