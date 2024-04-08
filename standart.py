from sklearn.preprocessing import StandardScaler
import numpy as np

# Создаем массив данных
data = np.array([-2, 4, 129, 2, -322, 0, 21])

# Создаем экземпляр StandardScaler
scaler = StandardScaler()

# Применяем масштабирование к данным
scaled_data = scaler.fit_transform(data)

# Выводим результаты
print(scaled_data)