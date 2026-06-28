#!/usr/bin/env python3

import os
import sys

# Configure SDL BEFORE importing pygame.
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame

from core.config import Config

VERSION = "0.1.1"

BACKGROUND = (8, 8, 8)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
BLUE = (120, 220, 255)


def main():
    config = Config()

    pygame.init()

    display = pygame.display.Info()
    screen_width = display.current_w
    screen_height = display.current_h

    screen = pygame.display.set_mode(
        (screen_width, screen_height),
        pygame.FULLSCREEN,
    )

    pygame.display.set_caption("SnapDisplay")

    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("DejaVu Sans", 60, bold=True)
    small_font = pygame.font.SysFont("DejaVu Sans", 28)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND)

        title = title_font.render(
            "SnapDisplay",
            True,
            WHITE,
        )

        version = small_font.render(
            f"Version {VERSION}",
            True,
            GRAY,
        )

        status = small_font.render(
            "Waiting for Home Assistant...",
            True,
            BLUE,
        )

        screen.blit(
            title,
            (
                screen_width // 2 - title.get_width() // 2,
                screen_height // 2 - 90,
            ),
        )

        screen.blit(
            version,
            (
                screen_width // 2 - version.get_width() // 2,
                screen_height // 2,
            ),
        )

        screen.blit(
            status,
            (
                screen_width // 2 - status.get_width() // 2,
                screen_height // 2 + 60,
            ),
        )

        pygame.display.flip()
        clock.tick(config.get("display.fps", 60))

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
