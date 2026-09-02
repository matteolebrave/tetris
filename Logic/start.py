import tkinter as tk
from random import randint

from Logic.parameters import WIDTH, HEIGHT, SPEED
from Logic.logic import Piece, move_piece, rotate_piece, check_collision
from Logic.shapes import T, S, Z, O, L, J, I

from UI.game_ui import GameUI


SHAPES = [T, S, Z, O, L, J, I]


def create_empty_grid():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


def create_piece():
    return Piece(
        shape=SHAPES[randint(0, len(SHAPES) - 1)],
        rotation=0,
        posX=WIDTH // 2 - 2,
        posY=0
    )


def is_game_over(piece, grid):
    return check_collision(piece, grid, 0, 0, 0)


def mainloop():
    grid = create_empty_grid()
    piece = create_piece()

    root = tk.Tk()

    # L'interface est maintenant dans UI/game_ui.py
    ui = GameUI(root)

    game_started = False

    def on_key(event):
        nonlocal grid, game_started

        # Première touche : démarrer la partie
        if not game_started:
            game_started = True
            ui.draw(grid, piece)

            root.after(300, game_loop)
            return

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
        nonlocal grid, piece, game_started

        if not game_started:
            return

        # La pièce tombe
        if not piece.locked:
            grid = move_piece("down", piece, grid)
            ui.draw(grid, piece)

        # La pièce est verrouillée
        else:
            print("Pièce verrouillée !")

            piece = create_piece()

            if is_game_over(piece, grid):
                print("GAME OVER")
                root.destroy()
                return

            ui.draw(grid, piece)

        root.after(SPEED, game_loop)

    ui.draw(grid, piece)

    root.after(SPEED, game_loop)

    root.mainloop()

    return "Game_over"
