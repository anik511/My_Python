class Sorter:
    def __init__(self, f_name, c_n):
        self.f_n = f_name
        self.c_n = c_n
        self.writer()

    def writer(self):
        with open(self.f_n, "a") as wr:
            wr.write(self.c_n)


b_country = "B_country.txt"
i_country = "I_country.txt"
p_country = "P_country.txt"
n_country = "N_country.txt"
with open("countryname.txt", "r") as rdr:
    for country in rdr:
        if country[0] == "B":
            sort = Sorter(b_country, country)
        elif country[0] == "I":
            sort = Sorter(i_country, country)
        elif country[0] == "P":
            sort = Sorter(p_country, country)
        elif country[0] == "N":
            sort = Sorter(n_country, country)
