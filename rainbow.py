# Import necessary Python libraries.
import csv  # For reading and writing CSV files.
import logging  # For logging messages and tracking the execution flow.
from hashlib import sha256  # For generating hash values, used here for password hashing.

# Configure the logging to include the timestamp, log level, and message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def precompute_hashes(start, end):
    """
    Generate a dictionary of hash values for a range of numbers.

    This function precomputes hashes for all numbers in a specified range, which
    facilitates quick lookup during the password cracking process.

    :param start: The starting number for hash computation.
    :param end: The ending number for hash computation.
    :return: A dictionary mapping hash values to their original numbers.
    """
    # Log the beginning of hash computation.
    logging.info('Pre-computing hashes.')
    # Use dictionary comprehension to create a map of hash values to numbers.
    return {sha256(str(i).encode()).hexdigest(): i for i in range(start, end)}

def hack_passwords(input_file_name, output_file_name, hashes):
    """
    Hack hashed passwords by comparing against a precomputed hash dictionary.

    This function reads a CSV file containing hashed passwords, attempts to find
    corresponding original values using the precomputed hash dictionary, and writes
    the results to an output file.

    :param input_file_name: Path to the input CSV file with name-hash pairs.
    :param output_file_name: Path to the output CSV file for saving hacked passwords.
    :param hashes: A dictionary of precomputed hash values.
    """
    try:
        # Start reading and hacking process.
        logging.info('Reading input file and attempting to hack passwords.')
        with open(input_file_name, 'r') as fin:
            reader = csv.reader(fin)
            # Dictionary comprehension to match hash values and retrieve original numbers.
            hacked = {name: hashes[hash_value] for name, hash_value in reader if hash_value in hashes}

        # Start writing the hacked passwords to the output file.
        logging.info('Writing hacked passwords to output file.')
        with open(output_file_name, 'w', newline='') as fout:
            writer = csv.writer(fout)
            # Iterate over hacked items and write each to the output CSV.
            for name, password in hacked.items():
                writer.writerow([name, password])

    except Exception as e:
        # Log any exceptions that occur during the read/hack/write process.
        logging.error(f'An error occurred: {e}')

def main(input_file_path, output_file_path):
    """
    Main function to orchestrate the hashing and password hacking process.

    This function serves as the primary controller, orchestrating the hash
    precomputation, password hacking, and result writing.

    :param input_file_path: Path to the input CSV containing hashed passwords.
    :param output_file_path: Path to the output CSV for cracked passwords.
    """
    # Generate precomputed hash values.
    hashes = precompute_hashes(1000, 9999)
    # Attempt to crack the passwords using the precomputed hashes.
    hack_passwords(input_file_path, output_file_path, hashes)
    # Indicate completion of the process.
    logging.info('Process completed.')

# This condition checks if the script is being run directly (as opposed to being imported).
if __name__ == "__main__":
    # Define input and output file paths.
    input_file_path = "test_passwords.csv"
    output_file_path = "cracked_passwords.csv"
    # Invoke the main function with the specified paths.
    main(input_file_path, output_file_path)
