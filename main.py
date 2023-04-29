import os
import telebot
from telebot import types
import backpack
import investment

bot = telebot.TeleBot(os.environ['api_key'])

backpackButton = 'Задача о рюкзаке'
backpackFlag = False

investmentButton = 'Задача об инвестициях'
investmentFlag = False


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(backpackButton)
    markup.add(btn1)
    btn2 = types.KeyboardButton(investmentButton)
    markup.add(btn2)
    bot.send_message(message.chat.id,
                     'Привет! Я умею в математику (в отличие от тебя, хахаха 😈).', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def inputMessage(message):
    global backpackFlag
    global investmentFlag

    if message.text.strip() == backpackButton:
        bot.send_message(message.chat.id, "Введи данные задачки. Сначала введи массив цен (числа через пробел), на \
                                          новой строке введи массив весов (числа через пробел), на новой строке \
                                          одно число - вместимость рюкзака")
        backpackFlag = True
        return

    if backpackFlag:
        try:
            data = message.text.strip()
            data = data.split("\n")
            for i in range(len(data)):
                data[i] = data[i].split(' ')
                for k in range(len(data[i])):
                    data[i][k] = int(data[i][k])
            print(data)
            answer = backpack.backpack(data[0], data[1], data[2][0])
            output = ""
            for k in range(1, len(answer)):
                for i in range(1, len(answer[k])):
                    ans = str(answer[k][i])
                    ans = "⠀" * (2 - len(ans)) + ans
                    output += ans + "⠀"
                output += "\n"
                if k == len(answer) - 2:
                    output += "Ответ:⠀"
            bot.send_message(message.chat.id, output)
            backpackFlag = False
        except:
            bot.send_message(message.chat.id, "Ты ебобо?")
        return

    if message.text.strip() == investmentButton:
        bot.send_message(message.chat.id, "Введи данные задачки. Введи двумерный массив: столбцы - предприятия,\
                                            строки - сумма прибыли за года, начиная с 0 и далее")
        investmentFlag = True
        return

    if investmentFlag:
        try:
            data = message.text.strip()
            data = data.split("\n")
            for i in range(len(data) - 1):
                data[i] = data[i].split(' ')
                for k in range(len(data[i])):
                    data[i][k] = int(data[i][k])
            print(data)
            answer = investment.investment(data)
            output = ""
            for k in range(1, len(answer)):
                for i in range(1, len(answer[k])):
                    ans = str(answer[k][i])
                    ans = "⠀" * (2 - len(ans)) + ans
                    output += ans + "⠀"
                output += "\n"
                if k == len(answer) - 2:
                    output += "Ответ:⠀"
            bot.send_message(message.chat.id, output)
            investmentFlag = False
        except:
            bot.send_message(message.chat.id, "Ты ебобо?")
        return


    bot.send_message(message.chat.id, 'Команда не распознана')


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
