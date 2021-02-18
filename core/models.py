from datetime import datetime
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer
from sqlalchemy.dialects.postgresql import JSONB

from .extensions import db


class BaseModel(db.Model):
    __abstract__ = True


class HistoryModel(BaseModel):
    __tablename__ = "history"

    id = Column("id", Integer, primary_key=True)
    result = Column(JSONB, nullable=False)
    queried_at = Column(DateTime, default=datetime.utcnow)
