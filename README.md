# *The*-*Office*-US
This repo contains data concerning NBC's mockumentary series [*The Office* (U.S. version)](https://www.nbc.com/the-office). 

Developers, programmers, and others who are fans of the series can use this data for educational purposes.

Data was originally structured as JSON but has been converted to both CSV and XML formats using the code in [convert.py](convert.py).

## Disclaimer
**This repo is neither authorized by nor affiliated with NBC or *The Office* in any way.**

## Data Structure
Subheadings below give an indication of how the data is structured in different formats.
In some cases, compacted/minified versions are available.

*Original US Viewers* is a number representing *millions* of viewers.

### [CSV](CSV/episodes.csv)
| Season | Episode | Title | Director | Writer(s) | Air Date | Original US Viewers | Production Code | Two-Part Episode |
| -------| ------- | ------| -------- | --------- | -------- | ------------------- | --------------- | ---------------- |
| Season 1 | Episode 1 | Pilot | Ken Kwapis | Greg Daniels,Ricky Gervais,Stephen Merchant | March 24, 2005 | 11.2 | 1001 | False |
| Season 1 | Episode 2 | Diversity Day | Ken Kwapis | B.J. Novak | March 29, 2005 | 6.0 | 1002 | False |
| Season 1 | Episode 3 | Health Care | Ken Whittingham | Paul Lieberstein | April 5, 2005 | 5.8 | 1006 | False |

### [JSON](JSON/episodes.json)
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

### [XML](XML/episodes.xml)
```XML
<?xml version="1.0" encoding="UTF-8"?>
<The-Office>
    <Season-1>
        <Episode-1>
            <Title>Pilot</Title>
            <Director>Ken Kwapis</Director>
            <Writers>
                <Writer-1>Greg Daniels</Writer-1>
                <Writer-2>Ricky Gervais</Writer-2>
                <Writer-3>Stephen Merchant</Writer-3>
            </Writers>
            <Air-Date>
                <Year>2005</Year>
                <Month>3</Month>
                <Day>24</Day>
            </Air-Date>
            <Original-US-Viewers>11.2</Original-US-Viewers>
            <Production-Code>1001</Production-Code>
            <Two-Part-Episode>False</Two-Part-Episode>
        </Episode-1>
    </Season-1>
</The-Office>
```

## Contributing
If you find incorrect data or have any suggestions, open an issue. No pull requests.

## License & Terms of Use
This data was retrieved and adapted from the [__List of *The Office* (U.S. TV series) episodes__ Wikipedia page](https://en.wikipedia.org/wiki/List_of_The_Office_(U.S._TV_series)_episodes) where it was originally formatted in HTML tables. Please see that page for relevant citations.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png"/></a><br/>This work is licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. (Plain text version [here](LICENSE.txt).)