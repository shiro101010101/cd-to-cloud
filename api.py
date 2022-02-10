from fastapi import FastAPI
#add comment add awesome stuff
app = FastAPI()


@app.get("/")
def root():
    return "Hello from Cloud Run CD"
