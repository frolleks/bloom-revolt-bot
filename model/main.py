from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Prompt(BaseModel):
    input: str


app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tokenizer = AutoTokenizer.from_pretrained(
    "bigscience/bloom-3b")
model = AutoModelForCausalLM.from_pretrained(
    "bigscience/bloom-3b",
    use_cache=True
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/prompt")
async def generate_prompt(prompt: Prompt):
    input_ids = torch.tensor(
        tokenizer(prompt.input,
                  return_tensors='pt')['input_ids']
    )
    output = model.generate(input_ids, penalty_alpha=1,
                            top_k=1.8, top_p=1, max_length=96)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    return {"output": decoded_output}
