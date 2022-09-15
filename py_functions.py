import pandas as pd

def get_all(conn):
    query1 = 'SELECT * FROM emp_table ;'
    df = pd.read_sql(query1, conn)
    return df



def count_by_dept(conn):
    query1 = 'SELECT emp_dept, COUNT(*) FROM emp_table GROUP BY emp_dept;'
    df = pd.read_sql(query1, conn)
    return df


def fetch_emp_by_condition(conn, empName, condition):
    # conditions ->  startWith   or  endsWith  or  like or caseSensitive  or  caseInsensitive

    if condition == 'startWith':
        query =  'SELECT emp_name ,emp_dept FROM emp_table WHERE emp_name like "{}%";'.format(empName)
    elif condition == 'endsWith':
        query =  'SELECT emp_name ,emp_dept FROM emp_table WHERE emp_name like "%{}";'.format(empName)
    elif condition == 'like':
        query = 'SELECT emp_name ,emp_dept FROM emp_table WHERE emp_name like  "%{}%";'.format(empName)
    elif condition == 'caseSensitive':
        query = 'SELECT emp_name ,emp_dept FROM emp_table WHERE emp_name = BINARY"{}";'.format(empName)
    elif condition == 'caseInsensitive':
        query = 'SELECT emp_name ,emp_dept FROM emp_table WHERE emp_name = "{}";'.format(empName)
    else:
        print(" Please Choose  COndition among -- startWith   or  endsWith  or  like or caseSensitive  or  caseInsensitive")
        return pd.DataFrame({'WRONG INVALID'})

    df = pd.read_sql(query, conn)
    return df

def add_entry(conn,emp_n,dept):
    cursor = conn.cursor()
    insert_query = ''' INSERT INTO emp_table (emp_name, emp_dept) VALUES (?,?);'''
    values = (emp_n, dept)
    cursor.execute(insert_query, values)
    return 1