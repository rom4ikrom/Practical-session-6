shoplist = []
ask_user = input("Please write what you want to buy: ")
shoplist.append(ask_user)
while ask_user != "":
    ask_user = input("Please write what you want to buy: ")
    shoplist.append(ask_user)
shoplist.remove("")
print("Your shoplist is: \n", shoplist)
