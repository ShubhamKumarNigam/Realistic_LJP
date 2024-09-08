import csv
import time
import openai
import csv
openai.api_key="<Put Your API-KEY HERE>"
#openai.api_key="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"
import os
file1=open("/home/judgement.xlsx","r")
#print(file1.read())
csv_file=csv.reader(file1)
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('/home/judgement.xlsx')

#print(dataframe1)


lll=csv_file
v=[]
c=0


f = open('judgement.csv', 'w')

# create the csv writer
writer = csv.writer(f)
writer.writerow(["Id","Answer"])



f = open('judgement2.txt', 'w')

# create the csv writer
#writer = csv.writer(f)
#writer.writerow(["answer"])
count=0
print(dataframe1.keys())
print(dataframe1['Unnamed: 1'])
count=0
for i in dataframe1['Unnamed: 1']:
    count=count+1
    if count==1:
        continue
    else:
        print(i)
    temp_summary2="You are asked to be a judge of a legal case and provide a judgment of the following legal judgment:- {"+str(i)+"}"
            #try:
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content":temp_summary2}],
                temperature=0.7,
                max_tokens=500,
                stop=None
                )
            #except:
            #    cc=0
            #temp_summary=temp_summary+parsed
           # response = openai.Completion.create(
          #  model="text-davinci-003",
          #  prompt="{"+temp_summary2+"}"+"Tl;Dr",
          #  temperature=0.7,
          #  max_tokens=ratio,
          #  top_p=1.0,
          #  frequency_penalty=0.0,
          #  presence_penalty=1
          #  )

    for choice in response.choices:
                print(choice)
                #if "text" in choice:
                #    print(choice.text)
                writer.writerow([count-1,choice["message"]["content"]])
   # f.write("------------------------------------------------------------------------------------------------------------------\n")
   # f.write("------------------------------------------------------------------------------------------------------------------\n")
   # f.write("------------------------------------------------------------------------------------------------------------------\n")

                #print(choice["message"]["content"])
           # llllll.write(str(response["choices"][0]["text"]))
                #print("---------------")
                #print(temp[0])
                #print("----")
                #print(choice["message"]["content"])
                #print("----")
                #print(temp_summary2)
                #print("-------------------------")

#for lines in lll:
#    print(lll[1])
'''
    count=count+1
    if count==1:
        continue
    else:
        print(lines[4])
        print(type(lines[4]))
        if type(lines[4])=="<class 'str'>":
            print(1)

        writer.writerow(["`:wq123abc",lines[4]])
    #count=count+1

#    f = open('final5.csv', 'w')

# create the csv writer
#writer = csv.writer(f)
#writer.writerow(["id","span","span2"])

#    print(str(lines[4]))

    #v.append(lines[4])
#print(str(0))
#print(len(v))

#for i in lll:
#    print(i)
'''
