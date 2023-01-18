def write_exceptins(exceptions, e):
    with open('exceptions.txt', 'w', encoding='utf-8') as file:
        about_exception = f'name : {exceptions} , meaning : {e}'
        file.write(f"{about_exception}\n")
