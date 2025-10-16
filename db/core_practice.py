from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")

with engine.connect() as connection_obj:
    res = connection_obj.execute(text("select 'hello world'"))
    print(res.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    res = connection_obj.execute(text("select * from some_table"))
    print(res.all())
    conn.commit()