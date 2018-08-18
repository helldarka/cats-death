import uuid
import telebot
import random
import PIL
from PIL import Image
from telebot import types


files = {}
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
token = "676260489:AAFaMj85on44WgEGssFWN3vSOJnto89EI2g"
bot = telebot.TeleBot(token=token)
def process1(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    i = (img.width)
    j = (img.height)
    yakov = Image.open('yakov.png')
    yakov = yakov.resize(img.size)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 2, j // 2), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 4, j // 4), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 8, j // 8), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 16, j // 16), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 32, j // 32), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    yakov = yakov.resize((i // 64, j // 64), Image.BICUBIC)
    img.paste(yakov, (0, 0), yakov)
    img.save(files[user])
def process2(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    i = (img.width)
    j = (img.height)
    mark = Image.open('cat.png')
    mark = mark.resize((img.width, img.height), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    mark = Image.open('cat4.png')
    mark = mark.resize((img.width // 2, img.height // 2), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    mark = Image.open('cat2.png')
    mark = mark.resize((img.width // 4, img.height // 4), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    mark = Image.open('cat.png')
    mark = mark.resize((img.width // 8, img.height // 8), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    mark = Image.open('cat4.png')
    mark = mark.resize((img.width // 16, img.height // 16), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    mark = Image.open('cat2.png')
    mark = mark.resize((img.width // 32, img.height // 32), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    img.save(files[user])
    img.save(files[user])
def process3(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
                pixels = img.load()
                r, g, b = pixels[i, j]
                z = (r + g + b) // 3
                if z > 100:
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = 0, 0, 0
                pixels[i, j] = r, g, b
        img.save(files[user])
def process4(message):
    user = message.chat.id
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
            pixels = img.load()
            r, g, b = pixels[i, j]
            r, g, b = b, r, g
            pixels[i, j] = r, g, b
    mark = Image.open('texnik.png')
    mark = mark.resize((img.width, img.height), Image.BICUBIC)
    img.paste(mark, (0, 0), mark)
    img.save(files[user])
def process5(message):
    img = Image.open(files[message.chat.id])
    for i in range(img.width):
        for j in range(img.height):
            pixels = img.load()
            r, g, b = pixels[i, j]
            z = (r + g + b) // 3
            if z > 100:
                r, g, b = r + 20, g, b
            if z > 140:
                r, g, b = r + 45, g, b
            if z > 100:
                r, g, b = r, g + 30, b
            else:
                r, g, b = r + 40, g - 30, b + 90
            pixels[i, j] = r, g, b

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_id = message.chat.id
    user = message.chat.id
    bot.send_message(user, '📷 Отправь мне фотографию, которую хочешь обработать!')
    bot.send_photo(user, "https://i.imgur.com/tEJYtBN.jpg")
@bot.message_handler(content_types=['photo'])
def photo(message):
    keyboard = types.InlineKeyboardMarkup()
    user = message.chat.id
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)
    extn = '.' + str(path.file_path).split('.')[-1]
    pikcha = 'images/' + str(uuid.uuid4()) + extn
    with open(pikcha, 'wb') as new_file:
        new_file.write(downloaded_file)
    files[user] = pikcha
    button1 = types.InlineKeyboardButton(text='RECURSIVE YAKOV 👼', callback_data="button1")
    button2 = types.InlineKeyboardButton(text='RECURSIVE CATS 🐈', callback_data="button2")
    button3 = types.InlineKeyboardButton(text='BANKSY 🎆', callback_data="button3")
    button4 = types.InlineKeyboardButton(text='PASHA TECHNIQUE 🐒', callback_data = 'button4')
    button5 = types.InlineKeyboardButton(text='L$D 😳', callback_data='button5')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    bot.send_message(user, 'Пожалуйста выберите фильтр', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def photoo(call):
    user = call.message.chat.id
    if call.message:
        if call.data == 'button1':
            process1(call.message)
        if call.data == 'button2':
            process2(call.message)
        if call.data == 'button3':
            process3(call.message)
        if call.data == 'button4':
            process4(call.message)
        if call.data == 'button5':
            process5(call.message)
        with open(files[user], 'rb') as new_file:
            bot.send_photo(user, new_file.read())
bot.polling(none_stop=True)