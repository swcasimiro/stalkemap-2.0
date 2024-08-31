from django.db import models
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(
        'Название локации',
        max_length=120,
        db_index=True
    )
    slug = models.SlugField(
        'URL - автоматически загружается',
        max_length=200,
        db_index=True,
        unique=True
    )
    image = models.ImageField(
        upload_to='locations/%Y/%m/%d',
        blank=True,
        help_text='Фотография будет высвечиваться в категории локации.'
                  'Загружайте хорошего качества. Желательно full-hd. '
    )
    type_locations = (
        ('Красная', 'Красная'),
        ('Желтая', 'Желтая'),
        ('Зеленая', 'Зеленая'),
    )
    type = models.CharField(
        'Статус локации',
        choices=type_locations,
        max_length=40,
        null=True,
        help_text='Выставляйте статус локации. Для худзоны есть отдельная db!'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('location-list', kwargs={'slug': self.slug})


class Hood(models.Model):
    location = models.ForeignKey(
        Location,
        related_name='Location',
        on_delete=models.PROTECT,
        help_text='Выберите локацию на которой находится худзона'
    )
    slug = models.SlugField(
        'URL - автоматически загружается',
        max_length=200,
        db_index=True,
        unique=True
    )
    name = models.CharField(
        'Название худа',
        max_length=50
    )
    description = models.TextField(
        'Описание худзоны',
        max_length=500,
    )
    status_zone = (
        ('Красная', 'Красная'),
        ('Желтая', 'Желтая'),
        ('Зелёная', 'Зелёная'),
    )
    status = models.CharField(
        'Статус площадки',
        choices=status_zone,
        max_length=30,
    )
    faction_name = models.CharField(
        'Название фракции',
        max_length=120,
        default='Свободна'
    )
    faction_link = models.CharField(
        'Ссылка на фракцию',
        null=True,
        max_length=300,
        default='#'
    )
    image = models.ImageField(
        upload_to='images',
        help_text='Формат фотографии КВАДРАТ от 600x600'
    )
    popular = models.BooleanField(
        'Популярность',
        default=False,
        help_text='Если место популярное. Оставляйте активным. '
                  'В ином случае - нет. Влияет лишь на попадания '
                  'в раздел популярно.'
    )
    medical = models.BooleanField(
        'Присутствие медика',
        default=False,
        help_text='Если медик присутствует - тыкайте на актив.'
    )
    technician = models.BooleanField(
        'Присутствие техника',
        default=False,
        help_text='Если медик присутствует - тыкайте на актив.'
    )
    salesman = models.BooleanField(
        'Присутствие торгаша',
        default=False,
        help_text='Если торгаш системный/игрок присутствует - тыкайте на актив.'
    )

    def __str__(self):
        return f'[{self.location}] {self.name} - {self.status} зона'

    class Meta:
        verbose_name = 'Худ'
        verbose_name_plural = 'Худ'
