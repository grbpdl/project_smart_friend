from csv import writer
list_data=['S.N','Name','Crush_name','Mail']

with open('namemail.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(list_data)  
    f_object.close()