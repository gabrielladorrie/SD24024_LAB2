# SD24024_LAB2

# Evolution Engine: Genetic Algorithm for Binary Pattern Generation

## 1. Project Overview

This project implements a **Genetic Algorithm (GA)** using Python to generate an optimal binary pattern consisting of 80 bits, with exactly 50 ones.

A Genetic Algorithm is an optimisation technique inspired by the principles of natural selection and evolution. It works by generating a population of possible solutions and gradually improving them through selection, crossover, and mutation.

The application provides an interactive interface developed using Streamlit, allowing users to execute the algorithm and observe its performance through visualisations and fitness evaluations.

## 2. Problem Statement

The objective of this project is to generate a binary chromosome that contains exactly 50 ones within a chromosome length of 80 bits.

The Genetic Algorithm evaluates each individual using a fitness function. The individual with exactly 50 ones achieves the maximum fitness value of 80.

The algorithm operates with a predefined population size and number of generations to search for an optimal solution.

## 3. Genetic Algorithm Parameters

The following parameters are used in this implementation:

| Parameter | Value |
|---|---:|
| Population Size | 300 |
| Chromosome Length | 80 |
| Target Number of Ones | 50 |
| Maximum Fitness Value | 80 |
| Number of Generations | 50 |

## 4. Fitness Function

The fitness function measures how close an individual's number of ones is to the target value of 50.

The formula is:

**Fitness(x) = 80 - |N₁ - 50|**

Where:

- N₁ = Total number of ones in the chromosome.
- 50 = Target number of ones.
- 80 = Maximum fitness value.

### Examples of Fitness Calculation

| Number of Ones | Fitness Value |
|---:|---:|
| 30 | 60 |
| 40 | 70 |
| 45 | 75 |
| 50 | 80 |
| 55 | 75 |
| 60 | 70 |
| 70 | 60 |

The maximum fitness value of 80 is achieved when an individual contains exactly 50 ones.

## 5. Genetic Algorithm Process

The algorithm follows these main stages:

### 5.1 Population Initialization
An initial population of 300 individuals is randomly generated. Each individual is represented as a binary chromosome containing 80 bits.

### 5.2 Fitness Evaluation
Each chromosome is evaluated using the fitness function to determine how close its number of ones is to the target of 50.

### 5.3 Selection
The selection process chooses individuals based on their fitness values. Individuals with better fitness have a higher chance of contributing to the next generation.

### 5.4 Crossover
Crossover combines genetic information from selected parent chromosomes to produce new offspring. This introduces new combinations of binary patterns into the population.

### 5.5 Mutation
Mutation randomly changes selected bits in a chromosome. This maintains population diversity and helps the algorithm explore alternative solutions.

### 5.6 Generation Update
The new population is evaluated repeatedly across 50 generations. The algorithm tracks the fitness performance to observe improvements during the evolutionary process.

### 5.7 Optimal Solution
The objective is to identify a chromosome containing exactly 50 ones, achieving the maximum fitness value of 80.

## 6. Application Features

The Streamlit application provides an interactive platform for demonstrating the Genetic Algorithm.

Its main features include:

- **Interactive Interface:** Provides a user-friendly environment for running the Genetic Algorithm.
- **Parameter Display:** Shows the predefined GA parameters, including population size, chromosome length and number of generations.
- **Evolution Execution:** Allows users to execute the Genetic Algorithm through an interactive button.
- **Fitness Evaluation:** Displays the fitness performance of the generated individuals.
- **Binary Chromosome Visualisation:** Presents the resulting binary pattern for easier interpretation.
- **Fitness Evolution Graph:** Visualises the improvement of fitness throughout the evolutionary process.
- **Algorithm Explanation:** Provides explanations of the main Genetic Algorithm operations to help users understand how the solution is generated.

## 7. Technologies Used

The project is developed using the following technologies:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Development of the interactive web application |
| Pandas | Data handling |
| NetworkX | Graph and network-related functionality |
| Matplotlib | Data visualisation |

## 8. Project Structure

```text
SD24024_LAB2/
│
├── SD24024_LAB2.py
│   └── Main Genetic Algorithm application
│
├── requirements.txt
│   └── Required Python libraries
│
└── README.md
    └── Project documentation
```


## 9. Live Application

The application is deployed using Streamlit Community Cloud.

**Streamlit Application:**  
https://sd24024lab2-p2ucmmyeexfp2qz2jrppn2.streamlit.app/

**GitHub Repository:**  
https://github.com/gabrielladorrie/SD24024_LAB2

## 10. Conclusion

This project implements a Genetic Algorithm to solve a binary pattern optimisation problem.

Through population initialization, fitness evaluation, selection, crossover, and mutation, the algorithm searches for an individual with exactly 50 ones in an 80-bit chromosome.

The Streamlit application further provides an interactive way to understand the evolutionary process through fitness evaluation, chromosome visualisation and graphical representation.

Overall, this project illustrates how Genetic Algorithms can be applied to optimisation problems using artificial intelligence techniques and Python-based software development.
