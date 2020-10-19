class Writer:
    def __init__(self, f_name, story, mode):
        self.f_n = f_name
        self.s = story
        self.m = mode
        self.writer()

    def writer(self):
        with open(self.f_n, self.m) as wr:
            for s in self.s:
                wr.write(s + "\n")
        self.reader()

    def reader(self):
        with open(self.f_n, "r") as rdr:
            lines = rdr.readlines()
            print("1 Lines:\n", lines)
            for line in lines:
                print('2 Line:\n', line)
            # content = rdr.read()
            # print(content)
        with open(self.f_n, "r") as fun:
            for line in fun:
                print("Fun:", line)


# file_name = input("Please name your file with extensions(.doc & .txt only) first:")
file_name = 'test.txt'
# mode = input("If you want to clear previous data then enter 'c' or want to add some line write 'add':")
# if mode == "c":
#     mode = "w"
# else:
#     mode = "a"
mode = "w"
# story = input("After Writing hit Enter:")
story = ["First Line", "Second Line", "Third line"]
pen = Writer(file_name, story, mode)
