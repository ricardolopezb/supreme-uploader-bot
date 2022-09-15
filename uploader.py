from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, glob


gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 


def upload():
    # upload_file_list = ['SQL.pdf']
    # for upload_file in upload_file_list:
    #     gfile = drive.CreateFile({'parents': [{'id': '1oSOvj_obkaEec6v1BNhN7XtVX_0YplfN-t'}]})
    #     # Read file and set it as the content of this instance.
    #     gfile.SetContentFile(upload_file)
    #     gfile.Upload() # Upload the file.

    # with open("SQL.pdf","r") as file:
    #     file_drive = drive.CreateFile({'title':os.path.basename(file.name) })  
    #     file_drive.SetContentString(file.read()) 
    #     file_drive.Upload()

    # folder_id = '1oSOvj_obkaEec6v1BNhN7XtVX_0YplfN-t'
    # f = drive.CreateFile({'title': 'testing_pdf',
    #                     'mimeType': 'application/pdf',
    #                     'parents': [{'kind': 'drive#fileLink','id':folder_id}]})
    # f.SetContentFile('SQL.pdf')
    # f.Upload()
    file1 = drive.CreateFile({'title': 'SQL.pdf'})
    file1.SetContentFile('SQL.pdf')
    file1.Upload() # Upload the file.

upload()

