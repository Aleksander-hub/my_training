

import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())




if __name__ == '__main__':
    names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start_time = time.time()
    for f_name in names:
        read_info(f_name)
    lineinyi_timt = time.time() - start_time
    print('Линейный', round(lineinyi_timt), 'c')

    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, names)
    parallel_time = time.time() - start_time
    print('многопроцессный', round(parallel_time), 'c')




