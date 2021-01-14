import pandas as pd

file = pd.read_csv("credit_scoring_eng.csv")

file.info()

#Step 2. Preprocess the data:
#Identify and fill in missing values

children_counter = file['children'].isna().sum()
days_employed_counter = file['days_employed'].isna().sum()
dob_years_counter = file['dob_years'].isna().sum()
education_counter = file['education'].isna().sum()
education_id_counter = file['education_id'].isna().sum()
family_status_counter = file['family_status'].isna().sum()
family_status_id_counter = file['family_status_id'].isna().sum()
gender_counter = file['gender'].isna().sum()
income_type_counter = file['income_type'].isna().sum()
debt_counter = file['debt'].isna().sum()
total_income_counter = file['total_income'].isna().sum()
purpose_counter = file['purpose'].isna().sum()

print(file['income_type'].unique())
file[file['days_employed'].isna() & file['total_income'].isna()].count()

file.fillna(0, inplace = True)

#Replace the real number data type with the integer type

columns = ['days_employed', 'total_income']
for col in columns:
    file[col] = file[col].astype(int)

file.info()

#Delete duplicate data
#print(file.groupby(file.columns.tolist(),as_index=False).size())

#Categorize the data