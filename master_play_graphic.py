import play
import judge
import pygame
from pygame.locals import *


class Mastermind:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 320)
        self.shortcuts = {
                            (K_x, KMOD_LMETA): 'print("cmd+X")',
                            (K_x, KMOD_LALT): 'print("alt+X")',
                            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
                            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
                            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
                            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
                            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()',
                            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
                            (K_g, KMOD_LMETA): 'self.toggle_frame()'
                        }

        Mastermind.screen = pygame.display.set_mode(self.rect.size, self.flags)
        Mastermind.t = Text('Welcome to Mastermind', pos=(40, 130))
        
        Mastermind.running = True

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

    def run(self):
        """Run the main event loop."""
        while Mastermind.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.do_shortcut(event)

                if event.type == QUIT:
                    Mastermind.running = False

            Mastermind.screen.fill(Color('gray'))
            Mastermind.t.draw()
            pygame.display.update()

        pygame.quit()


class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        Mastermind.screen.blit(self.img, self.rect)


class Scene:
    """Create a new scene (room, level, view)."""
    id = 0
    bg = Color('gray')

    def __init__(self, *args, **kwargs):
        # Append the new scene and make it the current scene
        Mastermind.scenes.append(self)
        Mastermind.scene = self

        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

    def draw(self):
        """Draw all objects in the scene."""
        Mastermind.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self):
        return f'Scene {self.id}'


if __name__ == '__main__':
    Mastermind().run()

    # print('Welcome to the Mastermind Game! The rules are simple:')
    # print('Guess the hidden sequence of k colors and n positions!')
    # print('*Press (ctrl+d) to surrender\n')
    # k, n = play.ask_for_k_n()
    # hidden = play.generate_hidden(k, n)

    # # Play the game
    # print(f'Colors to choose from: {[color+1 for color in range(k)]}')
    # X_seq = 'X '*n
    # print(f'Hidden sequence: {X_seq}')

    # round_n = 0
    # MAX_ROUNDS = 10

    # while True:
    #     round_n += 1
    #     if round_n > MAX_ROUNDS:
    #         print('Maximum amount of rounds reached! You lose!')
    #         break
    #     new_query = play.ask_for_sequence(k, n, type='query', hidden=hidden)
    #     score = judge.check(k, n, hidden, new_query)
    #     X1, Y1 = score
    #     print(f'ROUND {round_n} ||| Query: {new_query} | full  hits: {X1}, color hits: {Y1}')
    #     if X1 == n:
    #         print('Congratulations! Hidden sequence guessed!')
    #         break