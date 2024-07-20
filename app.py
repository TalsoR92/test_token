from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/create-file', methods=['POST'])
def create_file():
    data = request.get_json()
    file_name = data.get('fileName')

    if not file_name:
        return jsonify({'message': 'File name is required!'}), 400

    # Create the file
    with open(file_name, 'w') as file:
        file.write('')

    # Add the file to git and push to GitHub
    subprocess.run(['git', 'add', file_name])
    subprocess.run(['git', 'commit', '-m', f'Add {file_name}'])
    subprocess.run(['git', 'push'])

    return jsonify({'message': f'File {file_name} created and pushed to GitHub!'})

if __name__ == '__main__':
    app.run(debug=True)
