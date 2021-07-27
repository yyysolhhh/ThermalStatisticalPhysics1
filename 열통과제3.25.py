import numpy as np
import matplotlib.pyplot as plt


def C(T):
    return np.exp(1/T) / (T**2 * (np.exp(1/T)-1) ** 2)


n_steps = 10000
T = np.linspace(0, 100, n_steps+1)


fig, ax = plt.subplots()
plt.grid()

plt.xlim(0, 2)
plt.ylim(0, 1)
plt.xlabel('kT/$\epsilon$')
plt.ylabel('Cv/Nk')
plt.title('6(1)_3.25_Lee YSH')

ax.plot(T, C(T))

# plt.savefig('6주차_화_문제')
plt.show()
