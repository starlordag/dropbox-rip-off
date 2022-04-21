import dropbox 
import os

from dropbox.files import WriteMode

class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token='sl.BGGl7iq8gWekzT_DMCJLlaDx7Aujqlqdyba0KM0rdfRd9a68Ifz9qFjss2mGkjMiqBL9Cbl00nH2pdSCIt4a2eLHXSHtKxypwdbyAtdFaUFKCTQkKN2IDHdvNpGeXGal169z0H-gg9U'
    transferdata=Transferdata(access_token)
    file_from=input('enter the file path to tranfer :-')
    file_to=input("eneter the full path to upload to dropbox :-")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved for your convinience!")

main()