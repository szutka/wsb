import openai

OPENAI_API_KEY = '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'

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_article(prompt: object) -> object:
    client = openai.OpenAI()

    response = client.chat.completions.create( #trzeba o tym pamietac generalnie, bo jest nowa metoda na api, tu jest poprawna
        messages=[
            {"role": "system", "content": "blah blah blah!"},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4"
    )
    return response.choices[0].message.content

prompt = "Napisz artykuł nt:"
article = generate_article(prompt)
print(article)