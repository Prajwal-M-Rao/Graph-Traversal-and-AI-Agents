from collections import Counter

def calculate_probabilities(dataset):
    total_count = len(dataset)

    # Calculate the frequency of each unique value in the dataset
    value_counts = Counter(dataset)

    # Calculate probabilities for each unique value
    probabilities = {value: count / total_count for value, count in value_counts.items()}

    return probabilities


def main():
    # Example dataset, replace this with your actual dataset
    dataset =['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'B','A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'B', 'B']

    # Calculate probabilities
    probabilities = calculate_probabilities(dataset)

    # Display the results
    print("Dataset:", dataset)
    print("\nProbabilities:")
    for value, probability in probabilities.items():
        print(f"{value}: {probability:.2f}")


if __name__ == "__main__":
    main()
