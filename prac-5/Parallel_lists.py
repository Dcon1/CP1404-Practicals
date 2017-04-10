def main():
    users_dict = {"jane": "", "jack": "", "jill": "", "john": "", "jerry": ""}
    for name, age in users_dict.items():
        users_dict[name] = int(input("Please enter {}'s date of birth".format(name)))
    print(users_dict)

main()
