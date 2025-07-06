from langchain.memory import ConversationTokenBufferMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from src.Prompt import PromptClass
from dotenv import load_dotenv
load_dotenv()

class MemoryClass:
    def __init__(self,memorykey="chat_history",model="gpt-4o-mini"):
        self.memorykey = memorykey
        self.memory = []
        self.chatmodel = ChatOpenAI(model=model)

    def summary_chain(self,store_message):
        SystemPrompt = PromptClass().SystemPrompt
        Moods = PromptClass().MOODS
        prompt = ChatPromptTemplate.from_messages([
            ("system", SystemPrompt+"\nThis is a conversation memory between you and the user. Summarize it. The summary uses the first person pronoun “I” and extracts the key user information, such as the user's name, birthday, hobbies, etc., and returns it in the following format:\n Summary|Key user information\nFor example, user Zhang San greeted me, I replied politely, and then he asked me how to improve his nutritional status. I gave him some simple suggestions, and then he said goodbye and left. |Lola, birthday January 1, 1990"),
            ("user", "{input}")
        ])
        chain = prompt | self.chatmodel
        summary = chain.invoke({"input": store_message,"who_you_are":Moods["default"]["roloSet"]})
        return summary
    
    def get_memory(self):
        try:
            chat_message_history =RedisChatMessageHistory(
                url="redis://localhost:6379/0", session_id="session1"
            )
            # Summarize long chat histories
            store_message = chat_message_history.messages
            if len(store_message) > 10:
                str_message = ""
                for message in store_message:
                    str_message+=f"{type(message).__name__}: {message.content}"
                summary = self.summary_chain(str_message)
                chat_message_history.clear() #Clear existing conversation
                chat_message_history.add_message(summary) #Save summary
                print("After adding summary:",chat_message_history.messages)
                return chat_message_history
            else:
                print("go to next step")
                return chat_message_history
        except Exception as e:
            print(e)
            return None

    def set_memory(self):
        self.memory = ConversationTokenBufferMemory(
            llm=self.chatmodel,
            human_prefix="user",
            ai_prefix="Dr. Lin Yalin",
            memory_key=self.memorykey,
            output_key="output",
            return_messages=True,
            max_token_limit=1000,
            chat_memory=self.get_memory(),
        )
        return self.memory

    