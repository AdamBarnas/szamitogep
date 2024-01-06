import matplotlib.pyplot as plt
import struktury_danych as sd
import os
#print(a[4]['best_ant_dest_fun']

max_iter = 101
options = ["\method_1", "\method_1_best", "\method_1_f_density", "\method_2", "\method_2_best", "\method_2_f_density", "\method_3", "\method_3_best", "\method_3_f_density", "\method_4", "\method_4_best", "\method_4_f_density"]
instances = ["test" + str(i) + ".txt" for i in range(10)]

iteration = [[[0 for _ in range(max_iter)] for _ in instances] for _ in options]
best_ant_dest_fun = [[[0 for _ in range(max_iter)] for _ in instances] for _ in options]
best_ant_in_iter_dest_fun = [[[0 for _ in range(max_iter)] for _ in instances] for _ in options]

avg_iteration = [[0 for _ in range(max_iter)] for _ in options]
avg_best_ant_dest_fun = [[0 for _ in range(max_iter)] for _ in options]
avg_best_ant_in_iter_dest_fun = [[0 for _ in range(max_iter)] for _ in options]

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

# for option in options:
#     plt.plot(avg_best_ant_dest_fun[options.index(option)])
# plt.show()

# for option in options:
#     plt.plot(avg_best_ant_in_iter_dest_fun[options.index(option)])
# plt.show()

for i in range(10):
    plt.plot(best_ant_dest_fun[0][i])
plt.show()

for i in range(10):
    plt.plot(best_ant_in_iter_dest_fun[0][i])
plt.show()



