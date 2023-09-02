import csv
import json
import os

def main():
    
    # check if the file exists
    if os.stat('input.csv').st_size == 0:
        print("File is empty") 
        exit()    

    # create output dictionary
    output = {
    "high_score": None,
    "low_score": None,
    "total_students": 0,
    "avg_score": None,
    "students": []
    }

    try:
        with open('input.csv', newline='', encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                
                # validate if the row is empty
                if len(row) == 0 or row[0] == '' or row[1] == '':
                    print("Row is empty")
                    continue

                # add student to the list
                output['students'].append({
                    row[0]: int(row[1]),
                })

                if output['high_score'] == None:
                    output['high_score'] = int(row[1])
                output['high_score'] = max(output['high_score'], int(row[1]))
                
                if output['low_score'] == None:
                    output['low_score'] = int(row[1])
                output['low_score'] = min(output['low_score'], int(row[1]))
                
                output['total_students'] += 1
                
                # if the last element of the loop calculate average score of all students
                if output['total_students'] == len(output['students']):
                    total_score = 0
                    for student in output['students']:
                        total_score += list(student.values())[0]
                    output['avg_score'] = total_score / output['total_students']
                    
        print(output)
        
        # write output to output.json
        with open('output.json', 'w') as outfile:
            json.dump(output, outfile)
            

    except Exception as e:
        print("Error: ", e)
        exit()

if __name__ == "__main__":
  main()