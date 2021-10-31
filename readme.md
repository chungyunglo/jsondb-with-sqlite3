# Jsondb with sqlite3
Json (save to/read from) database  
script by chungyunglo

## 簡介
這是為了以database(以下簡稱db)作為json使用的替代品，若您會寫db則很好，建議您可以自行撰寫效果較佳。

## 目的
起初寫discord bot用replit代管，存儲資料會使用json時，會不定時被replit還原回朔資料，而後來嘗試有用jsonstorage並使用requests做線上存儲，但又因為一次發現jsonstorage會有短暫的偶爾一天兩天會無法連線（應該是維護），所以嘗試在改用db來防止不穩定性。

## 使用方法(Module Document)

### ▼導入模組
```python
import jsondbsqlite3 as db
```
請將檔案放置在與主檔案同資料夾(或可以import到的目錄區)

### ▼打開檔案/連接資料庫
```python
b = db.op(file )
```
基礎的還是跟sqlite3一樣，要連接檔案
- `file`:(str )檔案名稱

### ▼建立執行游標
```python
c = db.cur(b )
```
建立給execute要用的游標
- `b`:(sqlite3.connection )連線的資料庫變數

### ▼建立表格
```python
db.create_table(b, c)
```
建立存放json的表格
- `b`:(sqlite3.connection )連線的資料庫變數
- `c`:(sqlite3.cursor )執行游標

### ▼建立json
```python
db.create_json(b, c, name, value={})
```
創建一個json，如同post
- `b`:(sqlite3.connection )連線的資料庫變數
- `c`:(sqlite3.cursor )執行游標
- `name`:(str )Json檔案名稱
- `value`={}:(list, tuple, dict)json值

### ▼讀取json
```python
data = db.read_json(c, name)
```
讀取json，如同get
- `c`:(sqlite3.cursor )執行游標
- `name`:(str )Json檔案名稱
return回傳
- `value`={}:(list, tuple, dict)json值

### ▼更新json
```python
db.dump_json(b, c, name, value)
```
更新json資料，如同put
- `b`:(sqlite3.connection )連線的資料庫變數
- `c`:(sqlite3.cursor )執行游標
- `name`:(str )Json檔案名稱
- `value`={}:(list, tuple, dict)json值

### ▼刪除json
```python
db.del_json(b, c, name)
```
刪除json
- `b`:(sqlite3.connection )連線的資料庫變數
- `c`:(sqlite3.cursor )執行游標
- `name`:(str )Json檔案名稱

### ▼所有json
```python
aj = db.alljson(c )
```
列出所有json檔案
- `c`:(sqlite3.cursor )執行游標
return回傳
- `list`:(list )所有json檔案列表

### ▼關閉資料庫連線
```python
db.close(b )
```
關閉資料庫，可以不用，但建議使用。
- `b`:(sqlite3.connection )連線的資料庫變數


## 範例
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
