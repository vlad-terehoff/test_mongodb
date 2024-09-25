import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from typing import Annotated
from fastapi import Depends
from src.base.db_settings.db_helper import db_helper
from typing import AsyncContextManager


ISession = Depends(db_helper.get_session)