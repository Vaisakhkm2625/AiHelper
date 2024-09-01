import time
from generate_penguin_logo import draw_penguin_logo

timelist = []


for i in range(10):
    start_time = time.perf_counter()
    draw_penguin_logo(1000,1000)
    end_time = time.perf_counter()
    timelist.append(end_time - start_time)

for i in timelist:
    print(f'{i:f}')

