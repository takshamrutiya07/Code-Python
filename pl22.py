# import pandas as pd
# csv_file_path = 'sample_data.csv'
# df_csv = pd.read_csv(csv_file_path)

# print("CSV Data:")
# print(df_csv)

# import pandas as pd
# csv_file_path = 'sample_data.csv'
# df_csv = pd.read_csv(csv_file_path)
# filtered_data = df_csv[df_csv['Age'] > 30]
# print("\nFiltered Data (Age > 30):")
# print(filtered_data)

# import pandas as pd
# json_file_path = 'sample_data.json'
# df_json = pd.read_json(json_file_path)
# print("\nJSON Data:")
# print(df_json)


# import pandas as pd
# json_file_path = 'sample_data.json'
# df_json = pd.read_json(json_file_path)
# average_age = df_json['Age'].mean()
# print("\nAverage Age:", average_age)

# import pandas as pd
# excel_file_path = 'sample_data.xlsx'
# df_excel = pd.read_excel(excel_file_path)
# print("\nExcel Data:")
# print(df_excel)


# import pandas as pd
# excel_file_path = 'sample_data.xlsx'
# df_excel = pd.read_excel(excel_file_path)
# entry_count = df_excel.shape[0]
# print("\nNumber of entries in Excel file:", entry_count)

# import pandas as pd
# csv_file_path = 'sample_data.csv'
# df_csv = pd.read_csv(csv_file_path)
# filtered_data = df_csv[df_csv['Age'] > 30]
# filtered_data.to_csv('filtered_data.csv', index=False)
# print("\nFiltered data saved to 'filtered_data.csv'.")


# import pandas as pd
# json_file_path = 'sample_data.json'
# df_json = pd.read_json(json_file_path)
# df_json.to_json('new_data.json', orient='records', lines=True)
# print("JSON data saved to 'new_data.json'.")


# import pandas as pd
# excel_file_path = 'sample_data.xlsx'
# df_excel = pd.read_excel(excel_file_path)
# df_excel.to_excel('new_data.xlsx', index=False)
# print("Excel data saved to 'new_data.xlsx'.")



# import pandas as pd
# csv_file_path = 'sample_data.csv'
# df_csv = pd.read_csv(csv_file_path)
# print(df_csv.dtypes)

import pandas as pd
import numpy as np
data = {
    "Age": [25, 30, np.nan, 40, np.nan]
}
df = pd.DataFrame(data)
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)
