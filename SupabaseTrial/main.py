from fastapi import FastAPI
from decouple import config
from supabase import create_client, Client 
import uvicorn
url = config("SUPERBASE_URL")
key = config("SUPERBASE_KEY")

app = FastAPI()
supabase : Client = create_client(url,key)

@app.get ("/")
def root():
    return {"Hare na gethu Vickey na MASSu"}

@app.post("/get_id")
def get_id():
    data = supabase.table("ID").select("*").execute()
    return data

if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

