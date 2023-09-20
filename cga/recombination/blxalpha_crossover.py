
import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List


class BlxalphaCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        chsize = len(p1.chromosome)
        child = [0 for i in range(chsize)]
        alpha = random.uniform(0, 1)
        c_min = 0.0
        c_max = 0.0
        min_range = 0.0
        max_range = 0.0
        for i in range(chsize):
            p1_allele = p1.chromosome[i]
            p2_allele = p2.chromosome[i]

            if (p1_allele > p2_allele):
                c_max = p1_allele
                c_min = p2_allele
            elif (p1_allele < p2_allele):
                c_max = p2_allele
                c_min = p1_allele
            else:
                c_max = p1_allele  # or p2_allele because it is the case where p1_allele=p2_allele

            l = c_max-c_min

            min_range = c_min - (l*alpha)
            max_range = c_max + (l*alpha)

            new_allele = random.uniform(min_range, max_range)
            child[i] = round(new_allele, 3)

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(child)
        indv.fitness_value = self.problem.f(child)
        return indv

    def get_recombinations(self) -> List[Individual]:

        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
