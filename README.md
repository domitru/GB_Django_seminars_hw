## Framework-Django

### gbhtproject

--------------------

### 📌 ht01app

- Создайте пару представлений в вашем первом приложении: главная и о себе.
- Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о вашем
первом Django сайте и о вас.
- *Сохраняйте в логи данные о посещении страниц

--------------------

### 📌 ht02app

- Создайте три модели Django: клиент, товар и заказ. Клиент может иметь несколько заказов. Заказ может содержать
несколько товаров. Товар может входить в несколько заказов.
- Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента
- Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара
- Поля модели "Заказ":
○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ
○ связь с моделью "Товар", указывает на товары, входящие в заказ
○ общая сумма заказа
○ дата оформления заказа
- *Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе данных.

--------------------

### 📌 ht03app

- Доработайте задачу из прошлого ht02app про клиентов, товары и заказы
- Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
- Подготовьте необходимый маршрут и представление.
- Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
- *Товары в списке не должны повторяться.

--------------------

### 📌 ht04app

- Измените модель продукта, добавьте поле для хранения фотографии продукта.
- Создайте форму, которая позволит сохранять фото.

- --------------------

### 📌 ht05: ht04app/admin.py

- Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации об объекте
и вывода списка объектов.

--------------------

### 📌 ht06
