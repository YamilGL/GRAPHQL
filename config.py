from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

HOST = os.getenv('HOST','localhost')
PORT = os.getenv('PORT',5000)
ENV = os.getenv('ENV','DEV')