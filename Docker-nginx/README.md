Для запуска потребуется ввести следующие косанды в консоль:

Эта команда создаст docker image mynginx на основе [Dockerfile](Dockerfile).

    docker build --tag=mynginx .

Эта команда создаст и запустит docker container mynginx-container, PORT = 8000


    docker run -d --name mynginx-container -p 8000:80 mynginx

Основная страница будет доступна по адресу [localhost:8000](localhost:8000)
