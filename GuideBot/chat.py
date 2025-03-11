from setup import Gemini_api_key
import google.generativeai as genai 
import chainlit as cl


genai.configure(api_key=Gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

#staters
@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Improve my study habits",
            message="I want to improve my study habits. Can you suggest a personalized study routine based on my schedule?",
            icon="/public/idea.svg",
        ),
        cl.Starter(
            label="Explain python",
            message="Can you explain python programming language and how to code with python? Assume I have no prior knowledge.",
            icon="/public/python.svg",
        ),
        cl.Starter(
            label="Help with exam preparation",
            message="I have an upcoming exam. Can you help me create a study plan and suggest revision strategies?",
            icon="/public/note.svg",
        ),
        cl.Starter(
            label="Math problem solver",
            message="Can you solve this math problem for me and explain it step by step? (2x + 5 = 15)",
            icon="/public/math.svg",
        ),
        cl.Starter(
            label="Programming help",
            message="I’m learning Python. Can you teach me the basics of functions with examples?",
            icon="/public/code.svg",
        ),
        cl.Starter(
            label="Essay writing tips",
            message="I need help writing an essay on climate change. Can you suggest a structure and key points?",
            icon="/public/write.svg",
        ),
        cl.Starter(
            label="Memorization techniques",
            message="I struggle with memorization. Can you suggest some memory techniques for learning historical dates?",
            icon="/public/memory.svg",
        ),
        cl.Starter(
            label="Learning a new language",
            message="I want to learn Spanish. Can you suggest a daily practice routine and essential phrases to start with?",
            icon="/public/language.svg",
        )
    ]




@cl.on_message
async def handle_message(message):
    """Handles user messages and generates responses from Gemini."""
    
    # Exit conditions
    exit_phrases = ["exit", "quit", "bye", "done", "got it", "ok"]
    if message.content.lower() in exit_phrases:
        await cl.Message(content="Chat ended.").send()
        return
    
    # Get response from Gemini
    response = model.generate_content(message.content)
    
    # Send response to Chainlit UI
    await cl.Message(content=response.text).send()