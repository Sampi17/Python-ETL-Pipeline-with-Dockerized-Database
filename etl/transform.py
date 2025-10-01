import pandas as pd
df = pd.read_csv('raw/HR_Analytics.csv')
#file path
def column_selection(raw_data):
#def transform_data(df):
    #Select columns of interest for this dataset
    df = raw_data[['EmpID','Age','Gender','Attrition','BusinessTravel','Department','Education','EducationField',
                        'JobRole','YearsAtCompany' ]]
    return df

def data_type_transformation(raw_data):
    #channging data types to the correct types
    df = raw_data.astype({
        'EmpID': 'string',
        'Gender': 'string', 
        'Attrition': 'string',
        'BusinessTravel': 'string',
        'Department': 'string',
        'EducationField': 'string',
        'JobRole': 'string',
        'Education': 'int32',
        'Age': 'int32',
        'YearsAtCompany': 'int32'
    })

    return df
    
def rename_column(raw_data): 
    #column renaming
    df = raw_data.rename(columns={'Attrition' : 'EmploymentStatus'})
    return df 


def filter_rows(raw_data):
    # only active employess
    df = raw_data[raw_data['EmploymentStatus'] == 'Yes']
    return df

def lowercase_all_columns(raw_data):
    # lower case all col names 
    raw_data.columns = raw_data.columns.str.lower()
    return raw_data

def transform_data(raw_data):    
    #df_transformed = raw_data
    transformations = [column_selection,data_type_transformation,rename_column,filter_rows,lowercase_all_columns]
    df_final = raw_data
    for step in transformations:
        df_final = step(df_final)

    return df_final
