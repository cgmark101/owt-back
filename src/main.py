import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from models import Payload
import json

deta = Deta('your_super_secret_deta_key')
db = deta.Base('ot')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get('/')
async def index():
    return {'hola' : 'mundo'}

@app.post('/position/')
async def post_position(request:Request):
    r = await request.body()
    r = r.decode('utf-8')
    r = json.loads(r)
    d = db.update(r, 'viiobn6mj1pf')
    return r

@app.post('/position2/')
async def post_position(payload:Payload):
    r = payload.dict()
    d = db.update(r, 'viiobn6mj1pf')
    return r

@app.get('/realtime/')
async def get_position():
    d = next(db.fetch())
    for items in d:
        lat = items['lat']
        lon = items['lon']
        geojson = {"geometry": {"type": "Point", "coordinates": [lon, lat]}, "type": "Feature", "properties": {}}
    return geojson

@app.get('/payload/')
async def get_payload():
    payload = db.get('viiobn6mj1pf')
    return payload
