import pandas as pd



def get_graph():
    image_path = '/Users/harshitgupta/Desktop/vs /VS-Data-Den/graphs/rm_sales_graph/50000002.0_sales_plot.png'
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return image_data

def get_csv():
    csv_path = 'rm_dataset_filtered.csv'
    df = pd.read_csv(csv_path)
    return df

