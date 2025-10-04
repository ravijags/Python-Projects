import pandas as pd

#Read data from CSV
csv_data = pd.read_csv("sample.csv")
print("CSV Data:")
print(csv_data)

#Write to Excel
csv_data.to_excel("data_output.xlsx",index=False)

#Read back from Excel
excel_data = pd.read_excel("data_output.xlsx")
print("\nExcel Data:")
print(excel_data)

# How It Works:
# Reads sample.csv 
# Converts and saves it as an Excel 
# Reads the Excel file to confirm successful write
