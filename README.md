# *The*-*Office*-(U.S.)
This repo contains JSON structured data concerning NBC's mockumentary series [*The Office* (U.S. version)](https://www.nbc.com/the-office). 

Developers, programmers, and others who are fans of the series can use this data to generate insights about the series.

**This repo is neither authorized by nor affiliated with NBC or *The Office* in any way.**

## JSON Structure Example
The example below gives an indication of the JSON structure for [episodes.json](JSON/episodes.json). 

```JSON
{
    "Season 1" : { 
        "Episode 1" : {
            "Title" : "Pilot",
            "Director" : "Ken Kwapis",
            "Writer(s)" : [
                "Greg Daniels",
                "Ricky Gervais",
                "Stephen Merchant"                 
            ],
            "Air Date" : "March 24, 2005",
            "Original US Viewers" : 11.20,
            "Production Code" : 1001,
            "Two-Part Episode" : false
        }
    }
}
```
* The *Original US Viewers* key value is a number representing *millions* of viewers.
* The *Writers* key value is an array of one or more strings.

## Python Code Examples
### Using Locally Downloaded JSON Data
```PYTHON
#Python
#Print list of everyone who served as a director for The Office.
import json

def main():
    file = open("JSON/episodes.json", "r")
    officeData = json.load(file)
    file.close()

    directorsList = sorted(set([officeData[season][episode][key] 
                    for season in officeData 
                        for episode in officeData[season] 
                            for key in officeData[season][episode] 
                                if key == "Director"]))

    print(f"Directors: {directorsList}")

if __name__ == "__main__": main()
```

### Using urllib.request for JSON Data
```python
#Python
#Print a dictionary with episode titles as keys and the titles' viewership as values.
import json
import urllib.request

def main():
    url = "https://raw.githubusercontent.com/jrdnbradford/The-Office-(U.S.)/master/JSON/episodes.json"
    response = urllib.request.urlopen(url)

    if response.status == 200:
        officeData = json.load(response)
        titleList = []
        viewershipList = []

        for season in officeData:    
            for episode in officeData[season]:
                data = officeData[season][episode]
                title = data["Title"]
                viewership = data["Original US Viewers"]

                titleList.append(title)
                viewershipList.append(viewership)

        viewershipDict = dict(zip(titleList, viewershipList))
        print(viewershipDict) 

if __name__ == "__main__": main()
```

## Contributing
Pull requests correcting data are welcome.

## License & Terms of Use
### [episodes.json](JSON/episodes.json)
This data was retrieved and adapted from the [__List of *The Office* (U.S. TV series) episodes__ Wikipedia page](https://en.wikipedia.org/wiki/List_of_The_Office_(U.S._TV_series)_episodes) where it was originally formatted in HTML tables. Please see that page for relevant citations.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png"/></a><br/>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. (Plain text version [here](CC_BY-SA_3.0.txt).)