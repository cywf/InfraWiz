import os
import subprocess
import time
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_user_input():
    print("Hi! I'm InfraWiz, your Infrastructure Management Wizard.")
    print("What can I help you with today?")
    user_input = input("Enter your request: ")
    return user_input

def ask_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def execute_bash_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

def main():
    user_input = get_user_input()
    prompt = f"The user wants to: {user_input}. Provide a list of required packages, configurations, and setup steps."
    ai_response = ask_openai(prompt)

    print("\nInfraWiz Analysis:\n")
    print(ai_response)

    confirmation = input("\nDo you want to proceed with the setup as described above? (yes/no): ")

    if confirmation.lower() == "yes":
        print("\nStarting setup...\n")
        commands = ai_response.split("\n")
        for command in commands:
            if command.strip():
                print(f"Executing: {command}")
                stdout, stderr = execute_bash_command(command)
                if stdout:
                    print(f"Output: {stdout}")
                if stderr:
                    print(f"Error: {stderr}")
                time.sleep(1)  # Adding a small delay between commands
        print("\nSetup completed successfully!")
    else:
        print("\nSetup aborted by user.")

if __name__ == "__main__":
    main()
