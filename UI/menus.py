import tkinter as tk

from Logic.parameters import WIDTH, HEIGHT


# ============================================================
# GIRLS GIRLS COLORS 
# ============================================================

BACKGROUND_COLOR = "#FFF5FA"
CARD_COLOR = "#FFFFFF"
CARD_BORDER_COLOR = "#FFD1E3"

TITLE_COLOR = "#FF5FA2"
SUBTITLE_COLOR = "#A56B87"
TEXT_COLOR = "#4A3040"
SECONDARY_TEXT_COLOR = "#B58A9F"

BUTTON_COLOR = "#FFF0F6"
BUTTON_HOVER_COLOR = "#FFE0ED"
BUTTON_BORDER_COLOR = "#FFC1D9"

DANGER_COLOR = "#FF4F87"
DANGER_HOVER_COLOR = "#FF78A5"

ACCENT_PURPLE = "#B89CFF"
PURPLE_HOVER = "#CBB8FF"


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


def create_button(parent, text, command, accent=False):
    """Crée un bouton cute / girls girls."""

    if accent:
        bg = TITLE_COLOR
        hover = DANGER_HOVER_COLOR
        fg = "#4A3040"
    else:
        bg = BUTTON_COLOR
        hover = BUTTON_HOVER_COLOR
        fg = TEXT_COLOR

    button = tk.Button(
        parent,
        text=text,
        font=("Arial", 12, "bold"),
        fg=fg,
        bg=bg,
        activeforeground=fg,
        activebackground=hover,
        width=20,
        height=2,
        borderwidth=0,
        relief="flat",
        cursor="hand2",
        command=command
    )

    def on_enter(event):
        button.configure(bg=hover)

    def on_leave(event):
        button.configure(bg=bg)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button


def create_card(root, width, height):
    """Crée une carte blanche avec une bordure rose."""

    outer = tk.Frame(
        root,
        bg=CARD_BORDER_COLOR,
        width=width + 4,
        height=height + 4
    )

    outer.pack_propagate(False)

    inner = tk.Frame(
        outer,
        bg=CARD_COLOR,
        width=width,
        height=height
    )

    inner.pack(
        padx=2,
        pady=2
    )

    inner.pack_propagate(False)

    return outer, inner


# ============================================================
# HOME UI 
# ============================================================

class HomeUI:
    def __init__(self, root, start_game):

        self.root = root
        self.start_game = start_game

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.root.title("Tetris ♡")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        window_width = 500
        window_height = 650

        center_window(
            self.root,
            window_width,
            window_height
        )

        # ----------------------------------------------------
        # BACKGROUND
        # ----------------------------------------------------

        self.background = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOR
        )

        self.background.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # TOP DECORATION
        # ----------------------------------------------------

        self.top_line = tk.Frame(
            self.background,
            bg=TITLE_COLOR,
            height=5
        )

        self.top_line.pack(
            fill="x",
            side="top"
        )

        # ----------------------------------------------------
        # MAIN CARD
        # ----------------------------------------------------

        self.card_outer, self.frame = create_card(
            self.background,
            380,
            540
        )

        self.card_outer.pack(
            pady=45
        )

        # ----------------------------------------------------
        # LITTLE HEART
        # ----------------------------------------------------

        self.heart = tk.Label(
            self.frame,
            text="♡",
            font=("Arial", 18),
            fg=ACCENT_PURPLE,
            bg=CARD_COLOR
        )

        self.heart.pack(
            pady=(28, 0)
        )

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        self.title = tk.Label(
            self.frame,
            text="TETRIS",
            font=("Arial", 42, "bold"),
            fg=TITLE_COLOR,
            bg=CARD_COLOR
        )

        self.title.pack(
            pady=(5, 3)
        )

        # ----------------------------------------------------
        # DECORATIVE LINE
        # ----------------------------------------------------

        self.title_line = tk.Frame(
            self.frame,
            bg=ACCENT_PURPLE,
            width=65,
            height=4
        )

        self.title_line.pack(
            pady=(5, 12)
        )

        # ----------------------------------------------------
        # SUBTITLE
        # ----------------------------------------------------

        self.subtitle = tk.Label(
            self.frame,
            text="✦ CLASSIC BLOCK PUZZLE ✦",
            font=("Arial", 9, "bold"),
            fg=SUBTITLE_COLOR,
            bg=CARD_COLOR
        )

        self.subtitle.pack(
            pady=(0, 32)
        )

        # ----------------------------------------------------
        # PLAY BUTTON
        # ----------------------------------------------------

        self.play_button = create_button(
            self.frame,
            "♡   JOUER",
            self.start_game,
            accent=True
        )

        self.play_button.pack(
            pady=7
        )

        # ----------------------------------------------------
        # QUIT BUTTON
        # ----------------------------------------------------

        self.quit_button = create_button(
            self.frame,
            "×   QUITTER",
            self.root.destroy
        )

        self.quit_button.pack(
            pady=7
        )

        # ----------------------------------------------------
        # CONTROLS
        # ----------------------------------------------------

        controls_title = tk.Label(
            self.frame,
            text="♡  COMMANDES  ♡",
            font=("Arial", 9, "bold"),
            fg=SECONDARY_TEXT_COLOR,
            bg=CARD_COLOR
        )

        controls_title.pack(
            pady=(27, 8)
        )

        self.controls = tk.Label(
            self.frame,
            text="←  →    Déplacer\n"
                 "↑       Tourner\n"
                 "↓       Accélérer",
            font=("Arial", 11),
            fg=TEXT_COLOR,
            bg=CARD_COLOR,
            justify="left"
        )

        self.controls.pack()

        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        self.footer = tk.Label(
            self.frame,
            text="♡  For Yuna • HAVE FUN  ♡",
            font=("Arial", 8, "bold"),
            fg=SECONDARY_TEXT_COLOR,
            bg=CARD_COLOR
        )

        self.footer.pack(
            side="bottom",
            pady=18
        )


# ============================================================
# GAME OVER UI 
# ============================================================

class GameOverUI:
    def __init__(self, root, restart_game):

        self.root = root
        self.restart_game = restart_game

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.root.title("Tetris ♡ Game Over")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        window_width = 500
        window_height = 600

        center_window(
            self.root,
            window_width,
            window_height
        )

        # ----------------------------------------------------
        # BACKGROUND
        # ----------------------------------------------------

        self.background = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOR
        )

        self.background.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # TOP LINE
        # ----------------------------------------------------

        self.top_line = tk.Frame(
            self.background,
            bg=DANGER_COLOR,
            height=5
        )

        self.top_line.pack(
            fill="x",
            side="top"
        )

        # ----------------------------------------------------
        # CARD
        # ----------------------------------------------------

        self.card_outer, self.frame = create_card(
            self.background,
            380,
            490
        )

        self.card_outer.pack(
            pady=45
        )

        # ----------------------------------------------------
        # LITTLE HEART
        # ----------------------------------------------------

        self.heart = tk.Label(
            self.frame,
            text="♡",
            font=("Arial", 20),
            fg=ACCENT_PURPLE,
            bg=CARD_COLOR
        )

        self.heart.pack(
            pady=(28, 0)
        )

        # ----------------------------------------------------
        # GAME OVER TITLE
        # ----------------------------------------------------

        self.title = tk.Label(
            self.frame,
            text="GAME OVER",
            font=("Arial", 38, "bold"),
            fg=DANGER_COLOR,
            bg=CARD_COLOR
        )

        self.title.pack(
            pady=(5, 5)
        )

        # ----------------------------------------------------
        # DECORATION
        # ----------------------------------------------------

        self.title_line = tk.Frame(
            self.frame,
            bg=ACCENT_PURPLE,
            width=65,
            height=4
        )

        self.title_line.pack(
            pady=(5, 22)
        )

        # ----------------------------------------------------
        # MESSAGE
        # ----------------------------------------------------

        self.message = tk.Label(
            self.frame,
            text="La partie est terminée ♡",
            font=("Arial", 12),
            fg=SUBTITLE_COLOR,
            bg=CARD_COLOR
        )

        self.message.pack(
            pady=(0, 30)
        )

        # ----------------------------------------------------
        # RESTART BUTTON
        # ----------------------------------------------------

        self.restart_button = create_button(
            self.frame,
            "♡   REJOUER",
            self.restart_game,
            accent=True
        )

        self.restart_button.pack(
            pady=7
        )

        # ----------------------------------------------------
        # QUIT BUTTON
        # ----------------------------------------------------

        self.quit_button = create_button(
            self.frame,
            "×   QUITTER",
            self.root.destroy
        )

        self.quit_button.pack(
            pady=7
        )

        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        self.footer = tk.Label(
            self.frame,
            text="YOU GOT THIS ♡",
            font=("Arial", 8, "bold"),
            fg=SECONDARY_TEXT_COLOR,
            bg=CARD_COLOR
        )

        self.footer.pack(
            side="bottom",
            pady=20
        )
