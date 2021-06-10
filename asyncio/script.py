import asyncio
import aiosqlite
from email.message import EmailMessage
import aiosmtplib


async def send_message(username, password, to, subject, text):

    message = EmailMessage()
    message["From"] = username
    message["To"] = to
    message["Subject"] = subject
    message.set_content(text)

    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username=username,
        password=password
    )


async def get_contacts(db_file):
    async with aiosqlite.connect(db_file) as conn:
        cursor = await conn.execute("SELECT first_name, last_name, email FROM contacts")
        rows = await cursor.fetchall()
        return rows


async def main(db_file, username, password):
    contacts = await get_contacts(db_file)
    tasks = []
    for contact in contacts:
        name = f'{contact[0]} {contact[1]}'
        text = f'Уважаемый {name}! Спасибо, что пользуетесь нашим сервисом объявлений.'
        task = asyncio.create_task(send_message(
            username=username,
            password=password,
            to=contact[2],
            subject='Привет!:)',
            text=text)
        )
        tasks.append(task)
    result = await asyncio.gather(*tasks)

