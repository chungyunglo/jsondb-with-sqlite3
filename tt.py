import jsondbsqlite3 as db

b=db.op("dd.db")
c=db.cur(b)
try:db.create_table(b,c)
except:pass
data= {"data":"value","key":"value2"}
db.dump_json(b,c,'na',data)
ndata=db.read_json(c,'na')
print(ndata['data'])
# db.del_json(b,c,'na')
# db.create_json(b,c,'na',data)
db.alljson(c)
db.close(b)