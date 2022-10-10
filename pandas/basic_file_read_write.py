
def read_file():
    file = open("test.txt","rt")
    for line in file:
        print(type(line))
        print(line)
    file.close()


def read_file_line_by_line():
    file = open("test.txt","rt")
    print(type(file.readline()))
    print(file.readline())
    print(file.readline(2))

    file.close()


def copy_file_line_by_line_to_another():
    file = open("test.txt","rt")

    copy_file = open("test_copy","wt")

    for line in file:
        print("writting line :"+ line)
        copy_file.writelines(line)
    copy_file.close()
    file.close()

if __name__ =="__main__":
    #read_file()
    #read_file_line_by_line()
    copy_file_line_by_line_to_another()