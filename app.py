import uvicorn
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Damilola",
        "description": "Zummit Africa customer relations ChatBot",
    },
    {
        "name": "Bot",
        "description": "Ask a question and get a response",
    },
]


# create a fastapi instance
app = FastAPI(title="Damilola", version="0.0.1", openapi_tags=tags_metadata)

# pydantic class
class TextInput(BaseModel):
    text: str


# create a bot instance
bot = ChatBot("Damilola", 
    preprocessors=[
    'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
    storage_adapter='chatterbot.storage.SQLStorageAdapter')


# train the bot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train( "./zummit.yml", "chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations")


# create a post route
@app.post("/bot", tags=["Bot"])
def get_response(text: TextInput):
    answer = bot.get_response(text.text)
    return {"Damilola": str(answer)}


# run the api
if __name__ == '__main__':
   
    uvicorn.run(app, host="0.0.0.0", port=8000)
