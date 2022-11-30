string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

#1
x = [i for i in range(1,1001) if i%17==0]
#2
x = [i for i in range(1,1001) if '2' in str(i)]
#3
x = [i for i in range(1,10001) if str(i) == str(i)[::-1] and len(str(i))>1]
#4
x = len([i for i in list(string) if i == ' '])
#5
vowels = "aeuioy"
x = "".join([i for i in list(string) if i.lower() not in vowels])
#6
x = [i for i in string.split(' ') if len(i)<=5]
#7
x = {i:len(i) for i in string.split(' ')}
#8
x = set([i.upper() for i in list(string) if i.isalpha()])
#9
numbers =[i for i in range(10)]
x = [i*i for i in numbers]
#10
coord = [(1, 1), (2, 3), (5, 3),(2,8)]
x = {c:(c[0]**2+c[1]**2)**0.5 for c in coord if c[1] == 5*c[0]-2}
#11
x = [i*i for i in range(2,28) if i%2 == 0]
#12
x = max([(i[0]**2+i[1]**2)**0.5 for i in coord])
#13
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
x = [(i+j,i-j) for i,j in zip(nums_first,nums_second)]
#14
n = ['43141', '32441', '431', '4154', '43121']
x = list(filter(lambda x: int(x)**2%2==0, n))
#15
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

l = [i.split(',') for i in input_str.split('\n')]
keys = [i[0] for i in l]
data = [i[1:] for i in l]
result_str = ''
for i in range(len(data[0])):
    t = map(lambda x,y: x+':'+y+',', keys, [j[i] for j in data])
    result_str += """{{\n{}\n}}""".format(('\n'.join(list(t))[:-1])) + ',\n'
result_str = """[\n{}\n]""".format(result_str[:-2])

#print(result_str)
"""[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]"""

#16
a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]

x = [sum(list(map(lambda row: row[i], a))) for i in range(len(a[0]))]