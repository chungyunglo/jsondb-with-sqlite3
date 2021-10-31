

import sqlite3,json

# class jsondbsqlite3:
#     import sqlite3,json
#     #內有連接檔案與建立TABLE
    
def op(file:str) :
    '''Connect to sql'''        
    try:        conn=sqlite3.connect(file)
    except Exception as a:
        print(a)
        return
    else:           print(f'Connected to {file} Database successfully .')
    return conn
    # Table偵測(name已存在)與建立，並撰寫table name var

def cur(b):
    '''execute.box'''
    return b.cursor()
    
def create_table(b,c):
    '''create fold for json'''
    try:        c.execute(f"""CREATE TABLE JSON(name text,value text)""")
    except Exception as a:
        print('Maybe there is a table created.If true, you can remove this command.')
        print(a)
    else:
        b.commit()

# # 建立json(post)，並且偵測是否已建立過檔案(name已存在)
def create_json(b,c,name,value={}):
    '''post json'''
    if name in alljson(c):        print(f'The name {name} had one in file.')
    else:
        try:        values=json.dumps(value)
        except Exception as a: 
            print("Jsondecode error")
            print(a)
            return
        else:
            try:c.execute(f"INSERT INTO JSON VALUES ('{name}','{values}')")
            except Exception as a:     
                print(a)
                return
            else:        
                print(f'Created jsonfile {name} successfully.')
                b.commit()
        return

# # 讀取json(get)，讀取失敗問題(name不存在)
def read_json(c,name:str):
    '''get json'''
    if name in alljson(c):  
        try:        re=c.execute(f'''SELECT value FROM JSON WHERE name='{name}' ''')
        except Exception as a:
            print(a)
            return
        else:
            try:                value=json.loads([i[0] for i in re][0])
            except Exception as a:
                print([i[0] for i in re][0])
                print("Jsondecode error")
                print(a)
                return
            else:
                print(f'Got jsonfile {name} successfully.')
                print(value) 
    else:
        print('No data.')
        value=None
    return value


# # 更新/寫入json(put)，寫入失敗問題(name不存在)
def dump_json(b,c,name:str,value):
    '''put json'''
    if name in alljson(c):
        try:            values=json.dumps(value)
        except Exception as a: 
            print("Jsondecode error")
            print(a)
            return
        else:
            try:      c.execute(f'''UPDATE JSON SET value='{values}' WHERE name='{name}' ''')
            except Exception as a:     
                print(a)
                return
            else:        
                b.commit()
                print(f'Put jsonfile {name} successfully.')
        
    else:print('No data.')
    return

# # 刪除json，刪除失敗問題(name不存在)
def del_json(b,c,name:str):
    '''remove json'''
    if name in alljson(c):
        c.execute(f'''DELETE FROM JSON WHERE name='{name}' ''')
        b.commit()
        print(f'Deleted jsonfile {name} successfully.')
    else:print('No data.')
    return

def alljson(c)->list:
    '''json list'''
    a=[ i[0] for i in ( c.execute('''SELECT name from JSON''') ) ]
    print(a)
    return a

def close(b):
    '''close connect'''
    b.close()
    print('Closed.')
