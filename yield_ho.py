def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

# <class 'generator'>
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# 4でストップ
# Traceback (most recent call last):
#   File "yield_ho.py", line 15, in <module>
#     print(next(gen))
# StopIteration
# for i in range(4):
#     print(next(gen))

def even_numbers(n):
    current = 0
    while current <= n:
        if current % 2 == 0:
            yield current
        current += 1

gen = even_numbers(10)

for i in gen:
    print(i)

def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('line:1\nline:2\nline:3\n')

gen = read_lines('example.txt')
for idx, line in enumerate(gen):
    print('read times:', idx + 1)
    print(line)