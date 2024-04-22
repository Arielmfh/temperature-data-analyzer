import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

avg_max_temp = data["MaxTemp"].mean()
avg_min_temp = data["MinTemp"].mean()

print(f"Average Maximum Temperature: {avg_max_temp:.2f} °C")
print(f"Average Minimum Temperature: {avg_min_temp:.2f} °C")

# Plot the temperature data
plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["MaxTemp"], label="Maximum Temperature", marker="o")
plt.plot(data["Date"], data["MinTemp"], label="Minimum Temperature", marker="o")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Data Analysis")
plt.legend()
plt.grid(True)
plt.show()