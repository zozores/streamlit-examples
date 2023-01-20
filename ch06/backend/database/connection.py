import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self, db_uri):
        self.engine = db.create_engine(db_uri)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def use_session(self):
        self.session = self.SessionLocal()
        return self.session

    def execute_query(self, query):
        result = self.engine.execute(query)
        return result
