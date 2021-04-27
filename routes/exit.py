from modules.view import Confirm
from routes.save import Save

def exit():
    msg = ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah?")
    if Confirm(msg):
        Save()
    