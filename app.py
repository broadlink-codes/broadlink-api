from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route
import uvicorn

from api import (
    health_check,
    ping
)

BASE_URL = "/api/"

routes = [
    Route(BASE_URL + "ping", ping, methods=["GET"]),
    Route(BASE_URL + "health-check", health_check, methods=["GET"]),
]

middleware = [
    Middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    )
]

app = Starlette(debug=True, routes=routes, middleware=middleware)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
