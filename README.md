# Question 2: Search Algorithms (Genetic Algorithm)

## 1. Project Description

This project implements a Genetic Algorithm using Python to generate an 80-bit chromosome containing exactly 50 ones.

The objective is to find a bit pattern that achieves the maximum fitness value of 80, based on the predefined fitness function.

The algorithm is implemented using Python and Streamlit to provide an interactive interface for executing the algorithm and displaying the results.

## 2. Problem Requirements

The Genetic Algorithm is configured according to the following requirements:

| Parameter | Value |
|---|---:|
| Population Size | 300 |
| Chromosome Length | 80 |
| Target Number of Ones | 50 |
| Maximum Fitness | 80 |
| Number of Generations | 50 |

## 3. Fitness Function

The fitness function is defined as:

\[
f(x)=80-|n-50|
\]

Where:
- \(n\) is the number of ones in a chromosome.
- The chromosome consists of 80 binary bits.
- The maximum fitness value is 80, achieved when \(n=50\).

Therefore, the optimal chromosome contains exactly 50 ones and 30 zeros.

## 4. Genetic Algorithm Methodology

The following procedures are applied:

1. **Population Initialization:** Generate 300 random chromosomes, each with 80 bits.
2. **Fitness Evaluation:** Calculate the fitness of each chromosome.
3. **Selection:** Use tournament selection with a tournament size of 3.
4. **Crossover:** Apply one-point crossover with a crossover rate of 0.9.
5. **Mutation:** Apply bit mutation with a mutation rate of 0.01 per bit.
6. **Elitism:** Preserve the two best individuals in each generation.
7. **Termination:** Perform 50 generations of evolution.
8. **Final Evaluation:** Evaluate the final population and identify the best chromosome.

## 5. Technologies Used

- Python
- NumPy
- Pandas
- Streamlit

## 6. Installation and Execution

### Prerequisites

Ensure that Python and pip are installed.

### Step 1: Install Dependencies

```bash
pip install streamlit numpy pandas
```

### Step 2: Run the Application

If the Python file is named `app.py`, execute:

```bash
streamlit run app.py
```

### Step 3: Execute the Algorithm

1. Open the application in your browser.
2. Click **Run Genetic Algorithm**.
3. View the generated bit pattern and fitness results.
4. Review the fitness chart and final population.
5. Download the final population in CSV format if required.

## 7. Results

The expected optimal solution satisfies the following conditions:

- Chromosome length: 80 bits
- Number of ones: 50
- Number of zeros: 30
- Fitness value: 80

The application displays the best chromosome, its fitness value, the number of ones and zeros, fitness history, and the final population.

**Note:** The Genetic Algorithm is stochastic, so the results may vary between executions. The algorithm aims to find a chromosome that achieves the maximum fitness value.

## 8. Project Files

```text
├── SD24024_LAB2.py
├── README.md
└── requirements.txt
```

