from fastapi import FastAPI
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to handle POST request
@app.post("/add")
async def add_num(a: int = Form(...), b: int = Form(...)):
    return {"sum": a + b}