from datetime import datetime

def create_new_file(filename):
    title = input("Title: ")
    description = input("Description: ")
    keywords = input("Keywords (comma-separated): ")
    current_date = datetime.now().strftime("%d-%m-%Y")

    metadata = f"""title="{title}"
description="{description}"
keywords="{keywords}"
date="{current_date}"
---
"""

    try:
        with open(filename, 'w') as file:
            file.write(metadata)
        print("\033[1;32mOK\033[0m\tGood writing")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    filename = input("File name (with .md extension): ")
    create_new_file(filename)
