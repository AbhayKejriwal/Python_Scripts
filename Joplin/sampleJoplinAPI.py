import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

def execute(command):
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, error = process.communicate()
  return output.decode(), error.decode()

def create_new_note_in_joplin(token, note):
  command = f'curl http://localhost:41184/notes?token={token} --data "{{\\"title\\": \\"{note['title']}\\", \\"body\\": \\"{note['body']}\\"}}"'
  
  return execute(command)

#driver code
if __name__ == "__main__":
  note = {
    "title": "test with api",
    "body": "Some text"
  }
  print(create_new_note_in_joplin(token, note))