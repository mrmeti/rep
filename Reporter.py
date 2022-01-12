from telethon.sync import TelegramClient
from telethon import functions, types
from colorama import Fore
from datetime import datetime
from os import name , system
from time import sleep
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
cyan = Fore.CYAN
lightgreen = Fore.LIGHTGREEN_EX
if name == 'nt':
	system('cls')
else:
	system('clear')
print(cyan+'╔═══════════════════════════════════════════════════════════════╗')
sleep(0.1)
print(cyan+'║  ████████╗███████╗██╗     ███████╗██╗  ██╗██╗██╗     ██╗      ║')
sleep(0.1)
print(cyan+'║  ╚══██╔══╝██╔════╝██║     ██╔════╝██║ ██╔╝██║██║     ██║      ║')
sleep(0.1)
print(cyan+'║     ██║   █████╗  ██║     █████╗  █████╔╝ ██║██║     ██║      ║')
sleep(0.1)
print(cyan+'║     ██║   ██╔══╝  ██║     ██╔══╝  ██╔═██╗ ██║██║     ██║      ║')
sleep(0.1)
print(cyan+'║     ██║   ███████╗███████╗███████╗██║  ██╗██║███████╗███████╗ ║')
sleep(0.1)
print(cyan+'║     ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ║')
sleep(0.1)
print(cyan+'╚═════════════════════════[Cᴏᴅᴇᴅ Bʏ Mᴇᴛɪᴡᴢ Tᴇᴀᴍ]═════════════════════════╝')
sleep(0.3)
name = 'Mᴇᴛɪᴡᴢ Tᴇᴀᴍ Tᴇʟᴇɢʀᴀᴍ Rᴇᴘᴏʀᴛᴇʀ'
api_hash = input(red+'┌─['+lightgreen+'Sᴄʀɪᴘᴛ'+blue+'~'+white+'Pʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ Tʜᴇ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ Aᴘɪ Hᴀsʜ : '+red+''']
└──╼ '''+white+'卍 ')
api_id = input(red+'┌─['+lightgreen+'Sᴄʀɪᴘᴛ'+blue+'~'+white+'Pʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ Tʜᴇ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ Aᴘɪ ID : '+red+''']
└──╼ '''+white+'卍 ')
target = input(red+'┌─['+lightgreen+'Sᴄʀɪᴘᴛ'+blue+'~'+white+'Pʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ Tʜᴇ ᴛᴀʀɢᴇᴛ ID : '+red+''']
└──╼ '''+white+'卍 ')
post_id = input(red+'┌─['+lightgreen+'Sᴄʀɪᴘᴛ'+blue+'~'+white+'Pʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ Tʜᴇ Tᴀʀɢᴇʀ Pᴏsᴛs ID : '+red+''']
└──╼ '''+white+'卍 ')
msg = input(red+'┌─['+lightgreen+'Sᴄʀɪᴘᴛ'+blue+'~'+white+'Pʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ Tʜᴇ Yᴏᴜʀ Rᴇᴘᴏʀᴛ Mᴇssᴀɢᴇ : '+red+''']
└──╼ '''+white+'卍 ')
while True:
    now = datetime.now()
    timee = now.strftime("%H:%M:%S")
    with TelegramClient(name, api_id, api_hash) as client:
        result = client(functions.messages.ReportRequest(
            peer=target,
            id=[post_id],
            reason=types.InputReportReasonSpam(),
            message=msg
        ))
        print(green+F'[{timee}]'+red+'Mᴇᴛɪᴡᴢ Tᴇᴀᴍ Tᴇʟᴇɢʀᴀᴍ Rᴇᴘᴏʀᴛᴇʀ Rᴇsᴜʟᴛ : ' + str(result))

#Coded By Mahdi Tabrizi version 9 python (Termux - Terminal)