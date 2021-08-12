import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fa

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['t1']
    y2 = data['t2']
    
    plt.cla()
    
    plt.plot(x,y1,label='Apple')
    plt.plot(x,y2,label='Microsoft')
    plt.title('Live Stock Updates')
    plt.legend(loc='lower left')
    plt.tight_layout()

ani = fa(plt.gcf(),animate,interval=1)
plt.tight_layout()
plt.show()
