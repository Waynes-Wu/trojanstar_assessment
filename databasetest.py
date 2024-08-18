from sqlalchemy import create_engine, text

master_engine = create_engine("mssql+pymssql://sa:!Abc123!@localhost:1433/recipebook")
result = ''

with master_engine.connect() as conn:
    with conn.begin():
    # if True:
        sql_script = """
        UPDATE recipe
        SET 
            name = '1',
            ingredients = '1',
            steps = '1',
            preparation_time = preparation_time + 1
        WHERE recipe_id = 11
    """
        result = conn.execute(text(sql_script))
    
    # rows = result.fetchall()
    # for row in rows:
    #     print(rows)
    # print('done')

