import pickle

with open ('files/conditions.bin', 'rb') as f:
    CONDITIONS = pickle.load (f, encoding='utf8')

def condition(i):
    print (CONDITIONS[int(i) - 1])

'''
CONDITIONS = []
with open('conditions.txt', 'r', encoding='utf8') as f:
    cond = f.readlines()
for i in cond:
    if '\n' in i:
        i = i.replace('\n', '')
    if i[0].isdigit():
        CONDITIONS.append(i)
    else:
        CONDITIONS[-1] += ' ' + i

#print(len(CONDITIONS))

f = open('conditions.bin', 'wb')
pickle.dump(CONDITIONS, f)
f.close()

f = open('conditions.bin', 'rb')
a = pickle.load(f)
print(a)
f.close()
'''