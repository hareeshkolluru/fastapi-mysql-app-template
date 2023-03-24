import json
import os

from decouple import config

# config = AutoConfig(search_path=os.path.join(os.getcwd(), "helloworldapp"))
ENV = config("ENV", cast=str, default="dev")

# fastapi
PROJECT_NAME = "helloworldapp"
API_V1_STR = "v1"
PORT = config("PORT", cast=int, default=8888)
URL = config("URL", default="0.0.0.0")

# Logging
LOGGER_NAME = "helloworldapp"
LOG_LEVEL = config("LOG_LEVEL", default="DEBUG")
LOG_COLORIZE = config("LOG_COLORIZE", cast=bool, default=False)
