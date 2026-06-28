#!/usr/bin/env python3

import os
import sys

# Don't let pygame steal the audio device.
os.environ["SDL_AUDIODRIVER"] = "dummy"

from core.config import Config
from providers.homeassistant import HomeAssistant
from renderers.pygame_renderer import Renderer


def main():

    config = Config()

    ha = HomeAssistant(
        config.get("homeassistant.url"),
        config.get("homeassistant.token")
    )

    if not ha.connect():

        print("Unable to connect to Home Assistant.")
        sys.exit(1)

    renderer = Renderer(
        config.get("display.fps", 60)
    )

    running = True

    while running:

        #
        # Window Events
        #

        running = renderer.events()

        #
        # Read Player
        #

        player = ha.get_player(
            config.get("musicassistant.player")
        )

        #
        # Draw Screen
        #

        renderer.draw(player)

        #
        # Limit FPS
        #

        renderer.tick()

    renderer.close()


if __name__ == "__main__":
    main()
