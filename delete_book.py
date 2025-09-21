from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_book(book_id):
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data

if __name__ == "__main__":
    bid = int(input("Enter book id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete book {bid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_book(bid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("No book deleted — check book_id.")
    else:
        print("Delete cancelled.")
