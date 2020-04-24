
import datetime

class Logger:

    def __init__(self, log_path, encoding='utf-8'):
        self.log_file = open(log_path, 'a', encoding=encoding)

    def __enter__(self):
        self.log_start = datetime.datetime.utcnow()
        self.log_file.write(f'{self.log_start}: "Начало работы"\n')
        print(f'Время запуска кода {self.log_start}')
        return self
    
    def write_log(self, action):
        self.log_file.write(f'{datetime.datetime.utcnow()}: {action}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'error: {exc_val}')
        self.log_end = datetime.datetime.utcnow()
        self.log_file.write(f'{self.log_end}: "Окончание работы"\n')
        print(f'Время завершения кода {self.log_end}')
        time_work_log = self.log_end - self.log_start
        print(f'Время выполнения кода {time_work_log}')
        self.log_file.close()



with open('recipes.txt') as f:
    ingredients = []
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        number_of_entries = f.readline()
        ingredients = []
        for ingredient in range(int(number_of_entries)):
            ingredients_dict = {}
            ingredient = f.readline().strip().split('|')
            ingredient_name, quantity, measure = ingredient
            ingredients_dict['ingredient_name'] = ingredient_name
            ingredients_dict['quantity'] = quantity
            ingredients_dict['measure'] = measure
            ingredients.append(ingredients_dict)
        cook_book[dish_name] = ingredients
        f.readline()
    #print(cook_book)
    #print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    result_dict = {}
    for dish in dishes:
        for (key, value) in cook_book.items():
            if dish == key:
                for entry in value:
                    a = (entry['ingredient_name']).strip()
                    b = (entry['measure']).strip()
                    c = int((entry['quantity']).strip())
                    if a in result_dict.keys():
                        result_dict[a]['quantity'] = c * person_count + (result_dict[a]['quantity'])
                    else:
                        result_dict[a] = {'measure': b, 'quantity': c * person_count}
    print(result_dict)

if __name__ == '__main__':
    with Logger('my.log') as log:
        get_shop_list_by_dishes(['Омлет', 'Запеченый картофель', 'Фахитос'], 2)
        log.write_log('запущена функция для списка блюд и количества персон')


