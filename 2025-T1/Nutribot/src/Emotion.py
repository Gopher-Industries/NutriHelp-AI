from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class EmotionClass:
    def __init__(self,model="gpt-4o-mini"):
        self.chat = None
        self.Emotion = None
        self.chatmodel = ChatOpenAI(model=model)

    def Emotion_Sensing(self, input):
        # Handle input length 
        original_input = input
        if len(input) > 100:
            input = input[:100]
            print(f"Input is too long, only the first 100 characters will be used. Original length: {len(original_input)}")
        
        print(f"Processing input: {input}")
        
        # Define JSON schema
        json_schema = {
            "title": "emotions",
            "description": "feedback emotions",
            "type": "object",
            "properties": {
                "input": {
                    "type": "string",
                    "description": "the user input",
                    "minLength": 1,
                    "maxLength": 100
                },
                "output": {
                    "type": "string",
                    "description": "the emotion of the user input",
                    "enum": ["depressed", "friendly", "default", "angry", "cheerful"]
                }
            },
            "required": ["input", "output"],
        }
        llm = self.chatmodel.with_structured_output(json_schema)
        
        prompt_emotion = """
        Based on the user's input, determine the user's emotion and respond according to the following rules:
            1.Content with negative emotion, only return 'depressed', without other content such as suppressed or melancholic statements.
            2.Content with positive emotion, only return 'friendly', without other content such as friendly or polite statements.
            3.Content with neutral emotion, only return 'default', without other content.
            4.Content with angry emotion, only return 'angry', without other content such as angry, abusive, stupid, or hateful statements.
            5.Content indicating very happy emotion, only return 'cheerful', without other content such as happy, ecstatic, excited, or praise statements. 
            User input content:{input}
        """
        
        # Simulate Emotion Chain
        EmotionChain = ChatPromptTemplate.from_messages([("system", prompt_emotion), ("user", input)]) | llm
        
        try:
            if not input.strip():
                print("Empty input received")
                return None
            
            if EmotionChain is not None:
                result = EmotionChain.invoke({"input": input})
                print(f"API response: {result}")
            else:
                raise ValueError("EmotionChain is not properly instantiated.")
            
            self.Emotion = result["output"]
            return result["output"]
        except Exception as e:
            print(f"Error in Emotion_Sensing: {str(e)}")
            return None
