from cga.problems.abstract_problem import AbstractProblem
class Maxcut20_01(AbstractProblem):
    """
    Maximum Cut (MAXCUT) function implementation for optimization problems.

    The MAXCUT function is used for testing optimization algorithms, particularly those involving maximum cut problems.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the MAXCUT function value for a given list of variables.

    Notes
    -----
    Length of chromosomes = 20
    Maximum Fitness Value = 10.119812
    """

    def f(self, x: list) -> float:
        """
        Calculate the MAXCUT function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The MAXCUT function value.
        """
        problema = [
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.359902,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.313702, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.848267, 0.000000, 0.000000, 0.000000, 0.287508, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.117489,
                0.000000, 0.000000, 0.000000, 0.000000, 0.190953, 0.000000, 0.000000, 0.000000, 0.000000, 0.916311],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.848267, 0.000000, 0.000000, 0.000000, 0.084579, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.721013, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.084579, 0.000000, 0.000000, 0.000000, 0.000000, 0.863363,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.032054],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.764415, 0.000000, 0.495863, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.287508, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.109939, 0.000000, 0.000000, 0.000000, 0.167750, 0.000000, 0.000000, 0.000000],
            [0.359902, 0.000000, 0.117489, 0.000000, 0.000000, 0.863363, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.928091, 0.000000, 0.000000, 0.118362, 0.000000, 0.000000, 0.969750],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.652776, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.764415, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.424253, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.109939, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.495863, 0.000000, 0.000000, 0.928091,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.190953, 0.000000, 0.721013, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.252964, 0.936165, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.652776, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.313702, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.167750, 0.118362,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.424253, 0.000000, 0.000000, 0.252964, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000000, 0.000000, 0.000000, 0.936165, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.916311, 0.000000, 0.000000, 0.032054, 0.000000, 0.000000, 0.000000, 0.969750,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]
        ]

        cols = 20
        fitness = 0.0

        for i in range(cols-1):
            j = i
            for j in range(cols):
                if x[i] ^ x[j]:
                    fitness += problema[i][j]

        return round(fitness, 6)
