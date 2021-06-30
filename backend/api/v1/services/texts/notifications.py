

unique_project_text = """
Новая заявка на уникальный проект № <b>{id}</b>!
Имя пользователя: <b>{username}</b>
Куда ответить: <b>{type_of_contact}</b>
Контакт пользователя: <b>{contact}</b>
Количество этажей: <b>{number_of_floors}</b>
Площадь: <b>{area}</b>
Количество комнат: <b>{number_of_rooms}</b>
Количество санузлов: <b>{number_of_bathrooms}</b>
Нужен гараж: <b>{garage_is_needed}</b>
Нужен ли кредит: <b>{credit_is_needed}</b>{credit_amount_text}
Другие пожелания: <b>{comment}</b>
Время создания заявки: <b>{created}</b>
<a href="{domain}/nobots/{admin_url}/contact_forms/individualprojectrequest/{id}/change/">Посмотреть в панели администратора</a>
"""


consultation_request_text = """
Новая заявка на предложение № <b>{id}</b>!
Имя пользователя: <b>{username}</b>
Куда ответить: <b>{type_of_contact}</b>
Контакт пользователя: <b>{contact}</b>
Нужен ли кредит: <b>{credit_is_needed}</b>{credit_amount_text}
Сообщение: <b>{message}</b> 
Название дома: <b>{house_name}</b>
Время создания заявки: <b>{created}</b>
<a href="{domain}/nobots/{admin_url}/contact_forms/consultationrequest/{id}/change/">Посмотреть в панели администратора</a>
"""


contact_message_text = """
Новое сообщение № <b>{id}</b>!
Имя пользователя: <b>{username}</b>
Куда ответить: <b>{type_of_contact}</b>
Контакт пользователя: <b>{contact}</b>
Сообщение: <b>{message}</b>
Время отправки сообщения: <b>{created}</b>
<a href="{domain}/nobots/{admin_url}/contact_forms/message/{id}/change/">Посмотреть в панели администратора</a>
"""


partnership_text = """
Новая заявка на сотрудничество № <b>{id}</b>!
Область деятельности: <b>{area_of_activity}</b>
Частное лицо/Компания: <b>{company_type}</b>{company_name_text}
Имя пользователя: <b>{firs_name}</b>
Фамилия пользователя: <b>{last_name}</b>
Куда ответить: <b>{type_of_contact}</b>
Контакт пользователя: <b>{contact}</b>
Время создания заявки: <b>{created}</b>
<a href="{domain}/nobots/{admin_url}/contact_forms/cooperationapplication/{id}/change/">Посмотреть в панели администратора</a>
"""
