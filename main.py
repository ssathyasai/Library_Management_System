import subprocess

def main():
    while True:
        print("\n=== Library Management Menu ===")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Update Book Stock")
        print("4. Add Member")
        print("5. Delete Member")
        print("6. Update Member Email")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. List All Books")
        print("10. Search Books")
        print("11. Member Details & Borrowed Books")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            subprocess.run(["python", "add_book.py"])
        elif choice == "2":
            subprocess.run(["python", "delete_book.py"])
        elif choice == "3":
            subprocess.run(["python", "update_book.py"])
        elif choice == "4":
            subprocess.run(["python", "add_member.py"])
        elif choice == "5":
            subprocess.run(["python", "delete_member.py"])
        elif choice == "6":
            subprocess.run(["python", "update_member.py"])
        elif choice == "7":
            subprocess.run(["python", "register_member.py"])
        elif choice == "8":
            subprocess.run(["python", "read_books.py"])
        elif choice == "9":
            subprocess.run(["python", "list_book.py"])
        elif choice == "10":
            subprocess.run(["python", "search_book.py"])
        elif choice == "11":
            subprocess.run(["python", "member_detail.py"])
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
