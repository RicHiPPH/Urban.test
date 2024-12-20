incorrect_data = 0
def personal_sum(numbers):


        result = 0
        for i in numbers:
            if isinstance(i,(int,float)):
                result += i
            else:
                print(f'В numbers записан некорректный тип данных: {i}')
        return result








def calculate_average(numbers):
    try:
        spr = personal_sum(numbers) / len(numbers)
        return spr
    except TypeError:
        global incorrect_data
        incorrect_data += 1
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0










print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(incorrect_data)



