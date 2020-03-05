def webscraper():
    n=0
    r = []
    while n<50:
        tmp = requests.get("http://18.207.92.139:8000/random_company").text    
        r = r + [tmp]
        n=n+1

    x=[]
    H=[]
    for i in r:
        soup = BeautifulSoup(i, 'html.parser')
        x.append(soup.find('li').text)
        v= soup.get_text()
        k = v.splitlines()
    
        for j in k:
            if j.startswith('Purpose'):
                H.append(j)

    z = open("foryou4.txt", "a") 

    for i in x:
        z.write(i + "\n")
    z.close()  
    z = open("foryou4.txt", "a") 
      
    for g in H:
        z.write(g + "\n")
    z= open("foryou4.txt", "r")
    z.read()
    z.close()     

if__name__=='main':
    webscraper()
    
  
