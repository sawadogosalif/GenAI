
import warnings
warnings.filterwarnings("ignore")


from dotenv import load_dotenv, find_dotenv
load_dotenv('.venv')
import openai

# API officia OpenAI
# get started https://platform.openai.com/docs/guides/text-generation/chat-completions-api
# what is a token ? pricing #https://openai.com/pricing
# Prompt engineering https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  seed=1,
  max_tokens=100,
  messages=[
    {"role": "system", "content": "You're a specialist in historical events for Burkina Faso."},
    {"role": "user", "content": "Why Thomas Sankara dead too young in 2 lines maximum? "}
  ]
)

print(completion.choices[0].message)

## =================================Use the wrapper langchain
from langchain_openai import ChatOpenAI
# temperature =0, safe
# temperature =2 very creative but might create some wrong output
client = ChatOpenAI( temperature =0.5,   model="gpt-3.5-turbo")
input ="what is the previous name of Burkina before THomas ankara change it"
print(client.invoke(input))


########################################
embedding = openai.Embedding.create(
    input="What's in a name? That which we call a rose by any other name would smell as sweet", model="text-embedding-ada-002"
)["data"]
[0]
["embedding"]
print(len(embedding))
print(embedding)


### =================================Use Hugginface

from langchain import HuggingFaceHub


# open source
question = "Who won the FIFA World Cup in the year 1994? "
llm = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={"temperature": 0.5})
print(llm.invoke("Can  you give a city in Burkina"))
