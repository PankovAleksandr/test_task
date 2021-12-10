text = 'Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии \
 Феодоровны, встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Он подошел к Анне Павловне, \
 поцеловал ее руку, подставив ей свою надушенную и сияющую лысину, и покойно уселся на диване'

word_list = []
temp_list = []
proper_name_list = []
bid_list = text.split('. ') #Разбиваем текст на предложения

for i_bid in bid_list: #Создаем из предложений общий список из слов
    for i in i_bid:
        temp_list = i_bid.split()
        temp_list.pop(0) #Убираем из предложений первые слова с большой буквы.
    word_list.extend(temp_list)
#print(word_list)

for i_word in word_list: #Находим имена собственные и добавляем их в список
    if i_word.istitle():
        proper_name_list.append(i_word)

print(proper_name_list)

# Не получилось привести слова к именительному падежу в и динственном числе.
# В целом, реализация такой задачи в Python трудно реализуема, и вряд ли получится корректный результат.