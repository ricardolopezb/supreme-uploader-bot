# This example requires the 'message_content' intent.
from dotenv import load_dotenv
import os
import discord
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from uploader import upload, add_folder, save_folderIds
import json

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
    
def get_filename(text, offset):
    if offset > len(text):
        raise Exception('Offset longer than str length')
    return text[offset:]

folder_ids= {}
#folder_ids = json.load(open('folderIds.json', 'r'))
#dawdawdwadawd
@client.event
async def on_ready(): 
    print(f'Ready! 🚀\nWe have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments and message.content.startswith('/upload'):
        try:
            nameToSave = get_filename(message.content, 8)
        except:
            nameToSave = message.attachments[0].filename
        
        await message.attachments[0].save(f'files/{nameToSave}')
        upload(nameToSave, str(message.channel.id))
        await message.channel.send("Archivo subido!")


    if message.content.startswith('/add'):
        add_folder(str(message.channel.id), get_filename(message.content, 5))
        print(message.channel.name, "has been saved in folderIds as", message.channel.id)
    

    if message.content.startswith('/save'):
        save_folderIds()


    if message.content.startswith('hello!'):
        await message.channel.send(f'Hello madafaka! {message.author}')



client.run(os.getenv('BOT_TOKEN'))
