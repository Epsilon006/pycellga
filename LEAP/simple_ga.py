from leap_ec.algorithm import generational_ea
from leap_ec import ops, decoder, representation
from leap_ec.binary_rep import initializers
from leap_ec.binary_rep import problems
from leap_ec.binary_rep.ops import mutate_bitflip

pop_size = 5
ea = generational_ea(
    max_generations=10,
    pop_size=pop_size,
    # Solve a MaxOnes Boolean optimization problem
    problem=problems.MaxOnes(),
    representation=representation.Representation(
        # Genotype and phenotype are the same for this task
        decoder=decoder.IdentityDecoder(),
        # Initial genomes are random binary sequences
        initialize=initializers.create_binary_sequence(length=10),
    ),
    # The operator pipeline
    pipeline=[  # Select parents via tournament_selection
        ops.tournament_selection,
        ops.clone,  # Copy them (just to be safe)
        # Basic mutation with a 1/L mutation rate
        mutate_bitflip(expected_num_mutations=1),
        # Crossover with a 40% chance of swapping each gene
        ops.uniform_crossover(p_swap=0.4),
        ops.evaluate,  # Evaluate fitness
        # Collect offspring into a new population
        ops.pool(size=pop_size),
    ],
)

print("Generation, Best_Individual")
for i, best in ea:
    print(f"{i}, {best}")
