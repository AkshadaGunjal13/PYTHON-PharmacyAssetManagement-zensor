import sys
import os

project_root = "c:/Users/Sai/Desktop/PharmacyAssetManagement"

sys.path.append(project_root)

print("Updated Python path:", sys.path)

import pandas as pd
from db.models import get_assets
from datetime import datetime

def generate_expiry_report():
    today = datetime.today().date()
    assets = get_assets()
    
    # Filter assets with expiry date before today
    expired_assets = [asset for asset in assets if asset[4] < str(today)]
    
    if expired_assets:
        data = {
            "ID": [asset[0] for asset in expired_assets],
            "Name": [asset[1] for asset in expired_assets],
            "Category": [asset[2] for asset in expired_assets],
            "Expiry Date": [asset[4] for asset in expired_assets],
            "Supplier": [asset[5] for asset in expired_assets]
        }
        
        df = pd.DataFrame(data)
        df.to_csv('expiry_report.csv', index=False)
        print("Expired assets report generated: expiry_report.csv")
    else:
        print("No expired assets found.")

generate_expiry_report()
