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
    
    with open("XML/episodes.xml", "w") as new_xml:
        with open("JSON/episodes.json", "r") as json_file:
            data = json.load(json_file)
            new_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n\n')
            new_xml.write(f"<The-Office>\n\n") #Begin XML
            for season in data:
                season_tag = season.replace(" ", "-")
                new_xml.write(f"\t<{season_tag}>\n\n") #Begin Season
                for episode in data[season]:
                    episode_tag = episode.replace(" ", "-") 
                    new_xml.write(f"\t\t<{episode_tag}>\n") #Begin Episode
                    for key in data[season][episode]:
                        if isinstance(data[season][episode][key], list): #For Writers
                            key_tag = key.replace("(s)", "s")
                            new_xml.write(f"\t\t\t<{key_tag}>\n") #Begin Writers
                            for i, writer in enumerate(data[season][episode][key]):
                                new_xml.write(f"\t\t\t\t<Writer-{i+1}>{writer}</Writer-{i+1}>\n")
                            new_xml.write(f"\t\t\t</{key_tag}>\n") #End Writers
                        else:
                            key_tag = key.replace(" ", "-")
                            new_xml.write(f"\t\t\t<{key_tag}>{data[season][episode][key]}</{key_tag}>\n") 
                    new_xml.write(f"\t\t</{episode_tag}>\n\n") #End Episode     
                new_xml.write(f"\t</{season_tag}>\n\n") #End Season
            new_xml.write(f"</The-Office>") #End XML
