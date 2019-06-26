#@urrGoTo_bot
import telebot
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green

import pdfrw
from reportlab.pdfgen import canvas

token = "662005408:AAGlsrD4kN6sHxy4PoEd45tnKRwbLZ8ea-c"

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

bot = telebot.TeleBot(token = token)

a = []

@bot.message_handler(commands=['start'])
def bott(message):
    global a
    a = []
    bot.send_message(message.chat.id, "Привет, меня зовут urrGoTo_bot и я помогу вам заполнить договор для поступления в GoTo School!")
    bot.send_message(message.chat.id, "Введите имя!\nВведите фамилию!\nВведите место рождения!\nВведите дату рождения\nВведите паспортные данные!")

@bot.message_handler(content_types=['text'])
def echo(message):
    global a
    if len(a) <= 4:
        a.append(message.text)
    else:
        bot.send_message(message.chat.id, "Ок, сейчас всё будет!")
        create_simple_form()

def create_simple_form():
    c = canvas.Canvas('simple_form.pdf')

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Employment Form')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, 'First Name:   ' + str(a[0]))

    c.drawString(10, 600, 'Last Name:   ' + str(a[1]))

    c.drawString(10, 550, 'Address:   ' + str(a[2]))

    c.drawString(10, 500, 'Birthday:   ' + str(a[3]))

    c.drawString(250, 500, 'Passport Number:   ' + str(a[4]))

    c.save()
    bot.send_document()


bot.polling(none_stop=True)
