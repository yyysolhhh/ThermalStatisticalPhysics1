import numpy as np
import matplotlib.pyplot as plt

# T0 =
A = 1
K = 1

t = [1, 2, 3, 4, 5]
#t = 1


def T(x, t):
    return A / np.sqrt(t) * np.exp(-x * x/(4*K*t))


n_steps = 100
x = np.linspace(-10, 10, n_steps+1)

'''fnT = []
for i in t:
    fnT.append(A / np.sqrt(t) * np.exp(-x * x/(4*K*t)))
'''
# print(t)

fig, ax = plt.subplots()
plt.grid()
ax.spines['left'].set_position('center')
plt.xlim(-10, 10)
plt.ylim(0, 1.3)
plt.xlabel('x')
plt.ylabel('T-T0')
plt.title('Lee YSH')

for i in t:
    ax.plot(x, T(x, i), label=i)

ax.legend(title='t=')
# plt.savefig('2주차_목_문제')
plt.show()
