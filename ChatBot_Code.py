import pandas as pd

dataset = pd.read_csv('studenthelpdeskDATASET.csv')

cleaned_dataset = dataset[['Intent', 'Patterns', 'Responses']].dropna()

def chatbot_response(user_input, dataset):
    user_input = user_input.lower()  
    
    
    for index, row in dataset.iterrows():
        
        intent = row['Intent'].lower()
        if intent in user_input:  
            return row['Responses']  
    
    return "Sorry, I didn't understand that. Can you please try asking in a different way?"

def start_chatbot(dataset):
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input, dataset)
        print(f"Chatbot: {response}")

start_chatbot(cleaned_dataset)
