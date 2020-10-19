class Writer:
    def __init__(self, f_name, story, mode):
        self.f_n = f_name
        self.s = story
        self.m = mode
        self.writer()

    def writer(self):
        with open(self.f_n, self.m) as wr:
            wr.write(self.s)
        self.reader()

    def reader(self):
        with open(self.f_n, "r") as rdr:
            content = rdr.read()
            print(content)


file_name = input("Please name your file with extensions(.doc & .txt only) first:")
mode = input("If you want to clear previous data then enter 'c' or want to add some line write 'add':")
if mode == "c":
    mode = "w"
else:
    mode = "a"
story = input("After Writing hit Enter:")

pen = Writer(file_name, story, mode)
