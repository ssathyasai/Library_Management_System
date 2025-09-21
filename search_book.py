from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def list_books():
    resp = sb.table("books").select("*").execute()
    return resp.data

if __name__ == "__main__":
    books = list_books()
    if books:
        for b in books:
            print(f"Book ID: {b['book_id']}, Title: {b['title']}, Author: {b['author']}, Category: {b['category']}, Stock: {b['stock']}")
    else:
        print("No books available.")
