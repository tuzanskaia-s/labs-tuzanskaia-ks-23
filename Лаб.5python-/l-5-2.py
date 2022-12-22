def f2(x):
    return x + 1
    
def f1(y, m):
    return y(5) + m

print(f1(f2, 5))
