import pandas as pd
import random
from faker import Faker

# Instantiate Faker to generate fake data (such as dates)
fake = Faker()

# Define a list of possible values for each column
therapeutic_names = [f"Bicycle{i}" for i in range(1, 11)]  # Names of therapeutics
therapeutic_types = ["Bicycle", "Antibody", "Small molecule"]  # Types of therapeutics
cancers = ["Breast Cancer", "Lung Cancer", "Colon Cancer", "Prostate Cancer", "Leukemia"]  # Types of cancers targeted
tissues = ["Breast Tissue", "Lung Tissue", "Colon Tissue", "Prostate Tissue", "Bone Marrow"]  # Tissues targeted
trial_phases = [1, 2, 3, 4]  # Phases of clinical trials

# Define the number of records
n = 10000  # We're creating 10,000 rows of data

# Initialize DataFrame with random values for each column
df = pd.DataFrame({
    "Trial_ID": [f"BCT{i:03d}" for i in range(1, n+1)],  # Trial IDs, unique for each trial
    "Therapeutic_Name": random.choices(therapeutic_names, k=n),  # Therapeutic names, randomly chosen from the list above
    "Therapeutic_Type": random.choices(therapeutic_types, k=n),  # Therapeutic types, randomly chosen from the list above
    "Targeted_Cancer": random.choices(cancers, k=n),  # Types of cancer, randomly chosen from the list above
    "Targeted_Tissue": random.choices(tissues, k=n),  # Types of tissue, randomly chosen from the list above
    "Trial_Start_Date": [fake.date_between(start_date='-3y', end_date='-1y') for _ in range(n)],  # Random trial start dates from the last 3 years
    "Trial_Phase": random.choices(trial_phases, k=n),  # Trial phases, randomly chosen from the list above
    "Number_of_Patients": [random.randint(50, 500) for _ in range(n)],  # Random number of patients per trial between 50 and 500
})

# Generate End_Date, Efficacy_Rate, Adverse_Events, and Success based on other columns
df["Trial_End_Date"] = pd.to_datetime(df["Trial_Start_Date"]) + pd.to_timedelta([random.randint(30, 365) for _ in range(n)], unit='D')  # Trial end dates calculated as 30 to 365 days after the start date
df["Efficacy_Rate"] = df["Trial_Phase"].apply(lambda x: round(random.uniform(0.5, 0.5 + 0.1*(5-x)), 2))  # Efficacy rate is a random value between 0.5 and 1, inversely correlated with the trial phase
df["Adverse_Events"] = df["Number_of_Patients"].apply(lambda x: random.randint(0, int(x/10)))  # Number of adverse events is a random value up to 10% of the number of patients
df["Success"] = df["Trial_Phase"].apply(lambda x: bool(random.getrandbits(x)))  # Success is more likely for earlier phase trials

# Save to CSV ( Directory path )
df.to_csv(r"C:\Users\SCHRODERKlaus\Documents\Tibco_Spotfire\Demo_Bicycle_Therapeutics\BicycleTherapeutics_ClinicalTrials.csv", index=False)
