from script import main
import asyncio

if __name__ == '__main__':
    username = input('Введите вашу Gmail почту: ')
    password = input('Введите пароль вашей почты: ')
    asyncio.run(main('contacts.db', username, password))