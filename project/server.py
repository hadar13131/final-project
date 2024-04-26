# server.py

import uvicorn

from api import app

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

def main() -> None:
    uvicorn.run(app, host=SERVER_IP, port=SERVER_PORT)


if __name__ == '__main__':
    main()
