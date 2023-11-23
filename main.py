import pygame
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtCore import Qt

from object import Object
from text import Text


class PygameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.player = Object('player.png', 50, 50, 600, 300, 1)
        self.text = Text("Arial", 36)
        self.run = True

    def player_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.run = False
        return pygame.key.get_pressed()

    def logic(self, action_from_input):
        if not action_from_input:
            self.run = False
        else:
            self.player.movement(action_from_input)

    def render_game(self):
        self.clock.tick(140)
        self.display.fill((0, 0, 0))
        pygame.draw.rect(self.display, (255, 255, 255), (550, 50, 840, 750), 5)
        self.display.blit(self.player.sprite, (self.player.x, self.player.y))
        self.text.render(self, str(self.player.x), 200, 200)
        self.text.render(self, str(self.player.y), 200, 240)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = PygameWidget()
        self.setCentralWidget(self.central_widget)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            # Toggle between Pygame and QTextEdit visibility
            self.central_widget.setVisible(not self.central_widget.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
