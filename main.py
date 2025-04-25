import requests

#gets cat facts from API
def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact") #gets the fact
        response.raise_for_status() #checks for errors
        data = response.json() #converts the response to JSON
        return data["fact"] #returns only the fact from the response (dictionary)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

#saves facts into text file
def save_to_file(facts, filename = "cat_facts.txt"):
    try:
        with open(filename, "w", encoding = "utf-8") as file:
            for i in facts:
                file.write(i + "\n")
            print(f"Saved {len(facts)} cat facts to file: {filename}")
    except Exception as e:
        print(f"Error occurred while saving {filename}: {e}")

def main():
    print("Welcome to Cat Fact Generator!")

    #user inputs a number of facts
    try:
        amount = int(input("Please enter how many facts would you like to know: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    facts = [] #empty list for facts

    #fills the list with requested amount of facts
    for i in range(amount):
        facts.append(get_cat_fact())

    print("\nHere are your cat facts:\n")
    for i in facts:
        print(i)
    print()

    #asks user if to save to files
    do_save = input("Would you like to save the facts into file? [yes/no]")
    if do_save in ["yes", "y"]:
        save_to_file(facts)

#only run the main() function if this file is being run directly — not if it's being imported somewhere else
#always use 'main() guard' to prevent unwanted run while imported
if __name__ == "__main__":
    main()


