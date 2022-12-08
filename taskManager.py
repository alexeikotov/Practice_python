from enum import Enum

class Task:
    
    def __init__(self, id, name, description, status):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def get_id(self):
        return self.id

    def get_task_values(self):
        return [self.id, self.name, self.description, self.status]


class Subtask(Task):
    
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id

    def get_subtask_values(self):
        return [self.id, self.name, self.description, self.status, self.parent_id]


class ComplexTask(Task):
    
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks
    
    def get_complex_task_values(self):
        return [self.id, self.name, self.description, self.status, self.subtasks]


class Status(Enum):
    process = "IN PROCESS"
    ready = "READY"

    
class TaskManager:

    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.complex_tasks = {}
        self.subtasks = {}

    def create_id(self):
        self.id_series+=1
        return self.id_series

    def create_task(self, name, description):
        current_id = self.create_id()
        new_task = Task(current_id, name, description, Status.process.value)
        self.tasks[current_id] = new_task
        return self.tasks
    
    def create_complex_tasks (self, name, description):
        current_id = self.create_id()
        new_complex_task = ComplexTask(current_id, name, description, Status.process.value, [])
        self.complex_tasks[current_id] = new_complex_task
        return self.complex_tasks

    def  create_subtask(self, parent_name, name, description):
        current_id = self.create_id()
        for i in self.complex_tasks.keys():
            if parent_name == self.complex_tasks[i].name:
                self.complex_tasks[i].subtasks.append(current_id)
                parent_id = self.complex_tasks[i].id      
        new_subtask = Subtask(current_id, name, description, Status.process.value, parent_id)
        self.subtasks[current_id] = new_subtask
        return self.subtasks, self.complex_tasks

    def get_tasks(self):
        if len(self.tasks) == 0:
            return 'Нет предстоящих задач'
        else:
            return self.tasks

    def get_subtasks(self):
        if len(self.subtasks) == 0:
            return 'Нет предстоящих подзадач'
        else:
            return self.subtasks
    
    def get_complex_tasks(self):
        if len(self.complex_tasks) == 0:
            return "Нет предстоящих сложных задач"
        else:
            return self.complex_tasks
    
    def get_tasks_by_id(self, id):
        if id not in self.tasks.keys():
            return "Нет задач с заданным ID"    
        else:
            return self.tasks[id]

    def get_subtasks_by_id(self, id):
        if id not in self.subtasks.keys():
            return "Нет задач с заданным ID"
        else:
            return self.subtasks[id]
    
    def get_complex_tasks_by_id(self, id):
        if id not in self.complex_tasks.keys():
            return "Нет задач с заданным ID"
        else:
            return self.complex_tasks[id]

    def remove_tasks(self):
        self.tasks = {}
        return self.tasks
    
    def remove_subtasks(self):
        self.subtasks = {}
        for i in self.complex_tasks.keys():
            self.complex_tasks[i].subtasks = []
        return self.subtasks, self.complex_tasks
    
    def remove_complex_tasks(self):
        self.complex_tasks = {}
        self.subtasks = {}
        return self.complex_tasks, self.subtasks
    
    def remove_task_by_id(self, id):
        if id not in self.tasks.keys():
            return "Нет задач с заданным ID"
        else:
            del self.tasks[id]
            return self.tasks
        
    def remove_subtask_by_id(self, id):
        if id not in self.subtasks.keys():
            return "Нет задач с заданным ID"
        else:
            parrent_id = self.subtasks[id].parrent_id
            self.complex_tasks[parrent_id].subtasks.remobe(id)
            del self.subtasks[id]
            return self.tasks, self.complex_tasks
        
    def remove_complex_task_by_id(self, id):
        if id not in self.complex_tasks.keys():
            return "Нет задач с заданным ID"
        else:
            subtasks_ids = self.complex_tasks[id].subtasks
            for i in subtasks_ids:
                self.remove_subtask_by_id(i)
            del self.complex_tasks[id]
            return self.subtasks, self.complex_tasks

    def update_status(self, task):
        task.status = Status.ready.value
        if task in self.tasks.values():
            return task
        elif task in self.subtasks.values():
            if "IN PROCESS" not in self.complex_tasks[task.parent_id].subtasks:
                self.complex_tasks[task.parent_id].status = Status.ready.value
        elif task in self.complex_tasks.values():
            for i in task.subtasks:
                self.subtasks[i] = Status.ready.value
        else:
            return "Не нашел задачу"
        return self.tasks, self.subtasks, self.complex_tasks
