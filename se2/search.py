from se2.documents import CloudDocument


def search(phrase,size=10,s=1):
    phrase = "*"+phrase+"*"    
    results = CloudDocument.search().query("query_string", query=phrase, fields=['ip','organization','common_name','sanip','sandns']).extra(size=size,from_=(int(s)*10-10))
    return results

#def search(phrase):
#    return get_search_query(phrase)
