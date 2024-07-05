import os

start_path = os.getcwd()
print(start_path)

print(os.listdir())

if 'tmp.py' not in os.listdir():
    print("Файл tmp.py отсутствует в данной директории")
