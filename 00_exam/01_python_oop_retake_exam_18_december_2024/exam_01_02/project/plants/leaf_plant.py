from project.plants.base_plant import BasePlant


class LeafPlant(BasePlant):

    VALID_SIZE = ["S", "M", "L"]

    def __init__(self, name: str, price: float, water_needed : int, size: str):

        super().__init__(name, price, water_needed)
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in self.VALID_SIZE:
            raise ValueError("Size must be a valid one!")
        self._size = value

    def plant_details(self):
        return f"Leaf Plant: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Size: {self.size}"
