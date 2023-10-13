number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
new_name = []
while True:
    error = 0
    name_input = input("enter")
    if "." in name_input:
        new_name = name_input.split(".", 1)
        if "." in new_name[1]:
            error += 1
            print("error")
        elif new_name[1] == "err":
            error += 1
            print("error")
        elif not(len(new_name[1]) == 3 or len(new_name[1]) == 2):
            error += 1
            print("error")
        for number in number:
            if number in new_name[1]:
                print("error") 
    for number in range(len(number)):
        if name_input.startswith(number[number]):
            error += 1
            print("error")
    if error == 0:
        print("True")
        again = input("again?(y, n)")
    if again == "y":
        break