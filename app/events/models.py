from django.db import models
from users.models import Users


class Events(models.Model):
    user = models.ForeignKey(
        Users,
        related_name='user',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(
        'Название мероприятия',
        max_length=60
    )
    description = models.TextField(
        'Описания мероприятия',
        max_length=300,
        help_text='Краткое описание для'
                  ' игроков.'
    )
    CHOICE_TYPE_EVENT = (
        ('Глобальные мероприятия', 'Глобальные мероприятия'),
        ('Локальные мероприятия', 'Локальные мероприятия')
    )
    type_event = models.CharField(
        'Категория ивента',
        choices=CHOICE_TYPE_EVENT,
        max_length=30,
        default='Локальные мероприятия',
    )
    vk = models.CharField(
        'Вконтакте',
        max_length=120,
        help_text='Контакт организатора '
                  'мероприятия'
    )

    # contact form eventer
    full_description = models.TextField(
        'Развёрнутое описание для проверяющего.',
        max_length=2500
    )
    property = models.TextField(
        'Список имущества, которое понадобится',
        max_length=300
    )
    nickname = models.CharField(
        'Никнейм персонажа для выдачи',
        max_length=60
    )
    status = models.BooleanField(
        'Доступна ли пользователям сайта мероприятие?',
        default=False
    )
    archive = models.BooleanField(
        'Мероприятие в архиве?',
        default=False
    )

    # assist-form
    CHOICE_TYPE_STATUS = (
        ('На рассмотрение', 'На рассмотрение'),
        ('Одобрено', 'Одобрено'),
        ('Отклонено', 'Отклонено')
    )
    type_status = models.CharField(
        'Статус мероприятия',
        choices=CHOICE_TYPE_STATUS,
        max_length=40,
        default='На рассмотрение',
    )
    description_status = models.TextField(
        'Если одобрено с пометками или отклонено, то объясните почему.',
        max_length=300,
        blank=True,
        null=True,
        default=''
    )

    def __str__(self):
        return f'[{self.user}] {self.name}'

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятие'


class ResponseEvent(models.Model):
    faction_link = models.CharField(
        'Ссылка на фракцию',
        max_length=300,
    )
    vk = models.CharField(
        'Ваш Вконтакте',
        max_length=120,
        help_text='Вконтакте фракционный'
    )
    description = models.CharField(
        'Описание / предпочтение в ивенте',
        max_length=130,
    )
    antispam = models.BooleanField(
        'Если мероприятие фейк - поставьте галочку',
        default=False
    )
    user = models.ForeignKey(
        Users,
        related_name='users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    archive = models.BooleanField(
        'Архив',
        default=False
    )

    def __str__(self):
        return f'[{self.active}] {self.vk}'

    class Meta:
        verbose_name = 'Заявление на мероприятия'
        verbose_name_plural = 'Заявление на мероприятии'
