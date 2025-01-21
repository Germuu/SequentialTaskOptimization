import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Import the Worker class from the carwash module
from carwash import Worker

# Generate synthetic worker profile data (for illustration)
# Assuming `Worker` class is defined in the carwash module with task times as attributes

# Example of synthetic worker profiles
n_samples = 100
vacuum_times = np.random.uniform(3, 12, n_samples)  # Vacuum times between 3 to 12 minutes
wipe_times = np.random.uniform(2, 10, n_samples)    # Wiping times between 2 to 10 minutes
pressure_times = np.random.uniform(5, 15, n_samples)  # Pressure washing times between 5 to 15 minutes

# Calculate current and optimized throughput based on these task times
current_throughputs = 60 / (vacuum_times + wipe_times + pressure_times) / 3
optimized_throughputs = 60 / np.maximum(vacuum_times, wipe_times, pressure_times)

# Calculate throughput improvement (optimized - current)
throughput_improvements = optimized_throughputs - current_throughputs

# Create a DataFrame to store the synthetic data
data = pd.DataFrame({
    'vacuum_time': vacuum_times,
    'wipe_time': wipe_times,
    'pressure_time': pressure_times,
    'throughput_improvement': throughput_improvements
})

# Display the first few rows of the data
print(data.head())

# Split the data into features and target variable
X = data[['vacuum_time', 'wipe_time', 'pressure_time']]  # Features
y = data['throughput_improvement']  # Target variable (throughput improvement)

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'Mean Absolute Error: {mae:.2f}')
print(f'R²: {r2:.2f}')

# Plot predicted vs actual throughput improvements
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', label='Perfect Prediction')
plt.xlabel('Actual Throughput Improvement')
plt.ylabel('Predicted Throughput Improvement')
plt.title('Predicted vs Actual Throughput Improvement')
plt.legend()
plt.show()

# Example of new worker profiles to predict throughput improvement
new_workers = np.array([[10, 5, 3],  # Worker 1: Vacuum=10, Wipe=5, Pressure=3
                        [8, 6, 4],   # Worker 2: Vacuum=8, Wipe=6, Pressure=4
                        [7, 7, 6]])   # Worker 3: Vacuum=7, Wipe=7, Pressure=6

# Use the trained model to predict throughput improvements
predictions = model.predict(new_workers)
print(f'Predicted Throughput Improvements for new workers: {predictions}')
