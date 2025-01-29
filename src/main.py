from datetime import datetime
import os

# Define the correct file path for version.md
file_path = os.path.join(os.getcwd(), "version.md")

# Get the current date and time
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

try:
    # Write the date and time to version.md
    with open(file_path, "w") as file:
        file.write(f'Current Date and Time: {now}\n')

    print(f"✅ File successfully created at: {file_path}")

except Exception as e:
    print(f"❌ Error creating file: {e}")
from datetime import datetime

# Get the current date and time
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Write the date and time to version.md
with open('../version.md', 'w') as file:
    file.write(f'Current Date and Time: {now}\n')
