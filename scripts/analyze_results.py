#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
import os
def load_results(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
def plot_results(results_files):
    fitness_values = []
    runs = []
    for file in results_files:
        data = load_results(file)
        runs.append(data["run"])
        fitness_values.append(data["results"]["final_fitness"])
    plt.figure(figsize=(8, 4))
    plt.plot(runs, fitness_values, marker="o")
    plt.title("Simulation Fitness Across Runs")
    plt.xlabel("Run ID")
    plt.ylabel("Final Fitness")
    plt.grid(True)
    plt.savefig("simulation_fitness.png")
    plt.show()
if __name__ == "__main__":
    results_dir = os.path.join("..", "experiments", "simulation_results")
    results_files = [os.path.join(results_dir, f) for f in os.listdir(results_dir) if f.endswith(".json")]
    plot_results(results_files)
