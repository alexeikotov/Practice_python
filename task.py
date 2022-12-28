class StrategyDeal:
    def __init__(self, deal):
        self.bank = float(deal['Bank'])
        self.entry = float(deal['Entry'])
        self.targets = [float(i) for i in deal['Target'].split(';')]
        self.close = float(deal['Close'])

    def get_targets(self):
        return self.targets
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]

    def get_target_percents(self):
        self.target_persents = []
        for i in self.targets:
            self.target_persents.append(round(i/self.entry,3))
        return self.target_persents
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]

    def get_target_banks(self): 
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    DELIM = '-----'
    with open(file_name,'r') as f:
        data = f.read()
    data = data.split(DELIM)
    return(data)

def parse_data(data):
    deals = []
    for deal in data:
        deal = [j for j in deal.split('\n') if j!='']
        deals.append({i.split(':')[0]:i.split(':')[1].replace('USD','') for i in deal if i!=[]})
    return(deals)



def write_data(file_name, data):
    pass


def main():
    content = read_data('deals.txt')
    deals = parse_data(content)
    
    #result = content
    #write_data('out.txt', result)


if __name__ == '__main__':    
    main() 
