ram = [None]*10
ram2 =[None for _ in range(10)]
'''for i in range(0, 10):
    ram[i] = None
    pass'''
ram2[2]= 3
print(ram2[2])
ram2.append(5)
print("RAM: [")
for  i in range (0,11):
    print("",ram2[i],"|")
print("]")