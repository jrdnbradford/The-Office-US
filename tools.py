import json
import csv


def convert_json2csv():
    """Converts original JSON to CSV"""
    
    with open("CSV/episodes.csv", "w") as new_csv:
        csv_writer = csv.writer(new_csv, delimiter = ",")
        header = ["Season", "Episode", "Title", "Director", 
                  "Writer(s)", "Air Date", "Original US Viewers", 
                  "Production Code", "Two-Part Episode"]
        csv_writer.writerow(header)
        
        with open("JSON/episodes.json", "r") as json_file:
            data = json.load(json_file)
            row = []
            for season in data:
                for episode in data[season]:
                    row.append(season)
                    row.append(episode)
                    for key in data[season][episode]:
                        if isinstance(data[season][episode][key], list):
                            row.append(",".join(data[season][episode][key]))
                        else:
                            row.append(data[season][episode][key])        
                    csv_writer.writerow(row)
                    row = []
