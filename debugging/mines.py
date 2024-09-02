#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_count = 0  # Compteur pour les cases révélées
        self.total_cells = width * height
        self.total_safe_cells = self.total_cells - len(self.mines)

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True  # Si déjà révélé, ne rien faire

        if (y * self.width + x) in self.mines:
            return False  # Mine touchée

        self.revealed[y][x] = True
        self.revealed_count += 1

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)

        return True

    def get_valid_coordinate(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0 or value >= self.width:
                    raise ValueError
                return value
            except ValueError:
                print(f"Entrée invalide. Veuillez entrer un nombre entre 0 et {self.width - 1}.")

    def play(self):
        while True:
            self.print_board()
            x = self.get_valid_coordinate("Entrez la coordonnée x: ")
            y = self.get_valid_coordinate("Entrez la coordonnée y: ")
            
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! Vous avez touché une mine.")
                break
            if self.revealed_count == self.total_safe_cells:
                self.print_board(reveal=True)
                print("Félicitations! Vous avez gagné la partie.")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
