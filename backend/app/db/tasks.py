from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL


async def connect_to_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=5)

    await database.connect()
    app.state.db = database


async def close_db_connection(app: FastAPI) -> None:
    await app.state.db.disconnect()
