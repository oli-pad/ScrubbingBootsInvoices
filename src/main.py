from modules.Get_Scrubbed_Detail import Get_Scrubbed_Detail
from modules.RenameInvoices import RenameInvoices
from modules.BootsInvoiceDetail import BootsInvoiceDetail

import pandas as pd


RenameInvoices(r"W:\Audit\Loreal\Invoice Images\EmailStagingBay\Boots")

df = Get_Scrubbed_Detail('W:\Audit\Loreal\Invoice Images\ImageStagingBay\Boots','CL031','BOO01')

#For faster testing CSV to check the data in the dataframe
df.to_csv('W:\Audit\Loreal\Boots.csv',index=False)
