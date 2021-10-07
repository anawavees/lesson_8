
class CookBook:
    # cook_book = dict()
    def __init__(self, file_name):
        self.cook_book = dict()
        self.file_name = file_name
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                dish_name = line.strip()
                counter = int(file.readline())
                temp_list = []
                for item in range(counter):
                    ingredient_name, quantity, measure = file.readline().split('|')
                    temp_list.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
                    )
                    self.cook_book[dish_name] = temp_list
                file.readline()
            print(self.cook_book)

    def get_shop_list_by_dishes(self, dishes, person_count):
        new_dist = {}
        for c in self.cook_book.keys():
            if c in dishes:
                for ingrts in self.cook_book[c]:
                    if ingrts['ingredient_name'] not in new_dist:
                        new_dist[ingrts['ingredient_name']] = {'measure': ingrts['measure'], 'quantity': ingrts['quantity']}
                    else:
                        new_dist[ingrts['ingredient_name']]['quantity'] += ingrts['quantity']
        for c in new_dist.keys():
            new_dist[c]['quantity'] *= person_count
        print(new_dist)


book = CookBook('./2_files/recipes.txt')
print(book)

book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

import glob, os

path = '.\sorted'
pattern = '*.txt'

glob_path = os.path.join(path, pattern)
list_files = glob.glob(glob_path)
# расширение нового файла установим как '.all'
new_file = 'new_file.all'

# чтение и запись
if list_files:
    temp_dist = {}
    for file_name in list_files:
        with open(file_name, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
            # дописываем строку с названием файла
            # fw.write(f'\n\n------------ {file_name}\n\n')
            count = 0
            for line in fr:
                count +=1
            # fw.write(f'{count}\n')
            temp_dist[file_name] = count
    # print((temp_dist))
    sorted_values = sorted(temp_dist.values())  # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in temp_dist.keys():
            if temp_dist[k] == i:
                sorted_dict[k] = temp_dist[k]
                break
    # print(sorted_dict)
    for file, count_line in sorted_dict.items():
        with open(file, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
            fw.write(f'\n\n------------ {file}\n\n')
            fw.write(f'{count_line}\n')
            for line_new in fr:
                fw.write(line_new)





