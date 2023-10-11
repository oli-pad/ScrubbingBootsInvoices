from modules.Get_Scrubbed_Detail import Get_Scrubbed_Detail
from modules.RenameInvoices import RenameInvoices

import pandas as pd

#print(BootsInvoiceDetail(r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\0000100401_000101PKM_Boots UK Supplier Funding Invoice 0090326117.pdf","CL002","MOR01").Full_Invoice())

#BootsInvoiceDetail(
#    r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\0000100401_000101QOD_Boots UK Supplier Funding Invoice 0090335610.pdf","CL002","MOR01").Full_Invoice(
#    ).to_csv(r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\Boots.csv")

#RenameInvoices(r"W:\Audit\Loreal\Invoice Images\EmailStagingBay\Boots")

df = Get_Scrubbed_Detail('W:\Audit\Loreal\Invoice Images\ImageStagingBay\Boots','CL031','BOO01')

#For faster testing CSV to check the data in the dataframe
df.to_csv('W:\Audit\Loreal\Boots.csv',index=False)
