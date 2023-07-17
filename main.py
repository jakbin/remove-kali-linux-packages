import os

# Dictionary mapping category numbers to file names
file_mapping = {
    1: 'kali-linux-default.txt',
    2: 'kali-tools-bluetooth.txt',
    3: 'kali-tools-database.txt',
    4: 'kali-tools-exploitation.txt',
    5: 'kali-tools-forensics.txt',
    6: 'kali-tools-fuzzing.txt',
    7: 'kali-tools-identify.txt',
    8: 'kali-tools-information-gathering.txt',
    9: 'kali-tools-passwords.txt',
    10: 'kali-tools-post-exploitation.txt',
    11: 'kali-tools-recover.txt',
    12: 'kali-tools-reverse-engineering.txt',
    13: 'kali-tools-sdr.txt',
    14: 'kali-tools-social-engineering.txt',
    15: 'kali-tools-sniffing-spoofing.txt',
    16: 'kali-tools-vulnerability.txt',
    17: 'kali-tools-voip.txt',
    18: 'kali-tools-web.txt',
    19: 'kali-tools-wireless.txt'
}

# Print the available categories
print("Categories:")
for key, value in file_mapping.items():
    print(f"{key}. {value[:-4]}")

# Ask user for the category number
category_number = int(input("Enter the category number of packages to remove: "))

# Check if the input category number is valid
if category_number not in file_mapping:
    print("Invalid category number.")
    exit()

# Get the corresponding file name
file_name = file_mapping[category_number]

# Function to remove packages using apt-get command
def remove_packages(package_list):
    packages = ' '.join(package_list)
    print(packages)
    os.system(f"sudo apt remove {packages}")

# Read the packages from the file
with open(f"category/{file_name}", 'r') as file:
    package_list = [line.strip() for line in file]

# Remove the packages
if len(package_list) > 0:
    print("Removing the following packages:")
    packages = ' '.join(package_list)
    print(packages)
    confirmation = input("Do you want to proceed? (y/n): ")
    if confirmation.lower() == 'y' or confirmation == '':
        remove_packages(package_list)
        print("Packages removed successfully.")
    else:
        print("Aborted.")
else:
    print("No packages found in the selected category.")
