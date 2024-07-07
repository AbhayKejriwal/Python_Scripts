import os
import subprocess

def execute_command_from_directory(command, directory):
    try:
        # Change directory to the specified directory
        os.chdir(directory)
        
        # Execute the command in the terminal
        subprocess.run(command, shell=True)
        
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage:
if __name__ == "__main__":
    # Command to execute
    command_to_execute = "java -jar RemoteControlPC.jar"  # Replace this with your desired command
    
    # Directory from which to execute the command
    # Replace this with your desired directory
    target_directory = r"C:\\Users\\Abhay\\Documents\\Apps & Data\\Remote-Control-PC\\RemoteControlPC-JavaFXML\\dist"  
    
    # Execute the command from the specified directory
    execute_command_from_directory(command_to_execute, target_directory)
