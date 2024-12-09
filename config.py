from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="DB_")

class Settings(BaseSettings):
    db: DatabaseConfig = DatabaseConfig()

settings = Settings()
