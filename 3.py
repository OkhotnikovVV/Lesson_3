# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return print(sum(my_list))

my_func(
    a=int(input("Введите первый аргумент: ")),
    b=int(input("Введите второй аргумент: ")),
    c=int(input("Введите третий аргумент: ")),
)
