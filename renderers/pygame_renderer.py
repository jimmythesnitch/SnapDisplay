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

    def draw_text(self, font, text, colour, y):

        surface = font.render(text, True, colour)

        x = self.screen.get_width() // 2 - surface.get_width() // 2

        self.screen.blit(surface, (x, y))

    def draw(self, player):

        self.screen.fill(BACKGROUND)

        self.draw_text(
            self.title_font,
            "SnapDisplay",
            WHITE,
            40
        )

        self.draw_text(
            self.small_font,
            "Version 0.3.0",
            GRAY,
            115
        )

        if player is None:

            self.draw_text(
                self.artist_font,
                "Player Not Found",
                RED,
                260
            )

        else:

            self.draw_text(
                self.artist_font,
                player.artist or "Unknown Artist",
                WHITE,
                220
            )

            self.draw_text(
                self.song_font,
                player.title or "Unknown Title",
                GREEN,
                295
            )

            self.draw_text(
                self.small_font,
                player.album,
                GRAY,
                350
            )

            self.draw_text(
                self.small_font,
                player.state.capitalize(),
                GRAY,
                430
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
