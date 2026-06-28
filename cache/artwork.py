import hashlib
import os

import requests


class ArtworkCache:

    def __init__(self, base_url, token):

        self.base_url = base_url.rstrip("/")

        self.token = token

        os.makedirs("cache/images", exist_ok=True)

    def get(self, picture):

        if not picture:
            return None

        url = self.base_url + picture

        extension = os.path.splitext(picture)[1]

        if extension == "":
            extension = ".jpg"

        filename = hashlib.md5(
            url.encode()
        ).hexdigest() + extension

        path = os.path.join(
            "cache",
            "images",
            filename
        )

        if os.path.exists(path):
            return path

        headers = {
            "Authorization":
            f"Bearer {self.token}"
        }

        r = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if r.status_code != 200:
            return None

        with open(path, "wb") as f:

            f.write(r.content)

        return path
