def read(file):
    try:
        with open(file, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def read(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data