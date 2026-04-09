books = ["english","mathematics","physics","chemistry"]
largest_book = books[0]

large_book_index = -20
found = False
for index, book in enumerate(books):
    if(len(book) > len(largest_book)):
        largest_book = book
        large_book_index = index

print(f"largest book is {largest_book} and at index:{large_book_index }")
       

#dry run it...\
       