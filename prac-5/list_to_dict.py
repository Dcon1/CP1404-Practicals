def main():
    names = ["jack", "jill", "harry"]
    dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    users = dict(zip(names, dobs))
    print(users)


main()
