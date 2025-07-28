import telebot
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7889285425:AAFLKIPxVqAermAW3Y522hn-ZcXVSWZHjzw")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
     bot.reply_to(message, "Привет! Я твой Telegram бот. я буду подсказывать тебе рецепты!")
    
    
@bot.message_handler(commands=['eggs'])
def send_bye(message):
        bot.reply_to(message,  ['разагреваем сковородку ложим туда чють чють масла и разбиваем яица солим и ждём 8 мин после того как они пожарились ложим их на тарелку и наслаждаемся  '])
    
@bot.message_handler(commands=['sausages'])
def send_bye(message):
        bot.reply_to(message,  ['разрезаем сосиськи и разагреваем сковородку ложим чють чють масла и ложим сосиськи поджариваем до корочки и ложим их на торелку и наслаждаемся  '])
                    
@bot.message_handler(commands=['sandwiches'])
def send_bye(message):
        bot.reply_to(message,  ['нарезаем хлеб колбасу и сыр и ложим колбасу с сыром на хлеб'])
                     
@bot.message_handler(commands=['cheese'])
def send_bye(message):
        bot.reply_to(message,  ['нарезаем сосиськи разагреваем сковородку ложим чють чють масла и ложим туда сосиськи жарим их и добовляем кетчюп с мойнезом перемешеваем м добавляем сыр чють чють поджариваем пока сыр не растопится и ложим их на торелку и наслаждаемся'])
                    



