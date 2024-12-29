import reflex as rx
import os

database_url = os.getenv("DATABASE_URL", "sqlite:///repoapp1.db")

config = rx.Config(
    app_name="rx_app1",
    db_url=database_url,
)