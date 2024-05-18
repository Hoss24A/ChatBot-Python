import openai

# Replace 'your_secre_api_key_here' with your actual OpenAI API key
openai.api_key = 'your_secret_api_key_here'

def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "gpt-3.5-turbo" if available for GPT-4 equivalent
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to the GPT-based Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()