#Google Web Crawler
''''# Things to add:-
1)Extract the description from each title.
2)Get the links of the suggestion of the first search result and store it properly.
3)The link of wikipedia when it comes sideways.(Search Boots in google)
4)Add the number of pages
'''





import requests
from bs4 import BeautifulSoup
import bs4


search = input("Enter your search\n")
url = "https://www.google.co.in/search?q="+ search




def keyword_result1(url1,search1):

    source_code = requests.get(url1)
    source_text = source_code.text

    soup = BeautifulSoup(source_text,"lxml")
    for result in soup.find_all('h3',{'class':'r'}):
       result_tag = result.contents[0]                        #Get the anchor tag. It is a child of h3



       if type(result_tag) is bs4.element.NavigableString:    #In few cases we get suggestion.To exclude thoose. eg:- boots
           continue
       elif result_tag.get("class") is ['sla']:               #Removing the links of subsection
           continue
       else:
         print(result_tag.text)
         href1 = "" +result_tag.get('href')
         href2 = href1.split("=")
         href3 = (href2[1].split("&"))
         if "Images" in result_tag.text:
            print("https://www.google.com/search?tbm=isch&q="+href3[0])
            print('\n')
            continue
         if "News" in result_tag.text:
            print("https://news.google.com/news/search/section/q/"+href3[0])
            print('\n')
            continue
         print(href3[0])
       print("\n")
  else:
      exit(0)


keyword_result1(url,str(search))

