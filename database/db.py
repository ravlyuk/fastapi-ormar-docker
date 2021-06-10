import databases
import ormar
import sqlalchemy
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
db_path = os.environ["DATABASE_URL"]

metadata = sqlalchemy.MetaData()  # дозволяє використовувати sqlalchemy
database = databases.Database(db_path)  # для асинхронних запитів
engine = sqlalchemy.create_engine(db_path)


class MainMeta(ormar.ModelMeta):  # для роботи з core sqlalchemy та генерації SQL запитів
    metadata = metadata
    database = database
