#Towers of Hanoi

def setup(n,pegs):
    for i in range(n):
        pegs.append(i)


def TowerofHanoi(n,source,aux,target):
    if n > 0:
        TowerofHanoi(n-1,source,target,aux)
        
        if source:
            target.append(source.pop())

        print(A, B, C, sep= '   ')
        TowerofHanoi(n-1,aux,source,target)

        

A = []
B = []
C = []

NUM = int(input("Number of Rings: "))
setup(NUM,A)
TowerofHanoi(NUM,A,B,C)