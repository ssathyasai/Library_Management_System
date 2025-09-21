import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def add_member(name, email):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data


if __name__ == "__main__":
    name = input("Enter member name: ").strip()
    email = input("Enter member email: ").strip()
    created = add_member(name, email)
    print("Inserted:", created)

