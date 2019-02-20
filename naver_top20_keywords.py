# naver 실시간 검색어 추출
f = open("naver_source_190204.txt")
tx = f.readlines()
f.close()

# ver1
for s in tx:
    if "ah_k" in s:
        print(s[19:-8])

len('<span class="ah_k">')

# ver2
keys = []
for s in tx:
    if "ah_k" in s:
        keys.append(s[19:-8])
keys

# ver3
keys = [s[19:-8] for s in tx if "ah_k" in s]
