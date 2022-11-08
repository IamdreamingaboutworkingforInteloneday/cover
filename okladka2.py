import requests, re, dload, os
limit=40
adresy=[]
try:
    i=0
    while len(adresy)<=limit:
        strona = requests.get(f'https://katalog.bg.pg.edu.pl/search/query?facet_loc=170000&sort=dateCreated&pageNumber={i}&theme=system')
        w=strona.text
        adresy+=re.findall("http://www.nukat.edu.pl/nukat/icov/GD015/[a-z0-9_//\-.]+\.jpg",w)
        adresy+=re.findall("http://www.nukat.edu.pl/nukat/icov/GD101/[a-z0-9_//\-.]+\.jpg",w)
        adresy+=re.findall("http://www.nukat.edu.pl/nukat/icov/WALAZ/[a-z0-9_//\-.]+\.jpg",w)
        adresy=list(set(adresy))
        i+=1
    print(f"Przejrzano {i} stron w celu pobrania {limit} skanów okładek")
    if not os.path.exists("foty"):
        os.mkdir("foty")
    for w in range(limit):

        dload.save(adresy[w],f"foty/{adresy[w][-13:]}")
except:
    print("sorry, coś poszło nie tak")

# http://www.nukat.edu.pl/nukat/icov/GD015/xx005147588.jpg
