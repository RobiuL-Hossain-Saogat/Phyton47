class Book:
    def __init__(self,book_name,writer_name,Publisher,date_of_publication,Price):
        self.book_name=book_name
        self.writer_name=writer_name
        self.Publisher=Publisher
        self.date_of_Publication=date_of_publication
        self.Price=Price


book=Book("PROKRITIR PROTHOM PATH","Bipradash Barua","Srizoni, 40/41 Banglabazar, Dhaka-1100",2015,250)
print(f'''The book {book.book_name} is written by {book.writer_name} 
and the publisher of this book is {book.Publisher} 
which published in {book.date_of_Publication}.
and the price of the book is {book.date_of_Publication}''')