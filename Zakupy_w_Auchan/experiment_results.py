import matplotlib.pyplot as plt
import struktury_danych as sd
import numpy as np
import os
#print(a[4]['best_ant_dest_fun']

max_iter = 101
options = ["\method_1", "\method_1_best", "\method_1_f_density", "\method_2", "\method_2_best", "\method_2_f_density", "\method_3", "\method_3_best", "\method_3_f_density", "\method_4", "\method_4_best", "\method_4_f_density"]
instances = ["test" + str(i) + ".txt" for i in range(10)]

iteration = [[[0.0 for _ in range(max_iter)] for _ in instances] for _ in options]
best_ant_dest_fun = [[[0.0 for _ in range(max_iter)] for _ in instances] for _ in options]
best_ant_in_iter_dest_fun = [[[0.0 for _ in range(max_iter)] for _ in instances] for _ in options]
iteration = np.array(iteration)
best_ant_dest_fun = np.array(best_ant_dest_fun)
best_ant_in_iter_dest_fun = np.array(best_ant_in_iter_dest_fun)

avg_iteration = [[0.0 for _ in range(max_iter)] for _ in options]
avg_best_ant_dest_fun = [[0.0 for _ in range(max_iter)] for _ in options]
avg_best_ant_in_iter_dest_fun = [[0.0 for _ in range(max_iter)] for _ in options]
avg_iteration = np.array(avg_iteration)
avg_best_ant_dest_fun = np.array(avg_best_ant_dest_fun)
avg_best_ant_in_iter_dest_fun = np.array(avg_best_ant_in_iter_dest_fun)

std_iteration = [[0.0 for _ in range(max_iter)] for _ in options]
std_best_ant_dest_fun = [[0.0 for _ in range(max_iter)] for _ in options]
std_best_ant_in_iter_dest_fun = [[0.0 for _ in range(max_iter)] for _ in options]
std_iteration = np.array(std_iteration)
std_best_ant_dest_fun = np.array(std_best_ant_dest_fun)
std_best_ant_in_iter_dest_fun = np.array(std_best_ant_in_iter_dest_fun)

for option in options:
    for instance in instances:
        base_path = os.path.abspath(os.path.dirname(__file__))
        filename_parse = os.path.join(base_path, 'experiments' + option, instance)
        a = sd.parse(filename_parse)
        for it in a:
            iteration[options.index(option)][instances.index(instance)][it["Iteration"]] = it['Iteration']
            best_ant_dest_fun[options.index(option)][instances.index(instance)][it["Iteration"]] = it['best_ant_dest_fun']
            best_ant_in_iter_dest_fun[options.index(option)][instances.index(instance)][it["Iteration"]] = it['best_ant_in_iter_dest_fun']

for option in options:
    for it in range(max_iter):
        sum_b = 0
        sum_i = 0
        for i in range(10):
            sum_b += best_ant_dest_fun[options.index(option)][i][it]
            sum_i += best_ant_in_iter_dest_fun[options.index(option)][i][it]
        avg_best_ant_dest_fun[options.index(option)][it] = sum_b/10
        avg_best_ant_in_iter_dest_fun[options.index(option)][it] = sum_i/10

for option in options:
    for it in range(max_iter):
        sum_b = 0
        sum_i = 0
        for i in range(10):
            val_b = best_ant_dest_fun[options.index(option)][i][it] - avg_best_ant_dest_fun[options.index(option)][it]
            sum_b += val_b*val_b
            val_i = best_ant_in_iter_dest_fun[options.index(option)][i][it] - avg_best_ant_in_iter_dest_fun[options.index(option)][it]
            sum_i += val_i*val_i
        std_best_ant_dest_fun[options.index(option)][it] = np.sqrt(sum_b/10)
        std_best_ant_in_iter_dest_fun[options.index(option)][it] = np.sqrt(sum_i/10)


# każdy sposób średnia +/- odchylenie
for option in options:
    plt.plot(avg_best_ant_dest_fun[options.index(option)])
    plt.plot(avg_best_ant_dest_fun[options.index(option)] + std_best_ant_dest_fun[options.index(option)])
    plt.plot(avg_best_ant_dest_fun[options.index(option)] - std_best_ant_dest_fun[options.index(option)])
    plt.legend(["average", "+ standard deviation", "- standard deviation"])
    plt.title(option[1:])
    plt.show()

# każda metoda z różnicami w feromonach
n = 0
for option in options:
    n += 1
    plt.plot(avg_best_ant_dest_fun[options.index(option)])
    if n == 1:
        plt.title(option[1:])
    if n == 3:
        plt.legend(["default", "best_ants_feromones", "density_feromones"])
        plt.show()
        n = 0
    
# każde feromony z różnymi metodami    
n = 0
feromone_types = ["default", "best", "density_feromones"]
for i in range(3):
    for j in range(4):
        plt.plot(avg_best_ant_dest_fun[i + 3*j])
    plt.title(feromone_types[n])
    plt.legend(["method_1", "method_2", "method_3", "method_4"])
    plt.show()
    n += 1