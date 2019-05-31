import random
import statistics as stat

def IsInCircle(x, y):
    return x * x + y * y <= 0.25

def Find():
    result = -1
    new_result = 0
    num = 0
    cnt = 0
    while  abs(result - new_result) > 0.01 or result == new_result:
        num = num + 1
        x = random.random() - 0.5
        y = random.random() - 0.5

        if IsInCircle(x, y):
            cnt = cnt + 1
            result = new_result
            new_result = cnt * 4 / num

    return result
        
count = int(input("How many funcyion calls would you prefer? : "))

print(stat.mean([Find() for i in range(count)]))
