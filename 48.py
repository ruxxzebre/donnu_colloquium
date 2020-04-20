
namez = [input() for i in range(int(input('n: ')))]
n = len(namez) - 1
for i in range(n//2):
    namez[i], namez[n - i] = namez[n - i], namez[i]
print(namez)