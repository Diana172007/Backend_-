# file_actions.py

# Открыть на запись файл example.txt
file = open('example.txt', 'r', encoding='utf-8')
# Записать в файл строку.
# Закрыть файл.
reads=file.read(12)
print(reads)
file.close()