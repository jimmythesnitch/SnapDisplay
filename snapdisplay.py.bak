#!/usr/bin/env python3

import os
import sys

# Prevent SDL from grabbing the audio device.
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame

from core.config import Config
from providers.homeassistant import HomeAssistant

VERSION = "0.2.0"

BACKGROUND = (8, 8, 8)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
GREEN = (80, 220, 120)
RED = (220, 80, 80)


def draw_text(screen, font, text, colour, y):

    surface = font.render(text, True, colour)

    x = screen.get_width() // 2 - surface.get_width() // 2

    screen.blit(surface, (x, y))


def main():

    config = Config()

    pygame.init()

    display = pygame.display.Info()

    screen = pygame.display.set_mode(
        (display.current_w, display.current_h),
        pygame.FULLSCREEN
    )

    pygame.display.set_caption("SnapDisplay")

    title_font = pygame.font.SysFont(
        "DejaVu Sans",
        60,
        bold=True
    )

    artist_font = pygame.font.SysFont(
        "DejaVu Sans",
        42,
        bold=True
    )

    song_font = pygame.font.SysFont(
        "DejaVu Sans",
        34
    )

    small_font = pygame.font.SysFont(
        "DejaVu Sans",
        24
    )

    clock = pygame.time.Clock()

    #
    # Default values
    #

    player = None

    error = None

    try:

        ha = HomeAssistant(
            config.get("homeassistant.url"),
            config.get("homeassistant.token")
        )

        if ha.connect():

            player = ha.get_player(
                config.get("musicassistant.player")
            )

        else:

            error = "Authentication Failed"

    except Exception as e:

        error = str(e)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND)

        draw_text(
            screen,
            title_font,
            "SnapDisplay",
            WHITE,
            40
        )

        draw_text(
            screen,
            small_font,
            f"Version {VERSION}",
            GRAY,
            115
        )

        if error:

            draw_text(
                screen,
                artist_font,
                error,
                RED,
                250
            )

        elif player is None:

            draw_text(
                screen,
                artist_font,
                "Player Not Found",
                RED,
                250
            )

        else:

            draw_text(
                screen,
                artist_font,
                player.artist or "Unknown Artist",
                WHITE,
                220
            )

            draw_text(
                screen,
                song_font,
                player.title or "Unknown Title",
                GREEN,
                300
            )

            draw_text(
                screen,
                small_font,
                player.album or "",
                GRAY,
                360
            )

            draw_text(
                screen,
                small_font,
                f"State : {player.state}",
                GRAY,
                430
            )

        pygame.display.flip()

        clock.tick(
            config.get("display.fps", 60)
        )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
