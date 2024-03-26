from hashlib import sha256
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hash_password_hack(input_file_name, output_file_name):
    """
    Hack password hashes by comparing against pre-computed hash values.

    :param input_file_name: Path to the CSV file containing name and hash pairs.
    :param output_file_name: Path to the output CSV file to write hacked passwords.
    """
    logging.info('Pre-computing hashes.')
    hp = {sha256(str(i).encode()).hexdigest(): i for i in range(1000, 9999)}

    new_hp = {}

    try:
        logging.info('Reading input file and attempting to hack passwords.')
        with open(input_file_name, 'r') as fin:
            reader = csv.reader(fin)
            for row in reader:
                name, hash_value = row
                if hash_value in hp:
                    new_hp[name] = hp[hash_value]

        logging.info('Writing hacked passwords to output file.')
        with open(output_file_name, 'w', newline='') as fout:
            writer = csv.writer(fout)
            for name, password in new_hp.items():
                writer.writerow([name, password])

    except Exception as e:
        logging.error(f'An error occurred: {e}')

    logging.info('Process completed.')

# Here you specify the path directly when calling the function
input_file_path = "-"
output_file_path = "-"

# Call the function with the specified paths
hash_password_hack(input_file_path, output_file_path)
