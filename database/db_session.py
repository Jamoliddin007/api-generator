# database/db_session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# 📥 .env faylni yuklaymiz
load_dotenv()

# 🔌 PostgreSQL uchun ulanish URL'si
DATABASE_URL = (
    f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
    f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
)

# 🏗️ Engine — SQLAlchemy motor
engine = create_engine(DATABASE_URL)

# 🧱 Base — barcha modellar shu asosdan meros oladi
Base = declarative_base()
