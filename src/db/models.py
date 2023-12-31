import uuid

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func, UUID, Text

from sqlalchemy.orm import relationship, DeclarativeBase


class CmsEntity(DeclarativeBase):
    # postgres
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    # sqlite
    id = Column(
        'id',
        String(length=128),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = Column(String(100))
    description = Column(String(256))
    create_at = Column(DateTime(timezone=True), index=True, server_default=func.now())
    create_by = Column(String(100))
    update_at = Column(DateTime(timezone=True), index=True, server_default=func.now())
    update_by = Column(String(100))
    deleted = Column(Boolean, default=False)


class CmsUsers(CmsEntity):
    __tablename__ = "users"

    username = Column(String(100), unique=True)
    password = Column(String(100), nullable=False)


class CmsPage(CmsEntity):
    __tablename__ = "cmspage"

    page_name = Column(String(100))


class CmsEndpoint(CmsEntity):
    __tablename__ = "cms_page"

    endpoint = Column(String(256))
