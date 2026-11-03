
import streamlit as st
import random
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Evolution Engine | Genetic Algorithm",
    page_icon="🧬",
    layout="wide"
)


# =====================================================
# CUSTOM CSS DESIGN - VISIBILITY FIX
# =====================================================

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #F4F5FA !important;
    color: #1F2937 !important;
}

/* Main content text */
.stApp p,
.stApp li,
.stApp label,
.stApp span,
.stApp strong {
    color: #1F2937;
}

/* All headings */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #252B45 !important;
}

/* Main layout */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #111827, #312E81);
    padding: 35px;
    border-radius: 18px;
    color: white !important;
    margin-bottom: 25px;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    color: #C7D2FE !important;
    font-size: 16px;
}

/* Information cards */
.section-card {
    background: #FFFFFF !important;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #E5E7EB;
    margin-bottom: 15px;
    color: #1F2937 !important;
}

.section-card p,
.section-card strong {
    color: #1F2937 !important;
}

/* Metric cards */
.metric-card {
    background: #FFFFFF !important;
    padding: 20px;
    border-radius: 14px;
    border-left: 5px solid #6366F1;
}

.metric-label {
    color: #6B7280 !important;
    font-size: 13px;
}

.metric-value {
    color: #312E81 !important;
    font-size: 29px;
    font-weight: 700;
}

/* Explanation boxes */
.explanation {
    background: #EEF2FF !important;
    padding: 17px;
    border-radius: 12px;
    border-left: 4px solid #6366F1;
    color: #312E81 !important;
    margin: 12px 0;
}

.explanation p,
.explanation strong {
    color: #312E81 !important;
}

/* Binary chromosome visualization */
.bit-one {
    display: inline-block;
    background: #6366F1;
    color: white !important;
    padding: 5px 7px;
    margin: 2px;
    border-radius: 5px;
    font-family: monospace;
}

.bit-zero {
    display: inline-block;
    background: #E5E7EB;
    color: #374151 !important;
    padding: 5px 7px;
    margin: 2px;
    border-radius: 5px;
    font-family: monospace;
}

/* Tables */
.stApp table,
.stApp th,
.stApp td {
    color: #1F2937 !important;
}

/* Mathematical formula */
.stApp [data-testid="stLatex"] {
    color: #312E81 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #252630 !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label {
    color: #FFFFFF !important;
}

/* Buttons */
.stButton > button {
    background: #4F46E5 !important;
    color: #FFFFFF !important;
    border-radius: 9px;
    border: none;
    padding: 10px 22px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #3730A3 !important;
    color: #FFFFFF !important;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB;
    border-radius: 10px;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p {
    color: #252B45 !important;
}

/* Dataframe and metric text */
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #252B45 !important;
}

/* Footer */
.footer {
    color: #6B7280 !important;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# GENETIC ALGORITHM PARAMETERS
# =====================================================

POPULATION_SIZE = 300
CHROMOSOME_LENGTH = 80
TARGET_ONES = 50
GENERATIONS = 50

CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.01


# =====================================================
# FITNESS FUNCTION
# =====================================================

def fitness_function(chromosome):

    ones = sum(chromosome)

    # Maximum fitness is 80 when ones = 50
    return 80 - abs(ones - TARGET_ONES)


# =====================================================
# INITIAL POPULATION
# =====================================================

def create_population():

    population = []

    for i in range(POPULATION_SIZE):

        chromosome = [
            random.randint(0, 1)
            for _ in range(CHROMOSOME_LENGTH)
        ]

        population.append(chromosome)

    return population


# =====================================================
# SELECTION
# ROULETTE WHEEL SELECTION
# =====================================================

def selection(population):

    fitness_values = [
        fitness_function(chromosome)
        for chromosome in population
    ]

    parents = random.choices(
        population,
        weights=fitness_values,
        k=2
    )

    return parents


# =====================================================
# CROSSOVER
# SINGLE POINT CROSSOVER
# =====================================================

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:

        point = random.randint(
            1, CHROMOSOME_LENGTH - 1
        )

        child1 = parent1[:point] + parent2[point:]

        child2 = parent2[:point] + parent1[point:]

    else:

        child1 = parent1[:]
        child2 = parent2[:]

    return child1, child2


# =====================================================
# MUTATION
# =====================================================

def mutation(chromosome):

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < MUTATION_RATE:

            chromosome[i] = 1 - chromosome[i]

    return chromosome


# =====================================================
# MAIN GENETIC ALGORITHM
# =====================================================

def genetic_algorithm():

    population = create_population()

    best_history = []
    average_history = []

    best_chromosome = None
    best_fitness = -1

    for generation in range(GENERATIONS):

        # Calculate fitness
        fitness_values = [
            fitness_function(chromosome)
            for chromosome in population
        ]

        # Find best individual
        best_index = fitness_values.index(
            max(fitness_values)
        )

        current_best = population[best_index]
        current_fitness = fitness_values[best_index]

        # Update global best
        if current_fitness > best_fitness:

            best_fitness = current_fitness
            best_chromosome = current_best[:]

        best_history.append(best_fitness)

        average_history.append(
            sum(fitness_values) / POPULATION_SIZE
        )

        # Elitism
        new_population = [
            best_chromosome[:]
        ]

        # Generate next population
        while len(new_population) < POPULATION_SIZE:

            parent1, parent2 = selection(population)

            child1, child2 = crossover(
                parent1, parent2
            )

            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    # Evaluate final population
    final_best = max(
        population,
        key=fitness_function
    )

    if fitness_function(final_best) > best_fitness:

        best_chromosome = final_best[:]
        best_fitness = fitness_function(final_best)

    return (
        best_chromosome,
        best_fitness,
        best_history,
        average_history
    )


# =====================================================
# APPLICATION HEADER
# =====================================================

st.markdown("""
<div class="hero">

<p>COMPUTATIONAL INTELLIGENCE / SEARCH ALGORITHMS</p>

<h1>🧬 EVOLUTION ENGINE</h1>

<p>
An interactive Genetic Algorithm system designed to
discover the optimal binary chromosome.
</p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🧬 GA Laboratory")

    st.caption("SYSTEM CONFIGURATION")

    st.markdown("---")

    st.write("**Population Size**")
    st.write("300 individuals")

    st.write("**Chromosome Length**")
    st.write("80 binary bits")

    st.write("**Target Ones**")
    st.write("50")

    st.write("**Generations**")
    st.write("50")

    st.markdown("---")

    st.write("**Genetic Operators**")

    st.write("🎯 Roulette Wheel Selection")
    st.write("✂️ Single-Point Crossover")
    st.write("🔄 Bit-Flip Mutation")
    st.write("⭐ Elitism")

    st.markdown("---")

    st.caption("GENETIC ALGORITHM | PYTHON PROJECT")


# =====================================================
# PROBLEM INTRODUCTION
# =====================================================

st.subheader("01 / Problem Overview")

st.markdown("""
<div class="section-card">

<strong>Objective</strong>

<p>
The objective is to generate an 80-bit binary chromosome
containing exactly 50 ones using a Genetic Algorithm.
</p>

<p>
The algorithm starts with 300 randomly generated individuals.
Through selection, crossover and mutation, the population
evolves over 50 generations to find the best solution.
</p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# PARAMETER DISPLAY
# =====================================================

st.subheader("02 / System Parameters")

c1, c2, c3, c4 = st.columns(4)

parameters = [
    (c1, "Population", "300"),
    (c2, "Bit Length", "80"),
    (c3, "Target Ones", "50"),
    (c4, "Generations", "50")
]

for col, label, value in parameters:

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <div class="metric-label">{label}</div>

        <div class="metric-value">{value}</div>

        </div>
        """, unsafe_allow_html=True)


st.write("")


# =====================================================
# FITNESS FUNCTION EXPLANATION
# =====================================================

st.subheader("03 / Fitness Function")

st.latex(
    r"Fitness(x)=80-|Number\ of\ Ones-50|"
)

st.markdown("""
<div class="explanation">

<strong>How does the fitness function work?</strong>

<p>
The fitness function measures how close each chromosome
is to the target of 50 ones.
</p>

<p>
A chromosome with exactly 50 ones receives a fitness
score of 80, which is the maximum value.
A larger difference from 50 produces a lower fitness score.
</p>

</div>
""", unsafe_allow_html=True)

with st.expander("View fitness calculation examples"):

    st.table({
        "Number of Ones": [30, 40, 45, 50, 55, 60, 70],
        "Fitness Value": [60, 70, 75, 80, 75, 70, 60]
    })


# =====================================================
# ALGORITHM EXECUTION
# =====================================================

st.markdown("---")

st.subheader("04 / Run Evolution Process")

st.write(
    "Click the button below to start the Genetic Algorithm."
)

if st.button("▶ START EVOLUTION", use_container_width=True):

    with st.spinner("Evolving the population..."):

        (
            best_chromosome,
            best_fitness,
            best_history,
            average_history
        ) = genetic_algorithm()

    st.session_state["best_chromosome"] = best_chromosome
    st.session_state["best_fitness"] = best_fitness
    st.session_state["best_history"] = best_history
    st.session_state["average_history"] = average_history

    st.success("Evolution process completed successfully!")


# =====================================================
# DISPLAY RESULTS
# =====================================================

if "best_chromosome" in st.session_state:

    chromosome = st.session_state["best_chromosome"]

    fitness = st.session_state["best_fitness"]

    best_history = st.session_state["best_history"]

    average_history = st.session_state["average_history"]

    ones = sum(chromosome)

    zeros = CHROMOSOME_LENGTH - ones

    st.markdown("---")

    st.subheader("05 / Evolution Results")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Best Fitness", f"{fitness} / 80")

    with r2:
        st.metric("Number of Ones", ones)

    with r3:
        st.metric("Number of Zeros", zeros)

    if ones == TARGET_ONES:

        st.success(
            "OPTIMAL SOLUTION FOUND! "
            "The chromosome contains exactly 50 ones."
        )

    else:

        st.warning(
            "The best solution did not reach the target."
            " Run the algorithm again to explore another population."
        )

    # ---------------------------------------------
    # CHROMOSOME VISUALIZATION
    # ---------------------------------------------

    st.subheader("Best Binary Chromosome")

    st.write(
        "Each square represents one gene in the chromosome. "
        "Purple represents 1, while grey represents 0."
    )

    bit_html = ""

    for bit in chromosome:

        if bit == 1:

            bit_html += (
                '<span class="bit-one">1</span>'
            )

        else:

            bit_html += (
                '<span class="bit-zero">0</span>'
            )

    st.markdown(
        f'<div style="line-height:2.7">{bit_html}</div>',
        unsafe_allow_html=True
    )

    with st.expander("View complete binary sequence"):

        st.code(
            "".join(map(str, chromosome)),
            language=None
        )

    # ---------------------------------------------
    # FITNESS PROGRESS GRAPH
    # ---------------------------------------------

    st.subheader("Fitness Evolution")

    fig, ax = plt.subplots(figsize=(10, 4))

    generations = range(1, GENERATIONS + 1)

    ax.plot(
        generations,
        best_history,
        label="Best Fitness",
        linewidth=2.5,
        marker="o",
        markersize=3
    )

    ax.plot(
        generations,
        average_history,
        label="Average Fitness",
        linewidth=2,
        linestyle="--"
    )

    ax.axhline(
        y=80,
        linestyle=":",
        label="Maximum Fitness (80)"
    )

    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness Score")

    ax.set_title("Population Fitness Progress")

    ax.set_xlim(1, GENERATIONS)
    ax.set_ylim(0, 85)

    ax.grid(alpha=0.2)
    ax.legend()

    st.pyplot(fig)

    st.markdown("""
    <div class="explanation">

    <strong>Graph Interpretation</strong>

    <p>
    The best fitness line shows the highest fitness value
    achieved up to each generation. The average fitness line
    represents the mean fitness of the population.
    </p>

    <p>
    As generations progress, selection and genetic operators
    help the population search for better chromosomes.
    The maximum possible fitness is 80.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =====================================================
# LEARNING SECTION
# =====================================================

st.markdown("---")

st.subheader("06 / Understanding Genetic Algorithm")

st.write(
    "The Genetic Algorithm uses four main operations "
    "to improve the quality of the population."
)

with st.expander("1. Initialization - Creating the population"):

    st.write("""
    The algorithm randomly generates 300 individuals.

    Each individual contains 80 binary genes, where each
    gene can have a value of either 0 or 1.

    Example:
    101010101101001...

    This creates the initial population for the search process.
    """)

with st.expander("2. Selection - Choosing parents"):

    st.write("""
    Roulette Wheel Selection is used to choose two parents.

    Individuals with higher fitness values have a higher
    probability of being selected.

    This gives better chromosomes more opportunities
    to contribute their genes to the next generation.
    """)

with st.expander("3. Crossover - Producing offspring"):

    st.write("""
    Single-Point Crossover combines two selected parents.

    A random crossover point is selected between positions
    1 and 79.

    The genes after that point are exchanged between
    the two parents to produce two offspring.

    Crossover probability = 0.8 (80%).
    """)

with st.expander("4. Mutation - Changing genes"):

    st.write("""
    Mutation randomly changes a gene from 0 to 1
    or from 1 to 0.

    The mutation probability is 0.01 (1%) for each bit.

    Mutation helps maintain genetic diversity and
    allows the algorithm to explore new solutions.
    """)

with st.expander("5. Elitism - Preserving the best solution"):

    st.write("""
    The best chromosome from the current generation
    is copied directly into the next generation.

    This prevents the best solution from being lost
    during crossover or mutation.
    """)

with st.expander("6. Termination - Stopping the algorithm"):

    st.write("""
    The algorithm terminates after completing
    50 generations.

    The best chromosome obtained is then displayed
    together with its fitness score and binary pattern.
    """)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:15px; color:#6B7280;">

<strong>EVOLUTION ENGINE</strong>

<p>Genetic Algorithm | Python | Streamlit</p>

<p>Search • Evolve • Optimize</p>

</div>
""", unsafe_allow_html=True)
