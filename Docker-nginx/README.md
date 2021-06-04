Для запуска потребуется ввести следующие косанды в консоль:

    `docker build --tag=mynginx .`

    `docker run -d --name mynginx-container -p 8000:80 mynginx`

Основная страница будет доступна по адресу localhost:8000
