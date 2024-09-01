## Stalker-map2.0


<img src="https://img.shields.io/badge/django 3.2.9-Django Rest Framework-red?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 

<p>Данное приложение новая версию к <a href="https://github.com/swcasimiro/stalker-map">существующему</a>. Практически заново написанный проект. Переработан функционал и подход к реализации. Немного асинхронности и реализация api.</p>


<strong><p>Краткий перечень нововведений:</p></strong>
<ul>
<li>Поиск убран, вместо этого всё разбито на категории по локациям.</li>
<li>Некоторые функции во <strong>views</strong>, переписаны на асинхронный Python.</li>
<li>Написана полноценная система взаимодействия ивентеров с обычными игроками. Представляет из себя форму для запроса мероприятия. В дальнейшем ивент-команда может обрабатывать этот запрос.</li>
<li>Написан API для модели локаций. И многое другое.</li>
</ul>
<hr>
<strong><p>Активация проекта:</p></strong>
<code>python -m venv venv</code>
<br>
<br>
<code>venv\Scripts\activate.bat</code>
<br>
<br>
<code>pip install -r requirements.txt</code>
<br>
<br>
<code>python manage.py makemigrations</code>
<br>
<br>
<code>python manage.py migrate</code>
<br>
<br>
<code>python manage.py createsuperuser</code>
<br>
<br>
