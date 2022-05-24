import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib import style

# диапозон варьирования "истиных" значений коэффициентов модели 
num = 5.0
model_range = random.uniform(-num,num)

# число параметров факторов
parametrs_num = 6 

# число наблюдений для "истинной" модели
observations_num = 7 

# число "вычеркнутых" наблюдений
deleted_observations_num = 2

# коэффициенты "истинной" модели
model_coefficient = np.empty([1, parametrs_num])
for i in range(1):
    for j in range(parametrs_num):
        model_coefficient[i][j] = random.uniform(-num,num)     

print(model_coefficient)

# факторы для "истинной" модели
xx = float(10.0)

matrix_X = np.empty([observations_num, parametrs_num + 1])

for i in range(parametrs_num + 1):
        matrix_X[i][0] = 1          

for i in range(observations_num):
    for j in range(parametrs_num):
        matrix_X[i][j + 1] = random.uniform(-xx,xx)   

print(matrix_X)

# "истинные" результаты наблюдений (идеальная сходимость)
transpose_X = np.empty([parametrs_num + 1, observations_num])

for i in range(len(matrix_X)):
   for j in range(len(matrix_X[0])):
      transpose_X[j][i] = matrix_X[i][j]

matrix_Y0 = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*transpose_X)]
                                for A_row in model_coefficient]   

transpose_Y0 = np.empty([parametrs_num + 1, 1])

for i in range(len(matrix_Y0)):
   for j in range(len(matrix_Y0[0])):
      transpose_Y0[j][i] = matrix_Y0[i][j]

print(transpose_Y0)

# ошибки результатов "истинных" наблюдений
error_coefficient = 0.3
error_range = random.uniform(-error_coefficient,error_coefficient)

marix_ERR = np.empty([1, observations_num])
for i in range(1):
    for j in range(observations_num):
        marix_ERR[i][j] = matrix_Y0[i][j] * random.uniform(-error_coefficient,error_coefficient)     

transpose_ERR = np.empty([observations_num, 1])

for i in range(len(marix_ERR)):
   for j in range(len(marix_ERR[0])):
      transpose_ERR[j][i] = marix_ERR[i][j]

# результаты "истинных" наблюдений с учетом ошибок
matrix_Y = transpose_Y0 + transpose_ERR

# значения факторов в "фактических" наблюдениях (после исключения строк)
new_matrix_X = np.empty([observations_num - 2, parametrs_num + 1])

for i in range(observations_num - 2):
    for j in range(parametrs_num):
        new_matrix_X[i][j] = matrix_X[i][j]

# коэффициенты модели по "фактическим" результатам наблюдений
new_matrix_Y = np.empty([observations_num - 2, 1])

for i in range(observations_num - 2):
    for j in range(1):
        new_matrix_Y[i][j] = matrix_Y[i][j]

# коэффициенты модели по "фактическим" результатам наблюдений
transpose_new_matrix_X = np.empty([parametrs_num + 1, observations_num - 2])

for i in range(len(new_matrix_X)):
   for j in range(len(new_matrix_X[0])):
      transpose_new_matrix_X[j][i] = new_matrix_X[i][j]

new_model_coefficient_first = [[sum(a * b for a, b in zip(A_row, B_col))
                                            for B_col in zip(*new_matrix_X)]
                                              for A_row in transpose_new_matrix_X]  

inverse_new_model_coefficient_first = np.linalg.inv(new_model_coefficient_first)

new_model_coefficient_second = [[sum(a * b for a, b in zip(A_row, B_col))
                                            for B_col in zip(*new_matrix_X)]
                                              for A_row in inverse_new_model_coefficient_first] 

new_model_coefficient_third = [[sum(a * b for a, b in zip(A_row, B_col))
                                            for B_col in zip(*new_matrix_Y)]
                                              for A_row in new_model_coefficient_second]                                             

# результаты расчета выходной величины парметра по "фактической" модели
transpose_new_model_coefficient_third = np.empty([1, parametrs_num + 1])

for i in range(len(new_model_coefficient_third)):
   for j in range(len(new_model_coefficient_third[0])):
      transpose_new_model_coefficient_third[j][i] = new_model_coefficient_third[i][j]

new_matrix_Y0 = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*matrix_X)]
                              for A_row in transpose_new_model_coefficient_third]

transpose_new_matrix_Y0 = np.empty([parametrs_num + 1, 1])

for i in range(len(new_matrix_Y0)):
   for j in range(len(new_matrix_Y0[0])):
      transpose_new_matrix_Y0[j][i] = new_matrix_Y0[i][j]

# дополним "фактическую" модель случайными строчками
random_strings = np.empty([2, parametrs_num + 1])

for i in range(2):
        random_strings[i][0] = 1          

for i in range(2):
    for j in range(parametrs_num):
        random_strings[i][j + 1] = random.uniform(-xx,xx)   

coefficient_random = np.empty([2, 1])

for i in range(2):
    for j in range(1):
        coefficient_random[i][j] = random.uniform(-xx,xx)

# зададим веса всем наблюдениям, при этом для рандомно добавленных вес будет значительно меньше
weight = np.empty([1, parametrs_num + 1])

for i in range(1):
    for j in range(parametrs_num + 1):
        weight[i][j] = 1

for i in range(1):
    for j in range(parametrs_num - 4):
        weight[i][j + 5] = 0.0001                     

diagonal = np.diagflat(weight)

# дополненая матрица значений факторов
new_new_X = np.empty([observations_num, parametrs_num + 1])

for i in range(observations_num - 2):
    for j in range(parametrs_num + 1):
        new_new_X[i][j] = new_matrix_X[i][j]

for i in range(2):
    for j in range(parametrs_num + 1):
        new_new_X[i + 5][j] = random_strings[i][j] 

print(new_new_X)

# дополнительная матрица результатов наблюдений
new_new_Y = np.empty([parametrs_num + 1, 1])

for i in range(observations_num - 2):
    for j in range(1):
        new_new_Y[i][j] = new_matrix_Y[i][j]

for i in range(2):
    for j in range(1):
        new_new_Y[i + 5][j] = coefficient_random[i][j]

print(new_new_Y) 

# оценки коэффициентов модели по дополнительным данным
transpose_new_new_X = np.empty([parametrs_num + 1, observations_num])

for i in range(len(new_new_X)):
   for j in range(len(new_new_X[0])):
      transpose_new_new_X[j][i] = new_new_X[i][j]

double_diagonal = [[sum(a * b for a, b in zip(A_row, B_col))
                               for B_col in zip(*diagonal)]
                                for A_row in diagonal]      

pre_first_step = [[sum(a * b for a, b in zip(A_row, B_col))
                          for B_col in zip(*double_diagonal)]
                            for A_row in transpose_new_new_X]     

first_step = [[sum(a * b for a, b in zip(A_row, B_col))
                          for B_col in zip(*new_new_X)]
                            for A_row in pre_first_step]  

inverse_first_step = np.linalg.inv(first_step) 

second_step = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*transpose_new_new_X)]
                              for A_row in inverse_first_step]

third_step = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*double_diagonal)]
                              for A_row in second_step]   

fourth_step = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*new_new_Y)]
                              for A_row in third_step]  

# результаты оценки выходного параметра по модели на основе дополнительных данных
transpose_fourth_step = np.empty([1, parametrs_num + 1])

for i in range(len(fourth_step)):
   for j in range(len(fourth_step[0])):
      transpose_fourth_step[j][i] = fourth_step[i][j]

new_calc_Y = [[sum(a * b for a, b in zip(A_row, B_col))
                          for B_col in zip(*transpose_new_new_X)]
                            for A_row in transpose_fourth_step]     

print(new_calc_Y)

# сравнение 
transpose_new_calc_Y = np.empty([parametrs_num + 1, 1])

for i in range(len(new_calc_Y)):
   for j in range(len(new_calc_Y[0])):
      transpose_new_calc_Y[j][i] = new_calc_Y[i][j]

compare = matrix_Y - transpose_new_calc_Y

print(compare)

style.use('ggplot')  

plt.scatter(matrix_Y, new_calc_Y, color='r')
plt.plot(matrix_Y, matrix_Y, color='b') 
plt.scatter(matrix_Y, new_matrix_Y0, color='g')
plt.show()
