import json
import csv


def json_to_csv():
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


def json_to_xml():
    """Converts original JSON to XML"""
    import calendar


    months = {month: num for num, month in enumerate(calendar.month_name)}

    with open("XML/episodes.xml", "w") as new_xml:
        with open("JSON/episodes.json", "r") as json_file:
            data = json.load(json_file)
            new_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            new_xml.write(f"<The-Office>\n") #Begin XML
            for season in data:
                season_tag = season.replace(" ", "-")
                new_xml.write(f"\t<{season_tag}>\n") #Begin Season
                for episode in data[season]:
                    episode_tag = episode.replace(" ", "-") 
                    new_xml.write(f"\t\t<{episode_tag}>\n") #Begin Episode
                    for key in data[season][episode]:
                        datum = data[season][episode][key]
                        tag = key.replace(" ", "-").replace("(s)", "s")
                        if isinstance(datum, list): #For Writers
                            new_xml.write(f"\t\t\t<{tag}>\n") #Begin Writers
                            for i, writer in enumerate(datum):
                                new_xml.write(f"\t\t\t\t<Writer-{i+1}>{writer}</Writer-{i+1}>\n")
                            new_xml.write(f"\t\t\t</{tag}>\n") #End Writers
                        elif key == "Air Date":
                            new_xml.write(f"\t\t\t<{tag}>\n") #Begin Air-Date
                            month, day, year = datum.replace(",", "").split(" ")
                            new_xml.write(f"\t\t\t\t<Year>{year}</Year>\n")
                            new_xml.write(f"\t\t\t\t<Month>{months[month]}</Month>\n")
                            new_xml.write(f"\t\t\t\t<Day>{day}</Day>\n")
                            new_xml.write(f"\t\t\t</{tag}>\n") #End Air-Date
                        else:
                            new_xml.write(f"\t\t\t<{tag}>{datum}</{tag}>\n") 
                    new_xml.write(f"\t\t</{episode_tag}>\n") #End Episode     
                new_xml.write(f"\t</{season_tag}>\n") #End Season
            new_xml.write(f"</The-Office>") #End XML