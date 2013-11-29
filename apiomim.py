import urllib 
import re
lista=["254130","253601"] #example list


def clinicalSynopsis(apiKey,list):
    outfile=open("clinicalSynopsistext.txt","w",0)
    for i in list:
        if len(list)>10:
            print "List if too long. It should contain 10 items. String type."
        else:
            link = "http://api.omim.org/api/entry?mimNumber="+i+"&include=clinicalSynopsis&apiKey="+apiKey
            name= i+".xml"
            r = urllib.urlretrieve(link, name)
            o=open(name).read()
            pattern = r">(.*?)<"
            #pattern2 =".*"
            p = re.compile(pattern,re.DOTALL)
            znal2 = re.findall(p,o)
            for j in znal2:
                if j.strip():
                    outfile.write(j)
                   
def similarities(file):
    s={}
    l=[]
    o=open(file).read()
    oo=open(file)
    p="{.*?}"
    znal = re.findall(p,o)
    for z in znal:
        ile=0
        if s.has_key(z):
        
            s[z]=ile+1
        else:
            s[z]=0
    for x,y in s.iteritems():
        if y>=1:
            l.append(x)
    for i in oo.readlines():
        #ii=i.strip().split()
        for item in l:
            if item in i:
                print i
                
def reference(apiKey,list):
    #outfile1=open("omimreferences.txt","w",0)
    for i in list:
        link = "http://api.omim.org/api/entry/referenceList?mimNumber="+i+"&apiKey="+apiKey
        name=i+"references.xml"
        r = urllib.urlretrieve(link, name)
        o=open(name).read()
        #oo=open(name)
        pattern = r">(.*?)<"
        p = re.compile(pattern,re.DOTALL)
        znal2 = re.findall(p,o)
        for k in znal2:
            if k.strip():
                print k 
