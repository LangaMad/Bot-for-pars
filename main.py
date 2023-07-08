import asyncio
from datetime import datetime

from telethon import TelegramClient, events
from telethon.tl.types import InputMediaPhoto

from TOKEN import API,HASH , TOKEN
import re
import os
# Замените значения на свои, полученные в панели разработчика Telegram
api_id = API
api_hash = HASH

# Название сессии, по которой будет сохранена информация об авторизации
session_name = 'my_session'

bot_id  = 5801121725
group_id = -807595653  #-998111948
channel_id = -1001264468818
channel_id_2 = -1001340312639
channel_id_3 = -1001740033990
# Создание объекта TelegramClient
client = TelegramClient(session_name, api_id, api_hash)


async def main():
    try:
        await client.start()
        print("Client created!")
        me = await client.get_me()
        print(me.stringify())
    except Exception as e:
        print("Error while logging in:", e)

# Обработчик новых сообщений из канала
@client.on(events.NewMessage(chats=(channel_id,channel_id_2,channel_id_3)))

async def my_event_handler(event):
    try:

        # Если сообщение содержит только фото (без прикрепленного сообщения)

        if event.message.message:
            if event.media and event.photo:
                message = re.sub(r'''http\S+|www.\S+|t.me\S+|🛍|✅|🌷|\b(Телеграм|Вотсап
                                               |вотсап|писать на|телеграм|Менеджер|менеджер|Мунара|Сымбат|Нуркыял|Медина
                                               |Жаннат|Дианы|Эладена|Нура|Айдана|Альбина|Акбермет|Наргиза|Бегимай|Диана|Закуп товара ОПТОМ/ВБ
                                               |менеджера|Ширин|Сезимай|Обзор от|Керемет|
                                               Астра|Мадина|Тоша|Байер|Асема|байер|Асель|Нуриза
                                               |Гульзада|Дания|Адинай|Гулиза|Анеля|
                                               Алтынай|Надия|Мээрим|||)\b''', ' ', event.message.message)

                message = message.strip().replace('\n\n', '\n')
                message += '\n@Jaka_Dordoi_Trend'
                photo = await event.download_media()

                await client.send_file(group_id, photo, caption=message)
                os.remove(photo)





    except Exception as e:
        print("Error while processing message:", e)


# Запуск клиента
with client:
    client.loop.run_until_complete(main())
    # Добавляем обработчик события "разрыв соединения"
    client.run_until_disconnected()



