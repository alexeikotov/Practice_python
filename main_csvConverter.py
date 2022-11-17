from manual_csv import ManualCsvConverter

def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def main():
    data = read_data_to_list("input.csv")
    converer = ManualCsvConverter(data)
    result = converer.get_json()
    write_data("output.json", result)


if __name__== "__main__":
    main()
