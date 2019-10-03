#! python3
# findTheBadCsvRows.py - Sometimes there are more commas in a row than we expect.  Even worse, sometimes the amount of
# --COLUMNS-- silently changes on us. This is bad... This is very bad...
# This has caused the import process to fail in the past
# on numerous occasions. Bad things happened and many headaches followed.
#
# This program assumes you have a master list of the columns you're expecting in another file. It counts
# those columns, and then checks every row in the import file to make sure it has that exact number of columns.
# If it doesn't, it will save that row off to an output file for later review. If the import header row is different it
# stops the entire operation.
#
import csv
import datetime

with open('TestFiles/master_record_example.csv') as master_record:
    csv_reader = csv.reader(master_record, delimiter=',')
    master_column_count = 0
    for row in csv_reader:
        master_column_count = len(row)

cleanImportFile = open('TestFiles/cleanImportFile.csv', 'w')
errorLog = open('TestFiles/errorLog.txt', 'a')
testFile = 'TestFiles/testFileFTP.csv'

with open(testFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(csv_file)
    line_count = 0
    bad_row_count = 0
    for row in csv_reader:
        if line_count == 0:
            if len(row) != master_column_count:
                print("There are too many/few columns in this file. Please review what changed")
                errorLog.write("File: %s Line: %s Time: %s \n" % (testFile, line_count + 1, datetime.datetime.today()))
                errorLog.write("There are too many/few columns in this file. Please review what changed")
                errorLog.write("\n")
                errorLog.write("\n")
                errorLog.write("\n")
                errorLog.write("\n")
                exit()
            else:
                str_row = str(row)[1:-1]  # removing the brackets that get written with this
                cleanImportFile.write(str_row)
                cleanImportFile.write("\n")
        else:
            if len(row) != master_column_count:
                # Something is wrong with this row.
                # Log it, save the row to the error log and delete it from the import file
                print("Line %d is malformed" % line_count)
                errorLog.write("File: %s Line: %s Time: %s \n" % (testFile, line_count + 1, datetime.datetime.today()))
                errorLog.write(str(row))
                errorLog.write("\n")
                errorLog.write("\n")
                errorLog.write("\n")
                errorLog.write("\n")

                bad_row_count += 1
            else:
                str_row = str(row)[1:-1]  # removing the brackets that get written with this
                cleanImportFile.write(str_row)
                cleanImportFile.write("\n")

        line_count += 1

    if bad_row_count > 0:
        print("There were %d bad line(s). Please review the error log to see what went wrong" % bad_row_count)

csv_file.close()
