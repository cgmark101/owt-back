import os
from deta import Deta

## run this file one time

deta = Deta('your_super_secret_deta_key')
db = deta.Base('ot')

def set_db():
    payload = {
  "_type": "location",
  "acc": 1800,
  "alt": 78,
  "batt": 44,
  "bs": 1,
  "conn": "m",
  "created_at": 1612658146,
  "key": "viiobn6mj1pf",
  "lat": 8.3690592,
  "lon": -62.6282535,
  "t": "u",
  "tid": "12",
  "tst": 1612657933,
  "vac": 1,
  "vel": 0
}
    
    set = db.insert(payload)
    print('Done')
    return set

set_db()
