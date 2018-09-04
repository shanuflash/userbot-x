from telethon import TelegramClient, events
import os
phone_number=os.environ['PH']
api_id=os.environ['API_KEY']
api_hash=os.environ['API_HASH']
client = TelegramClient('session name', api_id, api_hash)
client.start(phone_number)
@client.on(events.NewMessage(pattern='(?i)hi'))
async def hi(e):
    await e.reply('Hello!')
@client.on(events.NewMessage(pattern='(?i)list'))
async def list(e):
    participants = client.get_participants(group)
    await bot.send_message(e.chat_id, participants)
client.run_until_disconnected()
