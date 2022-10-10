from functools import cmp_to_key


def sorting_using_sorted():
    array = [2,23,5,6,12,1]
    # sorted method returns new array with sorted elements
    array = sorted(array, reverse=True)
    print(array)


def sorting_using_sort():
    array = [2, 23, 5, 6, 12, 1]
    # sort() returns sorted array , it does not create new array
    array.sort(reverse=True)
    print(array)


#  ------ object sorting ------------------------
class Person:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.id) + " " + self.name


def sort_by_id(p1, p2):
    if p1.id > p2.id:
        return 1
    elif p1.id < p2.id:
        return -1
    else:
        return 0


def sort_by_name(p1, p2):
    if p1.name > p2.name:
        return 1
    elif p1.name < p2.name:
        return -1
    else:
        return 0


def sorting_person_objects():
    array = list()
    array.extend([Person(10, "gautam"), Person(2, "tommy"), Person(20, "ricky")])
    array.sort(key=cmp_to_key(sort_by_name))
    for person in array:
        print(person)


if __name__ == "__main__":
    # sorting_using_sorted()
    # sorting_using_sort()
    sorting_person_objects()
