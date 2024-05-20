from dotenv import load_dotenv, find_dotenv
load_dotenv('.venv')



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

from langchain_openai import ChatOpenAI
# notions of human message, ai message and system essage
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chatllm = ChatOpenAI(temperature =0.5,   model="gpt-3.5-turbo", max_tokens=100)

# print(chatllm([
# SystemMessage(content="You're an expert on statiscal learning"),
# HumanMessage(content="Why the chronolgy of Statistical modeling since 1900 until 2022, 1 line maximum")
# ]))


#+++++++++++output parser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

class BulletPointOutputParser(BaseOutputParser):
    def parse(self, text: str):
        # Split the text by semicolon and strip each item to remove extra spaces
        bullet_points = [point.strip() for point in text.split(";")]

        # Format the bullet points with bullet point indicator
        formatted_bullet_points = "\n".join(f"• {point}" for point in bullet_points)
        return formatted_bullet_points
template = """
You're a assistant for teaching in high school. 
            When I got an input from user, you should return the  words that have the same root like it. 
            Word should be separated by ;
            """

human_template = "{texte}"
chat_prompt = ChatPromptTemplate.from_messages([
    ("system",template),
    ("human",human_template)
])

chain = chat_prompt | chatllm
# print("********************without output parser*******************")
# print(chain.invoke("region"))

print("********************without output parser*******************")
chain = chat_prompt | chatllm | BulletPointOutputParser()
print(chain.invoke("region"))