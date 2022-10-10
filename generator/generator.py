def top_ten():
    n = 1
    while n <= 10:
        # yeild will give an iterator, here
        # we dont need to write __next__() or __iter__() yield does for us
        yield n
        n += 1


if __name__ == "__main__":

    gen = top_ten()

    for i in gen:
        print(i)
