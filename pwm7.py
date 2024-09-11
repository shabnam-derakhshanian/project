import numpy as np
import matplotlib.pyplot as plt

# Example PWM matrix (replace this with your own PWM matrix)
# Ensure your PWM matrix has shape (number_of_positions, 20)
pwm = np.array([
    [0.05, 0.02, 0.1, 0.01, 0.15, 0.12, 0.05, 0.02, 0.2, 0.1, 0.03, 0.02, 0.03, 0.05, 0.02, 0.05, 0.1, 0.1, 0.02, 0.03],
    [0.1, 0.03, 0.05, 0.02, 0.12, 0.1, 0.15, 0.1, 0.05, 0.05, 0.02, 0.1, 0.05, 0.03, 0.02, 0.1, 0.1, 0.1, 0.05, 0.02],
    [0.02, 0.05, 0.1, 0.15, 0.03, 0.05, 0.02, 0.1, 0.1, 0.02, 0.12, 0.1, 0.05, 0.1, 0.1, 0.03, 0.02, 0.02, 0.1, 0.1],
    [0.1, 0.1, 0.02, 0.03, 0.05, 0.02, 0.05, 0.12, 0.1, 0.05, 0.1, 0.03, 0.02, 0.1, 0.15, 0.02, 0.1, 0.03, 0.05, 0.1]
])

# Define amino acids
amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

# Define positions (assuming each row in pwm corresponds to a position)
positions = [f'Position {i+1}' for i in range(pwm.shape[0])]

# Create figure and axis
plt.figure(figsize=(14, 8))

# Plot each position as a bar plot
for i in range(pwm.shape[0]):
    plt.bar(amino_acids, pwm[i], alpha=0.8, label=positions[i])

# Add labels and title
plt.xlabel('Amino Acid')
plt.ylabel('Frequency')
plt.title('Position Weight Matrix')

# Add legend
plt.legend(title='Position')

# Adjust layout and show plot
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
