from sqlalchemy import Column, String

from db.models import CmsEntity


class TestCommon(CmsEntity):
    __tablename__ = "test_common"

    test_str = Column(String)
