from fastapi import FastAPI
from .v1.routers import router
from mangum import Mangum

app = FastAPI(title='Cryptocurrency API',
              description='API to track current prices and trading signals')
app.include_router(router, prefix="/v1")


@app.get("/")
def read_root():
    return {"msg": "from main FastAPI & API Gateway"}


# to make it work with Amazon Lambda, we create a handler object
def handler(event, context):
    '''
        The AWS Lambda handler event and context arguments are made available
            to an ASGI application in the ASGI connection scope.
        scope['aws.event']
        scope['aws.context']
    '''
    if event.get("some-key"):
        # Do something or return, etc.
        return
    print("CloudWatch log stream name:", context.log_stream_name)
    print(f"PieterDebug {event=} {context=}")
    asgi_handler = Mangum(app, log_level="info")
    response = asgi_handler(event, context)
    print(f"Debug2 {response=}")
    return response


def testapp():
    return app
