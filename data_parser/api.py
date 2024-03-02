import json
import secrets
from http.client import HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, status, Depends
from typing import List, Union, Dict
from pydantic import BaseModel

app = FastAPI()
# security = HTTPBasic()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
#     correct_username = secrets.compare_digest(credentials.username, "timemap-default-robotic-user@sthrandom.com")
#     correct_password = secrets.compare_digest(credentials.password, "$2a$10$DuVqoFKYaBmjoi/9Zhxy3.7bbGMFgsLS1MmOlMF15kt4f9TC5hUOS")
#     if not (correct_username and correct_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username

with open('api.json', 'r') as file:
    list_of_events = json.load(file)
# Assuming the structure for Events and Sources is similar to Associations.
# Replace these example lists with actual data as per your requirements.
events_data = list_of_events["Events"]

associations_data = list_of_events["Associations"]

sources_data = list_of_events["Sources"]


@app.get("/Military/{date}/", response_model=List[Union[dict, str]])
async def read_data_by_date(date: str):
    # datefile = date.replace("/", "-")
    with open(f'mil_data/{date}.json', 'r') as file:
        deepstate_data = json.load(file)

    if not deepstate_data:
        raise HTTPException(status_code=404, detail="Data not found for the specified date")
    return deepstate_data


@app.get("/Events/")
async def read_events():
    return events_data


@app.get("/Associations/")
async def read_associations():
    return associations_data


@app.get("/Sources/")
async def read_sources():
    return sources_data




