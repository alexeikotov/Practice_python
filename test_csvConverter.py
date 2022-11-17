import unittest
from manual_csv import ManualCsvConverter



class TestManualCsvConverter(unittest.TestCase):


    def test_prepare_title(self):
        test1 = ManualCsvConverter(['id,name\n','1,Mike'])
        self.assertEqual(test1.prepare_title(), ['id','name'])


    def test_prepare_title(self):
        test2 = ManualCsvConverter(['id, name, salary\n','1,Mike,'])
        self.assertEqual(test2.prepare_title(), ['id','name','salary'])


    def test_prepare_title(self):
        test3 = ManualCsvConverter(['id\n','1'])
        self.assertEqual(test3.prepare_title(), ['id'])


    def test_get_json(self):
        test4 = ManualCsvConverter(['id\n','1'])
        self.assertEqual(test4.get_json(), '[{  "id":"1"  }]')


    def test_get_json(self):
        test5 = ManualCsvConverter(['id, name, salary, birth\n','1, Petr,,1990\n','2, Ivan Ivanovich, 100000, '])
        self.assertEqual(test5.get_json(), '[{ "id":"1", "name":"Petr",  "salary":"", "birth":"1990" },{  "id":"2", "name":"Ivan Ivanovich",  "salary":"100000", "birth":""}]')


    def test_get_json(self):
        test6 = ManualCsvConverter(['id,city,number of reviewers\n','1,Moscow,4432\n','2,NY,12023','3,Hogwarts,NA'])
        self.assertEqual(test6.get_json(), '[{  "id":"1" , "city":"Moscow" , "number of reviewers":"4432"  },{  "id":"2" , "city":"NY" , "number of reviewers":"12023"  },{  "id":"3" , "city":"Hogwarts" , "number of reviewers":"NA"  }]')

if __name__== "__main__":
    unittest.main()