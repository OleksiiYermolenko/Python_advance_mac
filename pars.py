import time

import requests


def func_time_counter(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()
        print(f'Time: {finish_time - start_time} sec.')

    return wrapper


@func_time_counter
def time_req_webpage():
    webpage = requests.get('http://do.kart.edu.ua/')

for i in range (1, 1000):
    t = time_req_webpage()
    t2 = time_req_webpage()
    t3 = time_req_webpage()
    t4 = time_req_webpage()
    t5 = time_req_webpage()
    print(t, t2, t3,t4,t5)
x = float(input('x: '))
if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
    print('Something else')


# score = input("Enter Score: ")
# try:
#     score = float(score)
# except:
#     print("Please input score between 0.0 and 1.0.")
# if score > 1.0:
#     print("Please input score between 0.0 and 1.0.")
# elif score >= 0.9:
# 	print("A")
# elif score >= 0.8:
# 	print("B")
# elif score >= 0.7:
# 	print("C")
# elif score >= 0.6:
# 	print("D")
# elif score < 0.6:
# 	print("F")
