# Pharmacy Asset Management

Pharmacy Asset Management is a comprehensive tool for managing the inventory and assets of a pharmacy efficiently. It helps ensure optimal stock levels, minimizes losses due to expired items, and provides quick access to inventory data for streamlined operations.

---

## Features

### 🏥 Asset Management
- **Add Assets:** Input new items into the system with details like name, category, quantity, expiry date, and supplier.
- **Update Assets:** Modify existing inventory details to maintain accuracy.
- **Delete Assets:** Remove obsolete or unused inventory records.

### 📋 Reporting
- **Expiry Report Generation:** Automatically generate detailed reports of expired assets in CSV format for quick review and action.

### 🗂 Database Management
- **SQLite Database:** Lightweight and efficient storage solution for all asset data.
- **Table Auto-Creation:** Automatically sets up the database schema upon initialization.

### 💡 Simplicity and Automation
- Clean, modular code for easy maintenance.
- Automates key operations like filtering expired items and report generation.

---

## How It Works

1. **Database Initialization**
   The database is initialized with a table (`assets`) for storing pharmacy inventory details.

2. **CRUD Operations**
   - `add_asset`: Add new inventory items.
   - `get_assets`: Fetch a list of all items in the inventory.
   - `update_asset`: Modify details of an existing item.
   - `delete_asset`: Remove an item from the inventory.

3. **Expiry Reporting**
   A script scans for expired items in the inventory and creates a CSV report for easy sharing and documentation.

---

## Installation Guide

### Prerequisites
- Python 3.7 or higher
- SQLite (pre-installed with Python)
- Pandas library (`pip install pandas`)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pharmacy-asset-management.git
   cd pharmacy-asset-management
