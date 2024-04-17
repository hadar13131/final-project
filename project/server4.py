# server.py

import uvicorn

from api4 import app


def main() -> None:
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 1234
    uvicorn.run(app, host=SERVER_IP, port=SERVER_PORT)


if __name__ == '__main__':
    main()
