from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def add_obj(obj, other):
        if not any(x.id == obj.id for x in other):
            other.append(obj)

    def add_customer(self, customer: Customer):
        self.add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_obj(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):

        return (f"{''.join(str(x) for x in self.subscriptions)}\n"
                f"{''.join(str(x) for x in self.customers)}\n"
                f"{''.join(str(x) for x in self.trainers)}\n"
                f"{''.join(str(x) for x in self.equipment)}\n"
                f"{''.join(str(x) for x in self.plans)}\n")
