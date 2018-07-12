# AirlineCrawl
Get up-to-date airline information of China from ctrip.com.

## Resources to be Imported
```Java
import urllib.request
from bs4 import BeautifulSoup
```

BeautifulSoup needs to be installed before running this code.<br>
>[Download BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.6/)<br>

Find the directory of BeautifulSoup in cmd console, then input<br>
```
python setup.py install
```

## Input
File "aprs.txt" contains all airports in China.<br>
It might update over time.<br>

## Output
Result.ext contains all results.<br>
Results with commas separating columns, showing the following information:<br>
>* departure time
>* arrival time
>* departure airport
>* arrival airport
>* flight code
>* flight company
>* availability on Monday, Tuesday, ... , Sunday
