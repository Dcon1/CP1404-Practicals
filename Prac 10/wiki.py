import wikipedia

user_search = input("What would you like to search on wikipedia? \nEnter a blank choice to quit...")

try:
    while user_search != "":
        temp_page = wikipedia.page(user_search)
        print(temp_page.title, temp_page.content, temp_page.url)
        #print(wikipedia.summary(user_search))
        user_search = input("What would you like to search on wikipedia? \nEnter a blank choice to quit...")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)