# FindTheBadCSV

This addressed a specific issue I had at work, where we could not guarantee a vendor would send us .csv files in a consistent format. 

Sometimes there were more commas in a row than we expected.  Even worse, sometimes the --AMOUNT OF COLUMNS-- silently changed on us.

This predicably caused the import process to fail on numerous occasions. Bad things happened and many headaches followed.

This program assumes you have a master list of the columns you're expecting in another file. It counts those columns, and then checks every row in the import file to make sure it has that exact number of columns.

If it doesn't, it will save that row off to an output file for later review. 

If the import header row is different, it stops the entire operation.
