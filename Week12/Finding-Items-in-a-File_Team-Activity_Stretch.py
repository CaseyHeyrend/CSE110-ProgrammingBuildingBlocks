chosen_volume = input("Which  volume of scripture would you like to learn about? ")
max_chapters = -1
book_w_max = ""

with open("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week12/books_and_chapters.txt") as books_file:
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