from setup import Gemini_api_key
import google.generativeai as genai  

# Configure the API key
genai.configure(api_key=Gemini_api_key)

# Initialize the Gemini AI chat model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Start the chat loop
while True:
    try:
        user_input = input("You: ").strip()  
        if user_input.lower() in ["exit", "quit", "bye", "done", "got it", "ok"]:  
            print("Chat ended.")
            break

        response = model.generate_content(user_input)  # Corrected method
        print("Bot:", response.text)

    except Exception as e:
        print("Error:", str(e))
        break
