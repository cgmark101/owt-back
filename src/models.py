from pydantic import BaseModel

class Payload(BaseModel):
    _type: str
    acc: int
    alt: int
    batt: int
    bs: int
    conn: str
    created_at: int
    lat: float
    lon: float
    t: str
    tid: str
    ts: int
    vac: int
    vel: int

