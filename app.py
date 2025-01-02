import pandas as pd
import json

# Load the Excel file
file_path = 'resources.xlsx'
df = pd.read_excel(file_path)

# Extract unique resource groups
resource_groups = df['RESOURCE_GROUP'].unique().tolist()

# Group resources by resource group without using apply
grouped_resources = df.groupby('RESOURCE_GROUP').apply(
    lambda x: x[['RESOURCE_DESC', 'RESOURCE_CODE', 'RES_SPECIFICATION', 'PER_HOUR_RATE', 'MAX_HR_OF_BOOKING']].to_dict('records')
).to_dict()

resource_groups_json = json.dumps(resource_groups)
grouped_resources_json = json.dumps(grouped_resources)

