import telebot
import random
from io import BytesIO
from PIL import Image
import requests
from api import api_joke, api_cat, api_dog

bot = telebot.TeleBot('TG_BOT')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.from_user.first_name)


@bot.message_handler(commands=['cat'])
def cat(message):
    image_base = api_cat(message)
    for i in image_base.split():
        bot.send_photo(message.chat.id, i)


@bot.message_handler(commands=['dog'])
def dog(message):
    image_base = api_dog(message)
    for i in image_base.split():
        bot.send_photo(message.chat.id, i)


@bot.message_handler(commands=['joke'])
def joke(message):
    joke_text = api_joke(message.text)
    bot.send_message(message.chat.id, joke_text)


@bot.message_handler(commands=['lol'])
def lol(message):
    while True:
        alfa = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        abc = ''
        for i in range(4096):
            abc += alfa[random.randint(0, 25)]
        bot.send_message(message.chat.id, abc)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'id \n \n'
                                      ' is_bot \n \n'
                                      ' first_name \n \n'
                                      ' last_name \n \n'
                                      ' username \n \n'
                                      ' is_premium \n \n'
                                      ' /info_api \n Комманды с API \n')


@bot.message_handler(commands=['info_api'])
def info_api(message):
    bot.send_message(message.chat.id,
                     ' /dog фото собак \n (вы можете получить несколько фото \n если введёте число после команды) \n \n'
                     ' /cat фото кошек \n (вы можете получить несколько фото \n если введёте число после команды) \n \n'
                     ' /lol прикол \n (попробуйте если хотите) \n\n'
                     ' /joke_info \n')
@bot.message_handler(commands=['info_joke'])
def info_joke(message):
    bot.send_message(message.chat.id,'/joke и цифра согласно таблице: \n'
                                     '1 - Анекдот \n'
                                     '2 - Рассказы\n'
                                     '3 - Стишки\n'
                                     '4 - Афоризмы\n'
                                     '5 - Цитаты\n'
                                     '6 - Тосты\n'
                                     '8 - Статусы\n')

@bot.message_handler()
def info_user(message):
    if message.text.lower() == 'id':
        bot.send_message(message.chat.id, message.from_user.id)

    elif message.text.lower() == 'is_bot':
        bot.send_message(message.chat.id, message.from_user.is_bot)
        if not message.from_user.is_bot:
            bot.send_message(message.chat.id, 'Ты не бот , красава')

    elif message.text.lower() == 'first_name':
        bot.send_message(message.chat.id, message.from_user.first_name)
        bot.send_message(message.chat.id, 'Хай бро')

    elif message.text.lower() == 'last_name':
        bot.send_message(message.chat.id, message.from_user.last_name)
        bot.send_message(message.chat.id, 'Здравствуйте мисье')

    elif message.text.lower() == 'username':
        bot.send_message(message.chat.id, message.from_user.username)

    elif message.text.lower() == 'is_premium':
        if message.from_user.is_premium is None:
            bot.send_message(message.chat.id, f'{message.from_user.is_premium} \n Хаххахах нищеброт')

        else:
            bot.send_message(message.chat.id, f'{message.from_user.is_premium} \n Тебе совсем некуда деньги девать?')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Получаем файл фотографии
        file_info = bot.get_file(message.photo[-1].file_id)
        file_path = file_info.file_path
        file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_path}'

        # Загружаем файл фотографии
        response = requests.get(file_url)
        img = Image.open(BytesIO(response.content))
        # Сохраняем фотографии
        image_name = f"new{message.from_user.username}_{random.randint(1, 1000000000)}.jpg"
        img.save(f'img/{image_name}')

        # Конвертируем в градации серого
        img = img.convert('L')

        # Изменяем размер изображения
        width = 100
        aspect_ratio = img.height / img.width
        new_height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, new_height))

        # Конвертируем изображение в ASCII
        pixels = img.getdata()
        chars = ["@", "#", "B", "%", "M", "W", "&", "8", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m",
                 "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f",
                 "t", "/", r"\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i",
                 "!", "l", "I", ";", ":", ",", r"\"", "^", "`", "'", ".", " "]
        ascii_str = "".join([chars[pixel // 4] for pixel in pixels])

        # Форматируем строку ASCII
        ascii_img = "\n".join([ascii_str[index: index + width] for index in range(0, len(ascii_str), width)])

        # Отправляем ASCII изображение
        if len(f'```\n{ascii_img}\n```') > 4096:
            for i in range(0, round(len(f'```\n{ascii_img}\n```') / 4096) + 1):
                bot.send_message(message.chat.id, f'```\n{ascii_img[i * 4097:i + 4096 * (i + 1)]}\n```',
                                 parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, f'```\n{ascii_img}\n```', parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка при обработке изображения: {e}')


bot.polling(none_stop=True)
