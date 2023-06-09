from flask import Flask, render_template, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the uploaded file from the request
    uploaded_file1 = request.files['log_file']
    uploaded_file2 = request.files['srmtctl_log_file']
    
    # Save the file to a temporary location
    file_path1 = 'temp/' + uploaded_file1.filename
    uploaded_file1.save(file_path1)

    file_path2 = 'temp/' + uploaded_file2.filename
    uploaded_file2.save(file_path2)
    
    # Process the file using an external Python script
    # Replace "external_script.py" with the name of your script
    subprocess.run(['python', 'NCIRSALTGUI.py', file_path1, file_path2])
    
    # Define the path for the processed result
    result_file = 'temp/processed_result.txt'
    
    # Return the processed result as a downloadable file
    return send_file(result_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
