from Prac07.Guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(gibson.get_age())

print(gibson.is_vintage(gibson.get_age()))

print(gibson)