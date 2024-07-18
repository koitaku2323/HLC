from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize the Ollama LLM with the specific model
llm = Ollama(model="llama2")

# In-memory storage for chat history and titles
chats = {}
chat_titles = {}

# Function to load and combine contents of multiple PDFs
def load_multiple_pdfs(file_paths):
    combined_text = ""
    for path in file_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        # Combine text from all pages in the current PDF
        combined_text += "\n\n".join([doc.page_content for doc in docs]) + "\n\n"
    return combined_text

# Load and combine the PDFs initially if any
initial_file_paths = [
    "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/Ryan_Yee_Resume_2024_DA_DS_BA.pdf"
]
global full_text
full_text = load_multiple_pdfs(initial_file_paths)

@app.route('/')
def index():
    return render_template('index.html', chat_titles=chat_titles)

@app.route('/ask', methods=['POST'])
def ask():
    chat_id = request.form['chat_id']
    user_input = request.form['prompt']
    full_prompt = full_text + "\n\n" + user_input
    response = llm.invoke(full_prompt)

    if chat_id not in chats:
        chats[chat_id] = []
        title_prompt = f"Generate a short and concise title for this chat based on the prompt: '{user_input}'."
        title_response = llm.invoke(title_prompt).strip()
        chat_titles[chat_id] = title_response

    chats[chat_id].append({'role': 'user', 'content': user_input})
    chats[chat_id].append({'role': 'ai', 'content': response})

    return jsonify(response=response, title=chat_titles[chat_id], chat_id=chat_id)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        global full_text
        full_text = load_multiple_pdfs([file_path])
        return jsonify({"success": "File successfully uploaded and ingested"}), 200

@app.route('/chats', methods=['GET'])
def get_chats():
    return jsonify(chats=chats, chat_titles=chat_titles)

if __name__ == '__main__':
    app.run(debug=True)
