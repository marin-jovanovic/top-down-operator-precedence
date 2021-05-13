def main():

    # load data
    t_list = []
    a = ""
    for line in open("temp.txt").read().split("\n"):
        line = line.strip()
        print(line)
        if line.startswith("test"):
            t_list.append(a)
            a = line
        else:
            a += line

    # print check
    [print(i) for i in t_list]
    print()

    # main driver
    for t in t_list:
        if not t:
            continue

        t = t[4:]
        t = eval(t)

        # printer
        global counter
        print(f"def test_{counter}(self):")
        print(f'\toutput = self.execute("\\"{t[0]}\\"")')
        counter += 1
        print("\toutput = eval(output)")
        print()
        print(f"\tself.assertEqual(output, {t[1]})")

        print()


if __name__ == "__main__":
    global counter
    counter = 0

    main()
