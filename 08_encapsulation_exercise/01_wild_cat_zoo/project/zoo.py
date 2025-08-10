from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int,workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price) -> str:

        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity >= len(self.animals):
            return 'Not enough budget'
        return "Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return  f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        fired = [f for f in self.workers if f.name == worker_name]
        if fired:
            worker = fired[0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:

        for budger in self.workers:
            self.__budget -= budger.salary
            if self.__budget < 0:
                return "You have no budget to pay your workers. They are unhappy"

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"



    def tend_animals(self) -> str:

        for budget in self.animals:
            self.__budget -= budget.money_for_care
            if self.__budget < 0:
                return "You have no budget to tend the animals. They are unhappy."

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self) -> str:
        tigre = 0
        lion = 0
        cheetah = 0

        tigre_info = []
        lion_info = []
        cheetah_info = []

        info_animal = [x for x in self.animals]
        for animal in self.animals:
            if type(animal).__name__ == 'Tiger':
                tigre += 1
                tigre_info.append(animal)

            elif type(animal).__name__ == 'Lion':
                lion += 1
                lion_info.append(animal)

            else:
                cheetah += 1
                cheetah_info.append(animal)

            result_lion = '\n'.join(str(l) for l in lion_info)
            result_tigre = '\n'.join(str(t) for t in tigre_info)
            result_cheetah = '\n'.join(str(c) for c in cheetah_info)


        return (f'You have {len(info_animal)} animals\n'
                f'----- {lion} Lions:\n'
                f'{result_lion}\n'
                f'----- {tigre} Tigers:\n'
                f'{result_tigre}\n'
                f'----- {cheetah} Cheetahs:\n'
                f'{result_cheetah}')

    def workers_status(self):

        total_caretaker = 0
        total_keeper = 0
        total_vet = 0

        caretaker = []
        keeper = []
        vet = []

        for worker in self.workers:
            if type(worker).__name__ == 'Caretaker':
                total_caretaker += 1
                caretaker.append(worker)

            elif type(worker).__name__ == 'Keeper':
                total_keeper += 1
                keeper.append(worker)

            else:
                total_vet += 1
                vet.append(worker)

        info_caretaker = '\n'.join(str(x) for x in caretaker)
        info_keeper = '\n'.join(str(x) for x in keeper)
        info_vet = '\n'.join(str(x) for x in vet)

        return (f"You have {len(self.workers)} workers\n"
                
                f"----- {total_keeper} Keepers:\n"
                f"{info_keeper}\n"
                f"----- {total_caretaker} Caretakers:\n"
                f"{info_caretaker}\n"
                f"----- {total_vet} Vets:\n"
                f"{info_vet}")