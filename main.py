import requests
import os

# Your OpenAI API Keys - replace with your own keys
api_keys = ["your-api-key1", "your-api-key2", "your-api-key3", "your-api-key4"]

# Define the name and project for your prompt
name = "人文学"
project = "接力赛跑"

# The text prompt you want to generate a response
prompt = f"你是一名阳光积极向上的{name}院学生，你的学校即将要开运动会，请书写一份通讯稿，为{name}运动员加油。项目：{project}。字数：120字左右。要求：积极上进，富有文采，带有运动项目特色。参考样例：（输出请勿与样例重复）"

# Define the URL for the OpenAI API
url = "https://api.openai.com/v1/chat/completions"

# Define the data to be sent to the API
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 1200,
    "temperature": 0.5,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Loop to generate responses
for i in range(1, 2):
    # Select an API key
    api_key = api_keys[i % len(api_keys)]

    # The headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the response
        generated_text = response.json()['choices'][0]['message']['content']
        print(str(i) + ' request complete')

        # Save the text to a file with a numbered name
        with open(f'output/{name}院_{project}_{i}.txt', 'w', encoding='utf-8') as file:
            file.write(generated_text)
    else:
        # Handle the error
        print(f"Request failed with status code {response.status_code} for iteration {i}")
