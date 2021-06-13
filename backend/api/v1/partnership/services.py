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
    """Отправляем уведомление о новом сообщении со страницы Контакты"""
    message = f"""
Новая заявка на сотрудничество № <b>{data['id']}</b>!
Область деятельности: <b>{data['area_of_activity']}</b>
Частное лицо/Компания: <b>{data['company_type']}</b>
Название компании: <b>{data['company_name']}</b>
Имя пользователя: <b>{data['firs_name']}</b>
Фамилия пользователя: <b>{data['last_name']}</b>
Куда ответить: <b>{data['type_of_contact']}</b>
Контакт пользователя: <b>{data['contact']}</b>
<a href="{SITE_DOMAIN}/nobots/{ADMIN_URL}/partnership/cooperationapplication/{data['id']}/change/">Посмотреть в панели администратора</a>
"""
    send_message_to_admin(message, admin_id)
