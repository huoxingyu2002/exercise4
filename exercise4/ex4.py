import sqlite3

conn = sqlite3.connect('library.db')
cursor= conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Books
               (BookID INTEGER PRIMARY KEY,
                Title TEXT,
                Author TEXT,
                ISBN TEXT,
                Status TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (UserID INTEGER PRIMARY KEY,
                Name TEXT,
                Email TEXT)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations
               (ReservationID INTEGER PRIMARY KEY,
                BookID INTEGER,
                UserID INTEGER,
                ReservationDate DATE,
                FOREIGN KEY (BookID) REFERENCES Books (BookID),
                FOREIGN KEY (UserID) REFERENCES Users (UserID))''')



def add_book(title, author, isbn):
    cursor.execute("INSERT INTO Books (Title, Author, ISBN, Status) VALUES (?, ?, ?, 'Available')", (title, author, isbn))
    conn.commit()
    print("Successfully added new book:{}".format(title))


def find_book(book_id):
    cursor.execute('''SELECT Books.Title, Books.Author, Books.ISBN, Books.Status,
                          Users.Name, Users.Email, Reservations.ReservationDate
                   FROM Books
                   LEFT JOIN Reservations ON Books.BookID = Reservations.BookID
                   LEFT JOIN Users ON Reservations.UserID = Users.UserID
                   WHERE Books.BookID = ?''', (book_id,))
    book_info = cursor.fetchone()

    if book_info:
        title, author, isbn, status, user_name, reservation_date = book_info
        print("Book Information：")
        print("Book name：", title)
        print("author：", author)
        print("ISBN：", isbn)
        print("status：", status)
        if user_name:
            print("Booked by {} on {}".format(user_name, reservation_date))
    else:
        print("Book with BookID {} not found".format(book_id))


def menu():
    while True:
        print("menu：")
        print("1. add a new book")
        print("2. Find detailed information about books based on BookID")
        print("3. exit")

        choice = input("Please select an action (input number)：")

        if choice == '1':
            title = input("Please enter the book name：")
            author = input("Please enter the author：")
            isbn = input("Please enter ISBN：")
            add_book(title, author, isbn)
        elif choice == '2':
            book_id = input("please input BookID：")
            find_book(book_id)
        elif choice == '3':
            break
        else:
            print("Invalid selection, please try again.")




while True:
    print("Select one from the following:")
    print("1. add book")
    print("2. add user")
    print("3. reservation")
    print("4. BookID、Title、UserID、ReservationID search")
    print("5. Show detailed information for all books")
    print("6. exit")

    choice = input("Please enter the selection number: ")

    if choice == "1":
     
        book_id = input("input BookID: ")
        title = input("input Title: ")
        author = input("input Author: ")
        isbn = input("input ISBN: ")
        status = input("input Status: ")

        cursor.execute("INSERT INTO Books (BookID, Title, Author, ISBN, Status) VALUES (?, ?, ?, ?, ?)",
                       (book_id, title, author, isbn, status))
        conn.commit()
        print("Successfully book added！")

    elif choice == "2":
      
        user_id = input("input UserID: ")
        name = input("input Name: ")
        email = input("input Email: ")

        cursor.execute("INSERT INTO Users (UserID, Name, Email) VALUES (?, ?, ?)",
                       (user_id, name, email))
        conn.commit()
        print("user add success！")

    elif choice == "3":
        
        reservation_id = input("please input ReservationID: ")
        book_id = input("please input BookID: ")
        user_id = input("please input UserID: ")
        reservation_date = input("please input ReservationDate (YYYY-MM-DD): ")

        cursor.execute("INSERT INTO Reservations (ReservationID, BookID, UserID, ReservationDate) VALUES (?, ?, ?, ?)",
                       (reservation_id, book_id, user_id, reservation_date))
        conn.commit()
        print("reservation success！")

    elif choice == "4":
      
        search_text = input("please input BookID、Title、UserID或ReservationID: ")

        if search_text.startswith("LB"):
            cursor.execute("SELECT * FROM Books WHERE BookID=?", (search_text,))
        elif search_text.startswith("LU"):
            cursor.execute("SELECT * FROM Users WHERE UserID=?", (search_text,))
        elif search_text.startswith("LR"):
            cursor.execute("SELECT * FROM Reservations WHERE ReservationID=?", (search_text,))
        else:
            cursor.execute("SELECT * FROM Books WHERE Title=?", (search_text,))

        rows = cursor.fetchall()
        if len(rows) > 0:
            for row in rows:
                print(row)
        else:
            print("no match record！")

    elif choice == "5":
       
        import sqlite3

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        while True:
            print("Select one from the following:")
            print("1. add book")
            print("2. add user")
            print("3. reservation")
            print("4. BookID、Title、UserID、ReservationID search")
            print("5. Show detailed information for all books")
            print("6. exit")

            choice = input("Please enter the selection number: ")

            if choice == "1":
             
                book_id = input("input BookID: ")
                title = input("input Title: ")
                author = input("input Author: ")
                isbn = input("input ISBN: ")
                status = input("input Status: ")

                cursor.execute("INSERT INTO Books (BookID, Title, Author, ISBN, Status) VALUES (?, ?, ?, ?, ?)",
                               (book_id, title, author, isbn, status))
                conn.commit()
                print("Successfully book added！")

            elif choice == "2":
             
                user_id = input("input UserID: ")
                name = input("input Name: ")
                email = input("input Email: ")

                cursor.execute("INSERT INTO Users (UserID, Name, Email) VALUES (?, ?, ?)",
                               (user_id, name, email))
                conn.commit()
                print("user add success！")

            elif choice == "3":
             
                reservation_id = input("please input ReservationID: ")
                book_id = input("please input BookID: ")
                user_id = input("please input UserID: ")
                reservation_date = input("please input ReservationDate (YYYY-MM-DD): ")

                cursor.execute("INSERT INTO Reservations (ReservationID, BookID, UserID, ReservationDate) VALUES (?, ?, ?, ?)",
                               (reservation_id, book_id, user_id, reservation_date))
                conn.commit()
                print("reservaton success！")

            elif choice == "4":
             
                search_text = input("please input BookID、Title、User、IDReservationID: ")

                if search_text.startswith("LB"):
                    cursor.execute("SELECT * FROM Books WHERE BookID=?", (search_text,))
                elif search_text.startswith("LU"):
                    cursor.execute("SELECT * FROM Users WHERE UserID=?", (search_text,))
                elif search_text.startswith("LR"):
                    cursor.execute("SELECT * FROM Reservations WHERE ReservationID=?", (search_text,))
                else:
                    cursor.execute("SELECT * FROM Books WHERE Title=?", (search_text,))

                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        print(row)
                else:
                    print("no match record！")

            elif choice == "5":
        
                cursor.execute("SELECT * FROM Books")
                books = cursor.fetchall()
                cursor.execute("SELECT * FROM Users")
                users = cursor.fetchall()
                cursor.execute("SELECT * FROM Reservations")
                reservations = cursor.fetchall()

                print("Books:")
                for book in books:
                    print(book)
                print("Users :")
                for user in users:
                    print(user)
                print("Reservations:")
                for reservation in reservations:
                    print(reservation)

            elif choice == "6":
                break

        def update_book_details_by_id(book_id, **kwargs):
            cursor.execute("UPDATE Books SET Title = ?, Author = ?, ISBN = ?, Status = ? WHERE BookID = ?", (kwargs.get('title'), kwargs.get('author'), kwargs.get('isbn'), kwargs.get('status'), book_id))
            conn.commit()
        books = cursor.fetchall()
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        cursor.execute("SELECT * FROM Reservations")
        reservations = cursor.fetchall()

        print("Books:")
        for book in books:
            print(book)
        print("Users:")
        for user in users:
            print(user)
        print("Reservations:")
        for reservation in reservations:
            print(reservation)

    elif choice == "6":
      
        break

def update_book_details_by_id(book_id, **kwargs):
    
    cursor.execute("UPDATE Books SET Title = ?, Author = ?, ISBN = ?, Status = ? WHERE BookID = ?", (kwargs.get('title'), kwargs.get('author'), kwargs.get('isbn'), kwargs.get('status'), book_id))
    conn.commit()
    

    if kwargs.get('status') == 'Reserved':
        cursor.execute("UPDATE Reservations SET Status = 'Reserved' WHERE BookID = ?", (book_id,))
        conn.commit()
    elif kwargs.get('status') == 'Available':
        cursor.execute("UPDATE Reservations SET Status = 'Cancelled' WHERE BookID = ?", (book_id,))
        conn.commit()


def delete_book_by_id(book_id):
    cursor.execute("DELETE FROM Books WHERE BookID = ?", (book_id,))
    conn.commit()
    print("Book deleted successfully.")
    
    
    cursor.execute("SELECT COUNT(*) FROM Reservations WHERE BookID = ?", (book_id,))
    if cursor.fetchone()[0] > 0:
        cursor.execute("DELETE FROM Reservations WHERE BookID = ?", (book_id,))
        conn.commit()
        print("All reservations for this book have been cancelled.")






cursor.close()
conn.close()



