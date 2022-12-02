'''
max_chapters = -1
book_w_max = ""

with open("Week12/books_and_chapters.txt") as books_file:
    for line in books_file:
        parts = line.split(":")
        book = parts[0].strip()

        chapters = int(parts[1])

        scripture = parts[2].strip()

print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
'''
highest_chapter = -1
highest_books = ''
with open("Week12/books_and_chapters.txt") as books:
    for line in books:
        parts = line.strip().split(":")

        book = parts[0]
        chapters = int(parts[1])
        scriptures = parts[2]

        print(f"Scripture: {scriptures}, Book: {book}, Chapters: {chapters}")

        if chapters > highest_chapter:
            highest_chapter = chapters
            highest_books = book

        print(f"The book with the most chapter in the is: {highest_books}")
        print(f"It has {highest_chapter} chapters.")