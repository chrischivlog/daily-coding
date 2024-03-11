import csv

inputer = 'input.csv'
reference = 'reference.csv'

# Read input file into memory
input_data = set()
with open(inputer, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        # Combine ort and strasse to form a unique identifier for each row
        ort_strasse_combo = f"{row[0]}_{row[1]}"
        input_data.add(ort_strasse_combo)

# Now check each line in the reference file against the input data
with open(reference, 'r', encoding='utf-8') as file_ref:
    reader_ref = csv.reader(file_ref, delimiter=';')
    for row_ref in reader_ref:
        ort_strasse_combo_ref = f"{row_ref[0]}_{row_ref[1]}"

        if ort_strasse_combo_ref in input_data:
            # If the line from the reference file was found in the input file, print it
            print(f"Found in input file: {row_ref[0]}, {row_ref[1]}")
        else:
            # If not found in the input file, print it from the reference file, indicating it's not in the input file
            print(f"Not found in input file, from reference file: {row_ref[0]}, {row_ref[1]}")
