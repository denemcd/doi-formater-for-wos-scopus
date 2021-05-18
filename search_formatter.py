import pandas as pd
import os

# This code takes a CSV of DOIs in column 1 with a header of DOI and formats them for a DOI serach in Scopus and WOS.
# The output is displayed on screen and can be pasted into the advanced search of each search tool

os.system('cls')  # Clear the screen

# Open the CSV and convert into dataframe
fileName = input("Enter CSV name (minus extension): ") + ".csv"  # Get the file
file = open(fileName)
doilist = pd.read_csv(file, header=0)
file.close

print(str(len(doilist)) + " DOIs loaded")

# SCOPUS ####################################################

doistatement = ""

for i in range(len(doilist)):
    if i != len(doilist) - 1:
        doistatement = doistatement + doilist.loc[i, "DOI"] + ") OR DOI("
    elif i == len(doilist) - 1:
        doistatement = doistatement + doilist.loc[i, "DOI"] + ")"

doistatement = "DOI(" + doistatement

print("\n##### SCOPUS ##############\n" + doistatement + "\n")

# SCOPUS ####################################################

doistatement = ""

for i in range(len(doilist)):
    if i != len(doilist) - 1:
        doistatement = doistatement + doilist.loc[i, "DOI"] + " OR DO="
    elif i == len(doilist) - 1:
        doistatement = doistatement + doilist.loc[i, "DOI"] + ""

doistatement = "DO=" + doistatement

print("\n##### WOS ##############\n" + doistatement + "\n")
