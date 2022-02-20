

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>I ᴀᴍ 𝙇𝙂𝙘𝙔・𝘽𝙊𝙏 \n</b>ʙᴏᴛ ʜᴀɴᴅʟᴇʜᴀɴᴅʟᴇ ʙʏ [𝙇𝙂𝙘𝙔・𝘼𝙇𝙀𝙓](https://t.me/lgcyalex) \n<b>Do /help For More</b>",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>𝙎𝙚𝙣𝙙 𝙈𝙚 𝘼𝙣𝙮 𝙑𝙞𝙙𝙚𝙤 𝙊𝙧 𝙋𝙝𝙤𝙩𝙤 𝙄 𝙬𝙞𝙡𝙡 𝙐𝙥𝙡𝙤𝙖𝙙 𝙄𝙩 𝙄𝙣𝙩𝙤 Telegra.ph.</b> \n<b>Created By @LGcYALEX</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @LGcYALEX")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @LGcyALEX")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

