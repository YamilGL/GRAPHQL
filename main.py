from starlette.applications import Starlette
from ariadne.asgi import GraphQL
from schema import schema
import uvicorn
import config

debug = True if config.ENV =='DEV' else False

app= Starlette(debug=debug)
app.mount('/graphql',GraphQL(schema,debug=debug))

if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=int(config.PORT),log_level="info")


