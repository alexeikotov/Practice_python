class ManualCsvConverter:


    def __init__(self, csv_data):
        self.title = csv_data[0]
        self.values = csv_data[1:]


    def prepare_title(self):
        title = self.title.strip().split(',')
        return title
    

    def prepare_row_values(self):
        values = [v.strip().split(',') for v in self.values]
        return values

    
    def convert_row_to_json(self, data):
        #values = [""" "{}":"{}" """.format(k,v) for k,v in data.items()]
        #formatted_values = ','.join(values)
        formatted_values = ",".join([""" "{}":"{}" """.format(key,value) for key,value in data.items()])
        formatted_line = """{{ {} }}""".format(formatted_values)
        return formatted_line


    def check_data(self,title,row_values):
        for row in row_values:
            assert len(title) == len(row), "Title length does not match row length!"


    def get_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        self.check_data(title, row_values)
        result = [self.convert_row_to_json(dict(zip(title,row))) for row in row_values]
        return "[{}]".format(",".join(result))
