from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for name in filenames:
    read_info(name)
end = datetime.now()
time = end - start
print(f'Линейный вызов: {time}')
# Линейный вызов: 0:00:05.751656



    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    time = end - start
    print(f'Многопроцессный вызов: {time}')
# Многопроцессный вызов: 0:00:03.375631