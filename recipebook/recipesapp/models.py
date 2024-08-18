from sqlalchemy import create_engine, text

master_engine = create_engine("mssql+pymssql://sa:!Abc123!@recipebook-db-1:1433/recipebook")
def sqlExecute(query, mode):
    with master_engine.connect() as conn:
        if mode == 'write':
            with conn.begin():
                conn.execute(text(query))
        else:
            # mode == read
            result = conn.execute(text(query))
            return result.fetchall()
        return
COLUMN_RECIPE = ('recipe_id', 'name', 'ingredients', 'steps', 'preparation_time')
COLUMN_RATING = ('rating_id', 'recipe_id', 'rating', 'user_id')
COLUMN_COMMENT = ('comment_id','recipe_id','comment_text','user_id')
COLUMN_USER = ('user_id','username','password')