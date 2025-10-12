from project.computer_types.computer import Computer

class DesktopComputer(Computer):

    Desktop_PROCESSORS = {
    'AMD Ryzen 7 5700G': 500,
    'Intel Core i5-12600K': 600,
    'Apple M1 Max': 1800
    }

    DESKTOP_MAX_RAM = 128

    @property
    def computer_processors(self):
        return self.Desktop_PROCESSORS

    @property
    def max_ram(self):
        return self.DESKTOP_MAX_RAM

    @property
    def name_comp(self):
        return 'desktop computer'
