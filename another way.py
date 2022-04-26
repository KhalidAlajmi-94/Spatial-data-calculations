import arcpy

arcpy.env.workspace = r"C:\Khalid\Exam-03\Exam_3.gdb"

aFC="LandParcels"
aFL= ["TaxVal06","TaxVal00", "Per_Change"]
aQuery= '(TaxVal00 >0 AND TaxVal06 >0) AND (UseCode = \'A\' OR UseCode = \'B\')'
with arcpy.da.UpdateCursor(aFC, aFL, aQuery) as aCursor:
    for aRow in aCursor:
        aRow[2]=((float(aRow[0])-aRow[1])/(aRow[1])) *100
        aCursor.updateRow(aRow)
        
            
        

import datetime
Atime=datetime.datetime.now()
aFile= open(r"C:\Khalid\Exam-03\msg.txt", "w")
aFile.write(str(Atime))
aFile.close()

print "done"