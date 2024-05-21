# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"D400y00","system":"readv2"},{"code":"D400.00","system":"readv2"},{"code":"42H4.00","system":"readv2"},{"code":"D400400","system":"readv2"},{"code":"D400z00","system":"readv2"},{"code":"32141.0","system":"readv2"},{"code":"30008.0","system":"readv2"},{"code":"35719.0","system":"readv2"},{"code":"63204.0","system":"readv2"},{"code":"17705.0","system":"readv2"},{"code":"50375.0","system":"readv2"},{"code":"21258.0","system":"readv2"},{"code":"64300.0","system":"readv2"},{"code":"65903.0","system":"readv2"},{"code":"4818.0","system":"readv2"},{"code":"40310.0","system":"readv2"},{"code":"26325.0","system":"readv2"},{"code":"63055.0","system":"readv2"},{"code":"2071.0","system":"readv2"},{"code":"1955.0","system":"readv2"},{"code":"96380.0","system":"readv2"},{"code":"18054.0","system":"readv2"},{"code":"3372.0","system":"readv2"},{"code":"4463.0","system":"readv2"},{"code":"54000.0","system":"readv2"},{"code":"70337.0","system":"readv2"},{"code":"49346.0","system":"readv2"},{"code":"D70","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('agranulocytosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["agranulocytosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["agranulocytosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["agranulocytosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
