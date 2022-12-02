'''
chosen_volume = input("Which  volume of scripture would you like to learn about? ")
max_chapters = -1
book_w_max = ""

with open("Week12/books_and_chapters.txt") as books_file:
    for line in books_file:
        parts = line.split(":")

        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()

        if scripture.lower() == chosen_volume.lower():
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

            if chapters > max_chapters:
                max_chapters = chapters
                book_w_max = book
    
print(f"The book with the most chapter in the {chosen_volume} is: {book_w_max}")
print(f"It has {max_chapters} chapters.")
'''
ask_user = input("Which  volume of scripture would you like to learn about? ")

highest_chapter = -1
highest_books = ''
with open("Week12/books_and_chapters.txt") as books:
    for line in books:
        parts = line.strip().split(":")

        book = parts[0]
        chapters = int(parts[1])
        scriptures = parts[2]

        if scriptures.lower() == ask_user.lower():
            print(f"Scripture: {scriptures}, Book: {book}, Chapters: {chapters}") 

        if chapters > highest_chapter:
            highest_chapter = chapters
            highest_books = book

        print(f"The book with the most chapter in the {ask_user} is: {highest_books}")
        print(f"It has {highest_chapter} chapters.")