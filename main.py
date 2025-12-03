import pandas as pd
import numpy as np
import sklearn as skit
import pygad as evo
import flask as fk
import subprocess as sp
dataset = pd.read_excel('league_data.xlsx')
dataset_filtered = dataset[['champion_name','win']]


#NO OP used to stop the plot from popping up in a window
import matplotlib.pyplot as pp
def nop():
    pass
pp.show = nop

#These allow for the average win rates to be got for each character in the game
dataset_filtered["loss"] = dataset_filtered["win"].map(lambda x: not x)
rates = dataset_filtered.groupby("champion_name").aggregate("sum")
rates["total"] = rates["win"] + rates["loss"]
rates["rate"] = rates["win"]/rates["total"]

#Fitness function, instead of averages it simply returns a sum of all the win rates and that is the fitness
def fitness_function(ga_instance, individual, individual_idx):
    return sum(rates["rate"].iloc[champion] for champion in individual)

#The main function handling all the parameters for my genetic algorithm
def gen_team():
    ga_inst = evo.GA(
        num_generations= 30,
        num_parents_mating = 2,
        fitness_func = fitness_function,
        sol_per_pop=10,
        num_genes=6,
        gene_type=int,
        init_range_low=0,
        init_range_high=rates.shape[0]-1,
        parent_selection_type="tournament",
        K_tournament=3,
        keep_parents=-1,
        keep_elitism=1,
        crossover_type="single_point",
        crossover_probability=None,
        mutation_type="random",
        mutation_probability=None,
        mutation_num_genes=1,
        mutation_percent_genes="default",
        mutation_by_replacement=True,
        random_mutation_min_val= 0,
        random_mutation_max_val= rates.shape[0]-1,
        allow_duplicate_genes=False,
        random_seed=None
    )
    ga_inst.run()
   #Saving the fitness plot
    ga_inst.plot_fitness(
        save_dir= "fitness.png"
    )
    #The command to open the plot
    sp.run(["cmd", "/c", "start fitness.png"])

    best_solution = ga_inst.best_solution()
    print(best_solution)
    winners = best_solution[0]
    winrate = best_solution[1]
    return list(rates.index[int(champion)] for champion in winners)



#front end flask implemntation 
app = fk.Flask(__name__)

@app.route("/")
def main():
    team = gen_team()
    
    return fk.render_template("app.html",team=team)
