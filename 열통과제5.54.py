import numpy as np
import matplotlib.pyplot as plt


def F(v):
    return -0.8 * np.log(3*v-1) - 9/(8*v)


n_steps = 10000
v = np.linspace(0, 100, n_steps+1)


fig, ax = plt.subplots()
plt.grid()

plt.xlim(0, 5)
plt.ylim(-3, 0)
plt.xlabel('v')
plt.ylabel('F/Nk$T_c$')
plt.title('12(2)_5.54_Lee YSH')

ax.plot(v, F(v))

# plt.savefig('12주차_목_문제')
plt.show()
