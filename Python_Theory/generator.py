def generate_num(x):
    for i in range(x):
        yield i

gen = generate_num(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) StopIteration message

def infinite_num():
    i = 0
    while True:
        yield i
        i += 1
gen = infinite_num()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def even_num(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = even_num(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

