import os
import string
import random
import uuid
import pandas as pd

# initializing size of string
N1 = 10
N2 = 9

# Generate random ids, references and passport_numbers for dummy data

application_ids = [str(uuid.uuid1()) for i in range(0, 5)]
application_references = [''.join(random.choices(string.digits, k=N1)) for i in range(0, 5)]
forenames = ['James', 'John', 'Janet', 'Mary', 'Susan']
surnames = ['Jones', 'Lane', 'Stewart', 'Stone', 'Castle']
passport_numbers = [''.join(random.choices(string.digits, k=N2)) for i in range(0, 5)]
email_addresses = [f'{forenames[i]}.{surnames[i]}@email.com' for i in range(0, 5)]
ages = [random.randint(18, 80) for i in range(0,5)]


if __name__ == "__main__":
    # dictionary of lists 
    application_dict = {'application_id': application_ids,
                        'application_reference': application_references,
                        'forename': forenames,
                        'surname': surnames,
                        'passport_number': passport_numbers,
                        'email_address': email_addresses,
                        'age': ages} 
    
    df = pd.DataFrame(application_dict)
    df.to_csv("passport_applications.csv")



