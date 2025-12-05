from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    model_path: str = "model.pkl"
    model_version: str = "v1.0.0"
    target_names: list[str] = ["setosa", "versicolor", "virginica"]


settings = Settings()