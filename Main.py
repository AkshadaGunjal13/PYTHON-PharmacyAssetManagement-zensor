from ui.cli import main_menu
from db.database import initialize_db

# Initialize the database and start the command-line interface
if __name__ == "__main__":
    initialize_db()
    main_menu()