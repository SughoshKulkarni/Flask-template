import pandas as pd
from datetime import datetime


def sample(files):
    if files.filename[-1] == 'x' or files.filename[-1] == 'm':
        currentFileName = files.filename[:-5]
        extension = files.filename[-5:]
        input_data = pd.read_excel(files)
    else:
        currentFileName = files.filename[:-4]
        input_data = pd.read_csv(files)

    # Write your function here
    #  
    # 

    # Create input_data to an excel file
    input_data.to_excel("static/downloads/" + datetime.now().strftime("%Y%m%d-%H%M%S") + "_"+ currentFileName + '_sample_output.xlsx')