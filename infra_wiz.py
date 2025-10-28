import os
import subprocess
import time
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def get_user_input():
    print("Hi! I'm InfraWiz, your Infrastructure Management Wizard.")
    print("What can I help you with today?")
    user_input = input("Enter your request: ")
    return user_input

def ask_openai(prompt, client):
    """
    Ask OpenAI for infrastructure recommendations.
    Returns a response from the AI model.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are InfraWiz, an expert infrastructure management assistant. Provide clear, actionable advice for server setup and configuration. List specific packages, commands, or configuration steps."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with OpenAI: {str(e)}"

def execute_bash_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

def main():
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it by running: export OPENAI_API_KEY='your-api-key'")
        print("Or create a .env file with: OPENAI_API_KEY=your-api-key")
        sys.exit(1)
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    user_input = get_user_input()
    prompt = f"The user wants to: {user_input}. Provide a list of required packages, configurations, and setup steps for their infrastructure."
    
    print("\nAnalyzing your request with InfraWiz AI...\n")
    ai_response = ask_openai(prompt, client)

    print("InfraWiz Analysis:\n")
    print(ai_response)
    print("\n" + "="*60)
    
    print("\nNote: The above recommendations are suggestions from AI.")
    print("Review them carefully before executing any commands.")
    print("\nWARNING: Automatic command execution is disabled for safety.")
    print("Please review the recommendations and execute commands manually.")
    
    # Disabled automatic execution for safety
    # confirmation = input("\nDo you want to proceed with the setup as described above? (yes/no): ")
    # 
    # if confirmation.lower() == "yes":
    #     print("\nStarting setup...\n")
    #     commands = ai_response.split("\n")
    #     for command in commands:
    #         if command.strip():
    #             print(f"Executing: {command}")
    #             stdout, stderr = execute_bash_command(command)
    #             if stdout:
    #                 print(f"Output: {stdout}")
    #             if stderr:
    #                 print(f"Error: {stderr}")
    #             time.sleep(1)
    #     print("\nSetup completed successfully!")
    # else:
    #     print("\nSetup aborted by user.")

if __name__ == "__main__":
    main()
