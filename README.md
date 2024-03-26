# Rainbow

`Rainbow` is a Python script designed to crack numerical password hashes using a pre-computed hash table approach. It is specifically tailored to process CSV files containing usernames and their corresponding SHA-256 hash values, attempting to reverse-engineer the hash back into a four-digit numerical password.

## Features

- Efficient hash cracking for numerical passwords: specifically targets passwords in the range of 1000 to 9999.
- CSV input/output: reads user-hash pairs from an input CSV file and writes cracked passwords to an output CSV file.
- Logging: detailed logging to track the process flow and identify potential issues.

## Requirements

- Python 3.x
- No external Python libraries are required beyond the standard library.

## Usage

1. Prepare an input CSV file with the following format:
   ```
   username,hash
   john,5e884898da28047151d0e56f8dc6292773603f8186d01823
   jane,ee26b0dd4af7e749aa1a8ee3c10aef57247cf9733dd0ad90
   ```

2. Run the script using Python, providing the input and output file names:
   ```
   python rainbow.py input.csv output.csv
   ```

3. After execution, the output CSV file will contain the cracked passwords:
   ```
   john,1234
   jane,5678
   ```

## How It Works

The script pre-computes SHA-256 hashes for all numbers in the range 1000 to 9999 and stores them in a dictionary. When reading the input file, it compares each hash against this dictionary. If a match is found, the script deduces that the original password was the number that corresponds to the hash.

## Limitations

- The script only works with numerical passwords in the specified range.
- It is not designed for cracking more complex or longer passwords outside of the pre-defined scope.

## Contributing

Contributions to `Rainbow` are welcome. Please ensure to follow best coding practices and include tests where applicable.

## License

`Rainbow` is open-sourced software licensed under the MIT license.