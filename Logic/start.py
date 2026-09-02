import tkinter as tk
from random import randint

from Logic.parameters import WIDTH, HEIGHT, SPEED, MOVE_DELAY
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

    ui = GameUI(root)

    game_started = False

    # Permet de savoir quelles touches sont actuellement pressées
    keys_pressed = set()

    def on_key_press(event):
        nonlocal grid, game_started

        # Première touche : démarrer la partie
        if not game_started:
            game_started = True
            ui.draw(grid, piece)

            root.after(SPEED, game_loop)
            return

        if piece.locked:
            return

        keys_pressed.add(event.keysym)

        # Déplacement immédiat
        if event.keysym == "Left":
            grid = move_piece("left", piece, grid)

        elif event.keysym == "Right":
            grid = move_piece("right", piece, grid)

        elif event.keysym == "Down":
            grid = move_piece("down", piece, grid)

        elif event.keysym == "Up":
            grid = rotate_piece(piece, grid)

        ui.draw(grid, piece)

    def on_key_release(event):
        keys_pressed.discard(event.keysym)

    def move_keys():
        """
        Répète les déplacements horizontaux/rotations
        sans modifier la vitesse de descente.
        """
        nonlocal grid

        if not game_started:
            return

        if piece.locked:
            return

        # Gauche
        if "Left" in keys_pressed:
            grid = move_piece("left", piece, grid)

        # Droite
        if "Right" in keys_pressed:
            grid = move_piece("right", piece, grid)

        # Rotation
        if "Up" in keys_pressed:
            grid = rotate_piece(piece, grid)

        ui.draw(grid, piece)

        # On répète les déplacements
        root.after(MOVE_DELAY, move_keys)

    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)

    def game_loop():
        nonlocal grid, piece, game_started

        if not game_started:
            return

        # La pièce tombe automatiquement
        # SPEED n'est PAS modifié.
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

        # La vitesse de descente reste toujours SPEED
        root.after(SPEED, game_loop)

    ui.draw(grid, piece)

    # Boucle de descente
    root.after(SPEED, game_loop)

    # Boucle de déplacement des touches
    root.after(MOVE_DELAY, move_keys)

    root.mainloop()

    return "Game_over"