import pygame

pygame.init()

white = (255, 255, 255)
lbrown = (196, 164, 132)
brown = (150, 75, 0)
display = pygame.display.Info()
width = display.current_w
height = display.current_h
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Chess")

wpawn = pygame.image.load("/Users/prn/PycharmProjects/chess/chessimgs/wP.svg")
bpawn = pygame.image.load("/Users/prn/PycharmProjects/chess/chessimgs/bP.svg")
wpawn = pygame.transform.scale(wpawn, (100, 100))
bpawn = pygame.transform.scale(bpawn, (100, 100))

class Board:
    def __init__(self):
        self.rows, self.cols = 8, 8
        self.blockSize = min(screen.get_width() // self.cols, screen.get_height() // self.rows)
        self.topLeftX = (screen.get_width() - self.blockSize * self.cols) // 2
        self.topLeftY = (screen.get_height() - self.blockSize * self.rows) // 2
        self.blockMap = {}

        for x in range(self.cols):
            for y in range(self.rows):
                block_center = (self.topLeftX + (x + 0.5) * self.blockSize, self.topLeftY + (y + 0.5) * self.blockSize)
                self.blockMap[(x, y)] = block_center

    def drawBoard(self):
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pygame.Rect(self.topLeftX + x * self.blockSize, self.topLeftY + y * self.blockSize,
                                   self.blockSize, self.blockSize)
                color = lbrown if (x + y) % 2 == 0 else brown
                pygame.draw.rect(screen, color, rect)


class Pieces:
    def __init__(self, board_instance):
        self.board_instance = board_instance
        self.pawn_positions = []
        self.desired_y = 1  # Desired y-coordinate

    def move_pawns_to_desired_blocks(self):
        desired_blocks = [(x, self.desired_y) for x in range(8)]
        self.pawn_positions = [self.board_instance.blockMap[block_coord] for block_coord in desired_blocks]

    def drawPawns(self, screen):
        self.move_pawns_to_desired_blocks()
        pawn_size = wpawn.get_size()
        for position in self.pawn_positions:
            pawn_x = position[0] - pawn_size[0] // 2
            pawn_y = position[1] - pawn_size[1] // 2
            screen.blit(wpawn, (pawn_x, pawn_y))


def run():
    global screen
    running = True
    board_instance = Board()
    pieces_instance = Pieces(board_instance)

    while running:
        screen.fill(white)
        board_instance.drawBoard()
        pieces_instance.drawPawns(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for x in range(board_instance.cols):
                        for y in range(board_instance.rows):
                            rect = pygame.Rect(board_instance.topLeftX + x * board_instance.blockSize,
                                               board_instance.topLeftY + y * board_instance.blockSize,
                                               board_instance.blockSize, board_instance.blockSize)
                            if rect.collidepoint(event.pos):
                                print("Selected block:", (x, y))
                                print("Block center coordinates:", board_instance.blockMap[(x, y)])

        if pygame.event.get(pygame.VIDEORESIZE):
            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

        pygame.display.flip()


if __name__ == "__main__":
    run()
