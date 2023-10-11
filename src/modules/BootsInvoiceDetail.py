import re
from collections import namedtuple
import pandas as pd
from modules.ConvertPDFtoText import ConvertPDFtoText

Months={'JAN':'01','FEB':'02','MAR':'03','APR':'04','MAY':'05','JUN':'06','JUL':'07','AUG':'08','SEP':'09','OCT':'10','NOV':'11','DEC':'12'}

Line = namedtuple('Line','Salitix_Client_Number Salitix_Customer_Number SAL_Invoice_type Unit_Funding_Type Line_Description Deal_Type Invoice_No Invoice_Date Promotion_No Product_No Start_Date End_Date Quantity Unit_Price Net_Amount VAT_Rate Gross_Amount Store_Format Invoice_Description Acquisition_Ind')

class BootsInvoiceDetail:

    def __init__(self,filename,Salitix_Client_Number,Salitix_Customer_Number):
        self.filename=filename
        self.pdf_text=ConvertPDFtoText(filename)
        self.lines=self.pdf_text.split('\n')
        self.Salitix_Client_Number=Salitix_Client_Number
        self.Salitix_Customer_Number=Salitix_Customer_Number

    