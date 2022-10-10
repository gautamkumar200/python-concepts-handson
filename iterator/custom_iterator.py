class TopTen:

    # def __int__(self):
    #     self.num = 1

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 10:
            num = self.num
            self.num += 1
            return num
        else:
            # this execption is to stop iteration which is handle py python
            raise StopIteration()


if __name__ == "__main__":
    it = TopTen()
    #print(next(iter(it)))
    #print(it.__next__())
    for i in iter(it):
        print(i)
