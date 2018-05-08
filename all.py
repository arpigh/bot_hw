import pymorphy2
import re
import codecs
import random
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

f = codecs.open('1grams-3.txt', r, utf_8 ) #ñëîâàÿ âçÿòû ñ httpruscorpora.rucorpora-freq.html
words = f.read()
f.close()
words = re.sub('[0-9]', '', words)
words = words.split()
words_dct = {} #ñëîâàðü èç ñëîâ ðàçíûõ ÷àñòåé ðå÷è
len(words) #âðåìÿ íà îáðàáîòêó òàêîãî êîë-âà ñëîâ áóäåò âåëèêî, äëÿ ðàáîòû áîòà áåðåì òîëüêî ïåðâûå 10 òûñ. ñëîâ
words_10 = words[10000]

for word in words_10 #ñîñòàëåíèÿ ñëîâàÿ
    analysis = morph.parse(word)[0]
    try
        lst = words_dct[analysis.tag.POS]
        words_dct[analysis.tag.POS] = lst + [analysis.normal_form]        
    except     
        words_dct[analysis.tag.POS] = [analysis.normal_form] 
        
def new_message(mes) #ñîçäàíèå íîâîãî ñîîáùåíèÿ
    mes = re.sub('[^à-ÿsÀ-ß]', '', mes) #óäàëÿåì èç ïðåäëîæåíèÿ âñå, êðîìå áóêâ è ïðîáåëîâ
    print(mes)
    new_mes = ''
    for word in mes.split()
        analysis = morph.parse(word)[0]
        j = 0 
        while(j == 0) #ïîäáèðàåì ñëîâà , ïîêà íå âñòåòèì ñëîâî ñ òåìè æå òåãàìè ëåêñåìû, ÷òî è ââåäåííîå ñëîâî 
            new_word = words_dct[analysis.tag.POS][random.randint(0, len(words_dct[analysis.tag.POS])-1)]
            analysis_new = morph.parse(new_word)[0]                                                      
            for i in analysis_new.lexeme #ïðîõîäèìñÿ ïî âñåì ëåêñåìàì ñëó÷. ñëîâà
                if (i.tag == analysis.tag)#ñðàâíèâàåò òåãè
                    j = 1 
                    analysis_new = i #åñëè íàõîäèì îäèíàêîâûå òåãè, âûõîäèì èç öèêëà while

        #print(analysis_new.word)
        new_mes += analysis_new.word + ' '
    return new_mes[-1]
    
import telebot  # èìïîðòèðóåì ìîäóëü pyTelegramBotAPI
import config    # èìïîðòèðóåì íàø ñåêðåòíûé òîêåí

bot = telebot.TeleBot(config.TOKEN)  # ñîçäàåì ýêçåìïëÿð áîòà

# ýòîò îáðàáîò÷èê çàïóñêàåò ôóíêöèþ send_welcome, êîãäà ïîëüçîâàòåëü îòïðàâëÿåò êîìàíäû start èëè help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message)
    bot.send_message(message.chat.id, Çäðàâñòâóéòå! Ââåäèòå ïðåäëîæåíèå, ðàçäåëÿÿ êàæäîå ñëîâî ïðîáåëîì. )
    
@bot.message_handler(func=lambda m True)  # ýòîò îáðàáîò÷èê ðåàãèðóåò íà ëþáîå ñîîáùåíèå
def send_len(message)
    bot.send_message(message.chat.id, new_message(message.text))
    
if __name__ == '__main__'
    bot.polling(none_stop=True) 
