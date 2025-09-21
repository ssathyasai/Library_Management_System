from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_member(member_id, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    mid = int(input("Enter member id to update: ").strip())
    new_email = input("Enter new email: ").strip()
    updated = update_member(mid, new_email)
    if updated:
        print("Updated:", updated)
    else:
        print("No record updated — check member_id.")
