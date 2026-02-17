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
#Path to in and out files
inn="Your Path To question.txt"
out="Your Path To answer.txt"

#Here goes the GEMINI API KEY
GEMINI_API_KEY = "Your-API-KEY"

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=read_file(inn)
)


write_file(out, response.text)
