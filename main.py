from fastapi import FastAPI
import random
from get_sentence_list import get_sentences_from_paragraph
#from pydantic import BaseModel

app = FastAPI()

# define class item (inputs for scoring model)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

# example random integer function
@app.get("/random")
async def get_random():
    rn: int = random.randint(0,100)
    return {'number':rn, 'limit': 100}

@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(0,limit)
    return {'number':rn, 'limit': limit}

# Given a paragraph of text, returns each sentence as a single item in a dictionary.
@app.get("/get-sentences")
def get_sentences(input: str):
    output = get_sentences_from_paragraph(input)
    return output