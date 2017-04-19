from Prac07.Guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))


for i, guitar in enumerate(guitars):
    print(i + 1,guitar)
    """Could not figure out how to pass the enumerate to the class __str__"""