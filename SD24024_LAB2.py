
import random
import numpy as np
import pandas as pd
import streamlit as st

# ==========================================
# 1. PROBLEM PARAMETERS
# ==========================================

POPULATION_SIZE = 300
CHROMOSOME_LENGTH = 80
TARGET_ONES = 50
MAX_FITNESS = 80
GENERATIONS = 50

CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.01
TOURNAMENT_SIZE = 3
ELITISM = 2


# ==========================================
# 2. FITNESS FUNCTION
# ==========================================

def fitness_function(chromosome):

    number_of_ones = int(np.sum(chromosome))

    fitness = MAX_FITNESS - abs(number_of_ones - TARGET_ONES)

    return fitness


# ==========================================
# 3. INITIALIZE POPULATION
# ==========================================

def initialize_population():

    population = []

    for i in range(POPULATION_SIZE):

        chromosome = np.random.randint(
            0, 2, CHROMOSOME_LENGTH
        )

        population.append(chromosome)

    return np.array(population)


# ==========================================
# 4. TOURNAMENT SELECTION
# ==========================================

def tournament_selection(population, fitness):

    selected = random.sample(
        range(len(population)),
        TOURNAMENT_SIZE
    )

    best = max(selected, key=lambda i: fitness[i])

    return population[best].copy()


# ==========================================
# 5. ONE-POINT CROSSOVER
# ==========================================

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:

        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = np.concatenate([
            parent1[:point],
            parent2[point:]
        ])

        child2 = np.concatenate([
            parent2[:point],
            parent1[point:]
        ])

    else:

        child1 = parent1.copy()
        child2 = parent2.copy()

    return child1, child2


# ==========================================
# 6. BIT MUTATION
# ==========================================

def mutation(chromosome):

    child = chromosome.copy()

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < MUTATION_RATE:

            child[i] = 1 - child[i]

    return child


# ==========================================
# 7. EVALUATE POPULATION
# ==========================================

def evaluate_population(population):

    return np.array([
        fitness_function(individual)
        for individual in population
    ])


# ==========================================
# 8. RUN GENETIC ALGORITHM
# ==========================================

def run_genetic_algorithm():

    # Initialize population
    population = initialize_population()

    history_best = []
    history_average = []
    history_worst = []

    for generation in range(GENERATIONS):

        # Calculate fitness
        fitness = evaluate_population(population)

        # Record fitness values
        best_fitness = np.max(fitness)
        average_fitness = np.mean(fitness)
        worst_fitness = np.min(fitness)

        history_best.append(best_fitness)
        history_average.append(average_fitness)
        history_worst.append(worst_fitness)

        # Elitism: preserve the best individuals
        elite_indices = np.argsort(fitness)[-ELITISM:]

        elites = population[elite_indices].copy()

        # Create next generation
        next_population = []

        while len(next_population) < POPULATION_SIZE - ELITISM:

            # Select parents
            parent1 = tournament_selection(
                population, fitness
            )

            parent2 = tournament_selection(
                population, fitness
            )

            # Crossover
            child1, child2 = crossover(
                parent1, parent2
            )

            # Mutation
            child1 = mutation(child1)
            child2 = mutation(child2)

            next_population.append(child1)

            if len(next_population) < POPULATION_SIZE - ELITISM:
                next_population.append(child2)

        # Add elite individuals
        population = np.vstack([
            np.array(next_population),
            elites
        ])

    # Evaluate final population
    final_fitness = evaluate_population(population)

    best_index = np.argmax(final_fitness)

    best_solution = population[best_index]

    best_fitness = final_fitness[best_index]

    history = pd.DataFrame({
        "Best Fitness": history_best,
        "Average Fitness": history_average,
        "Worst Fitness": history_worst
    })

    return {
        "best_solution": best_solution,
        "best_fitness": best_fitness,
        "final_population": population,
        "final_fitness": final_fitness,
        "history": history
    }


# ==========================================
# 9. STREAMLIT USER INTERFACE
# ==========================================

st.set_page_config(
    page_title="Genetic Algorithm - Bit Pattern",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Genetic Algorithm - Bit Pattern Generation")

st.write(
    "This application uses a Genetic Algorithm "
    "to generate an 80-bit chromosome containing "
    "exactly 50 ones."
)

# Display predefined parameters
st.subheader("Genetic Algorithm Parameters")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Population Size", POPULATION_SIZE)
col2.metric("Chromosome Length", CHROMOSOME_LENGTH)
col3.metric("Target Ones", TARGET_ONES)
col4.metric("Maximum Fitness", MAX_FITNESS)
col5.metric("Generations", GENERATIONS)

st.divider()

# Run button
if st.button("Run Genetic Algorithm", type="primary"):

    with st.spinner("Running Genetic Algorithm..."):

        result = run_genetic_algorithm()

        st.session_state["ga_result"] = result


# ==========================================
# 10. DISPLAY RESULTS
# ==========================================

if "ga_result" in st.session_state:

    result = st.session_state["ga_result"]

    best_solution = result["best_solution"]

    best_fitness = result["best_fitness"]

    number_of_ones = int(np.sum(best_solution))

    st.subheader("Genetic Algorithm Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Best Fitness",
        f"{best_fitness:.0f} / 80"
    )

    col2.metric(
        "Number of Ones",
        f"{number_of_ones} / 80"
    )

    col3.metric(
        "Number of Zeros",
        f"{CHROMOSOME_LENGTH - number_of_ones} / 80"
    )

    # Display best bit pattern
    st.subheader("Best Bit Pattern")

    bitstring = ''.join(
        map(str, best_solution.astype(int))
    )

    st.code(bitstring, language="text")

    # Display whether target was achieved
    if number_of_ones == TARGET_ONES:

        st.success(
            "Target achieved! The chromosome contains "
            "exactly 50 ones and has a fitness value of 80."
        )

    else:

        st.warning(
            f"Target not fully achieved. The chromosome "
            f"contains {number_of_ones} ones."
        )

    # Fitness chart
    st.subheader("Fitness Over 50 Generations")

    st.line_chart(result["history"])

    # Final population
    st.subheader("Final Population")

    population_df = pd.DataFrame(
        result["final_population"],
        columns=[
            f"Bit_{i+1}"
            for i in range(CHROMOSOME_LENGTH)
        ]
    )

    population_df["Number of Ones"] = np.sum(
        result["final_population"],
        axis=1
    )

    population_df["Fitness"] = result["final_fitness"]

    st.dataframe(
        population_df,
        use_container_width=True
    )

    # Download results
    csv = population_df.to_csv(index=False)

    st.download_button(
        label="Download Final Population (CSV)",
        data=csv,
        file_name="genetic_algorithm_results.csv",
        mime="text/csv"
    )

else:

    st.info(
        "Click 'Run Genetic Algorithm' to generate "
        "the bit pattern and view the results."
    )
