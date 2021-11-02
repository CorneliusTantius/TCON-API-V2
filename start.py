import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run("Server.startup:program", host="127.0.0.1", port=5000, reload=True)
    os.system("pyclean . -q")