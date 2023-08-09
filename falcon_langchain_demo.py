from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import os
from dotenv import load_dotenv
load_dotenv()

huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token, 
                     repo_id=repo_id, 
                     model_kwargs={"temperature":0.6, "max_new_tokens":2000})

template = """
You are an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the users questions.
Question: {query}
Answer:"""

prompt = PromptTemplate(template=template, input_variables=["query"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "How many colors are there in a rainbow?"

print(llm_chain.run(question))