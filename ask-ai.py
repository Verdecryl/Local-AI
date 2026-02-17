from google import genai

def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File '{filename}' written successfully.")
    except OSError as e:
        print(f"Error writing file '{filename}': {e}")


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
        return None

inn="C:/Users/Adrian/Desktop/question.txt"
out="C:/Users/Adrian/Desktop/answer.txt"

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
#1: AIzaSyA-DZIAHeiVFsTGbbycRAhBoAsJm0mceBY
#2: AIzaSyBDNODMwvvcVpue2mM6mObbLxoAcyM89M8
#3: AIzaSyCjJasTN28oiJrYVF7WCz3-JPFsNKzsI38
#4: AIzaSyC74HEVtJ_EA4zugwUs-LI06RUQrDLJ9tk
#5: AIzaSyArISjICT8UPQjtTnI9sGbzOVl3orOcw8M
GEMINI_API_KEY = "AIzaSyA-DZIAHeiVFsTGbbycRAhBoAsJm0mceBY"

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=read_file(inn)
)

write_file(out, response.text)