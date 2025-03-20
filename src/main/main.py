from protocol.protocol_manager import ProtocolManager
import os
import json
import matplotlib.pyplot as plt
import yaml

def load_results(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def plot_best_configuration(best_config):
    config_text = ""
    for module, params in best_config.items():
        config_text += f"{module.capitalize()}:\n"
        for i, p in enumerate(params, start=1):
            config_text += f"  Param {i}: {p:.4f}\n"
        config_text += "\n"
    plt.figure(figsize=(6, 4))
    plt.text(0.5, 0.5, config_text, fontsize=12, ha="center", va="center", wrap=True)
    plt.axis('off')
    plt.title("Best Evolved Configuration")
    plt.savefig("best_configuration.png")
    plt.show()

def plot_simulation_fitness(results_files):
    fitness_values = []
    runs = []
    for file in results_files:
        try:
            data = load_results(file)
            if "results" not in data or "final_fitness" not in data["results"]:
                print(f"Skipping {file} due to missing keys.")
                continue
            run_val = data.get("run")
            if run_val is None:
                run_val = os.path.splitext(os.path.basename(file))[0]
            runs.append(run_val)
            fitness_values.append(data["results"]["final_fitness"])
        except Exception as e:
            print(f"Error processing {file}: {e}")
    if not runs:
        print("No valid simulation results found.")
        return
    plt.figure(figsize=(8, 4))
    plt.plot(runs, fitness_values, marker="o")
    plt.title("Simulation Fitness Across Runs")
    plt.xlabel("Run")
    plt.ylabel("Final Fitness")
    plt.grid(True)
    plt.savefig("simulation_fitness.png")
    plt.show()

def plot_fitness_evolution(generation_fitness):
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, len(generation_fitness)+1), generation_fitness, marker="o", color="green")
    plt.title("Best Fitness Evolution Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)
    plt.savefig("fitness_evolution.png")
    plt.show()

def plot_parameter_distribution(best_config):
    modules = ["encryption", "routing", "deception"]
    averages = []
    for module in modules:
        averages.append(sum(best_config[module]) / len(best_config[module]))
    plt.figure(figsize=(8, 4))
    plt.bar(modules, averages, color=["blue", "orange", "green"])
    plt.title("Average Parameter Distribution")
    plt.xlabel("Module")
    plt.ylabel("Average Value")
    plt.ylim(0, 1)
    plt.savefig("parameter_distribution.png")
    plt.show()

def analyze_results():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiments", "simulation_results")
    if not os.path.exists(base_dir):
        print("No simulation results folder found at:", base_dir)
        return
    results_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                results_files.append(os.path.join(root, file))
    if results_files:
        plot_simulation_fitness(results_files)
    else:
        print("No JSON files found.")

def write_dynamic_config(best_config, final_fitness):
    dynamic_config = {
        "timestamp": __import__("datetime").datetime.now().isoformat(),
        "final_fitness": final_fitness,
        "protocol_parameters": best_config,
        "simulation_details": {
            "dummy_duration": 1000,
            "num_nodes": 50
        }
    }
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiments")
    config_path = os.path.join(base_dir, "config.yaml")
    with open(config_path, "w") as f:
        yaml.dump(dynamic_config, f)
    print("Dynamic config.yaml file created at:", config_path)

def main():
    pm = ProtocolManager()
    best_config = pm.run_evolution(generations=50)
    print("Best evolved protocol configuration:", best_config)
    final_fitness = pm.evaluate_fitness(pm.ga.population[0])
    write_dynamic_config(best_config, final_fitness)
    plot_best_configuration(best_config)
    analyze_results()
    if hasattr(pm.ga, "generation_fitness"):
        plot_fitness_evolution(pm.ga.generation_fitness)
    plot_parameter_distribution(best_config)

if __name__ == "__main__":
    main()
