import openai
import json
import os
class ChatGptAnswer():
    def __init__(self,model,appkey):
        self.model=model
        openai.api_key = appkey

    def ask_gpt(self,content):
        rsp = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role":"user","content":content}
            ]
        )
        return rsp.get("choices")[0]["message"]["content"]
