from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
from pydantic import BaseModel, Field, EmailStr
load_dotenv()

model = ChatOpenAI()

#Schema for structured output
class Review(TypedDict):

    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""This place has hands down the best brunch in town! The avocado toast with poached eggs was 
incredible, and their freshly squeezed orange juice was the perfect complement. The restaurant has such a bright, 
cheerful atmosphere with friendly staff who make you feel right at home.
 I've been here three weekends in a row and plan to keep coming back. Don't miss their homemade pastries - they're to die for!""") 

print(result)

print(result['summary'])
print(result['sentiment'])