import time
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово  № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time.time()
print(f'Время выполнения функции: {end_time - start_time} секунд')

threads = []
args = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]

start_time_threading = time.time()
for word_count, file_name in args:
    thread = Thread(target=wite_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

threading_end_time = time.time()
print(f'Время выполнения функции: {threading_end_time - start_time_threading} секунд')

