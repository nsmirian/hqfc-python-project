#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# تعداد ذرات
num_particles = 5

# تعریف مقادیر بتا و اپسیلون برای محاسبه سیگما
beta_x = 1.0  # مقدار مثالی برای بتا x
epsilon_x = 0.5  # مقدار مثالی برای اپسیلون x
beta_y = 1.0  # مقدار مثالی برای بتا y
epsilon_y = 0.5  # مقدار مثالی برای اپسیلون y

# محاسبه سیگما x و سیگما y
sigma_x = np.sqrt(beta_x * epsilon_x)
sigma_y = np.sqrt(beta_y * epsilon_y)

# تعریف ماتریس اولیه بر اساس سیگما x و سیگما y
initial_positions = np.zeros((num_particles, 4))
initial_positions[:, 0] = np.random.normal(0, sigma_x, num_particles)  # x positions
initial_positions[:, 1] = np.random.normal(0, sigma_x, num_particles)  # x' positions
initial_positions[:, 2] = np.random.normal(0, sigma_y, num_particles)  # y positions
initial_positions[:, 3] = np.random.normal(0, sigma_y, num_particles)  # y' positions

# تعریف ماتریس انتقالات هلیکال کوادروپل
def helical_quadrupole_matrix(L, k):
    cos_kl = np.cos(k * L)
    sin_kl = np.sin(k * L)
    M_x = np.array([[cos_kl, sin_kl/k, 0, 0],
                    [-k*sin_kl, cos_kl, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    M_y = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, cos_kl, sin_kl/k],
                    [0, 0, -k*sin_kl, cos_kl]])
    return M_x, M_y

# پارامترهای شبیه‌سازی
L = 1.0  
k = 0.1  

# دریافت ماتریس‌های انتقال
M_x, M_y = helical_quadrupole_matrix(L, k)

# تعداد مراحل شبیه‌سازی
num_steps = 100
# ذخیره‌سازی موقعیت‌ها
positions = np.zeros((num_steps, num_particles, 4))
positions[0] = initial_positions

# حلقه شبیه‌سازی
for step in range(1, num_steps):
    for i in range(num_particles):
        # به‌روز‌رسانی موقعیت با ضرب داخلی
        positions[step, i] = M_y @ (M_x @ positions[step-1, i])  

# ترسیم نمودار
plt.figure(figsize=(10, 6))
for i in range(num_particles):
    plt.plot(positions[:, i, 0], positions[:, i, 2], label=f'Particle {i+1}')
plt.xlabel('x position')
plt.ylabel('y position')
plt.title('Particle trajectories in a helical quadrupole focusing channel')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




