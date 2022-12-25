import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"
# Use the GPT-3 model
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Once upon a time, in a land far, far away, there was a princess who...",
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print(completion.choices[0].text)

