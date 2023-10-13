
file = open("mov.txt", "r")
data = file.readlines()
def read_data():
    dict_data = {}
    for each_data in data:
        ddata = each_data.rstrip()
        name, imdb = ddata.split("  ")
        dict_data[name] = imdb
    return dict_data
def add(dictt):
    name = input("enter name of movie: ")
    imdb = float(input("entre movie imdb: "))
    dictt.update({name : str(imdb)})
    return dictt
def show_list(dictt):
    for i in sorted(dictt.keys()):
        print(i, dictt[i])

def show_imdb(dictt):
    s_dict = sorted(dictt.values(), reverse=True)  
    for i in range(5):
        for j in dictt.keys():
            if dictt[j] == s_dict[i]:
                print(s_dict[i], j)
def exit(dictt):
    file = open("movies.txt", "w")
    for i in dictt.keys():
        string = i + "  " + dictt[i]+ "\n"
        file.write(string)

dic_data = read_data()
while True:
    op = int(input())
    if op == 1:
        dic_data = add(dic_data)
        exit(dic_data)
    elif op == 2:
        show_list(dic_data)
    elif op == 3:
        show_imdb(dic_data)
    elif op == 4:
        exit(dic_data)
        break
    else:
        print("")
    try_again = input(" ")
    if not(try_again ==  "y"):
        exit(dic_data)
        break