from sqlalchemy import Column, String

from src.db.db import Base


class TestCommon(Base):
    __tablename__ = "test_common"
    id = Column(
        'id',
        String(length=128),
        primary_key=True)
    test_str = Column(String)
