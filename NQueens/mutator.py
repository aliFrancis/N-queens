from NQueens.board import Board
from NQueens.piece import Piece
from NQueens.breeder import RandomPieceChangeBreeder

class Mutator():
    def __init__(self, population, scoreboard, survivor_ratio, metrics = None, breeder = None):
        self.population = population
        self.scoreboard = scoreboard
        if metrics is None:
            self.metrics = ['is_peaceable']
        self.survivor_ratio = survivor_ratio
        if breeder is None:
            self.breeder = RandomPieceChangeBreeder()

    def __call__(self):
        survivor_IDs = self.scoreboard.sort_by(self.metrics)[0:self.survivor_cutoff]
        survivors = self.population(survivor_IDs)
        new_generation = breeder(survivors)

    @property
    def survivor_cutoff(self):
        return round(len(self.population)*self.survivor_ratio)

    
