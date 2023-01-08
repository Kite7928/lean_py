# import openai
#
# openai.api_key = "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"
#
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="谁是世界上最有钱的人？",
#   temperature=0,
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#
# )
# print(response)


def talk(message:str):
    return "Talk " + message
def main():
    print(talk("Hello World"))
if __name__ == "__main__":
    main()
