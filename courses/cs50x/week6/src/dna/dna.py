import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the database file
    with open(database_file, "r") as file:
        database = list(csv.reader(file))

    # TODO: Read DNA sequence file into a variable
    with open(sequence_file, "r") as file:
        dna_sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    strs = database[0][1:]

    # Initialize a dictionary and find the longest match for each STR in the DNA sequence
    longest_matches = {}
    for str in strs:
        longest_matches[str] = longest_match(dna_sequence, str)

    # TODO: Check database for matching profiles
    # Iterate over each row in the database (excluding the header)
    for row in database[1:]:
        # Get the name from the first column
        name = row[0]

        # Get the list of STR counts from the remaining columns
        str_counts = list(map(int, row[1:]))

        # Check if the STR counts match the longest matches
        if str_counts == list(longest_matches.values()):
            print(name)
            return

    # Else (if not found)
    print("No match\n")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
