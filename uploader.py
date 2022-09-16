from matplotlib.font_manager import json_load
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json


gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

folderIds = {}

def open_folderId():
    with open('ids.json', 'r') as fp:
        folderIds = json.load(fp)

def save_folderIds():
    with open('ids.json', 'w') as fp:
        json.dump(folderIds, fp)
    print("New IDs were saved.")

def add_folder(new_channel_id, drive_folder_id):
    if len(folderIds) == 0: open_folderId()
    folderIds[new_channel_id] = drive_folder_id


def upload(filename, channelId):
    with open('ids.json', 'r') as fp:
        folderIds = json.load(fp)
    print("upload filename", filename)

    folderId = folderIds[channelId]
    file1 = drive.CreateFile({
        'title': filename, 
        'parents':[
            {'kind': 'drive#fileLink', 
            'id':folderId 
            }]
        })
    file1.SetContentFile(f'files/{filename}')
    file1.Upload() # Upload the file.


