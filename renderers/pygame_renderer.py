import os
import pygame

BACKGROUND = (8, 8, 8)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
GREEN = (80, 220, 120)
RED = (220, 80, 80)


class Renderer:

    def __init__(self, fps=60):

        pygame.init()

        self.display = pygame.display.Info()

        self.screen = pygame.display.set_mode(
            (
                self.display.current_w,
                self.display.current_h
            ),
            pygame.FULLSCREEN
        )

        pygame.display.set_caption("SnapDisplay")

        self.clock = pygame.time.Clock()

        self.fps = fps

        self.title_font = pygame.font.SysFont(
            "DejaVu Sans",
            60,
            bold=True
        )

        self.artist_font = pygame.font.SysFont(
            "DejaVu Sans",
            42,
            bold=True
        )

        self.song_font = pygame.font.SysFont(
            "DejaVu Sans",
            34
        )

        self.small_font = pygame.font.SysFont(
            "DejaVu Sans",
            24
        )

        self.artwork = None

        artwork_file = "assets/test.jpg"

        if os.path.exists(artwork_file):

            try:

                image = pygame.image.load(artwork_file)

                self.artwork = pygame.transform.smoothscale(
                    image,
                    (300, 300)
                )

            except Exception as e:

                print(e)

                self.artwork = None

    def draw_text(self, font, text, colour, x, y):

        surface = font.render(text, True, colour)

        self.screen.blit(surface, (x, y))

    def draw(self, player):

        self.screen.fill(BACKGROUND)

        self.draw_text(
            self.title_font,
            "SnapDisplay",
            WHITE,
            40,
            40
        )

        self.draw_text(
            self.small_font,
            "Version 0.4.0",
            GRAY,
            45,
            110
        )

        #
        # Album artwork
        #

        if self.artwork:

            self.screen.blit(
                self.artwork,
                (40, 170)
            )

        else:

            pygame.draw.rect(
                self.screen,
                (50, 50, 50),
                (40, 170, 300, 300),
                2
            )

        #
        # Metadata
        #

        text_x = 380

        if player is None:

            self.draw_text(
                self.artist_font,
                "Player Not Found",
                RED,
                text_x,
                220
            )

        else:

            self.draw_text(
                self.artist_font,
                player.artist or "Unknown Artist",
                WHITE,
                text_x,
                190
            )

            self.draw_text(
                self.song_font,
                player.title or "Unknown Title",
                GREEN,
                text_x,
                255
            )

            self.draw_text(
                self.small_font,
                player.album or "",
                GRAY,
                text_x,
                315
            )

            self.draw_text(
                self.small_font,
                player.state.capitalize(),
                GRAY,
                text_x,
                390
            )

        pygame.display.flip()

    def tick(self):

        self.clock.tick(self.fps)

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return False

        return True

    def close(self):

        pygame.quit()
