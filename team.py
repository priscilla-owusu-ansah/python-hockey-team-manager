import datetime # Handles date and time-related operations, such as automatically setting creation dates

# Class for Team
class Team:
    # Class variable to keep track of the next available ID (track or assign unique ID)
    next_id = 1
    
    def __init__(self, name, team_type, fee_paid=False):
        # Private instance variables 
        self.__id = Team.next_id             # Auto-generate ID
        Team.next_id += 1                    # Increment the class-level ID counter for the next team
        self.__date = datetime.date.today()  # Auto-set registration date
        self.__name = name                   # Store the team's name
        self.__team_type = team_type         # Store whether the team is for Boys or Girls
        self.__fee_paid = fee_paid           # Boolean value for whether the fee has been paid
        self.__fee = 50                      # Default fee amount set to 50
        self.__cancellation_date = None      # Initially set to None, indicating the team has not canceled
    
    # Getter and Setter methods (properties) to access private instance variables
    @property
    def id(self):
        """Returns the teams's unique ID."""
        return self.__id
    
    @property
    def date(self):
        """Returns the team's creation date."""
        return self.__date
    
    @property
    def name(self):
        """Gets the team's name."""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Sets a team's new name."""
        self.__name = value
    
    @property
    def team_type(self):
        """Gets the type of team (Boys/Girls)."""
        return self.__team_type
    
    @team_type.setter
    def team_type(self, value):
        self.__team_type = value
    
    @property
    def fee_paid(self):
        """Checks if the team has paid."""
        return self.__fee_paid
    
    @fee_paid.setter
    def fee_paid(self, value):
        """Updates the fee payment status of the team."""
        self.__fee_paid = value
    
    @property
    def fee(self):
        """Gets the fee amount."""
        return self.__fee
    
    @fee.setter
    def fee(self, value):
        """Updates the fee amount."""
        self.__fee = value
    
    @property
    def cancellation_date(self):
        """Gets the cancellation date."""
        return self.__cancellation_date
    
    @cancellation_date.setter
    def cancellation_date(self, value):
        """Sets the cancellation date if the team withdraws.""" 
        self.__cancellation_date = value
    
    def __str__(self):
        # Format the creation date in YYYY-MM-DD format
        formatted_date = self.date.strftime("%Y-%m-%d") # Format the creation date
        
        # Format cancellation date if it exists
        cancellation_info = ""
        if self.__cancellation_date:
            cancellation_info = f", Cancelled on: {self.__cancellation_date}"
        
        # Return a formatted string representation of the team
        return (f"ID: {self.__id}, Created: {formatted_date}, Name: {self.__name}, "
                f"Type: {self.__team_type}, Fee Paid: {self.__fee_paid}, "
                f"Fee Amount: ${self.__fee:.2f}{cancellation_info}")
    
    def to_dict(self):
        # Convert team object to dictionary for file storage
        cancellation_date_str = None
        if self.__cancellation_date:
            cancellation_date_str = self.__cancellation_date.strftime("%Y-%m-%d")
            
        return {
            "id": self.__id,
            "date": self.__date.strftime("%Y-%m-%d"), # Convert date to string format
            "name": self.__name,
            "team_type": self.__team_type,
            "fee_paid": self.__fee_paid,
            "fee": self.__fee,
            "cancellation_date": cancellation_date_str
        }