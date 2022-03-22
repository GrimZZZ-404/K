from dotenv import load_dotenv
from os import environ
load_dotenv()

Token: str = environ.get("TOKEN")
Owner_IDS: list[int] = [756258832526868541, 697323031919591454]