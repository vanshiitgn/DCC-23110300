import fitz
import pandas as pd

doc1 = fitz.open("pdf_data/electoralbond1.pdf")

pages1 = []
for page in doc1:
    tables = page.find_tables()
    table = tables[0]
    page_dataframe = table.to_pandas()
    pages1.append(page_dataframe)

Data1 = pd.concat(pages1)
Data1.to_csv(f"csv_data/electoralbond1.csv",index =False)



doc2 = fitz.open("pdf_data/electoralbond2.pdf")

pages2 = []
for page in doc2:
    tables = page.find_tables()
    table = tables[0]
    page_dataframe = table.to_pandas()
    pages2.append(page_dataframe)

Data = pd.concat(pages2)
Data.to_csv(f"csv_data/electoralbond2.csv",index =False)
