---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]

## JSON Format
JavaScript Object Notation
Stores data using key-value pairs

A sample response from xkcd API is
```json
{"month": "11", "num": 2068, "link": "", "year": "2018", "news": "",  
"safe_title": "Election Night", "transcript": "", "alt": "\"Even the  
blind\u00e2\u0080\u0094those who are anxious to hear, but are not able  
to see\u00e2\u0080\u0094will be taken care of. Immense megaphones have  
been constructed and will be in use at The Tribune office and in the  
Coliseum. The one at the Coliseum will be operated by a gentleman who  
draws $60 a week from Barnum & Bailey's circus for the use of his  
voice.\"", "img": "https://imgs.xkcd.com/comics/election_night.png",  
"title": "Election Night", "day": "5"}
```

Online JSON viewers can help make sense of it.

## Parsing JSON data using the JSONObject class
Once you are able to make sense of this data, you are able to parse it. One way is to use the **JSONObject** class.
The **JSONObject** constructor takes in a string variable that contains the JSON data. You then retrieve the value using the **key** and one of the appropriate **get** methods.
```java
JSONObject jsonObject = new JSONObject(json);
String safe_title = jsonObject.getString("safe_title");
```

Another alternative is the GSON library. Learn by yourself.
