lines = open("regexpr_example.txt").readlines()

re.search("http.{20,100}\.jpg", lines[20])
re.search("http.{20,100}\.jpg", lines[20]).group()
re.search("http.{20,100}\.jpg", lines[1]).group()

re.search("http.{20,100}\.jpg", lines[1]) == None
re.search("http.{20,100}\.jpg", lines[20]) == None

urls = []
for s in lines:
    ss = re.search("http.{20,100}\.jpg", s)
    if ss != None:
        urls.append(ss.group())
urls

df_urls = pd.DataFrame({"obs": range(len(urls)),
                        "url": urls})
df_urls.head(2)
