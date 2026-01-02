from groq import Groq

def get_groq_client(api_key):
    return Groq(api_key=api_key)

def ask_groq(client, prompt):
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return res.choices[0].message.content
