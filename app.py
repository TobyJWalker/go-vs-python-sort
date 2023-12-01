import random
import time

def bubble_sort(num_list):
    n = 10000
    swapped = True

    while swapped:
        swapped = False
        
        for i in range(1, n):
            if num_list[i-1] > num_list[i]:
                num_list[i-1], num_list[i] = num_list[i], num_list[i-1]
                swapped = True

num_list = []

for i in range(10000):
    num_list.append(random.randint(0, 100))

start = time.time()
bubble_sort(num_list)
end = time.time()

print(f"{(end - start)*1000}ms")