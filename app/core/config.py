from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_NAME: str

    public: str
    secret: str
    s3_endpoint: str
    s3_port: str
    s3_region: str
    s3_bucket_name: str

    @property
    def db_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def get_access_key(self):
        return self.public

    @property
    def get_secret_access_key(self):
        return self.secret
    
    @property
    def get_s3_endpoint(self):
        return self.s3_endpoint
    
    @property
    def get_s3_port(self):
        return self.s3_port
    
    @property
    def get_s3_region(self):
        return self.s3_region
    
    @property
    def get_s3_bucket_name(self):
        return self.s3_bucket_name

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore
