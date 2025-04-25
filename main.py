import requests

def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact") #gets the fact
        response.raise_for_status() #checks for errors
        data = response.json() #converts the response to JSON
        return data["fact"] #returns only the fact from the response (dictionary)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

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

#only run the main() function if this file is being run directly — not if it's being imported somewhere else
if __name__ == "__main__":
    main()


