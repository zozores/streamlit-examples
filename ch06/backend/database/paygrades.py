from sqlalchemy import Column, Integer, String
from .base import Base


class Paygrades(Base):
    __tablename__ = "paygrades"
    id = Column(Integer, primary_key=True)
    base_salary = Column(String)
    reimbursement = Column(String, default=True)
    bonuses = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "base_salary": self.base_salary,
            "reimbursement": self.reimbursement,
            "bonuses": self.bonuses,
        }
