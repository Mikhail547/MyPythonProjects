import time
import collections
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- НАСТРОЙКИ ---
HISTORY_SIZE = 100  # Количество точек, отображаемых на графике
SENSOR_LIMITS = [0, 500]  # Ожидаемый диапазон давления (в кПа)

# Хранилище для данных (очередь с фиксированной длиной)
time_data = collections.deque(maxlen=HISTORY_SIZE)
pressure_data_wing_tip = collections.deque(maxlen=HISTORY_SIZE)  # Кончик крыла
pressure_data_wing_root = collections.deque(maxlen=HISTORY_SIZE)  # Корень крыла

start_time = time.time()


# --- ФУНКЦИЯ ПОЛУЧЕНИЯ ДАННЫХ ---
def get_telemetry():
    """
    Симуляция получения данных.
    В реальной системе здесь должно быть чтение из Serial:
    # data = ser.readline().decode('utf-8').strip().split(',')
    # return float(data[0]), float(data[1])
    """
    current_time = time.time() - start_time

    # Симулируем базовое давление + турбулентный шум
    base_pressure = 250 + 50 * np.sin(current_time * 0.5)
    noise_1 = random.uniform(-15, 15)
    noise_2 = random.uniform(-25, 25)

    root_p = base_pressure * 1.3 + noise_2  # У корня крыла давление обычно выше
    tip_p = base_pressure * 0.8 + noise_1  # На конце крыла

    return current_time, root_p, tip_p


# --- НАСТРОЙКА ГРАФИКА ---
fig, ax = plt.subplots(figsize=(10, 5))
line_root, = ax.plot([], [], label='Корень крыла (Wing Root)', color='red', lw=2)
line_tip, = ax.plot([], [], label='Кончик крыла (Wing Tip)', color='blue', lw=1.5)

ax.set_title('Мониторинг давления на крыло в реальном времени', fontsize=14, fontweight='bold')
ax.set_xlabel('Время (сек)', fontsize=11)
ax.set_ylabel('Давление (кПа)', fontsize=11)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(SENSOR_LIMITS)
ax.legend(loc='upper left')

# Текстовые индикаторы на графике
text_root = ax.text(0.70, 0.95, '', transform=ax.transAxes, fontsize=10, color='red', fontweight='bold')
text_tip = ax.text(0.70, 0.90, '', transform=ax.transAxes, fontsize=10, color='blue', fontweight='bold')


def init():
    line_root.set_data([], [])
    line_tip.set_data([], [])
    return line_root, line_tip


# --- ФУНКЦИЯ ОБНОВЛЕНИЯ (АНИМАЦИЯ) ---
def update(frame):
    t, root_p, tip_p = get_telemetry()

    # Добавляем новые значения в очереди
    time_data.append(t)
    pressure_data_wing_root.append(root_p)
    pressure_data_wing_tip.append(tip_p)

    # Обновляем линии на графике
    line_root.set_data(time_data, pressure_data_wing_root)
    line_tip.set_data(time_data, pressure_data_wing_tip)

    # Сдвигаем ось X вслед за временем
    if len(time_data) > 1:
        ax.set_xlim(time_data[0], time_data[-1])

    # Обновляем цифровые значения на экране
    text_root.set_text(f"Корень: {root_p:.1f} кПа")
    text_tip.set_text(f"Кончик: {tip_p:.1f} кПа")

    # Аварийная подцветка при превышении критического давления (например, 400 кПа)
    if root_p > 400 or tip_p > 400:
        ax.set_facecolor('#ffcccc')  # Бледно-красный фон при опасности
    else:
        ax.set_facecolor('white')

    return line_root, line_tip, text_root, text_tip


# Запуск анимации (интервал 20 мс = ~50 кадров в секунду)
ani = animation.FuncAnimation(
    fig, update, init_func=init, blit=False, interval=20, cache_frame_data=False
)

plt.show()
