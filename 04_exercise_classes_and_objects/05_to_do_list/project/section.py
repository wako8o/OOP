from typing import List

from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):

        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task {task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):

        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):

        total_task = [x for x in self.tasks if x.completed]

        # total_task = 0
        # for t in self.tasks:
        #     if t.completed:
        #         total_task += 1
        #         self.tasks.remove(t)

        return f"Cleared {len(total_task)} tasks."

    def view_section(self):

        result = '\n'.join(x.details() for x in self.tasks)

        return (f"Section {self.name}:\n"
                f"{result}\n")
