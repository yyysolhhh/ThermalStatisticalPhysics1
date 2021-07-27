import numpy as np
import matplotlib.pyplot as plt


def C(T):
    return np.exp(-1/T) / (T*T)


n_steps = 10000
T = np.linspace(0, 100, n_steps+1)


fig, ax = plt.subplots()
plt.grid()

plt.xlim(0, 0.2)
plt.ylim(0, 0.15)
plt.xlabel('kT/$\epsilon$')
plt.ylabel('Cv/Nk')
plt.title('5(2)_3.8_Lee YSH')

ax.plot(T, C(T))

# plt.savefig('2주차_목_문제')
plt.show()
