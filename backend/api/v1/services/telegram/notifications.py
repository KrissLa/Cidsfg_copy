import requests
from config.settings import TG_BOT_TOKEN, TG_ADMIN_ID


def _send_message(message, chat_id=TG_ADMIN_ID):
    """ Отправляем сообщение в телеграм"""

    return requests.get(
        f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=HTML',
        data={'key': 'value'})


def send_notification(data, message, data_updater, chat_id=TG_ADMIN_ID):
    """ Форматирует сообщение и отправляет уведомление в чат"""
    data_updater(data)
    return _send_message(message.format(**data), chat_id)
