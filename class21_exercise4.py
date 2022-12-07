name,char=input("enter comma separated name ,age: ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count is: {name.lower().count(char.lower())}")