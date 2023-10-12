#task 1
# def distance (*args): 
#     return ((args[2] - args[0]) ** 2 + (args[3] - args[2]) ** 2) ** 0.5
# print(distance(int(input('x1')), int(input('y1')),int(input('x2')),int(input('y2')) ))

# #task 3
# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n - 2)
# print(fib(4))
#task 2 
# def power(a, n):
#     res = 1 
#     if n == 0:
#         return 1
#     elif n > 0:
#         for i in range(n):
#             res *= a 
#         return res
#     else:
#         for i in range(-n):
#             res /= a 
#         return res
# print(power(2, -3))      

#task 4
# def is_year_leap(year):
#     if year % 4 == 0:
#         return 'Год весокостный!'
#     else:
#         return 'Год не весокостный'
# print(is_year_leap(2021))


#task 5
# def square(l):
#     return l * 4, l ** 2, (l**2 + l**2)**0.5
# print(square(int(input())))

#task 6
# def season(month):
#     if month == 12 or month == 1 or month == 2:
#         return 'Зима'
#     elif month == 3 or month == 5 or month == 4:
#         return 'Весна'
#     elif month == 6 or month == 7 or month == 8:
#         return 'Лето'
#     elif month == 9 or month == 10 or month == 11:
#         return 'Весна'
# print(season(int(input())))

#task 7
# def bank(a, years):
#     for i in range(years):
#         a +=  a * 0.1
#         return a
# print(bank(int(input('a')), int(input('year'))))

#task 8 
# def is_prime(num):
#     if num % num == 0 and num > 0 and num % 1 == num:
#         return True
#     else:
#         return False
    
# print(is_prime(int(input())))

#task 9 
# def date(day, month, year):
#     if 0 < month < 4 and month != 2 and month == 5 or 6 < month < 9 or 9 < month < 11 or month == 12 and day <= 31 and 0 < year <= 2023:
#         return True
#     elif month == 4 or month == 6 or month == 9 or month == 11 and day <= 30 and 0 < year <= 2023:
#         return True
#     elif month == 2 and day <= 28 or year % 4 == 0 and day <= 29:
#         return True
#     else:
#         return False
# print(date(int(input('day')), int(input('month')), int(input('year'))))
        
