import os

from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))