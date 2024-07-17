import csv

# Define the data in a structured format
data = [
    ["Service", "NameID", "Total INQs", "AE Rate (%)", "ENR Rate (%)", "Current Enrollees Start-End",
     "CS Rate (%)", "IC %", "Student IC%", "ABS-MU-VAC", "# First Time Drops", "Avg Hours Till Drop",
     "Drops # 0-30", "Drops % 0-30", "Drops # 31-50", "Drops % 31-50", "Total Instr Hours",
     "Avg Hrs Per Wk New ENR", "Avg Hrs Per Wk Existing Students", "Student Focused School Visits",
     "Event Focused School Visits*", "Merch Visits*", "Bulk Loans Amount", "Bulk Payment % Of Total",
     "Refunds % Of Total", "Total Charges", "Total Payments"],
    ["LC Combined = LC + LS + L1", "Yee and Chang-Cupertino,CA-Y24", 64, "36%", "60%", "16 - 26", "22%", "76%", "0%",
     "0 - 0 - 31", 6, 105, 0, "0%", 2, "33%", 1685, 4.68, 4.85, 0, 0, 0, "$113,082", "83%", "0.00%", "$113,082", "$122,262"],
    ["EP Combined = S1 + A1", "Yee and Chang-Cupertino,CA-Y24", 14, "29%", "50%", "1 - 1", "14%", "0%", "0%",
     "0 - 0 - 160", 1, 46, 0, "0%", 1, "100%", 49, 2.00, 2.00, 0, 0, 0, "$4,684", "0%", "0.00%", "$4,684", "$3,345"],
    ["E1", "Yee and Chang-Cupertino,CA-Y24", 3, "33%", "0%", "0 - 0", "0%", "0%", "0%", "0 - 0 - 0", 0, 0, 0, "0%", 0, "0%",
     0, 0.00, 0.00, 0, 0, 0, "$0", "0%", "0.00%", "$0", "$0"],
    ["ST", "Yee and Chang-Cupertino,CA-Y24", 14, "N/A", "N/A", "8 - 1", "21%", "0%", "0%", "0 - 0 - 71", 8, 28, 5, "62%",
     3, "37%", 189, 1.88, 3.00, 0, 0, "N/A", "$18,200", "24%", "0.00%", "$18,200", "$24,325"]
]

# Specify the output CSV file path
output_file = "C:/Users/aryye/OneDrive/Documents/GitHub/HLC/data/formatted_table_CR.csv"

# Write data to CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"CSV file '{output_file}' has been created successfully.")
