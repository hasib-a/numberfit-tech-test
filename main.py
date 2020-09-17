import sys
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

objects = {'Walk', 'Cycle', 'Car'}
y_pos = np.arange(len(objects))
x_args = [sys.argv[1], sys.argv[2], sys.argv[3]]
x_args = [int(x) for x in x_args]
plt.bar(y_pos, sorted(x_args), align='center',
        color=['blue', 'yellow', 'red'])
plt.xticks(y_pos, objects)
plt.title('How many children walk')

print('your values are walk: ' +
      str(x_args[0]) + ', cycle: ' + str(x_args[1]) + ', car: ' + str(x_args[2]))
plt.savefig('maths_equation.png')
plt.show()
