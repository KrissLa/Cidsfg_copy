from django.db import models
from loguru import logger


class IndividualProjectRequest(models.Model):
    """
    Модель заявки на индивидуальный проект
    """
    number_of_floors = models.PositiveSmallIntegerField('Количество этажей')
    area = models.PositiveSmallIntegerField('Площадь')
    number_of_rooms = models.PositiveSmallIntegerField('Количество комнат')
    number_of_bathrooms = models.PositiveSmallIntegerField('Количество санузлов')
    garage_is_needed = models.BooleanField('Нужен гараж')
    credit_is_needed = models.BooleanField('Нужен ли кредит', default=False)
    credit_amount = models.PositiveBigIntegerField('Сумма кредита (руб)', default=0)
    comment = models.TextField('Другие пожелания', blank=True, null=True)
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки заявки', auto_now_add=True)

    @classmethod
    def get_new_count(cls):
        logger.info(cls.objects.filter(processed=False).count())
        return cls.objects.filter(processed=False).count()

    def __str__(self):
        return f'Заявка на индивидуальный проект № {self.id}'

    class Meta:
        verbose_name = 'Заявка на уникальный проект'
        verbose_name_plural = f'Заявки на уникальный проект'


class Message(models.Model):
    """ Модель сообщения, отправляемого через форму на странице контакты """
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    message = models.TextField('Сообщение пользователя')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение, отправленное через форму со страницы Контакты'
        verbose_name_plural = 'Сообщения отправленные через форму со страницы Контакты'

    @classmethod
    def get_new_count(cls):
        logger.info(cls.objects.filter(processed=False).count())
        return cls.objects.filter(processed=False).count()

    def __str__(self):
        if self.processed:
            processed = ''
        else:
            processed = '(Новое сообщение!)'
        return f'Сообщение № {self.id} от пользователя {self.username}. {processed}'


class ConsultationRequest(models.Model):
    """ Модель заявки на консультацию со страницы с подробным описанием дома """
    username = models.CharField('Имя пользователя', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    credit_is_needed = models.BooleanField('Нужен ли кредит', default=False)
    credit_amount = models.PositiveBigIntegerField('Сумма кредита (руб)', default=0)
    message = models.TextField('Сообщение пользователя', blank=True, null=True)
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    house_name = models.CharField('Название модели дома, со страницы которого отправлена заявка', max_length=100)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на предложение'
        verbose_name_plural = 'Заявки на предложение'

    @classmethod
    def get_new_count(cls):
        logger.info(cls.objects.filter(processed=False).count())
        return cls.objects.filter(processed=False).count()

    def __str__(self):
        if self.processed:
            processed = ''
        else:
            processed = '(Новая!)'
        return f'Заявка на консультацию № {self.id} от пользователя {self.username}. {processed}'


class CooperationApplication(models.Model):
    """ Заявка на сотрудниччество """
    area_of_activity = models.CharField('Область деятельности', max_length=100)
    company_type = models.CharField('Частное лицо/Компания', max_length=50)
    company_name = models.CharField('Название компании', max_length=255, blank=True, null=True)
    firs_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    type_of_contact = models.CharField('Куда ответить', max_length=100, default='Мобильный')
    contact = models.CharField('Контакт', max_length=255, default='')
    processed = models.BooleanField('Отметить заявку как обработанную', default=False)
    created = models.DateTimeField('Время отправки сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на сотрудничество'
        verbose_name_plural = 'Заявки на сотрудничество'

    @classmethod
    def get_new_count(cls):
        logger.info(cls.objects.filter(processed=False).count())
        return cls.objects.filter(processed=False).count()

    def __str__(self):
        return f'Заявка на сотрудничество №{self.id}'
