class StrategyDeal:
    def __init__(self, deal):
        self.bank = float(deal['Bank'])
        self.entry = float(deal['Entry'])
        self.targets = [float(i) for i in deal['Target'].split(';')]
        self.close = float(deal['Close'])

    def get_targets(self):
        return list(self.targets)

    def get_target_percents(self):
        self.target_persents = []
        for i in self.targets:
            self.target_persents.append(round(i/self.entry,3))
        return list(self.target_persents)


    def get_target_banks(self): 
        self.target_banks = [round(i*self.bank,3) for i in self.targets]
        return list(self.target_banks)

    def __str__(self):
        return f'Bank: {self.bank}, entry: {self.entry}, targets: {self.targets}, target_banks: {self.target_banks}'


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
        deal = {i.split(':')[0]:i.split(':')[1].replace('USD','') for i in deal if i!=[]}
        if deal != {}:
            deals.append(deal)
    return(deals)



def write_data(file_name, deals):
    out = open(file_name, 'w')
    template = """
{} target: {}
Percent: {}
Bank: {}
"""
    for i in deals:
        print(i)
        deal = StrategyDeal(i)
        out.write(f"BANK: {i['Bank']}\nSTART_PRICE: {i['Entry']}\nSTOP_PRICE: {i['Close']}\n")
        for j in range(len(deal.get_targets())):
            out.write(template.format(j+1,deal.get_targets()[j],deal.get_target_percents()[j],deal.get_target_banks()[j]))
        out.write('-----\n')




def main():
    content = read_data('deals.txt')
    deals = parse_data(content)
    write_data('out.txt',deals)


if __name__ == '__main__':    
    main() 
