import unittest
from taskManager import *



class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.taskmanager = TaskManager()
    
    def test_create_task(self):
        result = self.taskmanager.create_task("name", "description")
        expected = {1:Task(1,'name','description','IN PROCESS')}
        self.assertEqual([result[1].id, result[1].name, result[1].description, result[1].status], 
            [expected[1].id, expected[1].name, expected[1].description, expected[1].status])

    def test_remove_task_by_id(self):
        self.taskmanager.create_task('name','description')
        self.taskmanager.create_task('name2','description2')
        self.taskmanager.remove_task_by_id(1)
        result = [len(self.taskmanager.tasks), self.taskmanager.tasks[2].name]
        expected = [1, 'name2']
        self.assertEqual(result, expected)
    
    def test_update_status(self):
        self.taskmanager.create_task('name','description')
        self.taskmanager.update_status(self.taskmanager.tasks[1])
        result = self.taskmanager.tasks[1].status
        expected = 'READY'
        self.assertEqual(result,expected)
        
    def test2_update_status(self):
        self.taskmanager.create_complex_tasks('task1','description1')
        self.taskmanager.create_subtask('task1','subtask1','description_subtask1')
        self.taskmanager.update_status(self.taskmanager.get_subtasks_by_id(2))
        result = self.taskmanager.complex_tasks[1].status
        expected = 'READY'
        self.assertEqual(result, expected)
        
        
    # к сожалению нет времени расписывать все тесты
    # так как это учебная задача написал в качестве тренировки три

if __name__ == "__main__":
    unittest.main()
