"""
from https://sqlmodel.tiangolo.com/tutorial/

Here I added my own notes while following the tutorial.
""" 


from sqlmodel import Field, SQLModel, Session, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database_fromcode.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)



def create_db_and_tables():
    # - `metadata` has the Hero table registered because 
    #   of the use of `table=True`
    # - the line below creates the file + the table
    # - this statement is inside a function because otherwise
    #   tables would be attempted to be created every time 
    #   someone imports this module   
    SQLModel.metadata.create_all(engine)

def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    # From the docs, "create a new session for each 
    # group of operations with the database that belong together"
    # (in web app - single session per request)
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit() # this is the line that pushes the statements to db


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()