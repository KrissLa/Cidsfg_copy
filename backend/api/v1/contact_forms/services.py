from datetime import datetime

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
    """Отправляем уведомление о новой заявке на уникальный проект"""
    message = """
Новая заявка на уникальный проект № <b>{id}</b>!
Имя пользователя: <b>{username}</b>
Куда ответить: <b>{type_of_contact}</b>
Контакт пользователя: <b>{contact}</b>
Количество этажей: <b>{number_of_floors}</b>
Площадь: <b>{area}</b>
Количество комнат: <b>{number_of_rooms}</b>
Количество санузлов: <b>{number_of_bathrooms}</b>
Нужен гараж: <b>{garage_is_needed}</b>
Другие пожелания: <b>{comment}</b>
Время создания заявки: <b>{created}</b>
<a href="{domain}/nobots/{admin_url}/contact_forms/individualprojectrequest/{id}/change/">Посмотреть в панели администратора</a>
    """
    if data['garage_is_needed']:
        data['garage_is_needed'] = 'ДА'
    else:
        data['garage_is_needed'] = 'НЕТ'
    data['created'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    send_message_to_admin(message.format(domain=SITE_DOMAIN, admin_url=ADMIN_URL, **data), admin_id)


def send_notification_message(data, admin_id=TG_ADMIN_ID):
    """Отправляем уведомление о новом сообщении со страницы Контакты"""
    message = f"""
Новое сообщение № <b>{data['id']}</b>!
Имя пользователя: <b>{data['username']}</b>
Куда ответить: <b>{data['type_of_contact']}</b>
Контакт пользователя: <b>{data['contact']}</b>
Сообщение: <b>{data['message']}</b>
<a href="{SITE_DOMAIN}/nobots/{ADMIN_URL}/contact_forms/message/{data['id']}/change/">Посмотреть в панели администратора</a>
"""
    send_message_to_admin(message, admin_id)
