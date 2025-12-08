from fastapi import FastAPI , Body
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uvicorn
from dcf import Stock

app = FastAPI()
#api shits


@app.post("/api/get-ticker")
def get_ticker(user_query:dict = Body()):
    payload = user_query.get("user_query")
    stock = Stock.getTicker(query=payload)
    return stock





#spa setup
build_dir = Path(__file__).parent.parent / "frontend" / "build"


app.mount("/_app", StaticFiles(directory=build_dir / "_app"), name="_app")

app.mount("/immutable", StaticFiles(directory=build_dir / "_app" / "immutable"), name="immutable")


#  Fallback to index.html for all other routes (SPA routing)
@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    return FileResponse(build_dir / "index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
