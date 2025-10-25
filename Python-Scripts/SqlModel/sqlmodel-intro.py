# from https://sqlmodel.tiangolo.com/tutorial/
from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database_fromcode.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


# - `metadata` has the Hero table registered because 
#   of the use of `table=True`
# - the line below creates the file + the table  
SQLModel.metadata.create_all(engine)