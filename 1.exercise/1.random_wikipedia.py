import wikipedia


def get_wiki_article(my_title):
    # get random title
    summary = wikipedia.summary(my_title)
    url = wikipedia.page(my_title).url
    print(f'{summary} read more at {url}')


while True:
    # prompt user for a new topic
    user_choice = int(input('Do you want a new topic?, Enter 1 to continue, 0 to quick\n'))
    print('\n')
    if user_choice == 0:
        print('Thank you for using franky wiki reader...Goodbye')
        break
    elif user_choice == 1:
        title = wikipedia.random(1)
        get_wiki_article(title)
