from modules.view import Confirm
from modules.store import GetCurrentUser
from routes.save import SaveRoute
from modules.store import GetCurrentUser

def ExitRoute():
    user = GetCurrentUser()
    if user is not None:
        msg = "Apakah Anda mau melakukan penyimpanan file yang sudah diubah?"
        if Confirm(msg):
            SaveRoute()
    
    print("Exiting...")
    print("Terimakasih sudah menggunakan katong ajaib kami. Sampai jumpa lagi")
