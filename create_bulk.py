__author__ = 'Asus'
import json
import codecs

bulkFileName="bulk.txt"
index="blog_index"

bulkFile = codecs.open(bulkFileName,'w+','utf-8')

fileNames=["techcrunch.json","engadget.json","cnet.json"]

for fileName in fileNames:
    jfile=open(fileName,"r")
    jstr=jfile.read()
    blog=json.loads(jstr)

    idx=0
    for page in blog:
        bulkFile.write('{ "create": { "_index": "blog_index", "_type": "doc"}}\n')
        bulkFile.write('{"doc_id": "'+page["sitename"]+"_"+str(idx)+'"')
        bulkFile.write(', "url" : "'+page["url"]+'"')
        bulkFile.write(', "sitename" : "'+page["sitename"]+'"')
        bulkFile.write(', "datetime" : "'+page["datetime"]+'"')
        bulkFile.write(', "body" : "'+page["body"]+'"')
        bulkFile.write(', "title" : "'+page["title"]+'"')
        bulkFile.write('}\n')
        idx+=1

