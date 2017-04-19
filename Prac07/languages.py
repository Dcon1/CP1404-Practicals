from Prac07.ProgrammingLanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java", "Static", True, 1995)
c = ProgrammingLanguage("C++", "Static", False, 1983)
languages = [ruby, python, vb, java, c]

print("The dynamically typed languages are:")
for language in languages:
    language.is_dynamic()

    """I could not quite work out how to print the for loop in one line as shown in the lecture
     video could you please give an example if possible"""