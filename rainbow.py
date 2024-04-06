# Import necessary libraries
from hashlib import sha256  # Used for hashing strings.
import csv  # Used for reading and writing CSV files.
import logging  # Used for logging messages.
from tqdm import tqdm  # Used for displaying progress bars.

# Configure logging to display time, log level, and message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hash_password_hack(input_file_name, output_file_name):
    """
    This function attempts to 'hack' hashed passwords by comparing them against a
    list of pre-computed hash values. If a match is found, the corresponding number
    (the password before hashing) is considered 'hacked'.

    :param input_file_name: The path to a CSV file that contains name and hash pairs.
    :param output_file_name: The path to the output CSV file where results will be written.
    """
    # Log the start of the pre-computation process.
    logging.info('Pre-computing hashes.')
    # Compute hash values for numbers between 1000 and 9999 and store them in a dictionary.
    hp = {sha256(str(i).encode()).hexdigest(): i for i in tqdm(range(1000, 9999), desc='Computing hashes')}

    new_hp = {}  # Initialize a dictionary to store hacked password results.

    try:
        # Log the start of the hacking process.
        logging.info('Reading input file and attempting to hack passwords.')
        # Open and read the input CSV file.
        with open(input_file_name, 'r') as fin:
            reader = csv.reader(fin)
            rows = list(reader)  # Read all rows into a list for progress tracking.
            for row in tqdm(rows, desc='Processing rows'):
                name, hash_value = row  # Extract name and hash from each row.
                if hash_value in hp:  # Check if the hash is one of the pre-computed values.
                    new_hp[name] = hp[hash_value]  # If so, store the corresponding password.

        # Log the start of the writing process.
        logging.info('Writing hacked passwords to output file.')
        # Open and write the hacked passwords to the output CSV file.
        with open(output_file_path, 'w', newline='') as fout:
            writer = csv.writer(fout)
            for name, password in tqdm(new_hp.items(), desc='Writing output'):
                writer.writerow([name, password])  # Write each name and hacked password pair.

    except Exception as e:
        # Log any errors that occur.
        logging.error(f'An error occurred: {e}')

    # Log the completion of the process.
    logging.info('Process completed.')

# Specify the paths for the input and output files.
input_file_path = "test_passwords.csv"
output_file_path = "cracked_passwords.csv"

# Execute the function using the specified file paths.
hash_password_hack(input_file_path, output_file_path)
