import os # Gives access to os functionalities (file handling and directory operations)
import json # Allows conversion of Python objects to JSON format and vice versa for data storage and exchange
import datetime # Handles date and time-related operations, such as automatically setting creation dates
from team import Team # Imports the Team class from a separate module

# Class for UI 
class UserInterface:
    def __init__(self):
        # Initialize empty list for team objects
        self.teams = []
        """
        Displays the main menu for the Hockey Team Management System.
        """    
    def display_menu(self):
        """Display the main menu and return user choice"""
        print("*************************************")
        print("\n*** Hockey Team Management System ***")
        print("*************************************")
        print("1. Register a New Team")         # Register or Add New team
        print("2. Display Team by ID")          # Shows Team Info using its ID
        print("3. Display Teams by type (boys/girls)") # Shows Team by Type
        print("4. Display all Teams")           # Shows all Team Info
        print("5. Update Team Information")     # Updates Team Info
        print("6. Delete Team")                 # Deletes Team Info
        print("7. Display Team Statistics")     # Shows Team Statistics 
        print("8. Save Team Information")       # Saves team data into a .txt file
        print("9. Restore Team Information")    # Restores previously saved team data
        print("0. Quit Program")                        # Ends program
        
        # Prompt user to select from (0-9) and return their selection
        choice = input("\nEnter your choice (0-9): ")
        return choice
    
    def create_team(self):
        """Register a new team and add it to the teams list"""
        print("\n--- Register New Team ---")
        
        # Get team information from user (checks for empty name)
        while True:
            name = input("Enter team name: ").strip()  # Remove leading/trailing spaces
            if name:  # Check if name is not empty
                break
            print("Team name cannot be empty. Please enter a name.")
        
        # Validate team type (keep asking until valid input)
        while True:
            team_type = input("Enter team type (boys/girls): ").lower()
            if team_type in ["boys", "girls"]:
                break
            print("Invalid team type. Please enter 'boys' or 'girls'.")
        
        # Ask about fee payment
        while True:
            fee_paid_input = input("Has the fee been paid? (yes/no): ").lower()
            if fee_paid_input in ["yes", "no"]:
                fee_paid = fee_paid_input == "yes"
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Create new team instance
        new_team = Team(name, team_type, fee_paid)
        
        # Add to teams list
        self.teams.append(new_team)
        print(f"Team registered successfully! Team ID: {new_team.id}")
    
    def display_team(self, team):
        """Display information about a single team"""
        print("\n--- Team Information ---")
        print(team)
    
    def display_all_teams(self):
        """Display information about all teams"""
        if not self.teams:
            print("\nNo teams available.")
            return
        
        print("\n--- All Teams ---")
        for team in self.teams:
            print(team)
        print(f"Total teams: {len(self.teams)}")
    
    def display_teams_by_type(self, team_type):
        """Display teams filtered by type (boys/girls)"""
        filtered_teams = [team for team in self.teams if team.team_type == team_type]
        
        if not filtered_teams:
            print(f"\nNo {team_type} teams available.")
            return
        
        print(f"\n--- {team_type.capitalize()} Teams ---")
        for team in filtered_teams:
            print(team)
        print(f"Total {team_type} teams: {len(filtered_teams)}")
    
    def find_team_by_id(self, team_id):
        """Find a team by its ID"""
        for team in self.teams:
            if team.id == team_id:
                return team
        return None
    
    def update_team(self):
        """Update team information except ID and creation date"""
        if not self.teams:
            print("\nNo teams available to update.")
            return
        
        print("\n--- Update Team ---")
        
        # Show available teams
        print("Available teams:")
        for team in self.teams:
            print(f"ID: {team.id}, Name: {team.name}")
        
        # Ask for team ID to update
        while True:
            try:
                team_id = int(input("\nEnter team ID to update: "))
                team = self.find_team_by_id(team_id)
                if team:
                    break
                print("Team not found. Please enter a valid ID.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Show current team information
        print("\nCurrent team information:")
        print(team)
        
        # Update team information
        print("\nEnter new information (press Enter to keep current value):")
        
        # Update name with validation
        while True:
            new_name = input(f"Name [{team.name}]: ").strip()
            if not new_name:  # If Enter was pressed, keep current name
                break
            if len(new_name) > 0:  # If name is not empty, update it
                team.name = new_name
                break
            print("Team name cannot be empty. Please enter a valid name.")
        
        # Update team type
        while True:
            new_type = input(f"Type (boys/girls) [{team.team_type}]: ").lower()
            if not new_type:
                break
            if new_type in ["boys", "girls"]:
                team.team_type = new_type
                break
            print("Invalid team type. Please enter 'boys' or 'girls'.")
        
        # Update fee paid status
        while True:
            new_fee_paid = input(f"Fee paid (yes/no) [{'yes' if team.fee_paid else 'no'}]: ").lower()
            if not new_fee_paid:
                break
            if new_fee_paid in ["yes", "no"]:
                team.fee_paid = new_fee_paid == "yes"
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Update fee amount
        while True:
            new_fee = input(f"Fee amount [${team.fee:.2f}]: ")
            if not new_fee:
                break
            try:
                team.fee = float(new_fee)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # Update cancellation status
        if team.cancellation_date:
            print(f"Team is currently marked as cancelled on {team.cancellation_date}")
            while True:
                remove_cancellation = input("Remove cancellation? (yes/no): ").lower()
                if remove_cancellation in ["yes", "no"]:
                    if remove_cancellation == "yes":
                        team.cancellation_date = None
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            while True:
                cancel_team = input("Mark team as cancelled? (yes/no): ").lower()
                if cancel_team in ["yes", "no"]:
                    if cancel_team == "yes":
                        while True:
                            cancel_date = input("Enter cancellation date (YYYY-MM-DD) or press Enter for today: ")
                            if not cancel_date:
                                team.cancellation_date = datetime.date.today().strftime("%Y-%m-%d")
                                break
                            try:
                                # Validate date format
                                datetime.datetime.strptime(cancel_date, "%Y-%m-%d")
                                team.cancellation_date = cancel_date
                                break
                            except ValueError:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        print("\nTeam updated successfully!")
    
    def delete_team(self):
        """Delete a team from the list"""
        if not self.teams:
            print("\nNo teams available to delete.")
            return
        
        print("\n--- Delete Team ---")
        
        # Show available teams
        print("Available teams:")
        for team in self.teams:
            print(f"ID: {team.id}, Name: {team.name}")
        
        # Ask for team ID to delete
        while True:
            try:
                team_id = int(input("\nEnter team ID to delete: "))
                team = self.find_team_by_id(team_id)
                if team:
                    break
                print("Team not found. Please enter a valid ID.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete team '{team.name}'? (yes/no): ").lower()
        if confirm == "yes":
            self.teams.remove(team)
            print("Team deleted successfully!")
        else:
            print("Deletion cancelled.")
    
    def show_statistics(self):
        """Show statistics about teams"""
        if not self.teams:
            print("\nNo teams available.")
            return
        
        print("\n--- Team Statistics ---")
        
        # Count total teams
        total_teams = len(self.teams)
        print(f"Total teams: {total_teams}")
        
        # Count teams by type
        boys_teams = sum(1 for team in self.teams if team.team_type == "boys")
        girls_teams = sum(1 for team in self.teams if team.team_type == "girls")
        print(f"Boys teams: {boys_teams}")
        print(f"Girls teams: {girls_teams}")
        
        # Count paid teams
        paid_teams = sum(1 for team in self.teams if team.fee_paid)
        paid_percentage = (paid_teams / total_teams * 100) if total_teams > 0 else 0
        print(f"Teams that paid fee: {paid_teams} ({paid_percentage:.1f}%)")
        
        # Count cancelled teams
        cancelled_teams = sum(1 for team in self.teams if team.cancellation_date)
        print(f"Cancelled teams: {cancelled_teams}")
    
    def save_teams_to_file(self):
        """Save teams to a text file"""
        print("\n--- Save Teams to File ---")
        filename = input("Enter filename (default: teams.txt): ")
        if not filename:
            filename = "teams.txt"
        elif not filename.endswith(".txt"):
            filename += ".txt"
        
        try:
            # Convert each team to a dictionary and save as JSON
            teams_data = [team.to_dict() for team in self.teams]
            
            with open(filename, "w") as file:
                json.dump(teams_data, file, indent=2)
            
            print(f"Teams saved successfully to {filename}!")
        except Exception as e:
            print(f"Error saving teams to file: {e}")
    
    def load_teams_from_file(self):
        """Load teams from a text file"""
        print("\n--- Load Teams from File ---")
        
        # Show available text files in current directory
        txt_files = [f for f in os.listdir() if f.endswith('.txt')]
        if txt_files:
            print("Available text files:")
            for file in txt_files:
                print(f"- {file}")
        
        filename = input("Enter filename (default: teams.txt): ")
        if not filename:
            filename = "teams.txt"
        elif not filename.endswith(".txt"):
            filename += ".txt"
        
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"File {filename} not found.")
                return
            
            with open(filename, "r") as file:
                teams_data = json.load(file)
            
            # Clear existing teams list
            self.teams.clear()
            Team.next_id = 1  # Reset ID counter
            
            # Create Team objects from data
            for team_dict in teams_data:
                team = Team(team_dict["name"], team_dict["team_type"], team_dict["fee_paid"])
                
                # Set ID to match saved ID
                team._id = team_dict["id"]
                if team._id >= Team.next_id:
                    Team.next_id = team._id + 1
                
                # Set creation date
                team._date = datetime.datetime.strptime(team_dict["date"], "%Y-%m-%d").date()
                
                # Set fee amount
                team._fee = team_dict["fee"]
                
                # Set cancellation date if present
                team._cancellation_date = team_dict["cancellation_date"]
                
                # Add to teams list
                self.teams.append(team)
            
            print(f"Restored {len(self.teams)} teams from {filename}!")
        except Exception as e:
            print(f"Error restoring teams from file: {e}")
    
    def view_team_by_id(self):
        """View a specific team by ID"""
        if not self.teams:
            print("\nNo teams available.")
            return
        
        # Show available teams
        print("\nAvailable teams:")
        for team in self.teams:
            print(f"ID: {team.id}, Name: {team.name}")
        
        # # Ask for team ID
        try:
            team_id = int(input("\nEnter team ID to view: "))
            team = self.find_team_by_id(team_id)
            if team:
                self.display_team(team)
            else:
                print("Team not found.")
        except ValueError:
            print("Please enter a valid number.")
    
    def run(self):
        """Run the main program loop"""
        print("Welcome to the Hockey Team Management System!")
        
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.create_team()
            elif choice == "2":
                self.view_team_by_id()
            elif choice == "3":
                while True:
                    team_type = input("\nEnter team type to view (boys/girls): ").lower()
                    if team_type in ["boys", "girls"]:
                        self.display_teams_by_type(team_type)
                        break
                    print("Invalid team type. Please enter 'boys' or 'girls'.")
            elif choice == "4":
                self.display_all_teams()
            elif choice == "5":
                self.update_team()
            elif choice == "6":
                self.delete_team()
            elif choice == "7":
                self.show_statistics()
            elif choice == "8":
                self.save_teams_to_file()
            elif choice == "9":
                self.load_teams_from_file()
            elif choice == "0":
                print("\nThank you for using the Team Management System!")
                break
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")
