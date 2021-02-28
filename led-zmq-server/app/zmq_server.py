import zmq
from led_core import LedCore

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5567")
lc = LedCore()
while True:
    result = "success"
    message = socket.recv_pyobj()
    try:
        if message["action"] == "get_pixels":
            result = lc.strip_action("get_pixels")
        else:
            lc.strip_action(message["action"], **message["kwargs"])
        socket.send_pyobj(result)
    except Exception as e:
        result = "An exception of type {} occurred. Arguments:\n{}".format(
            type(e).__name__, str(e.args)
        )

socket.close()
context.term()
