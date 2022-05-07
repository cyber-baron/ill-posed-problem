import random
import sympy as sp
import numpy as np
from sympy.abc import z
import functions as mpf

# диапозон варьирования "истиных" значений коэффициентов модели 
num = 5.0
model_range = random.uniform(-num,num)

# число параметров факторов
parametrs_num = 6 # n

# число наблюдений для "истинной" модели
observations_num = 7 # N

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

# "истинные" результаты надюдений (идиальная сходимость)
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

print(transpose_ERR)

# результаты "истинных" наблюдений с учетом ошибок
matrix_Y = transpose_Y0 + transpose_ERR

print(matrix_Y)

# значения факторов в "фактических" наблюдениях (после исключения строк)
new_matrix_X = np.empty([observations_num - 2, parametrs_num + 1])

for i in range(observations_num - 2):
    for j in range(parametrs_num):
        new_matrix_X[i][j] = matrix_X[i][j]

print(new_matrix_X)

# коэффициенты модели по "факическим" результатам наблюдений
new_matrix_Y = np.empty([observations_num - 2, 1])

for i in range(observations_num - 2):
    for j in range(1):
        new_matrix_Y[i][j] = matrix_Y[i][j]

print(new_matrix_Y)
