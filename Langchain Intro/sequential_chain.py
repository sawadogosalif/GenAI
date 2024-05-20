from dotenv import load_dotenv, find_dotenv
load_dotenv('.venv')



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

from langchain_openai import ChatOpenAI
gpt3_5 = ChatOpenAI( temperature =0.5,   model="gpt-3.5-turbo")

##### BASIC ###################################

president_template = PromptTemplate(
    input_variables=["Country"],
    template = "Tell me the  first President 'name of {Country}"
)
president_chain = LLMChain(llm=gpt3_5, prompt=president_template)
# print(president_chain.run(["Burkina faso"]))

datedeath_template = PromptTemplate(
    input_variables=["President"],
    template="Tell the  death date of the President {President}"
)
datedeath_chain = LLMChain(llm=gpt3_5, prompt=datedeath_template)
# print(datedeath_chain.run(["Burkina faso"]))


chain = SimpleSequentialChain(chains=[president_chain, datedeath_chain])

# print(chain.run(["Burkina Faso", "Cote d'Ivoire"]))

######## ADVANCED ################################
president_chain = LLMChain(llm=gpt3_5, prompt= president_template, output_key='President')
datedeath_chain = LLMChain(llm=gpt3_5, prompt=datedeath_template, output_key="datedeath")
chain = SequentialChain(chains=[president_chain, datedeath_chain],
                    input_variables=["Country"],
                    output_variables=["President", "datedeath"]
                    )

print(chain({"Country": "Burkina Faso"}))