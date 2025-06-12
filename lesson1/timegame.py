import time as d
import random as r
print("Готовий? У тебе є 3 секунди, щоб натиснути Enter, як тільки з'явиться повідомлення!")
stoptime = r.randint(2,5)
d.sleep(stoptime)
print("Натискай Enter")
start = d.time()
input()
end = d.time()
react = end - start
print(f"Твій час реакції: {react:} секунд")
