projekt
=======
API OMIM MODULE
This module provides a high-level interface for fetching data form http://omim.org/. It contains
three functions. Two of them requires API key which is unique to every developer wanting to
access the OMIM API. For more details please visit site http://omim.org/api. 
This module focuses on searching omim clinical Synopsis and references database
FUNCTIONS
clinicalSynopsis(apiKey,list)

Arguments for this function are API key (which is special for every omim user), and list of strings
with omim disease ID. List length should be less than ten. These are OMIM API requirements. 
This function returns txt document called "clinicalSynopsistext.txt"which is made from parsed
XML OMIM files. But for your convenience it also saves XML files on your computer.

similarities(file)

This function takes txt file made by clinicalSynopsis(apiKey,list) function as an argument and
returns similarities between diseases. Similarities are based on SNOMEDCT, UMLS, HPO HP
and ICD numbers.

reference(apiKey,list)

This function requires OMIM API key, and string list of OMIM ID's. It returns titles, authors,
pubmed id etc. known to OMIM. 
