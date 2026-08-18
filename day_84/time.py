
import time

print("Hello")

time.sleep(2)

print("World")


start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Time taken:", end - start)

t = time.localtime()

print(t)

current_time = time.strftime("%H:%M:%S")

print(current_time)