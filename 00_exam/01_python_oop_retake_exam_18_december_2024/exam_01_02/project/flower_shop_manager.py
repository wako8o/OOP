from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS = {
        "Flower": Flower,
        "LeafPlant": LeafPlant,
    }

    VALID_CLIENTS = {
        "BusinessClient": BusinessClient,
        "RegularClient": RegularClient,
    }

    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self,
                  plant_type: str,
                  plant_name: str,
                  plant_price: float,
                  plant_water_needed: int,
                  plant_extra_data: str):

        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        new_plant = self.VALID_PLANTS[plant_type](
            plant_name,
            plant_price,
            plant_water_needed,
            plant_extra_data,
            )
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        if self._find_obj_by_phone_number(client_phone_number, self.clients) is not None:
            raise ValueError("This phone number has been used!")

        new_client = self.VALID_CLIENTS[client_type](client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):

        client = self._find_obj_by_phone_number(client_phone_number, self.clients)
        if client is None:
            raise ValueError("Client not found!")

        matching_plants = self._find_objs_by_name(plant_name, self.plants)
        if not matching_plants:
            raise ValueError("Plants not found!")

        if len(matching_plants) < plant_quantity:
            return "Not enough plant quantity."

        total_price = sum(plant.price for plant in matching_plants[:plant_quantity])
        discount = client.discount / 100
        order_amount = total_price * (1 - discount)
        self.income += order_amount

        for _ in range(plant_quantity):
            self.plants.remove(matching_plants.pop(0))

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        plants = self._find_objs_by_name(plant_name, self.plants)

        if not plants:
            return "No such plant name."

        plant_info = plants[0].plant_details()
        self.plants.remove(plants[0])
        return f"Removed {plant_info}"

    def remove_clients(self):
        initial_count = len(self.clients)
        self.clients = [client for client in self.clients if client.total_orders > 0]
        return f"{initial_count - len(self.clients)} client/s removed."

    def shop_report(self):
        report = ["~Flower Shop Report~"]

        total_orders = sum(client.total_orders for client in self.clients)
        report.append(f"Income: {self.income:.2f}")
        report.append(f"Count of orders: {total_orders}")
        report.append(f"~~Unsold plants: {len(self.plants)}~~")

        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1

        sorted_plant_counts = (f"{plant_name}: {count}" for plant_name, count in sorted(
            plant_counts.items(), key=lambda x: (-x[1], x[0])
        ))
        report.extend(sorted_plant_counts)

        report.append(f"~~Clients number: {len(self.clients)}~~")
        sorted_clients = (client.client_details() for client in sorted(
            self.clients, key=lambda c: (-c.total_orders, c.phone_number)
        ))
        report.extend(sorted_clients)

        return "\n".join(report)

    # helper methods
    @staticmethod
    def _find_obj_by_phone_number(obj_phone_number, collection):
        return next((obj for obj in collection if obj.phone_number == obj_phone_number), None)

    @staticmethod
    def _find_objs_by_name(obj_name, collection):
        return [obj for obj in collection if obj.name == obj_name] or None