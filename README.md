# Desktop-Database-App
- Python code that creates a GUI using Tkinter to access  and manage the database of a bookstore.
- Spyder IDE used for coding.
- To run the python code, run only **main.py** as it imports backend.py.
- To create a **.exe** file, we need to install ***pyinstaller*** : `pip install pyinstaller`.
- Once done, we run `pyinstaller --onefile --windowed main.py` to create the **.exe** file.

## main.py - Front end
### The GUI stores the following information:
- Title
- Author
- Year
- ISBN

### It allows users to:
- View all records
- Search for a record
- Add a record
- Update a record
- Delete a record
- Close the GUI

## backend.py - Back end
- The code uses sqlite to create a 'books.db' database.
- The code creates functions to :
<br>-- Connect to the database.
<br>-- Insert elements into database
<br>-- View all elements
<br>-- Search for specific elements
<br>-- Delete specific elements
<br>-- Update specific elements
