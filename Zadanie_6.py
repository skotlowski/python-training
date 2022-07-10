import numpy as np
import math
import random as r
from datetime import datetime as time

array_range = r.randint(1, 1000000)

# numpy
numpy_array = np.array(range(array_range))


start = time.now()
avg = numpy_array.mean()
avg_geom = np.power(np.prod(numpy_array), 1/len(numpy_array))
avg_harm = len(numpy_array)/np.sum(1/numpy_array)
end = time.now()

print(f"Avg: {avg}, avg_geom: {avg_geom}, avg_harm: {avg_harm}. Time taken: {end-start}.")

# python

python_array = list(numpy_array)

start = time.now()
avg_py = sum(python_array)/len(python_array)


avg_geom_py = math.pow(math.prod(python_array), 1/len(python_array))
inverse_sum = 0

for i in range(len(python_array)):
    inverse_sum += 1/python_array[i]

avg_harm_py = len(python_array)/inverse_sum

end = time.now()

print(f"Avg: {avg_py}, avg_geom: {avg_geom_py}, avg_harm: {avg_harm_py}. Time taken: {end-start}.")


