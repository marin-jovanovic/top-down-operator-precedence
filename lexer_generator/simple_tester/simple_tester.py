

if __name__ == '__main__':

    file1 = [i for i in open("../test_cases/3/simplePpjLang.out")]

    file2 = [i for i in open("out.txt")]

    print(file1 == file2)