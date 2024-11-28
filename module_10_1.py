
import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as txt:
        for i in range(1, word_count + 1):
            txt.write(f"Накося выкуся N{i}\n")
            sleep(0.01)
    print(f"Запись - {file_name}")


start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f"Время пополнения: {end_time - start_time}")

list_t = []
list_t.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
list_t.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
list_t.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
list_t.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

start_time_list = time()
for thread in list_t:
    thread.start()
for thread in list_t:
    thread.join()
end_time_list = time()

print(f"Конец всему, албибек {end_time_list - start_time_list}")

# вроде что то получилось


