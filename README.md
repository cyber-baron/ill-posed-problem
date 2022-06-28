# Некорректная задача 
Исследование одного из методов решения.

## Инструменты
Для проведения исследвания был выбран язык Python. Проект выполнен с использованием [NumPy](https://numpy.org/doc/).

## Описание задачи
В данной работе рассматрена некоректная задача, на примере задачи, в которой параметров модели больше, чем значений. Исследуем квазирешение, то есть обобщенное решение некорректной задач. Такое решение при достаточно общих условиях, в отличие от истинного решения, удовлетворяет условиям корректности по Адамару.

Предполагаем, что имеется набор измерений, но для решения поставленной задачи его недостаточно. Недастающие значения берем случайным образом, но только из определенного диапозона. Диапозон определяется самым большим и самым маленьким значением в уже имеющимся наборе. Можно считать, что задача при дополнительных условиях стала корректной, но только с оговоркой, что количество строк со случайными значениями не превосходит количество строк с фактическим набором измерений.

Данные, кеоторые используются в задаче, подобраны случайным образом. Данный подход дает возможность провести анализ разных выборок данных, не углубляясь в тонкости каждого случая.

## Решение задачи
Изначально задется диапозон варьирования "истиных" значений коэффициентов модели, далее задается число параметров факторов 𝑛 и число наблюдений для "истинной" модели 𝑛 + 1. Заранее обозначаем количиство "вычеркнутых" наблюдений, важно чтобы их количство строго не привышало 𝑛/2. 

Проще всего, для организации данных этой задачи, использовать матрицы. Таким образом, записываем коэффициенты "истинной" модели в матрице 1×𝑛 и факторы для "истинной" модели в матрице 𝑛 × 𝑛. На данный момент задача является корректной, поэтому с легкостью можно найти ее "истинные" результаты наблюдений. Для точных измерений, найдем ошибки результатов "истинных" наблюдений и будем считать верными результаты "истинных" наблюдений с учетом ошибок. 

Теперь для демонстрации квазирешения удалим значения факторов в "истиных" наблюдениях. Дополним получившуюся модель случайными строчками, теперь будем считать эти измерения фактическими. Для использования добавленных элементов, необходимо понизить из приоритет, поэтому зададим веса всем наблюдениям, при этом для рандомно добавленных, вес будет значительно меньше. Далее создаем дополненую матрицу значений факторов. После определения приоритета значений, можем вычислить фактические значния модели.

Имея на руках значения "истинной" модели и фактической модели, определить работоспособность метода можно с помощью анализа разницы конечных результатов. Для простоты понимания, сравнение визуализированно и отображено на графиках. Рассмотрим первый график модели, на нем зелеными точками отображено отношение значений "истинной" модели к результатам оценки выходного параметра по модели на основе дополненных данных, красными точками отборажено отношение значений "истинной" модели и результаты расчета выходной величины параметра по "фактической" модели, линейным графиком является отношение значений "истинной" модели к этим же значениям.

<p align="center">
  <img src="https://github.com/cyber-baron/ill-posed-problem/blob/main/graphics/example%201.1.png" alt="example 1.1"/>
</p>

<p align="center">
  <img src="https://github.com/cyber-baron/ill-posed-problem/blob/main/graphics/example%201.2.png" alt="example 1.2"/>
</p>
  
На втором графике, для сравнения, отображены те же отношеия, за исключением отношений значений "истинной" модели к результатам оценки выходного параметра по модели на основе дополненных данных. При сравнении двух графиков видно, что данные полученные случайным образом достаточно близки к значениям "истинной" модели.

Чтобы сравнить значения, полученные предложенным способом, можно также воспользоваться элементарной разностью. В случае с представленными выборками, значение разности отношения значений "истинной" модели и результаты расчета выходной величины параметра по "фактической" модели близко к нулевым значениям, следовательно значения близки к корректным(подходящим). Таким образом, логично будет предположить, что данное квазирешение может быть использованно для решения подобного рода некорректных задач.

## Выводы о проделанной работе
По результатам иследоваия делаем вывод, что предложенный метод является рабочим. Более того, данное иследование имеет вполне конкретную перспективу − генерация и иследование различных распределений, а также анализ истинных и нестабильных даных различных моделей.
