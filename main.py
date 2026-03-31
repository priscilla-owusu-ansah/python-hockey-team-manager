# Entry point of the program
# initializes the user interface and starts program
from user_interface import UserInterface # Imports the UserInterface class from a separate module

def main():
    """Main program function"""
    # Create an instance of UserInterface class and run it
    ui = UserInterface()
    ui.run()

# Runs on direct execution
if __name__ == "__main__":
    main() 
