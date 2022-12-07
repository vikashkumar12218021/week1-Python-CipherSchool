name = input("enter your name: ")
tem_variable=""
i = 0
while i < len(name):
    if name[i] not in tem_variable:
        tem_variable += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
        i += 1