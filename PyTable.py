num_row = int(input('Введите количество строк: '))
num_column = int(input('Введите количество столбцов: '))
choice = input('Выберите бираную операцию для выполнения функции: \n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\nВаш выбор: ')
def print_operation_table(operation, num_row, num_column): 
    for i in range(1, num_row + 1):
        print('\n')
        for j in range(1, num_column + 1):
            print(f'{operation(i, j)} ', end='\t')
match choice:
    case "1":
        print_operation_table(lambda x, y: x + y, num_row, num_column)
    case "2":
        print_operation_table(lambda x, y: x - y, num_row, num_column)
    case "3":
        print_operation_table(lambda x, y: x * y, num_row, num_column)
    case "4":
        print_operation_table(lambda x, y: round(x / y, 1), num_row, num_column)
    case _:
        print('Неправильный ввод!')
