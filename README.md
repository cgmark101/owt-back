OwT server
=====

This is a server implementation of the HTTP protocol of the `OwnTracks` app client,
it can handle the payload and store in a cloud data base `DetaBase` for further read/query, 
and also be hosted on `DetaMicros`


Installation
----------

Install it using:


```bash
    $ git clone https://github.com/cgmark101/owt-back.git
    $ cd owt-back
    $ virtualenv env
    $ . env/bin/activate
    $ cd src
    $ pip install -r requirements.txt
    
```

Config
----------------

Edit base.py and main.py, paste your deta key (generated in their website) at [deta.sh](https://web.deta.sh)

```python
    deta = Deta('your_super_secret_deta_key')
    db = deta.Base('ot') # Database name
```

Run
----------------
Run this file one time to initial fill the database.

```bash
    $ python base.py
```

And finally run

```bash
    $ python main.py
```

Navigate to [localhost:8000/docs](http://127.0.0.1:8000/docs) to see the endpoints

