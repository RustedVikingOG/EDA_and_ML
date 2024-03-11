from faker import Faker
import numpy as np
import pandas as pd
import random


fake = Faker()

def generate_data_telecom_churn(row_count):
    data = {'CustomerID': [],
            'Gender': [],
            'Age': [],
            'Tenure': [],
            'ServiceCalls': [],
            'MonthlyCharges': [],
            'TotalCharges': [],
            'Churn': []}
    
    for _ in range(row_count):
        data['CustomerID'].append(fake.uuid4())
        data['Gender'].append(random.choice(['Male', 'Female']))
        data['Age'].append(np.random.randint(18, 90))
        data['Tenure'].append(np.random.randint(0, 72))
        data['ServiceCalls'].append(np.random.randint(0, 10))
        data['MonthlyCharges'].append(round(random.uniform(29.99, 130.00), 2))
        # Simulate TotalCharges as a function of MonthlyCharges and Tenure
        data['TotalCharges'].append(round(data['MonthlyCharges'][-1] * data['Tenure'][-1], 2))
        data['Churn'].append(random.choice(['Yes', 'No']))

    # Introduce missing values and outliers
    for _ in range(row_count // 10):  # ~10% missing values
        column = random.choice(['Age', 'Tenure', 'MonthlyCharges'])
        data[column][random.randint(0, row_count-1)] = np.nan

    for _ in range(row_count // 20):  # ~5% outliers
        column = random.choice(['ServiceCalls', 'MonthlyCharges'])
        if column == 'ServiceCalls':
            data[column][random.randint(0, row_count-1)] = data[column][random.randint(0, row_count-1)] + 15
        else:
            data[column][random.randint(0, row_count-1)] = data[column][random.randint(0, row_count-1)] * 1.5 + 50
    
    return pd.DataFrame(data)


