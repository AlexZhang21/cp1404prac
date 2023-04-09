FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        # Remove the \n
        line = line.strip()
        # Separate the data into its parts
        parts = line.split(',')
        # Make the number an integer
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data


def display_subjects(data):
    """Display subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
