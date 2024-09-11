import matplotlib.pyplot as plt

def antigenicity(sequence):
    """
    Calculates the antigenicity of a given protein sequence using the Kolaskar and Tongaonkar scale.
    """
    antigenicity_values = {
        'A': 0.603, 'R': 0.901, 'N': 0.678, 'D': 0.617, 'C': 0.717, 'Q': 0.793,
        'E': 0.669, 'G': 0.570, 'H': 0.813, 'I': 1.009, 'L': 0.931, 'K': 0.711,
        'M': 0.823, 'F': 1.019, 'P': 0.674, 'S': 0.644, 'T': 0.669, 'W': 1.009,
        'Y': 0.881, 'V': 0.881
    }
    
    total_value = 0
    for amino_acid in sequence:
        if amino_acid in antigenicity_values:
            total_value += antigenicity_values[amino_acid]
        else:
            return None  # Return None if the sequence contains an unknown amino acid
    
    return total_value / len(sequence)

# Get the protein sequence from the user
protein_sequence = input("Enter the protein sequence: ")

# Find the most antigenic region
window_size = 7  # Adjust the window size as needed
max_antigenicity = -float('inf')
most_antigenic_region = None

antigenicity_scores = []
for i in range(len(protein_sequence) - window_size + 1):
    region_sequence = protein_sequence[i:i+window_size]
    region_antigenicity = antigenicity(region_sequence)
    if region_antigenicity is not None and region_antigenicity > max_antigenicity:
        max_antigenicity = region_antigenicity
        most_antigenic_region = region_sequence
    antigenicity_scores.append(region_antigenicity)

if most_antigenic_region is None:
    print("No valid antigenic region found in the sequence.")
else:
    print(f"The most antigenic region is: {most_antigenic_region}")

# Plot the antigenicity profile
plt.figure(figsize=(12, 4))
plt.plot(antigenicity_scores)
plt.axhline(y=0.8, color='r', linestyle='--', label='Antigenicity Threshold')
plt.xlabel('Amino Acid Position')
plt.ylabel('Antigenicity Score')
plt.title('Antigenicity Profile of the Protein Sequence')
plt.legend()
plt.show()