## Stalker-map2.0


<img src="https://img.shields.io/badge/django 3.2.9-black?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 

<p>Данное приложение новая версию к <a href="https://github.com/swcasimiro/stalker-map">существующему</a>. Практически заново написанный проект. Переработан функционал и подход к реализации. Немного асинхронности и реализация api.</p>

<strong><p>Используемые технологии:</p></strong>
  <p>Все использованные инструменты, которые были задействованы в реализации данного проекта.</p>
<div>
<p><code>Языки программирования</code></p>
  <a>
    <img src="https://img.shields.io/badge/python-346c99?style=for-the-badge&logo=python&logoColor=fecd3a" alt="Python Badge"/>

  </a>
<br>
<br>  
<p><code>Фреймворк</code></p>

<a>
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>
    <img src="https://img.shields.io/badge/django 3.2.9-Django Rest Framework-red?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 
</a>
<br>
<br>
<p><code>База данных</code></p>
<a>
  <img src="https://img.shields.io/badge/postgresql-316093?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge"/>
</a>
<a>
    <img src="https://img.shields.io/badge/sqlite-3f9cd8?style=for-the-badge&logo=sqlite&logoColor=white" alt="nginx Badge"/>
</a>

</div>

<br>

<strong><p>Краткий перечень нововведений:</p></strong>
<ul>
<li>Поиск убран, вместо этого всё разбито на категории по локациям.</li>
<li>Некоторые функции во <strong>views</strong>, переписаны на асинхронный Python.</li>
<li>Написана полноценная система взаимодействия ивентеров с обычными игроками. Представляет из себя форму для запроса мероприятия. В дальнейшем ивент-команда может обрабатывать этот запрос.</li>
<li>Написан API для модели локаций. И многое другое.</li>
</ul>
<hr>
<strong><p>Активация проекта:</p></strong>
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


<strong><p>Инструкция при первом запуске:</p></strong>
<p>Перед использованием административной панели и создание новый суперюзеров. Ознакомьтесь с инструкцией ниже. Пользователь создан с которым вы можете перейти на следующий этап. А именно заполнению
самого сайта нужным вам контентом.</p>
<ul>
<li>База данных заполнена.</li>
<li>Произведены миграции</li>
<li>Создан superuser
<ul>
<li>Login: root</li>
<li>Password: 123</li>
</ul></li>
<li>Категории товаров создаются через административную панель</li>
</ul>

<br>
<strong><p>Адреса для входа в административную панель:</p></strong>
<ul>
<li>http://127.0.0.1:8000/admin/</li>
<li>http://localhost/admin/</li>
<li><code>http://domain_name.ru/admin/</code></li>
</ul>
