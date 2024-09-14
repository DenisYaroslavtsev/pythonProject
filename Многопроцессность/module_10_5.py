from multiprocessing import Pool
import datetime


def reed_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            text = file.readline()
            if not text:
                break
            all_data.append(text)


# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start_line = datetime.datetime.now()
# for file in filenames:
#     reed_info(file)
# end_line = datetime.datetime.now()
# finish_line = end_line - start_line
# print(f'Линейный вызов занял {finish_line} секунд')
#
# # Линейный вызов занял 0:00:03.573637 секунд

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with Pool(processes=4) as pool:
        start_multi = datetime.datetime.now()
        pool.map(reed_info, filenames)
    end_multi = datetime.datetime.now()
    finish_multi = end_multi - start_multi
    print(f'Многопроцессный вызов занял {finish_multi} секунд')

# Многопроцессный вызов занял 0:00:01.497613 секунд
