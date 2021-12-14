#Marcus Lycke
#Substitute-Santa

def create_list(listname):
    with open(listname, "w", encoding="utf8") as x:
        name = input("what is the child called?: ")
        x.write(name+"\n") #f"{name}\n"


        while True:
            thing = input("What do you want to add to the list? Type # if you want to break: ")
            if "#" in thing: break
            else: x.write(f"{thing}")


def import_list(openlist):
    with open(openlist, "r", encoding="utf8") as f:
        return[int(entry) for entry in f.readlines()]


def menu():
    # skapa en meny
    filename = input("What is the file called?: ")
    create_list(filename)


def main():

    menu()


if __name__ == "__main__":
    main()