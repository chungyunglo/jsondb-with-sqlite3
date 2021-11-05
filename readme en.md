# Jsondb with sqlite3
Json (save to/read from) database  
script by chungyunglo

## Introduce
This is to use database (hereinafter referred to as db) as a substitute for json. If you can write db, it is very good. It is recommended that you can write by yourself for better results.

## Purpose
At first, I wrote discord bot with replit hosting. When storing data using json, it will be restored by replit from time to time. Later, I tried to use jsonstorage and use requests for online storage, but once I found that jsonstorage would have a brief occasion , Two days will be unable to connect (should be maintenance), so try to use db instead to prevent instability.

## Method to use(Module Document)

### ▼Import module
```python
import jsondbsqlite3 as db
```
Please place the file in the same folder as the main file (or a directory area that can be imported to).

### ▼Open file/Connect DB
```python
b = db.op(file )
```
The basic is the same as sqlite3, to connect to the file (db).
- `file`:(str )File name.

### ▼Create execute cursor
```python
c = db.cur(b )
```
Create a cursor for execute.
- `b`:(sqlite3.connection )Connected database variables.

### ▼Create Table
```python
db.create_table(b, c)
```
Create a table to store json.
- `b`:(sqlite3.connection )Connected database variables.
- `c`:(sqlite3.cursor )The cursor used for execution variables.

### ▼Create json
```python
db.create_json(b, c, name, value={})
```
Create a json, just like post.
- `b`:(sqlite3.connection )Connected database variables.
- `c`:(sqlite3.cursor )The cursor used for execution variables.
- `name`:(str )Json's (file) name.
- `value`={}:(list, tuple, dict)Json's value.

### ▼Read(Load) json
```python
data = db.read_json(c, name)
```
Read json, just like get.
- `c`:(sqlite3.cursor )The cursor used for execution variables.
- `name`:(str )Json's (file) name. 
**>Return**
- `value`:(list, tuple, dict)Json's value.

### ▼Update json
```python
db.dump_json(b, c, name, value)
```
Update json data, just like put.
- `b`:(sqlite3.connection )Connected database variables.
- `c`:(sqlite3.cursor )The cursor used for execution variables.
- `name`:(str )Json's (file) name.
- `value`:(list, tuple, dict)Json's value.

### ▼Remove(Delete) json
```python
db.del_json(b, c, name)
```
Delete json.
- `b`:(sqlite3.connection )Connected database variables.
- `c`:(sqlite3.cursor )The cursor used for execution variables.
- `name`:(str )Json's (file) name.

### ▼All json
```python
aj = db.alljson(c )
```
List all json files.
- `c`:(sqlite3.cursor )The cursor used for execution variables.  
**>Return**
- `list`:(list )ALL Json's (file) name list.

### ▼Close connection of DB
```python
db.close(b )
```
It is not necessary to close the database, but it is recommended.
- `b`:(sqlite3.connection )Connected database variables.


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
