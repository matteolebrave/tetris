import tkinter as tk

from UI.menus import HomeUI, GameOverUI
from Logic.start import mainloop


def start_game(root, difficulty):
    print("Le jeu commence !")
    root.destroy()
    # Pour l'instant, on peut simplement fermer le menu.
    result = mainloop(difficulty)

    if result == "Game_over":
        print("Afficher écran de fin")
        end_game(difficulty)
    # Plus tard, on lancera ici ton GameUI.
    
def end_game(difficulty):
    root = tk.Tk()
    game_over = GameOverUI(root, lambda: restart_game(root, difficulty))
    root.mainloop()

    return 

def restart_game(root, difficulty):
    root.destroy()

    root = tk.Tk()
    start_game(root, difficulty)


def main():
    root = tk.Tk()

    home = HomeUI(
        root,
        lambda difficulty: start_game(root, difficulty)
    )

    root.mainloop()


if __name__ == "__main__":
    main()
