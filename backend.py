import pandas as pd
from flask import Flask, request, send_file
import os

app = Flask(__name__)

def get_graph():
    print("Getting graph...")
    image_path = '/Users/harshitgupta/Desktop/vs /VS-Data-Den/graphs/rm_sales_graph/50000002.0_sales_plot.png'
    with open(image_path, 'rb') as f:
        image_data = f.read()
    print("Graph loaded.")
    return image_data

def get_csv():
    print("Getting CSV...")
    csv_path = 'rm_dataset_filtered.csv'
    df = pd.read_csv(csv_path)
    print("CSV loaded.")
    return df

@app.route('/input_csv', methods=['POST'])
def upload_csv():
    print("Received request...")
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    if not file.filename.endswith('.csv'):
        return 'Invalid file format. Please upload a CSV file.'

    print("Saving uploaded file...")
    file.save('inference.csv')

    print("Reading uploaded CSV...")
    df = pd.read_csv('inference.csv')

    required_columns = ['masterstyle', 'choice_id','regional_master_cd','on_floor','off_floor','drop_group','drop_rank']
    if not all(col in df.columns for col in required_columns):
        return f'CSV file must contain columns: {required_columns}'
    
    print("Generating graph and CSV...")
    graph = get_graph()
    csv = get_csv()

    # Construct the path for the temporary CSV file
    temp_csv_path = os.path.join(os.path.dirname(__file__), 'temp.csv')
    csv.to_csv(temp_csv_path, index=False)

    print("Sending response...")
    # send_file(graph, mimetype='image/png')
    
    return send_file(temp_csv_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
