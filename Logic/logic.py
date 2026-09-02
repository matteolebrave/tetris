from Logic.parameters import WIDTH, HEIGHT, SPEED

class Piece:
    def __init__(self, shape, rotation, posX, posY):
        self.shape = shape
        self.rotation = rotation
        self.posX = posX
        self.posY = posY
        self.locked = False

    def change_pos(self, posX, posY):
        self.posX += posX
        self.posY += posY

    def rotate(self):
        self.rotation = (self.rotation + 1) %4

    def lock(self, boolean):
        self.locked = boolean

def check_rows(grid):
    new_grid = [row for row in grid if row.count(1) < WIDTH]

    while len(new_grid) < HEIGHT:
        new_grid.insert(0, [0 for _ in range(WIDTH)])

    return new_grid

def move_piece(direction, piece, grid):
    if not piece.locked:
        dx = 0
        dy = 0
        if direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1
        elif direction == "down":
            dy = 1

        if not check_collision(piece,grid,dx,dy, 0):
            piece.change_pos(dx,dy)
        elif direction == "down":
            shape = piece.shape[piece.rotation]
            for y in range(4):
                for x in range(4):
                    if shape[y][x] == 1:

                        new_x = piece.posX + x 
                        new_y = piece.posY + y

                        grid[new_y][new_x] = 1 
            piece.lock(True)
            grid = check_rows(grid)
        return grid
    return grid

def rotate_piece(piece, grid):
    if not piece.locked:
        if not check_collision(piece,grid,0,0,1):
            piece.rotate()
    return grid

def check_collision(piece, grid, dx, dy, indice):
    shape = piece.shape[(piece.rotation + indice)%4]

    for y in range(4):
        for x in range(4):
            if shape[y][x] == 1:

                new_x = piece.posX + x + dx
                new_y = piece.posY + y + dy

                # Wall / floor
                if new_x < 0 or new_x >= WIDTH:
                    return True

                if new_y < 0 or new_y >= HEIGHT:
                    return True

                # Another piece
                if grid[new_y][new_x] == 1:
                    return True

    return False



