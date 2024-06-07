'''
from waitress import serve
#from drflearn.wsgi import application
from drflearn.asgi import application

if __name__ == '__main__':
    serve(application, port=8000)

'''

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from drflearn import asgi

#asyncio.run(serve(asgi:application, Config()))
result= asyncio.run(serve(asgi.application, Config(
    
    port=8000
)))
print(result)