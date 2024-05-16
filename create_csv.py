import pandas as pd
from faker import Faker

fake = Faker()

num_rows = 100

headers = ['masterstyle', 'choice_id', 'regional_master_cd', 'on_floor', 'off_floor', 'drop_group', 'drop_rank']

def generate_row():
    return {
        'masterstyle': fake.word(),
        'choice_id': fake.random_int(),
        'regional_master_cd': fake.random_int(),
        'on_floor': fake.random_int(),
        'off_floor': fake.random_int(),
        'drop_group': fake.word(),
        'drop_rank': fake.random_int()
    }

data = [generate_row() for _ in range(num_rows)]

df = pd.DataFrame(data)

df.to_csv('sample_data.csv', index=False)

print("CSV file generated successfully.")
