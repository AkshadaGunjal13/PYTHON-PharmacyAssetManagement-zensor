import matplotlib.pyplot as plt

# Sample data: Asset categories and their corresponding quantities
categories = ['Medicine', 'Syringes', 'PPE', 'Vitamins', 'Bandages']
quantities = [150, 200, 50, 120, 180]

def plot_asset_data(categories, quantities):
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, quantities, color='skyblue')
    
    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Quantity')
    plt.title('Asset Quantity by Category')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    plot_asset_data(categories, quantities)
