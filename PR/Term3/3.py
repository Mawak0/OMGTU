import numpy as np
import scipy
import scipy.stats as stats
import statistics as stat


def show_matrix(mat):
    s = ""
    for line in mat:
        for e in line:
            if (e-int(e) == 0):
                s = s+" "+str(int(e))
            else:
                s = s + " " + str(e)
        s = s+"\n"
    print(s)


A = [[2.3, 0, -3.4, -12], [2.6, 8.4, -9, 3], [1.3, 4.5, -17, 2], [1.8, 0, 15, 16]]

P, L, U = scipy.linalg.lu(A)
print("Нижняя треугольная матрица:")
show_matrix(L)
print("Верхняя треугольная матрица:")
show_matrix(U)

det_A = np.linalg.det(A)
print("Определитель исходной матрицы: "+str(det_A))
diag_el = np.prod(np.diag(L))*np.prod(np.diag(U))
det_r_p = 1 / np.linalg.det(P)
det_A = diag_el*det_r_p
print("Определитель исходной матрицы: "+str(det_A))



uniform_sample = np.random.randint(0, 100, size=100)

normal_sample = np.random.normal(loc=50, scale=15, size=100).astype(int)


def calculate_statistics(sample):
    mean = np.mean(sample)
    mode = stat.mode(sample)
    median = np.median(sample)
    minimum = np.min(sample)
    maximum = np.max(sample)
    std_dev = np.std(sample)

    return {
        "Среднее": mean,
        "Мода": mode,
        "Медиана": median,
        "Минимум": minimum,
        "Максимум": maximum,
        "Стандартное отклонение": std_dev
    }


print("Статистика равномерного распределения: ", calculate_statistics(uniform_sample))

print("Статистика нормального распределения: ", calculate_statistics(normal_sample))


chi2_stat, p_value_uniform = stats.chisquare(uniform_sample)
print(f"Хи-квадрат для равномерного распределения: p-value = {p_value_uniform}")

chi2_stat_normal, p_value_normal = stats.chisquare(normal_sample)
print(f"Хи-квадрат для нормального распределения: p-value = {p_value_normal}")