
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

class ReadFiles:
    def __init__(self, file_name):
        self.file_name = file_name
        temp_dist = {}
        count = 0
        with open(file_name, "r", encoding='utf-8') as f:
            counter = int(file_name.readline())
            print(counter)

file = ReadFiles('./sorted/1.txt')
print(file)


