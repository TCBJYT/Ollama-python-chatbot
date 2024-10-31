from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
import pickle
import json
# Vector import
from langchain_core.vectorstores import InMemoryVectorStore



#embedding or something
template = """
Conversation history: {context}
Name(User): {name}
Question: {question}
About you(The AI): {AI_introduction}
"""

model = OllamaLLM(model="llama3", stream=True)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

    
def handle_conversation():
    context = ""
    nameuser = input("What name would you like to be called?")
    AI_introduction = input("Explain your AI: ")
    print("Type in the AI on what you want: ")
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke(
                {
                    "AI_introduction": AI_introduction, 
                    "name": nameuser,
                    "context": context, 
                    "question": user_input
                }
            )
        
        print("Bot: ", result)
        
        context += f"\nUser: {user_input}\nAI: {result}"

#Test this if it works, i have no more storage :cry:
    with open('data.pickle', 'wb') as file:
        pickle.dump(context, file)


if __name__ == "__main__":

    handle_conversation()
