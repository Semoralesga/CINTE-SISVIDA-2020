# coding=utf-8
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer
import time


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(String)
    updated_at = Column(String)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now().strftime('%s')+'123'
        self.updated_at = datetime.now().strftime('%s')+'123'
        self.last_updated_by = created_by