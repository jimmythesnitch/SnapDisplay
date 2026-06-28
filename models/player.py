class Player:

    def __init__(self):

        self.connected = False

        self.entity = ""

        self.state = "idle"

        self.title = ""

        self.artist = ""

        self.album = ""

        self.picture = ""

        self.volume = 0

        self.source = ""

    def update(self, entity):

        self.entity = entity.get("entity_id", "")

        self.state = entity.get("state", "unknown")

        attributes = entity.get("attributes", {})

        self.title = attributes.get("media_title", "")

        self.artist = attributes.get("media_artist", "")

        self.album = attributes.get("media_album_name", "")

        self.picture = attributes.get("entity_picture", "")

        self.volume = attributes.get("volume_level", 0)

        self.source = attributes.get("source", "")

        self.connected = True
