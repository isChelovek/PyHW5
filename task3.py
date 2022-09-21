# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

languages = list(map(lambda language: language.upper(), ['python', 'c#', 'java', 'с++', 'java_script','php','fortaran']))

print(languages)
numbers = [x for x in range(1, len(languages)+1)]
numbers2 = list(enumerate(languages, 1))
print(numbers2)
numbprs_languages = list(zip(numbers, languages) )
print(numbprs_languages)

def swaped_numbers_languages(num_lan):
    filtered_list =[]
    sum_ord = 0
    for num,lan in num_lan:
        for l in lan:
            sum_ord+=ord(l)
        if sum_ord % num == 0:
          filtered_list.append((sum_ord, lan) )
    return filtered_list

print((swaped_numbers_languages(numbprs_languages)))