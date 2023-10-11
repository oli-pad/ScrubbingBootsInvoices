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

    def SAL_Invoice_type(self):
        if self.Deal_Type()=='Promotion Site Fees':
            return 'MS'
    
    def Unit_Funding_Type(self):
        if self.SAL_Invoice_type()=='MS':
            return ''
    
    def Line_Description(self):
        return ['Boots Invoice Detail']
    
    def Deal_Type(self):
        line_desc_status=False
        for line in self.lines:
            if re.search('FUNDING TYPE  QUANTITY  UNIT PRICE   VALUE   VAT RATE /',line):
                line_desc_status=True
            elif line_desc_status and re.search('(\s?)(.*) ([0-9.,]*) ([0-9.,]*)[%]',line):
                return re.search('(\s?)(.*) ([0-9.,]*) ([0-9.,]*)[%]',line).group(2)

    def Invoice_No(self):
        for line in self.lines:
            if re.search('INVOICE NO: (\d+)',line):
                return re.search('INVOICE NO: (\d+)',line).group(1)
            if re.search('(\d+)     PAGE 1',line):
                return re.search('(\d+)     PAGE 1',line).group(1)
    
    def Invoice_Date(self):
        for line in self.lines:
            if re.search('DATE [(]TAX POINT[)]: (\d{2})[.](\d{2})[.](\d{4})',line):
                return re.search('DATE [(]TAX POINT[)]: (\d{2})[.](\d{2})[.](\d{4})',line).group(3)+'-'+re.search('DATE [(]TAX POINT[)]: (\d{2})[.](\d{2})[.](\d{4})',line).group(2)+'-'+re.search('DATE [(]TAX POINT[)]: (\d{2})[.](\d{2})[.](\d{4})',line).group(1)
            
    def Promotion_No(self):
        if self.SAL_Invoice_type()=='MS':
            return ''
        
    def Product_No(self):
        if self.SAL_Invoice_type()=='MS':
            return ['']
        
    def Start_Date(self):
        if self.SAL_Invoice_type()=='MS':
            return self.Invoice_Date()
    
    def End_Date(self):
        if self.SAL_Invoice_type()=='MS':
            return self.Invoice_Date()
        
    def Quantity(self):
        if self.SAL_Invoice_type()=='MS':
            return ['']
    
    def Unit_Price(self):
        if self.SAL_Invoice_type()=='MS':
            return ['']
    
    def Net_Amount(self):
        if self.SAL_Invoice_type()=='MS':
            for line in self.lines:
                if re.search('NETT VALUE             ([0-9.,]*)   GBP',line):
                    return [re.search('NETT VALUE             ([0-9.,]*)   GBP',line).group(1).replace(',','')]
    
    def VAT_Rate(self):
        if self.SAL_Invoice_type()=='MS':
            line_desc_status=False
            for line in self.lines:
                if re.search('FUNDING TYPE  QUANTITY  UNIT PRICE   VALUE   VAT RATE /',line):
                    line_desc_status=True
                elif line_desc_status and re.search('(\s?)(.*) ([0-9.,]*) ([0-9.,]*)[%]',line):
                    return [str(float(re.search('(\s?)(.*) ([0-9.,]*) ([0-9.,]*)[%]',line).group(4))/100)]
                
    def Gross_Amount(self):
        if self.SAL_Invoice_type()=='MS':
            for line in self.lines:
                if re.search('TOTAL             ([0-9.,]*)   GBP',line):
                    return [re.search('TOTAL             ([0-9.,]*)   GBP',line).group(1).replace(',','')]
                
    def Store_Format(self):
        if self.SAL_Invoice_type()=='MS':
            return ['']
        
    def Invoice_Description(self):
        if self.SAL_Invoice_type()=='MS':
            for line in self.lines:
                if re.search('PROMOTION: (.*)',line):
                    return re.search('PROMOTION: (.*)',line).group(1)
                
    def Acquisition_Ind(self):
        return 'A'

    def Full_Invoice(self):
        df=pd.DataFrame()
        Invoice_Details = [Line(self.Salitix_Client_Number,self.Salitix_Customer_Number,self.SAL_Invoice_type(),self.Unit_Funding_Type(),self.Line_Description()[i],self.Deal_Type(),self.Invoice_No(),self.Invoice_Date(),self.Promotion_No(),self.Product_No()[i],self.Start_Date(),self.End_Date(),self.Quantity()[i],self.Unit_Price()[i],self.Net_Amount()[i],self.VAT_Rate()[i],self.Gross_Amount()[i],self.Store_Format()[i],self.Invoice_Description(),self.Acquisition_Ind()) for i in range(len(self.Line_Description()))]
        for i in range(len(Invoice_Details)):
            df2=pd.DataFrame([Invoice_Details[i]],columns=Line._fields)
            df=pd.concat([df,df2])
        return df
