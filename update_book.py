from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_book(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data

if __name__ == "__main__":
    bid = int(input("Enter book id to update stock: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
    updated = update_book(bid, new_stock)
    if updated:
        print("Updated:", updated)
    else:
        print("No record updated — check book_id.")
