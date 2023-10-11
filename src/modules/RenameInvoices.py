from modules.BootsInvoiceDetail import BootsInvoiceDetail
from modules.ProduceFileList import ProduceFileList
import os
import shutil

def RenameInvoices(directory):
    FileList = ProduceFileList(directory)
    for file in FileList:
        try:
            instance = BootsInvoiceDetail(os.path.join(directory,file),'123','456')
        except:
            pass
        try:
            Invoice_No = instance.Invoice_No()
        except:
            Invoice_No = 'Unknown'
        print(file)
        print(Invoice_No)
        if Invoice_No != 'Unknown' and Invoice_No != None:
            shutil.copy(os.path.join(directory,file),os.path.join("W:\Audit\Loreal\Invoice Images",Invoice_No+'.pdf'))
            try:
                os.rename(os.path.join(directory,file),os.path.join("W:\Audit\Loreal\Invoice Images\ImageStagingBay\Boots",Invoice_No+'.pdf'))
            except:
                try:
                    os.replace(os.path.join(directory,file),os.path.join("W:\Audit\Loreal\Invoice Images\ImageStagingBay\Boots",Invoice_No+'.pdf'))
                except:
                    pass