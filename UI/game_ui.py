import tkinter as tk

from Logic.parameters import WIDTH, HEIGHT


# ============================================================
# GIRLS GIRLS COLORS
# ============================================================

BACKGROUND_COLOR = "#FFF5FA"
GRID_COLOR = "#F2D6E3"

BLOCK_COLOR = "#FF5FA2"
BLOCK_HOVER_COLOR = "#FF8FBB"

LOCKED_COLOR = "#B89CFF"

BLOCK_BORDER_COLOR = "#FFFFFF"


# ============================================================
# HELPERS
# ============================================================

def center_window(root, width, height):
    """Centre la fenêtre sur l'écran."""

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")


# ============================================================
# GAME UI
# ============================================================

class GameUI:
    def __init__(self, root):

        self.root = root

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.root.title("Tetris")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        cell_size = 30

        window_width = WIDTH * cell_size
        window_height = HEIGHT * cell_size

        center_window(
            self.root,
            window_width,
            window_height
        )

        # ----------------------------------------------------
        # CANVAS
        # ----------------------------------------------------

        self.canvas = tk.Canvas(
            root,
            width=window_width,
            height=window_height,
            bg=BACKGROUND_COLOR,
            highlightthickness=0
        )

        self.canvas.pack()

    def draw(self, grid, piece=None):
        """
        Dessine la grille, les pièces verrouillées
        et la pièce actuellement en mouvement.
        """

        self.canvas.delete("all")

        cell_size = 30

        # ----------------------------------------------------
        # GRILLE + BLOCS VERROUILLÉS
        # ----------------------------------------------------

        for y in range(HEIGHT):
            for x in range(WIDTH):

                if grid[y][x] == 1:
                    color = LOCKED_COLOR
                else:
                    color = BACKGROUND_COLOR

                self.canvas.create_rectangle(
                    x * cell_size,
                    y * cell_size,
                    (x + 1) * cell_size,
                    (y + 1) * cell_size,
                    fill=color,
                    outline=GRID_COLOR,
                    width=1
                )

                # Effet glossy sur les blocs verrouillés
                if grid[y][x] == 1:
                    self.canvas.create_rectangle(
                        x * cell_size + 3,
                        y * cell_size + 3,
                        (x + 1) * cell_size - 3,
                        y * cell_size + 7,
                        fill="#CBB8FF",
                        outline=""
                    )

        # ----------------------------------------------------
        # PIÈCE EN MOUVEMENT
        # ----------------------------------------------------

        if piece is not None and not piece.locked:

            shape = piece.shape[piece.rotation]

            for y in range(4):
                for x in range(4):

                    if shape[y][x] == 1:

                        grid_x = piece.posX + x
                        grid_y = piece.posY + y

                        if (
                            0 <= grid_x < WIDTH
                            and 0 <= grid_y < HEIGHT
                        ):

                            # Bloc principal
                            self.canvas.create_rectangle(
                                grid_x * cell_size + 1,
                                grid_y * cell_size + 1,
                                (grid_x + 1) * cell_size - 1,
                                (grid_y + 1) * cell_size - 1,
                                fill=BLOCK_COLOR,
                                outline=BLOCK_BORDER_COLOR,
                                width=1
                            )

                            # Highlight glossy
                            self.canvas.create_rectangle(
                                grid_x * cell_size + 4,
                                grid_y * cell_size + 4,
                                (grid_x + 1) * cell_size - 4,
                                grid_y * cell_size + 9,
                                fill=BLOCK_HOVER_COLOR,
                                outline=""
                            )
