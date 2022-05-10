---
aliases: Universal Resource Indicators, URI
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## URI
URI is a string of characters used to identify a resource.

## Absolute URIs
Specify a scheme
- **http://www.google.com**: a document on the internet (AKA URL)
- **file:/Users/Macintosh/Downloads/url.html**: a file in your com
- **geo:0.0?q=test**: a geographic location
- **mailto:test@sutd.edu.sg**: an email

## Hierarchical URIs
Have a slash character after hte scheme.
Can be parsed as follows:

> \[scheme:\]\[authority\]\[path\]\[?query\]\[\#fragment//\]

## Opaque URIs
Do not have slash characters and can be parsed as follows

> \[scheme : \]\[opaque part\]\[? Query\]

## Show a location in maps app on phone
- Specify the geo URI correctly
- Execute an [[Intents#Implicit intent|implicit intent]]