from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return "Learning Fast API at Praxis"

@app.get('/test_name')
def print_name(name:str):
    return f"Welcom to praxis,{name}"

if __name__=='__main__':
    uvicorn.run(app)