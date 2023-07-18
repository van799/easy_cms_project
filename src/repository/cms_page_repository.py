from core.base.repository_base import RepositoryBase
from db.models import CmsPage


class CmsPageRepository(RepositoryBase):
    def __init__(self, engine):
        super().__init__(engine, CmsPage)
