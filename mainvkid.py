import telebot
import random
#create file secretdocuments
#from secretdocuments import admin_id1, admin_id2, bot_id
#admin_id1, admin_id2 - id in telegram, bot_id - bot id

bot = telebot.TeleBot(bot_id)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет папищек! Присылай сюда мемы и мы будем рассматривать их!")
    bot.send_message(message.chat.id, "Отправь изображение чтобы отправить в предложку, отправь сюда фото")
@bot.message_handler(content_types=['photo'])
def send_photo_to_admin(message):
    First_name = message.from_user.first_name
    Last_name = message.from_user.last_name
    random_num = random.randint(0, 2)
    if random_num == 0:
        random_string = "Хммм, мы посмотрим"
    elif random_num == 1:
        random_string = "Принято, посмотрим"
    else:
        random_string = "Получили, глянем"
    photo_to_admin = message.photo[-1].file_id
    bot.send_message(message.chat.id, random_string)
    bot.send_photo(admin_id2, photo_to_admin)
    bot.send_message(admin_id2, f"Сообщение от {First_name} {Last_name}")
    bot.send_photo(admin_id1, photo_to_admin)
    bot.send_message(admin_id1, f"Сообщение от {First_name} {Last_name}")

bot.infinity_polling()
