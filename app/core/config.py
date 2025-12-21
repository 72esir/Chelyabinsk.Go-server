from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_NAME: str

    private_key_path: Path = BASE_DIR/"certs"/"jwt-private.pem"
    public_key_path: Path = BASE_DIR/"certs"/"jwt-public.pem"
    algorithm: str = "RS256"

    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    @property
    def db_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def private_key(self):
        return self.private_key_path

    @property
    def public_key(self):
        return self.public_key_path

    @property
    def get_algorithm(self):
        return self.algorithm

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore
