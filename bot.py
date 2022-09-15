# This example requires the 'message_content' intent.
from dotenv import load_dotenv
import os
import discord
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def upload():
    upload_file_list = ['1.jpg', '2.jpg']
    for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload() # Upload the file.

@client.event
async def on_ready(): 
    print(f'Ready! 🚀\nWe have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        await message.channel.send("Llego un file!")


    if message.content.startswith('hello!'):
        await message.channel.send(f'Hello madafaka! {message.author}')



client.run(os.getenv('BOT_TOKEN'))
