from fastapi import FastAPI
from decouple import config
from supabase import create_client, Client 
import uvicorn
from fastapi import HTTPException
from fastapi.requests import Request

url = config("SUPERBASE_URL")
key = config("SUPERBASE_KEY")

app = FastAPI()
supabase : Client = create_client(url,key)



@app.get ("/")
def root():
    return {"Hare na gethu Vickey na MASSu"}

@app.post("/get_id")
async   def get_id():
    data = supabase.table("ID").select("*").execute()
    return data

@app.post("/add_id")
def add_id(id: int, emp_id: int):
    data = supabase.table("ID").insert({"id": id, "emp_id": emp_id}).execute()
    return data

@app.post("/delete_id")
def delete_id(id: int):
    data = supabase.table("ID").delete().eq("id", id).execute()
    return data


@app.get("/get_company/{id}")
def get_company(id: int):
    try:
        response = supabase.table("Invoice").select("inv_company").filter('id', 'eq', id).execute()
        data = response.data
        if data:
            return {"inv_company": data[0]['inv_company']}
        else:
            return {"error": "No matching id found"}
    except Exception as e:
        return {"error": str(e)}


from fastapi import HTTPException, Body

@app.put("/update_company/{id}")
async def update_company(id: int, inv_company_name: str ):
    try:
        response = supabase.table("Invoice").update({"inv_company": inv_company_name}).match({'id': id}).execute()
        if response.error:
            raise HTTPException(status_code=400, detail=response.error.message)
        else:
            return {"message": "Company updated successfully"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

