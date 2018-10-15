from lxml import etree

def write_likers_file(driver):
    f = open("likers.html", "a")
    f.write(driver.page_source)
    f.close()

def save_likers(html, page_name: str):
    tree = etree.HTML(html)
    results = tree.xpath("//div[@data-testid='browse-result-content']")
    for result in results:
        try:
            link = result.xpath(".//a[@class='_32mo']/@href")[0]
            text = result.xpath(".//a[@class='_32mo']/span/text()")[0]
            print(text)
        except:
            print("oops, something went wrong parsing the html")
    
    print("Saving complete")