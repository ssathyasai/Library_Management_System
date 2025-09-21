from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def add_book(title, author, category, stock):
    resp = sb.table("books").insert({
        "title": title,
        "author": author,
        "category": category,
        "stock": stock
    }).execute()
    return resp.data

if __name__ == "__main__":
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category: ").strip()
    stock = int(input("Enter stock: ").strip())
    created = add_book(title, author, category, stock)
    print("Inserted:", created)
