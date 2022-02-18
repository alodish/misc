import pandas as pd
import numpy as np


table = pd.read_excel('reformat.xlsx')
last_name = table['Last Name'].tolist()
first_name = table['First Name'].tolist()
SSN = table['SSN'].tolist()
MRN = table['MRN'].tolist()
gender = table['Gender'].tolist()
birthday = table['Birthday'].tolist()
address = table['Address'].tolist()
last_name_alter = [0] * len(last_name)
first_name_alter = [0] * len(last_name)
SSN_alter = [0] * len(last_name)
gender_alter = [0] * len(last_name)
birthday_alter = [0] * len(last_name)
address_alter = [0] * len(last_name)
last_name_id = table['Last Name ID'].tolist()
first_name_id = table['First Name ID'].tolist()
SSN_id = table['SSN ID'].tolist()
birthday_id = table['Birthday ID'].tolist()
address_id = table['Address ID'].tolist()
true_MRN = table['True MRN'].tolist()

loop = len(last_name)

for i in range(3):
    for j in range(loop):
        true_MRN.append(MRN[j])
        if i == 0:
            MRN.append(MRN[j])
            birthday.append(birthday[j])
            birthday_id.append(birthday_id[j])
            birthday_alter.append(0)
            # drop the SSN in half of instances
            if j % 2 == 0:
                first_name_id.append(0)
                first_name.append('John')
                last_name.append(last_name[j])
                last_name_id.append(last_name_id[j])
                SSN.append(np.nan)
                SSN_id.append(0)
                SSN_alter.append(1)
                gender.append(gender[j])
                gender_alter.append(0)
                address.append(address[j])
                address_id.append(address_id[j])
                address_alter.append(0)
            # drop the gender in the other half
            else:
                first_name.append(first_name[j])
                first_name_id.append(first_name_id[j])
                last_name_id.append(0)
                last_name.append('Deer')
                SSN.append(SSN[j])
                SSN_id.append(SSN_id[j])
                SSN_alter.append(0)
                gender.append(2)
                gender_alter.append(1)
                address.append(np.nan)
                address_id.append(0)
                address_alter.append(1)

        elif i == 1:
            first_name.append(first_name[j])
            first_name_id.append(first_name_id[j])
            last_name.append(last_name[j])
            last_name_id.append(last_name_id[j])
            SSN.append(SSN[j])
            SSN_id.append(SSN_id[j])
            SSN_alter.append(0)
            MRN.append(max(MRN) + 1)
            gender.append(gender[j])
            gender_alter.append(0)
            birthday.append(0)      # will write to excel as min date
            birthday_id.append(0)
            birthday_alter.append(1)
            address.append(np.nan)
            address_id.append(0)
            address_alter.append(1)

        elif i == 2:
            first_name.append(first_name[j])
            first_name_id.append(first_name_id[j])
            last_name.append(last_name[j])
            last_name_id.append(last_name_id[j])
            SSN.append(np.nan)
            SSN_id.append(0)
            SSN_alter.append(1)
            MRN.append(max(MRN) + 1)
            gender.append(2)
            gender_alter.append(1)
            birthday.append(0)
            birthday_id.append(0)
            birthday_alter.append(1)
            address.append(address[j])
            address_id.append(address_id[j])
            address_alter.append(0)

data = [
    last_name,
    last_name_id,
    first_name,
    first_name_id,
    SSN,
    SSN_id,
    MRN,
    gender,
    birthday,
    birthday_id,
    address,
    address_id,
    SSN_alter,
    gender_alter,
    birthday_alter,
    address_alter,
    true_MRN
]

columns = [
    'Last Name',
    'Last Name ID',
    'First Name',
    'First Name ID',
    'SSN',
    'SSN ID',
    'MRN',
    'Gender',
    'Birthday',
    'Birthday ID',
    'Address',
    'Address ID',
    'SSN Missing',
    'Gender Missing',
    'Birthday Missing',
    'Address Missing',
    'True MRN'
]

data = np.transpose(data)

df = pd.DataFrame(
    data,
    columns=columns
)

print(df.head())
df.to_excel('erroneous-data-shuffle.xlsx')
