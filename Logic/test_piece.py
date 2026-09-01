import tkinter as tk
from random import randint
from parameters import WIDTH, HEIGHT
from logic import Piece, move_piece, rotate_piece
from shapes import T, S, Z, O, L, J, I


CELL_SIZE = 30
SHAPES = [T, S, Z, O, L, J, I]
BACKGROUND_COLOR = "#111111"
GRID_COLOR = "#333333"
BLOCK_COLOR = "#00bfff"
LOCKED_COLOR = "#ff9800"


def create_empty_grid():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


class GameUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Test Tetris")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        self.canvas = tk.Canvas(
            root,
            width=WIDTH * CELL_SIZE,
            height=HEIGHT * CELL_SIZE,
            bg=BACKGROUND_COLOR,
            highlightthickness=0
        )

        self.canvas.pack()

    def draw(self, grid, piece=None):
        self.canvas.delete("all")

        # Dessine la grille et les blocs déjà verrouillés
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] == 1:
                    color = LOCKED_COLOR
                else:
                    color = BACKGROUND_COLOR

                self.canvas.create_rectangle(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    (x + 1) * CELL_SIZE,
                    (y + 1) * CELL_SIZE,
                    fill=color,
                    outline=GRID_COLOR
                )

        # Dessine la pièce qui tombe
        if piece is not None and not piece.locked:
            shape = piece.shape[piece.rotation]

            for y in range(4):
                for x in range(4):
                    if shape[y][x] == 1:
                        grid_x = piece.posX + x
                        grid_y = piece.posY + y

                        if 0 <= grid_x < WIDTH and 0 <= grid_y < HEIGHT:
                            self.canvas.create_rectangle(
                                grid_x * CELL_SIZE,
                                grid_y * CELL_SIZE,
                                (grid_x + 1) * CELL_SIZE,
                                (grid_y + 1) * CELL_SIZE,
                                fill=BLOCK_COLOR,
                                outline=GRID_COLOR
                            )

def create_piece():
    return Piece(
        shape=SHAPES[randint(0, len(SHAPES) - 1)],
        rotation=0,
        posX=WIDTH // 2 - 2,
        posY=0
    )

def main():
    grid = create_empty_grid()

    piece = create_piece()

    root = tk.Tk()
    ui = GameUI(root)

    def on_key(event):
        nonlocal grid

        if piece.locked:
            return

        if event.keysym == "Left":
            grid = move_piece("left", piece, grid)

        elif event.keysym == "Right":
            grid = move_piece("right", piece, grid)

        elif event.keysym == "Down":
            grid = move_piece("down", piece, grid)
        elif event.keysym == "Up":
            grid = rotate_piece(piece, grid)

        ui.draw(grid, piece)

    root.bind("<KeyPress>", on_key)

    def game_loop():
        nonlocal grid, piece

        # La pièce actuelle tombe
        if not piece.locked:
            grid = move_piece("down", piece, grid)
            ui.draw(grid, piece)

        # La pièce vient d'être verrouillée
        else:
            print("Pièce verrouillée !")

            # Création d'une nouvelle pièce
            piece = create_piece()

            ui.draw(grid, piece)

        root.after(300, game_loop)

    ui.draw(grid, piece)

    root.after(300, game_loop)

    root.mainloop()



if __name__ == "__main__":
    main()
