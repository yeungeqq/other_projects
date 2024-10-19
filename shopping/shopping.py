import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open("shopping.csv") as f:
        reader = csv.reader(f)
        next(reader)

        data = []
        for row in reader:
            evidence = []
            evidence.append(int(row[0]))
            evidence.append(float(row[1]))
            evidence.append(int(row[2]))
            evidence.append(float(row[3]))
            evidence.append(int(row[4]))
            for cell in row[5:10]:
                evidence.append(float(cell))
            if row[10] == 'Jan':
                month = 0
            if row[10] == 'Feb':
                month = 1
            if row[10] == 'Mar':
                month = 2
            if row[10] == 'Apr':
                month = 3
            if row[10] == 'May':
                month = 4
            if row[10] == 'June':
                month = 5
            if row[10] == 'July':
                month = 6
            if row[10] == 'Aug':
                month = 7
            if row[10] == 'Sep':
                month = 8
            if row[10] == 'Oct':
                month = 9
            if row[10] == 'Nov':
                month = 10
            if row[10] == 'Dec':
                month = 11
            evidence.append(int(month))
            for cell in row[11:15]:
                evidence.append(int(cell))
            visitor = (1 if row[15] == 'Returning_Visitor' else 0)
            evidence.append(int(visitor))
            weekend = (1 if row[16] == True else 0)
            evidence.append(int(weekend))

            data.append({
                "evidence": evidence,
                "label": 0 if row[17] == 'FALSE' else 1
            })

    evidence = [row['evidence'] for row in data]
    labels = [row['label'] for row in data]

    return (evidence, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positive = []
    negative = []
    for i in range(len(labels)):
        if labels[i] == 1 and predictions[i] == 1:
            positive.append(1)
        if labels[i] == 1 and predictions[i] == 0:
            positive.append(0)
        if labels[i] == 0 and predictions[i] == 0:
            negative.append(1)
        if labels[i] == 0 and predictions[i] == 1:
            negative.append(0)

    sensitivity = float(sum(positive)/len(positive))
    specificity = float(sum(negative)/len(negative))
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
