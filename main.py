import os


def search_text_in_files(folder_path, search_text):
    """
    Search for text in 'Passwords.txt' files within a folder and its subfolders.

    This function searches for the specified text in all 'Passwords.txt' files within the specified folder and its subfolders.
    If it finds a 'Passwords.txt' file that contains the specified text, it prints the path of the subfolder that contains the file,
    along with the URL, username, and password that appear after the specified text in the file.
    If it doesn't find any 'Passwords.txt' files containing the specified text, it prints a message indicating that no matching files were found.

    Args:
        folder_path (str): The path of the folder to search in.
        search_text (str): The text to search for.

    Returns:
        None
    """
    found = False
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == 'Passwords.txt':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='latin-1') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if line.startswith('URL:') and search_text in line:
                            url = line.split(': ')[-1].strip()
                            username = lines[i+1].split(': ')[-1].strip()
                            password = lines[i+2].split(': ')[-1].strip()
                            print(f"Found '{search_text}' in {root}")
                            print(f"URL: {url}")
                            print(f"Username: {username}")
                            print(f"Password: {password.encode('utf-8')}")
                            found = True
                            break
    if not found:
        print(f"No matching files found in {folder_path}")
