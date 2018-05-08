import pymorphy2
import re
import codecs
import random
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

f = codecs.open('1grams-3.txt', r, utf_8 ) #������ ����� � httpruscorpora.rucorpora-freq.html
words = f.read()
f.close()
words = re.sub('[0-9]', '', words)
words = words.split()
words_dct = {} #������� �� ���� ������ ������ ����
len(words) #����� �� ��������� ������ ���-�� ���� ����� ������, ��� ������ ���� ����� ������ ������ 10 ���. ����
words_10 = words[10000]

for word in words_10 #���������� ������
    analysis = morph.parse(word)[0]
    try
        lst = words_dct[analysis.tag.POS]
        words_dct[analysis.tag.POS] = lst + [analysis.normal_form]        
    except     
        words_dct[analysis.tag.POS] = [analysis.normal_form] 
        
def new_message(mes) #�������� ������ ���������
    mes = re.sub('[^�-�s�-�]', '', mes) #������� �� ����������� ���, ����� ���� � ��������
    print(mes)
    new_mes = ''
    for word in mes.split()
        analysis = morph.parse(word)[0]
        j = 0 
        while(j == 0) #��������� ����� , ���� �� ������� ����� � ���� �� ������ �������, ��� � ��������� ����� 
            new_word = words_dct[analysis.tag.POS][random.randint(0, len(words_dct[analysis.tag.POS])-1)]
            analysis_new = morph.parse(new_word)[0]                                                      
            for i in analysis_new.lexeme #���������� �� ���� �������� ����. �����
                if (i.tag == analysis.tag)#���������� ����
                    j = 1 
                    analysis_new = i #���� ������� ���������� ����, ������� �� ����� while

        #print(analysis_new.word)
        new_mes += analysis_new.word + ' '
    return new_mes[-1]
    
import telebot  # ����������� ������ pyTelegramBotAPI
import config    # ����������� ��� ��������� �����

bot = telebot.TeleBot(config.TOKEN)  # ������� ��������� ����

# ���� ���������� ��������� ������� send_welcome, ����� ������������ ���������� ������� start ��� help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message)
    bot.send_message(message.chat.id, ������������! ������� �����������, �������� ������ ����� ��������. )
    
@bot.message_handler(func=lambda m True)  # ���� ���������� ��������� �� ����� ���������
def send_len(message)
    bot.send_message(message.chat.id, new_message(message.text))
    
if __name__ == '__main__'
    bot.polling(none_stop=True)