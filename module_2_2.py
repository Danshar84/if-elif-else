first = input('Введите первое число:',)
second = input('Введите второе число:',)
third = input('Введите третье число:',)
if first==second and second==third:
    print('Равных чисел:', 3)
elif first == second or second == third or first == third:
    print('Равных чисел:', 2)
elif first != second and second != third and first!=third:
    print('Равных чисел:', 0)
