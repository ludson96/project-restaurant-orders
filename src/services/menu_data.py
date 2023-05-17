import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        self.source_path = source_path
        self.dishes = set()
        self.load_menu()

    def load_menu(self):
        lines = self.read_csv_file(self.source_path)
        for line in lines[1:]:
            dish_name, price, ingredient_name, amount = self.parse_line(line)
            dish = self.find_or_create_dish(dish_name, price)
            self.add_ingredient_to_dish(dish, ingredient_name, amount)

    def read_csv_file(self, file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            return list(reader)

    def parse_line(self, line):
        dish_name = line[0]
        price = float(line[1])
        ingredient_name = line[2]
        amount = int(line[3])
        return dish_name, price, ingredient_name, amount

    def find_or_create_dish(self, dish_name, price):
        dish = next(
            (
                d
                for d in self.dishes
                if d.name == dish_name and d.price == price
            ),
            None,
        )
        if dish is None:
            dish = Dish(dish_name, price)
            self.dishes.add(dish)
        return dish

    def add_ingredient_to_dish(self, dish, ingredient_name, amount):
        ingredient = Ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, amount)
