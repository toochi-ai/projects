from pprint import pprint
f = open('test.txt', 'w', encoding='utf8')

f.write("This is a test string\n")
f.write("This is a new string\n")
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.read())

# Чтение и запись построчно
# Зачастую с файлами удобнее работать построчно, поэтому для этого есть отдельные методы:
#
# writelines — записывает список строк в файл;
# readline — считывает из файла одну строку и возвращает её;
# readlines — считывает из файла все строки в список и возвращает их.
# Метод f.writelines(sequence) не будет сам за вас дописывать символ
# конца строки (‘\n’). Поэтому при необходимости его нужно прописать вручную.

f = open('test.txt', 'a', encoding='utf8')

sequence = ["other string\n", "123\n", "test test\n"]

f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.readlines())

f = open('test.txt', 'r', encoding='utf8')
print(f.readline())
print(f.read(4))
print(f.readline())
print(f.tell())

f.close()
print('---')

f = open('test.txt')
for line in f:
    print(line, end='')

f.close()

file_name = 'Pushkin.txt'
file = open(file_name, 'r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)

count = 0
with open('Pushkin.txt', 'r', encoding='utf8') as file:
    for line in file:
        pprint(line)
        count += 1
    print('-----')
    pprint(f'Количество строк = {count}')
