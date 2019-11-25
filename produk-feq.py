#import
import sys
import subprocess
import json

#check argumen
if len(sys.argv) !=3 :
    print ("\n\nPenggunaan\n\tproduk-freq.py [dirData] [OutputFile]\n")
    sys.exit(1)

#Argumen store
sourceData = sys.argv[1]
ouputFile = sys.argv[2]

#get list file from source data
lists = str(subprocess.getoutput("ls "+sourceData+" -v"))
list_file = lists.split("\n") 

#dictionary
produk = {}


for file in list_file :
    #read file
    print("read data: "+file)
    file = open(sourceData+"/"+file).read()
    list_data = file.split("\n")
    
    for data in list_data :
        if (data == ""):
            continue
        content = json.loads(data) # load json
        
        if content['asin'] in produk :
            produk[str(content['asin'])]["total"] += 1
        else :
            x = {
            "total" : 1,
            "positif" : 0,
            "netral" : 0,
            "negatif" : 0,
            "score" : 0
            }
            produk[str(content['asin'])] = x
        
        if content['overall'] > 3.0 :
            produk[str(content['asin'])]['positif'] +=1
        elif content['overall'] == 3.0 :
            produk[str(content['asin'])]['netral'] +=1
        else :
            produk[str(content['asin'])]['negatif'] +=1

#check score
count= 0        
for x in produk :
    count+=1
    score = produk[x]['total'] + produk[x]['positif'] - produk[x]['negatif']
    produk[x]['score'] = score;

#make output
output = open(ouputFile+".json", 'w+')
print("output : "+ouputFile+".json")
i= 0
for x in sorted(produk.items(), key = lambda kv:(kv[1]['score']), reverse=True) :
    output.write("{\"produk\": \""+x[0]+"\", ")
    output.write("\"total\": "+str(x[1]['total'])) 
    output.write(", ")
    output.write("\"positif\": "+str(x[1]['positif']))
    output.write(", ")
    output.write("\"netral\": "+str(x[1]['netral'])) 
    output.write(", ")
    output.write("\"negatif\": "+str(x[1]['negatif']))
    output.write(", ")
    output.write("\"score\": "+str(x[1]['score']))
    output.write("}")

    i+=1
    if (i < count) :
        output.write("\n")

output.close()
