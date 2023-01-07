import numpy as np
import argparse
import ast

class Antiplagiat:


    def __init__(self, first_file, second_file):
        self.first_file = first_file
        self.second_file = second_file


    def levenshtain(self):
    num_1 = len(self.first_file) + 1 
    num_2 = len(self.second_file) + 1 
    D = np.zeros((num_1, num_2)) 
    for i in range(num_1): 
        D[i, 0] = i
    for j in range(num_2): 
        D[0, j] = j 
    for i in range(1, num_1): 
        for j in range(1, num_2): 
            if self.first_file[i - 1] == self.second_file[j - 1]: 
                D[i,j] = min(D[i, j - 1] + 1, D[i - 1, j] + 1, D[i - 1, j - 1] + 0)
            else: 
                D[i,j] = min(D[i,j - 1] + 1, D[i - 1,j] + 1, D[i - 1,j - 1] + 1)       
    result = D[num_1 - 1, num_2 - 1] / len(self.second_file)
    return float(result)


    def normilize(self):
        self.first_file = ast.unparse(ast.parse(self.first_file))
        self.second_file = ast.unparse(ast.parse(self.second_file))


parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r'))
parser.add_argument('file_1', type = argparse.FileType('w'))
args = parser.parse_args()
a = args.file
b = args.file_1
with open(a.name) as f:
    lines = [line.rstrip() for line in f]
results = [0] * len(lines)
for count, i in enumerate(lines):
    str = i.split()
    f1 = open(str[0],'r',encoding = 'utf-8').read() 
    f2 = open(str[1],'r',encoding = 'utf-8').read()
    Test = Antiplagiat(f1,f2)
    Test.normilize()
    result = Test.levenshtain()
    results[count] = repr(result)
results = "\n".join(results)
f3 = open(b.name,'w').write(results)

