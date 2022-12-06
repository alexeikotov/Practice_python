from enum import Enum


class Task:
    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status


class Subtask(Task):
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks


class Status(Enum):
    process = "PROCESS"
    ready = "READY"


class TaskManager:
    def __init__(self, tasks_list, subtasks_list, complex_tasks_list):
        self.tasks_list = tasks_list
        self.subtasks_list = subtasks_list
        self.complex_tasks_list = complex_tasks_list

    def create_task(self, task):
        self.tasks_list.append(task)

    def create_subtask(self, subtask):
        self.subtasks_list.append(subtask)
        return self.subtasks_list

    def create_complex_task(self, complex_task):
        self.complex_tasks_list.append(complex_task)
        return self.complex_tasks_list

    def get_tasks(self):
        return self.tasks_list

    def get_subtasks(self):
        return self.subtasks_list

    def get_complex_tasks(self):
        return self.complex_tasks_list

    def get_tasks_by_id(self, id):
        id_task = self.tasks_list[id]
        print(self.tasks_list)
        return id_task

    def get_subtasks_by_id(self, id):
        id_subtasks = self.subtasks_list[id]
        return id_subtasks

    def get_complex_tasks_by_id(self, id):
        id_complrx_tasks = self.complex_tasks_list[id]
        return id_complrx_tasks

    def remove_tasks(self):
        self.tasks_list.clear()
        return self.tasks_list

    def remove_subtasks(self):
        self.subtasks_list.clear()
        return self.subtasks_list

    def remove_complex_tasks(self):
        self.complex_tasks_list.clear()
        return self.complex_tasks_list

    def remove_task_by_id(self, id):
        self.tasks_list.remove(self.tasks_list[id])
        return self.tasks_list

    def remove_subtask_by_id(self, id):
        self.subtasks_list.remove(self.subtasks_list[id])
        return self.subtasks_list

    def remove_complex_task_by_id(self, id):
        self.complex_tasks_list.remove(self.complex_tasks_list[id])

    def update_status(self, task):
        task.status = Status.ready.value
        return task

def main():
    Taskmanager = TaskManager([], [], [])
    first_task = Task(1, "Prepare programm!", "Generate code for taskManager", Status.process.value)
    Taskmanager.create_task(first_task)

if __name__ == '__main__':
    main()