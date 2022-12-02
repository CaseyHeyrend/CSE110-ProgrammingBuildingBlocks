max_chapters = -1
book_w_max = ""

with open("Week12/books_and_chapters.txt") as books_file:
    for line in books_file:
        parts = line.split(":")
        book = parts[0].strip()

        chapters = int(parts[1])

        scripture = parts[2].strip()

print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
