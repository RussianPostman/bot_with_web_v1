# bot_with_web_v1

Это сервис развивающий идею из проекта My_test_bot (https://github.com/RussianPostman/My_test_bot)

Сервис состоит из трёх контейнеров:
- bot - по-сути это простосто бот из проекта My_test_bot. 
- google_auth - Приложение на Flask, реализующее авторизацию через Google's OAuth2. Если CLIENT_ID в полученом токине совпадает с заданным в переменных окружениея (CLIENT_ID владельца сервиса), происходит сохранение в общий для бота и Flask приложения Docker volume.
- nginx - прокси сервис для развёртки на удалённом сервере.

Это не финальная идея, а обкатка технологий взаимодействия систем. В данных момент, на основании опыта этого проекта, разрабатывается система на Doсker Swarm. Преимущество новой технологии в модульности и практически неограниченной масштабируемости, а так же лёгким подключением HTTPs протокола, необходимого для OAuth2 аутентификации. 