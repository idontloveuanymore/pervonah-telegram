from pyrogram import Client, filters, types
from pyrogram.errors.exceptions.forbidden_403 import Forbidden
from config import App_api_id, App_api_hash, My_number, channels

app = Client("my_account", api_id=App_api_id, api_hash=App_api_hash, phone_number=My_number)

async def reply_to_channel(client, channel, message_id, comment):
    try:
        dm = await client.get_discussion_message(channel, message_id)
        await dm.reply(comment)
    except Forbidden:
        await dm.chat.join()
        await dm.reply(comment)
    except Exception as e:
        print(f"Unexpected Error: {e}")

@app.on_message(filters.chat(list(channels.keys())))
async def handle_message(client, message: types.Message):
    channel = message.chat.username
    comment = channels[channel]
    await reply_to_channel(client, channel, message.id, comment)

if __name__ == "__main__":
    print("Starting the client...")
    app.run()
