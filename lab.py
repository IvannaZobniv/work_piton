import numpy as np
import pandas as pd
import matplotlib.pyplot as pit

# # Load the data from the text file into a pandas dataframe
# df = pd.read_csv('input.txt', sep='\t', header=None)
#
# # Perform Kalman filtering on the data using the KalmanFilter class from the PyKalman library
# from pykalman import KalmanFilter
# kf = KalmanFilter(transition_matrices=np.array([[1, 1], [0, 1]]), observation_matrices=np.array([[1, 0]]))
# (smoothed_state_means, smoothed_state_covariances) = kf.smooth(df.values)
#
# # Save the result to a CSV file
# result = pd.DataFrame(smoothed_state_means, columns=['x', 'y'])
# result.to_csv('output.csv', index=False)


# Load the data from the text file into a pandas dataframe
df = pd.read_csv('input.txt', sep='\t', header=None)

# Define the state transition matrix
F = np.array([[1, 1], [0, 1]])

# Define the observation matrix
H = np.array([[1, 0]])

# Define the process noise covariance matrix
Q = np.array([[0.0001, 0.0], [0.0, 0.0001]])

# Define the measurement noise covariance matrix
R = np.array([[0.1]])

# Define the initial state estimate
x_estimate = np.array([[0.0, 0.0]]).T

# Define the initial state covariance matrix
P = np.array([[10.0, 0.0], [0.0, 10.0]])

# Define the number of observations
num_observations = df.shape[0]

# Initialize the smoothed state estimate
smoothed_state_estimate = np.zeros((num_observations, 2))

# Store the first estimate as the first smoothed state estimate
smoothed_state_estimate[0, :] = x_estimate.flatten()

# Loop over each observation (starting from the second one)
for t in range(1, num_observations):
    # Predict the next state estimate
    x_predict = F @ x_estimate
    P_predict = F @ P @ F.T + Q

    # Compute the Kalman gain
    K = P_predict @ H.T / (H @ P_predict @ H.T + R)

    # Update the state estimate
    x_estimate = x_predict + K * (df.iloc[t, 0] - H @ x_predict)
    P = (np.eye(2) - K @ H) @ P_predict

    # Store the smoothed state estimate
    smoothed_state_estimate[t, :] = x_estimate.flatten()

# Save the result to a CSV file
result = pd.DataFrame(smoothed_state_estimate, columns=['x', 'y'])
result.to_csv('output.csv', index=False)
