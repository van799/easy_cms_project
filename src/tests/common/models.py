from sqlalchemy import Column, String, Boolean

from src.db.db import Base


class TestCommon(Base):
    __tablename__ = "test_common"
    id = Column(
        'id',
        String(length=128),
        primary_key=True)
    deleted = Column(Boolean, default=False)
    test_str = Column(String)
