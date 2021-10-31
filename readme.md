# Jsondb with sqlite3
Json (save to/read from) database  
script by chungyunglo

## Document
You can have your lang document.
Here are En and Zh.
More Introduce in there.

## Example
tt.py
```python
import jsondbsqlite3 as db

b=db.op("dd.db")
c=db.cur(b)
db.create_table(b,c)
data= {"data":"value","key":"value2"}
db.create_json(b,c,'na',data)
db.dump_json(b,c,'na',data)
ndata=db.read_json(c,'na')
# print(ndata['data'])
db.del_json(b,c,'na')
aj=db.alljson(c)
db.close(b)
```
