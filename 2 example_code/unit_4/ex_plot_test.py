import matplotlib.pyplot as plt
import random
import math

# Generate sample data - 24 hours of temperature readings
hours = list(range(24))  # 0 to 23 hours

# Create simulated temperature data with a sinusoidal pattern and some randomness
temperatures = []
for hour in hours:
    # Base temperature of 15°C + sinusoidal variation throughout the day + random noise
    base_temp = 15
    daily_variation = 10 * math.sin(hour * math.pi / 12)  # Peak at noon/midnight
    random_noise = random.uniform(-1, 1)  # Random variation between -1 and 1
    temperature = base_temp + daily_variation + random_noise
    temperatures.append(temperature)

temperatures_2 = [x + random.randint(-1, 1) for x in temperatures]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))

ax1.plot(hours, temperatures, color='red', linestyle='dashdot', marker='*', markersize=10, markerfacecolor='green', markeredgecolor='blue', label='Temperature')
ax2.plot(hours, temperatures_2)

ax1.set_xlabel('Hour of Day', fontsize=15)
ax1.set_ylabel('Temperature in °C', fontsize=15)
ax1.set_title('Temp Over Time')

ax1.set_xlim(-0.5, 23.5)
ax1.set_xticks(range(0,24,3))
ax1.grid(True, linestyle='--')
ax1.legend()

plt.show()
