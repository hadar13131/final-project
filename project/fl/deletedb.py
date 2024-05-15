import os

database_file = "PowerAppDatabase.db"

# Check if the file exists before attempting to delete
if os.path.exists(database_file):
    os.remove(database_file)
    print(f"The database file '{database_file}' has been deleted.")
else:
    print(f"The database file '{database_file}' does not exist.")