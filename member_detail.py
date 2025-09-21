from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def member_borrowed_books(member_id):
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
    return member, borrowed

if __name__ == "__main__":
    mid = int(input("Enter member_id to view details: ").strip())
    member, borrowed = member_borrowed_books(mid)
    if member:
        m = member[0]
        print(f"Member ID: {m['member_id']}, Name: {m['name']}, Email: {m['email']}, Joined: {m['join_date']}")
        if borrowed:
            print("Borrowed Books:")
            for b in borrowed:
                print(f"Record ID: {b['record_id']}, Book ID: {b['book_id']}, Borrow Date: {b['borrow_date']}, Return Date: {b['return_date']}")
        else:
            print("No borrowed books.")
    else:
        print("Member not found.")
