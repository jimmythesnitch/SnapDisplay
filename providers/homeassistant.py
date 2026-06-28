import json
import websocket


class HomeAssistant:

    def __init__(self, url, token):

        self.url = (
            url.replace("http://", "ws://")
               .replace("https://", "wss://")
            + "/api/websocket"
        )

        self.token = token

    def connect(self):

        ws = websocket.create_connection(self.url)

        hello = json.loads(ws.recv())

        if hello["type"] != "auth_required":
            return False

        ws.send(json.dumps({
            "type": "auth",
            "access_token": self.token
        }))

        reply = json.loads(ws.recv())

        ws.close()

        return reply["type"] == "auth_ok"
