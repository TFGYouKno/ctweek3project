#Project Requirements
#Your task is to develop a Contact Management System with the following features:

#User Interface (UI):
#Create a user-friendly command-line interface (CLI) for the Contact Management System.
#Display a welcoming message and provide a menu with the following options:
#Menu:
#Add a new contact
#Edit an existing contact
#Delete a contact
#Search for a contact
#Display all contacts
#Export contacts to a text file
#Import contacts from a text file
#Quit 

#Contact Data Storage:
#Use nested dictionaries as the main data structure for storing contact information.
#Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#Store contact details within the inner dictionary, including:
#Name
#Phone number
#Email address
#Additional information (e.g., address, notes).


#Menu Actions:
#Implement the following actions in response to menu selections:
#Adding a new contact with all relevant details.
#Editing an existing contact's information (name, phone number, email, etc.).
#Deleting a contact by searching for their unique identifier.
#Searching for a contact by their unique identifier and displaying their details.
#Displaying a list of all contacts with their unique identifiers.
#Exporting contacts to a text file in a structured format.
#Importing contacts from a text file and adding them to the system.


#User Interaction:
#Utilize input() to enable users to select menu options and provide contact details.
#Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

#Error Handling:
#Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

#Optional Bonus Points
#Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
#Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
#Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
#Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
#Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.
