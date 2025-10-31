from fastapi import FastAPI, HTTPException
import psycopg2, os

app = FastAPI()

# Connect to database
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = conn.cursor()

@app.post("/verify")
def verify(helmet_id: str, user_id: str):
    cursor.execute("SELECT * FROM helmets WHERE helmet_id=%s AND user_id=%s", (helmet_id, user_id))
    data = cursor.fetchone()
    if data:
        return {"status": "verified ✅"}
    else:
        raise HTTPException(status_code=403, detail="Helmet not registered ❌")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
