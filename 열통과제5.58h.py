import numpy as np
import matplotlib.pyplot as plt


def T(x):
    return (2*x - 1) / (np.log(x) - np.log(1 - x))


n_steps = 10000
x = np.linspace(0, 100, n_steps+1)


fig, ax = plt.subplots()
plt.grid()

plt.xlim(0, 1)
plt.ylim(0, 0.7)
plt.xlabel('x')
plt.ylabel('kT/n(u$_A$$_B$ - u$_0$)')
plt.title('13(1)_5.58(h)_Lee YSH')

ax.plot(x, T(x))

# plt.savefig('13주차_화_문제')
plt.show()
