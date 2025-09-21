from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_member(member_id):
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    mid = int(input("Enter member id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete member {mid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_member(mid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("No member deleted — check member_id.")
    else:
        print("Delete cancelled.")
