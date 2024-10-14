import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2/(math.sin(x)+4)


def tabulation(a, b, n):
    width = (b - a) / n
    tab = []

    for i in range(n):
        tab.append([a + i * width, f(a + i * width)])

    return tab

tab = tabulation(3, 6, 100)

print(tab)

x,y = zip(*tab)

plt.plot(x, y, label="f(x)", color='blue')

plt.title("График функции 2/(sin(x)+4)", fontsize=16)

plt.xlabel("Значения X", fontsize=14)
plt.ylabel("Значения Y", fontsize=14)
plt.legend()
plt.show()

plt.scatter(x, y, marker='o', color=(0.8, 0.5, 0.8))

plt.title("Точечный график функции y = x^2", fontsize=16)

plt.xlabel("Значения X", fontsize=14)
plt.ylabel("Значения Y", fontsize=14)

plt.grid(True, color='gray', alpha=0.5)

plt.show()

uniform_sample = np.random.randint(0, 100, size=100)

normal_sample = np.random.normal(loc=50, scale=15, size=100).astype(int)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.hist(uniform_sample, bins=15, color='blue', alpha=0.7)
ax1.set_title("Гистограмма равномерного распределения")
ax1.set_xlabel("Значения")
ax1.set_ylabel("Частота")

ax2.hist(normal_sample, bins=10, color='green', alpha=0.7)
ax2.set_title("Гистограмма нормального распределения")
ax2.set_xlabel("Значения")
ax2.set_ylabel("Частота")

plt.tight_layout()
plt.show()


sample = np.random.randint(1, 5, size=50)

unique_values, counts = np.unique(sample, return_counts=True)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.pie(counts, labels=unique_values, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Круговая диаграмма распределения чисел')

plt.subplot(1, 2, 2)
plt.bar(unique_values, counts, color=colors)
plt.title('Столбчатая диаграмма распределения чисел')
plt.xlabel('Числа')
plt.ylabel('Количество')

plt.xticks(unique_values)

plt.tight_layout()
plt.show()