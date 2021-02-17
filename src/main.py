import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from models import Payload
import json

## DetaBase setup
deta = Deta('your_super_secret_deta_key')
db = deta.Base('ot') ## Database name

app = FastAPI() ## FastAPI instance

## Cross-origin resource sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

## Health check
@app.get('/')
async def index():
    return {'hola' : 'mundo'}

## Post position from owntracks app to detabase
## This method use the direct request body to get the payload and processit to detabase
@app.post('/position/')
async def post_position(request:Request):
    r = await request.body()
    r = r.decode('utf-8') ## The payload comes in bites and must be decoded
    r = json.loads(r) ## Converted payload to json/dict format
    d = db.update(r, 'viiobn6mj1pf') ## Updates the database entry with the key 'viiobn6mj1pf' 
    ##This string value can be modified but must be changed in the base.py and all the other fields to match
    return r

## Post position from owntracks app 
## This method use a pydantic model to parse the data
@app.post('/position2/')
async def post_position(payload:Payload): ## Payload from pydantic model in models.py
    r = payload.dict() ## Pydantic model parsed to dictionary with the received data from owntracks app
    d = db.update(r, 'viiobn6mj1pf') ## Updates the database with the key 'viiobn6mj1pf' 
    ##This string value can be modified but must be changed in the base.py and all the other fields to match
    return r

## Get the realtime positition in Geojson format 
## Geojson allows the easy manipulation with any map library trough a GET request
@app.get('/realtime/')
async def get_position():
    d = next(db.fetch()) ## Fetch the entire database and return a list
    for items in d: ## Iterate over the list to parce the latitude and longitud values
        lat = items['lat'] ## Latitud
        lon = items['lon'] ## Longitud
        geojson = {"geometry": {"type": "Point", "coordinates": [lon, lat]}, "type": "Feature", "properties": {}} ## Geojson output for any GET request
    return geojson

## Get the full payload sended by owntracks app
@app.get('/payload/')
async def get_payload():
    payload = db.get('viiobn6mj1pf') ## get the entry saved in database by its key 'viiobn6mj1pf'
    ##This string value can be modified but must be changed in the base.py and all the other fields to match
    return payload
