import csv


##### STAŁE #####
file1 = 'Zakupy_w_Auchan/dane_do_eksp.csv'

##### FUNKJE #####
def form_csv_to_dict(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        dict_arr= []
        data = list(csv_reader)
        col_names = data[0]
        data = data[1:]
        for line in data:
            dict_tmp = dict(map(lambda i,j : (i,j), col_names, line))
            dict_arr.append(dict_tmp)
            print(f'Dict:\n {dict_tmp}')



form_csv_to_dict(file1)