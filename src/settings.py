from os.path import join, dirname

from dotenv import load_dotenv
from pydantic import BaseSettings

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


class Settings(BaseSettings):
    DATA_DIR: str = join(dirname(__file__), '../data')
    # Logger
    LOGGER_LEVEL: str
    LOG_SAVE_DIR: str = join(dirname(__file__), '../data/logs')

    # class Config:
    #     case_sensitive = True
    #     _base_dir = os.path.dirname(os.path.abspath(__file__))
    #     env_file = f'{_base_dir}/../.env'


settings = Settings()
