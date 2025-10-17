from project.computer_types.computer import Computer


class Laptop(Computer):

    LAPTOP_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }

    LAPTOP_MAX_RAM = 64

    @property
    def computer_processors(self):
        return self.LAPTOP_PROCESSORS

    @property
    def max_ram(self):
        return self.LAPTOP_MAX_RAM

    @property
    def name_comp(self):
        return 'laptop'