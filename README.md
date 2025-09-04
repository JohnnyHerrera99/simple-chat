# Simple Chat
This is a simple chat application built in Django, Channels and Redis.

## Dependencies
To run the app you must have previously installed `docker-compose` https://docs.docker.com/compose/install/

## Installation
Go to a directory and execute the following commands.

```
git clone https://github.com/JohnnyHerrera99/simple-chat.git && cd simple-chat
docker-compose build --no-cache
docker-compose up -d
```
If everything goes correctly, the application should be available on `localhost:8000` or `127.0.0.1:8000`

## Use
For the use of the chat it is mandatory to be registered, the registration can be found in this path `/accounts/register/`. Once registered you will be logged in and redirected to the page to choose the room you wish to enter.

When you wish to log out there is a link next to your username that will log you out and take you to the login page.

## Monitoring and Logs
For the application monitor, Django's native LogEntry is used to log message entries. You can access with a staff user in the admin panel where to find the logs.

In addition the loggin is used for the entries and interactions of each view, you can see it in the root of the project in the `loggin.log` file. Having the docker-compose active, you can access it using this command:
```
docker-compose exec django sh
tail -f loggin.log
```

## Test cases
Test cases can be run manually through this command:
project in the `loggin.log` file. Having the docker-compose active, you can access it using this command:
```
docker-compose exec django sh
python manage.py test
```

## Note
This application is NOT intended for production use and is merely a demonstration of how the django framework can be used to make connections using WebSockets.
