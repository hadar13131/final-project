# server.py

import uvicorn

from api import app


def main() -> None:
    SERVER_IP = "10.14.52.17"
    SERVER_PORT = 1234
    uvicorn.run(app, host=SERVER_IP, port=SERVER_PORT)


if __name__ == '__main__':
    main()
