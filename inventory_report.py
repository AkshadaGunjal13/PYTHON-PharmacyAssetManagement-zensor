import sys
import os
project_root = "c:/Users/Sai/Desktop/PharmacyAssetManagement"

sys.path.append(project_root)
print("Updated Python path:", sys.path)

import pandas as pd
from db.models import get_assets

def generate_inventory_report():
    assets = get_assets()
    data = {
        "ID": [asset[0] for asset in assets],
        "Name": [asset[1] for asset in assets],
        "Category": [asset[2] for asset in assets],
        "Quantity": [asset[3] for asset in assets],
        "Expiry Date": [asset[4] for asset in assets],
        "Supplier": [asset[5] for asset in assets]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('inventory_report.csv', index=False)
    print("Inventory report generated: inventory_report.csv")

generate_inventory_report()
