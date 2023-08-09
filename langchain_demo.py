from langchain import PromptTemplate
from langchain import HuggingFaceHub, LLMChain

# access huggingface token from .env file
import os
from dotenv import load_dotenv
load_dotenv()

huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

# user question
question = "How many colors are there in a rainbow?"

# initialize Hub LLM
hub_llm = HuggingFaceHub(
    repo_id='tiiuae/falcon-7b-instruct',
    model_kwargs={'temperature':0.6}
)

# create prompt template > LLM chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)

# ask the user question about NFL 2010
print(llm_chain.run(question))