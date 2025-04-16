from starlette.responses import JSONResponse

import broadlink

async def discover():
  devices = broadlink.discover()
  broadlink.remote.rm4mini.send_data
