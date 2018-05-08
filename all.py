import pymorphy2
import re
import codecs
import random
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

f = codecs.open('1grams-3.txt', r, utf_8 ) #слова€ вз€ты с httpruscorpora.rucorpora-freq.html
words = f.read()
f.close()
words = re.sub('[0-9]', '', words)
words = words.split()
words_dct = {} #словарь из слов разных частей речи
len(words) #врем€ на обработку такого кол-ва слов будет велико, дл€ работы бота берем только первые 10 тыс. слов
words_10 = words[10000]

for word in words_10 #состалени€ слова€
    analysis = morph.parse(word)[0]
    try
        lst = words_dct[analysis.tag.POS]
        words_dct[analysis.tag.POS] = lst + [analysis.normal_form]        
    except     
        words_dct[analysis.tag.POS] = [analysis.normal_form] 
        
def new_message(mes) #создание нового сообщени€
    mes = re.sub('[^а-€sј-я]', '', mes) #удал€ем из предложени€ все, кроме букв и пробелов
    print(mes)
    new_mes = ''
    for word in mes.split()
        analysis = morph.parse(word)[0]
        j = 0 
        while(j == 0) #подбираем слова , пока не встетим слово с теми же тегами лексемы, что и введенное слово 
            new_word = words_dct[analysis.tag.POS][random.randint(0, len(words_dct[analysis.tag.POS])-1)]
            analysis_new = morph.parse(new_word)[0]                                                      
            for i in analysis_new.lexeme #проходимс€ по всем лексемам случ. слова
                if (i.tag == analysis.tag)#сравнивает теги
                    j = 1 
                    analysis_new = i #если находим одинаковые теги, выходим из цикла while

        #print(analysis_new.word)
        new_mes += analysis_new.word + ' '
    return new_mes[-1]
    
import telebot  # импортируем модуль pyTelegramBotAPI
import config    # импортируем наш секретный токен

bot = telebot.TeleBot(config.TOKEN)  # создаем экземпл€р бота

# этот обработчик запускает функцию send_welcome, когда пользователь отправл€ет команды start или help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message)
    bot.send_message(message.chat.id, «дравствуйте! ¬ведите предложение, раздел€€ каждое слово пробелом. )
    
@bot.message_handler(func=lambda m True)  # этот обработчик реагирует на любое сообщение
def send_len(message)
    bot.send_message(message.chat.id, new_message(message.text))
    
if __name__ == '__main__'
    bot.polling(none_stop=True)