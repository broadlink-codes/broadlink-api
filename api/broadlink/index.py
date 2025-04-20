import time

from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_200_OK,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_404_NOT_FOUND,
)
from broadlink.remote import data_to_pulses, pulses_to_data

from config import get_device, LEARN_TIMEOUT_SEC

async def learn(request):
    try:
        device = get_device()

        captured_packet = None
        device.enter_learning()
        start_time = time.time()

        while True:
            try:
                captured_packet = device.check_data()
                break
            except:
                ## Packets not captured
                if time.time() - start_time > LEARN_TIMEOUT_SEC:
                    break
                time.sleep(1)
                continue

        if not captured_packet:
            return JSONResponse(
                {"error": "Unable to capture packet. Please try again"},
                status_code=HTTP_408_REQUEST_TIMEOUT,
            )

        return JSONResponse(
            {
                "message": "Packet captured successfully",
                "packet": data_to_pulses(captured_packet),
            },
            status_code=HTTP_200_OK,
        )

    except Exception as e:

        return JSONResponse(
            {"error": str(e)}, status_code=HTTP_500_INTERNAL_SERVER_ERROR
        )


async def send_packet(request):
    try:
        device = get_device()

        data = await request.json()
        packet = data.get("packet")
        if isinstance(packet, list):
            packet = pulses_to_data(pulses=packet)

        if not packet:
            return JSONResponse(
                {"error": "Packet not provided or invalid type"},
                status_code=HTTP_404_NOT_FOUND,
            )

        device.send_data(packet)
        return JSONResponse(
            {"message": "Packet sent successfully"}, status_code=HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            {"error": str(e)}, status_code=HTTP_500_INTERNAL_SERVER_ERROR
        )
