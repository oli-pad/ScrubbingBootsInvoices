from modules.ConvertPDFtoText import ConvertPDFtoText
from modules.BootsInvoiceDetail import BootsInvoiceDetail
from modules.RenameInvoices import RenameInvoices

import pandas as pd

#print(BootsInvoiceDetail(r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\0000100401_000101PKM_Boots UK Supplier Funding Invoice 0090326117.pdf","CL002","MOR01").Full_Invoice())

#BootsInvoiceDetail(
#    r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\0000100401_000101PKM_Boots UK Supplier Funding Invoice 0090326117.pdf","CL002","MOR01").Full_Invoice(
#    ).to_csv(r"C:\Users\Oliver.Oakes.SALITIX\OneDrive - Salitix\Desktop\Boots.csv")

RenameInvoices(r"W:\Audit\Loreal\Invoice Images\EmailStagingBay\Boots")