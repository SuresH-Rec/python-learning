books = [] 

while True:

   print("=" * 40)
   print("Library Management System")
   print("=" * 40)
   


   print("1. Add Book")
   print("2. View Book")
   print("3. Search Book")
   print("4. Exit")
   
   choose = input("Choose One Option:")
   
   if choose == "1":
        title = input("Title: ")
        author = input("Author Name: ")
        genre = input("Enter Genre: ")
        copies = int(input("Enter Copies: "))
       
        
        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "copies":copies,
        }
        
        books.append(book)
 
        print("\nBook Added Successfully!")
        print("\nBook Details")
        print("-" * 30)
        print(f"Title         : {title}")
        print(f"Author        : {author}")
        print(f"Genre         : {genre}")
        print(f"Copies        : {copies}")
        print("-" * 30)
        print()
       
   elif choose == "2":
       if len(books) == 0:
            print("No books added yet.")
       else:
            print("All Books")
            print("-" * 30)
            for i, book in enumerate(books, start=1):

                print(f"{i}. {book['title']} | {book['author']} | " f"{book['genre']} | {book['copies']} | ")
            print("-" * 30)
            print()
   elif choose == "3":

        while True:

            print("=" * 40)
            print("Search Book")
            print("=" * 40)

            print("1. Search by Author")
            print("2. Back to Main Menu")

            search_choice = input("Choose One Option: ")

            if search_choice == "1":

                author = input("Enter Author Name ")
                found = False

                for book in books:

                    if author.lower() == book["author"].lower():

                        print("-" * 30)
                        print(f"Name          : {book['title']}")
                        print(f"Author       : {book['author']}")
                        print("-" * 30)
                        print()

                        found = True

                if not found:
                    print(f"\nNo bookss found with skill: {skill}\n")


            elif search_choice == "2":
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option. Choose 1, 2 or 3.")
    
   elif choose == "4":
        print("Thank you for using Recruitment Management System!")
        break

   else:
        print("Invalid Option. Choose 1, 2, 3 or 4.")
      
