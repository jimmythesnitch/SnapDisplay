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
        self.ws = None
        self.msgid = 1

    def connect(self):

        self.ws = websocket.create_connection(self.url)

        hello = json.loads(self.ws.recv())

        if hello["type"] != "auth_required":
            return False

        self.ws.send(json.dumps({
            "type": "auth",
            "access_token": self.token
        }))

        reply = json.loads(self.ws.recv())

        return reply["type"] == "auth_ok"

    def get_entity(self, entity_id):

        self.ws.send(json.dumps({
            "id": self.msgid,
            "type": "get_states"
        }))

        self.msgid += 1

        while True:

            reply = json.loads(self.ws.recv())

            if reply.get("type") != "result":
                continue

            for entity in reply["result"]:

                if entity["entity_id"] == entity_id:
                    return entity

            return None
