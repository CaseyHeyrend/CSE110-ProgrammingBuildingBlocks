with open("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week11/books.txt") as book_file:
    for line in book_file:
        book = line.strip()
        print(book)