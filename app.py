from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SecureGate demo app"}


@app.get("/health")
def health():
    return {"status": "healthy"}