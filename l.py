import pandas as pd
import pdfkit
df1 = pd.read_csv('saree.csv')
print("The dataframe is:")
print(df1)
html_string = df1.to_html()
# pdfkit.from_string(df1, "output_file.pdf")
# print("PDF file saved.")
path_wkhtmltopdf = (r"C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_string(html_string, "out.pdf", configuration=config)