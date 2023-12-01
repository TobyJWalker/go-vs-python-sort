import random
import time

def bubble_sort(num_list):
    n = len(num_list)
    swapped = True

    while swapped:
        swapped = False
        
        for i in range(1, n):
            if num_list[i-1] > num_list[i]:
                num_list[i-1], num_list[i] = num_list[i], num_list[i-1]
                swapped = True

num_list = []

for i in range(100000):
    num_list.append(random.randint(0, 100))

start = time.time()
bubble_sort(num_list)
end = time.time()

print(f"{(end - start)}s")