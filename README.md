# *The*-*Office*-US
This repo contains data concerning NBC's mockumentary series [*The Office* (U.S. version)](https://www.nbc.com/the-office). 

Developers, programmers, and others who are fans of the series can use this data for educational purposes.

Data was originally structured as JSON but has been converted to both CSV and XML formats using the code in [convert.py](convert.py).

## Disclaimer
**This repo is neither authorized by nor affiliated with NBC or *The Office* in any way.**

## JSON Structure
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

## Python Code Examples for JSON
### Using Locally Downloaded Data
```PYTHON
#Print set of everyone who served as a director for The Office.
import json

def main():
    with open("JSON/episodes.json", "r") as f:
        office_data = json.load(f)

    directors = {office_data[season][episode]["Director"] 
                        for season in office_data 
                            for episode in office_data[season] 
                                for key in office_data[season][episode]}

    print(f"Directors: {directors}")

if __name__ == "__main__": main()
```

### Using urllib.request for Data
```python
#Print a dictionary with episode titles as keys and the titles' viewership as values.
import json
import urllib.request

def main():
    url = "https://raw.githubusercontent.com/jrdnbradford/The-Office-US/master/JSON/episodes.json"
    response = urllib.request.urlopen(url)

    if response.status == 200:
        office_data = json.load(response)
        titles = []
        viewerships = []

        for season in office_data:    
            for episode in office_data[season]:
                data = office_data[season][episode]
                title = data["Title"]
                viewership = data["Original US Viewers"]

                titles.append(title)
                viewerships.append(viewership)

        viewership_dict = dict(zip(titles, viewerships))
        print(viewership_dict) 

if __name__ == "__main__": main()
```

## Contributing
Pull requests correcting data are welcome.

## License & Terms of Use
This data was retrieved and adapted from the [__List of *The Office* (U.S. TV series) episodes__ Wikipedia page](https://en.wikipedia.org/wiki/List_of_The_Office_(U.S._TV_series)_episodes) where it was originally formatted in HTML tables. Please see that page for relevant citations.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png"/></a><br/>This work is licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. (Plain text version [here](LICENSE.txt).)