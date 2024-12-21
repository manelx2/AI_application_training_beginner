#setting api env 
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
import os
api_key = os.getenv("OPENAI_API_KEY")  
client = OpenAI(api_key=api_key)
#defining model and client
conversation = [{"role": "system", "content": "You are a parisian tourist guide"}]
user_msgs = ["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?", "Where is the Arc de Triomphe?","What are the must-see artworks at the Louvre Museum?"]

for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    conversation.append(user_dict)
    
    # Create the API request
    try:
        response = client.chat.completions.create(
            model=model,
            messages=conversation,
            max_tokens=100,
            temperature=0
        )
        
        # Convert the assistant's message to a dict and append to messages
        assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
        conversation.append(assistant_dict)
        print("Assistant: ", response.choices[0].message.content, "\n")
    except openai.error.RateLimitError as e:
        print(f"Rate limit error: {e}")
        break