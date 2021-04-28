from modules.view import Confirm
from routes.save import SaveRoute

def ExitRoute():
    msg = "Apakah Anda mau melakukan penyimpanan file yang sudah diubah?"
    if Confirm(msg):
        SaveRoute()
    
