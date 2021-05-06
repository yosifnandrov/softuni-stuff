# def uppercase(fn):
#     def wrapper():
#         result = fn()
#         return result.upper()
#     return wrapper
#
# @uppercase
# def say_hello():
#     return "hello"
#
#
# print(say_hello())

# import time
# def measure_time(fn):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = fn(*args,**kwargs)
#         end = time.time()
#         total_time = end - start
#         print(f"time needed: {total_time}")
#         return result
#     return wrapper
#
# @measure_time
# def find_fibonacci(n):
#     def fib_wrapper(n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return fib_wrapper(n-1) + fib_wrapper(n-2)
#     return fib_wrapper(n)
#
#
# print(find_fibonacci(33))

# def increase(n):
#     def inner(fn):
#         def wrapper(*args,**kwargs):
#             result = fn(*args,**kwargs)
#             return [i + n for i in result]
#         return wrapper
#     return inner
#
#
# @increase(10)
# def numbers():
#     return [1,2,3,4,5,6]
#
# print(numbers())


random_list = [1, 4, 1, 2, 7, 5, 2]
count = []
indexes = [i for i in range(10)]

for i in range(10):
    count.append(random_list.count(i))

print(count)

count = [sum(count[:i+1]) for i in range(len(count))]
print(count)
