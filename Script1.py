import arcpy
aWS=r"C:\Khalid\Exam-03\Exam_3.gdb"
arcpy.env.workspace=aWS

aFC="LandParcels"
with arcpy.da.UpdateCursor(aFC, "*",'TaxVal00 >0 AND TaxVal06 >0') as aCursor:
    for aRow in aCursor:
        if aRow[6]=="A" or aRow[6]=="B":
            aRow[10]=(float(aRow[3])-aRow[5])/(aRow[5])
        aCursor.updateRow(aRow)
        
            
        

del aRow
del aCursor
import datetime
Atime=datetime.datetime.now()
aFile= open(r"C:\Khalid\Exam-03\msg.txt", "w")
aFile.write(str(Atime))
aFile.close()

print "done"