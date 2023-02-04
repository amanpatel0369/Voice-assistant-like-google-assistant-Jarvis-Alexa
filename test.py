import sys
from lib2to3.pgen2.token import EQUAL
import smtplib
from datetime import datetime
from scipy.constants import hour
from neuralintents import GenericAssistant
import PyPDF2
import os
import webbrowser as wb
import psutil
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from PyQt5 import uic
from PyQt5.uic import loadUiType
from ARIESGUI import Ui_MainWindow
import wikipedia as wp

todo_list = []

def speak(text):
    os.system("echo \"" + text + "\" > test.txt")
    os.system("festival --tts test.txt")


def wish():
  current_time=datetime.now()
  hour = int(current_time.strftime("%H"))

  if hour>=0 and hour<=12:
        speak("Good Morning")
  elif hour>12 and hour<=18:
        speak("Good Evening")
  else:
        speak("Good Afternoon")

def battery():
    bat = psutil.sensors_battery()
    per=int(bat.percent)
    plug = bat.power_plugged
    speak(f'current battery of system is +{per} percentage')
    if plug == True:
        speak("Your system is on charging mode")
        print("Your system is on charging mode")
    else:
        speak("your system is not plugged in")
        print("your system is not plugged in")

def wiki():
    query = input("what do you want to search")
    print("Searching From Wikipedia")
    query = query.replace("wikipedia", "")
    text = wp.summary(query)
    print(text)
    speak(text)


def add_todo():
    item = input("what item do you want to add in your to do list\n")
    todo_list.append(item)


def pdf_reader():
    book = open('hello.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print(f"The number of pages in pdf are {pages}")
    print("sir please enter the page number i have to read")
    pg = int(input("Enter the page number"))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    print(text)


def show_todo():
    for i in todo_list:
        print(i)


def delete_todo():
    re = input("Which task do you want to remove from your to do list")
    if "1" in re or "one" in re:
        todo_list.remove(0)
    else:
        re = re - 1
        todo_list.remove(re)

        print(todo_list)


def function_for_stocks():
    print("You triggered the stocks intent!")
    # Some action you want to take




def function_for_mail():
    try:
        print("Sir please tell me i can manage all your work")
        send = input("whom do you want to send mail\n")
        message1 = input("what message do you want to send\n")
        mail = smtplib.SMTP_SSL("smtp.gmail.com", "465")
        mail.login("amanpatellll14@gmail.com", "fgssivybiqecirhg")
        mail.sendmail("amanpatellll14@gmail.com", f"{send}", f"{message1}")
        mail.quit()
        print("Message sent Successfully....................")

    except Exception as e:
        print("Sorry Sir Server establishment unsuccessful..........")


mappings = {
    'stocks': function_for_stocks,
    'mail': function_for_mail,
    'add_todo': add_todo,
    'show_todo': show_todo,
    'delete_todo': delete_todo,
    'pdf_reader': pdf_reader,
    'wiki': wiki
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
#assistant.train_model()
#assistant.save_model()
assistant.load_model()
'''def taskexecution():
    done = False
    wish()
    battery()

    speak("hello sir, how can i help you")
    while not done:

        message = input("Enter a message: ")

        if message == "stop" or message == "bye":
            speak("have a nice day")
            done = True
        elif 'open google' in message:
                wb.open("google.com")
        else:
            text = assistant.request(message)
            print(text)
            speak(text)'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------                GUI INTEGRATION         ---------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()


    def TaskExecution(self):

        done = False
        wish()
        battery()

        speak("hello sir, how can i help you")
        while not done:

            message = input("Enter a message: ")

            if message == "stop" or message == "bye":
                speak("have a nice day")
                done = True
            elif 'open google' in message:
                wb.open("google.com")
            else:
                text = assistant.request(message)
                print(text)
                speak(text)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.youtube)
        self.ui.pushButton_4.clicked.connect(self.hackerrank)
        self.ui.pushButton_5.clicked.connect(self.whats)
        self.ui.pushButton_6.clicked.connect(self.setting)
        self.ui.pushButton_7.clicked.connect(self.instagram)
        self.ui.pushButton_8.clicked.connect(self.file)

    def youtube(self):
        wb.open("youtube.com")

    def hackerrank(self):
        wb.open("hackerrank.com")

    def whats(self):
        wb.open("web.whatsapp.com")

    def file(self):
        os.system("nautilus")

    def setting(self):
        os.system("gnome-control-center")

    def instagram(self):
        wb.open("instagram.com")

    def facebook(self):
        wb.open("facebook.com")

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../../../home/aman/Pictures/aries/9e759fd37ccd98da121b670249f34afa.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        #self.ui.movie1 = QtGui.QMovie("../../../../home/aman/Pictures/aries/Dune_ Mentat.gif")
        #self.ui.label_2.setMovie(self.ui.movie1)
        #self.ui.movie1.start()
        #self.ui.movie.start()

        startExecution.start()

        def showtime():
            current_time = QTime.currentTime()
            current_date=QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.ISODate)
            #self.ui.text

app = QApplication(sys.argv)
test = Main()
test.show()
exit(app.exec_())





'''from  vosk import Model , KaldiRecognizer
import pyaudio

model = Model("/media/aman/F6CADA9ECADA5A87/ARIES/1)vosk-model-en-in-0.5/vosk-model-en-in-0.5")
reco = KaldiRecognizer(model , 16000)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if reco.AcceptWaveform(data):
        a = (reco.Result()[14:-3])
        print(a)'''



