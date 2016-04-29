
x = [1, 2, "hello", 7]

try:
    x.sort()
    print(x)
except TypeError:
    print("Errror =(")