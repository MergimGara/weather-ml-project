from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def init_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Testlauf
if __name__ == "__main__":
    supabase = init_supabase()
    print("✅ Verbindung zu Supabase erfolgreich.")

