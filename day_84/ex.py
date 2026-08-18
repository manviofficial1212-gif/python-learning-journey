import time
timer_value = int(input("enter the timer value: "))
for i in range(timer_value,0, -1):
    print(i)
    time.sleep(1)
    
print("Time's up!")