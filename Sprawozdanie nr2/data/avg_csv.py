import pandas as pd
import sys
import os

# get files from sys.argv[1] directory

path = sys.argv[1]
os.chdir(path)

if(not os.path.exists("average")):
    os.mkdir("average")


for file in os.listdir():

    if not file.endswith(".csv"):
        continue

    # Wczytaj dane z pliku CSV
    data = pd.read_csv(file, sep='\t', header=None)

    # Convert 2 and 3 columns to int
    data[data.columns[2]] = data[data.columns[2]].astype(int)
    data[data.columns[3]] = data[data.columns[3]].astype(float)

    # Uśrednij wyniki dla tych samych wartości X ale nie usuwaj pozostalych kolumn
    averaged_data = data.groupby([2])[3].mean().reset_index()
    averaged_data.sort_values(by=[2], inplace=True)
    averaged_data.reset_index(drop=True, inplace=True)

    print(os.path.join("./average", file))

    # Zapisz przetworzone dane do nowego pliku CSV
    averaged_data.to_csv(os.path.join("./average", file), sep='\t', index=False, float_format='%.10f', header=False)