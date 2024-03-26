from hashlib import sha256
import csv
import logging

# Set up basic logging configuration to output time, log level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hash_password_hack(input_file_name, output_file_name):
    """
    This function attempts to crack password hashes by comparing them against a dictionary
    of pre-computed hash values for a given range of numbers.

    :param input_file_name: String specifying the path to the input CSV file that contains
                            pairs of names and their corresponding hash values.
    :param output_file_name: String specifying the path to the output CSV file where the
                             names and their cracked passwords will be written.
    """

    # Generate hash values for all four-digit numbers (1000-9999) and store them in a dictionary
    # This allows for quick lookup of the number based on its hash value
    logging.info('Pre-computing hashes.')
    hp = {sha256(str(i).encode()).hexdigest(): i for i in range(1000, 9999)}

    # Initialize a dictionary to store the mapping of names to their successfully cracked passwords
    new_hp = {}

    try:
        # Open the input file and iterate over each row to find corresponding passwords
        logging.info('Reading input file and attempting to hack passwords.')
        with open(input_file_name, 'r') as fin:
            reader = csv.reader(fin)
            for row in reader:
                name, hash_value = row
                # Check if the hash from the file exists in the pre-computed hash dictionary
                if hash_value in hp:
                    # If a match is found, store the name and the cracked password
                    new_hp[name] = hp[hash_value]

        # Once all hashes are processed, write the results to the output file
        logging.info('Writing hacked passwords to output file.')
        with open(output_file_name, 'w', newline='') as fout:
            writer = csv.writer(fout)
            for name, password in new_hp.items():
                writer.writerow([name, password])

    except Exception as e:
        # Log any errors that occur during file reading or writing
        logging.error(f'An error occurred: {e}')

    # Indicate completion of the process
    logging.info('Process completed.')
