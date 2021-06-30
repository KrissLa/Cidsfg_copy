from datetime import datetime


from backend.services.price_to_str import price_to_str
from config.settings import SITE_DOMAIN, ADMIN_URL


def update_data(func):
    """
    Добавляем дополнительные значения в исходные данные
    """
    def wrapper(obj, data):
        data.update({'domain': SITE_DOMAIN, 'admin_url': ADMIN_URL, 'created': datetime.now().strftime('%Y-%m-%d %H:%M')})
        return func(data)
    return wrapper


def _credit_is_needed_update(data):
    """ Форматирование данных о кредите"""
    if data['credit_is_needed']:
        data['credit_is_needed'] = 'ДА'
        data['credit_amount_text'] = f'\nСумма кредита: <b>{price_to_str(data["credit_amount"])}</b> руб.'
    else:
        data['credit_is_needed'] = 'НЕТ'
        data['credit_amount_text'] = ''
    return data


def _comment_update(data, message_key):
    """ Явно показываем, если других пожеланий нет """
    if not data[message_key]:
        data[message_key] = 'не указаны'
    return data


@update_data
def unique_project_update_data(data):
    """ Преобразование данных для уникального проекта """
    if data['garage_is_needed']:
        data['garage_is_needed'] = 'ДА'
    else:
        data['garage_is_needed'] = 'НЕТ'
    _comment_update(data, 'comment')
    return _credit_is_needed_update(data)


@update_data
def consultation_request_update_data(data):
    """ Преобразование данных для заявок на консультацию """
    _comment_update(data, 'message')
    return _credit_is_needed_update(data)


@update_data
def contact_message_update_data(data):
    """ Преобразование данных для сообщений пользователей """
    return data


@update_data
def partnership_update_data(data):
    """ Преобразование данных для заявок на сотрудничество """
    if data['company_type'] == 'компания':
        data['company_name_text'] = f'\nНазвание компании: <b>{data["company_name"]}</b>.'
    else:
        data['company_name_text'] = ''
    return data

