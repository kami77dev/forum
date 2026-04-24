from fastapi import FastAPI

app = FastAPI

itens=[]

@app.get("/")
def root():
    return {"Hello": "World"} #É a nossa porta 

@app.post("/itens")
def create_item(item:str):
    itens.append(item)
    return item

@app.get("/itens/{item_id}")
def get_item(item_id: int) -> str:
    item = itens[item_id]
    return item