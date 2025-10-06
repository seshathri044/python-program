def generate_sqr(n):
    for i in range(n):
        yield i*i
for sqr in generate_sqr(5):
    print(sqr)