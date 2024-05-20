from dotenv import load_dotenv, find_dotenv
load_dotenv('.venv')

question = "Who won the FIFA World Cup in the year 1994? "


from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
client = ChatOpenAI( temperature =0.5,   model="gpt-3.5-turbo")

prompt_template = PromptTemplate(
    input_variables=["Country"],
    template = "Give two city of {Country}"
)

print(prompt_template.format(Country='Burkina'))

#print(client.predict(prompt_template.format(Country='Burkina')))


### not working separely without chain
# print(client.predict(prompt_template=prompt_template, text=["India"]))
from langchain.chains import LLMChain
chain = LLMChain(llm=client, prompt=prompt_template)
chain.run("Cote d'Ivoire")