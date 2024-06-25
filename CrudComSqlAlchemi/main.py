from fastapi import FastAPI
from core.configs import settings
from CrudComSqlAlchemi.api.v1.api import api_router

app = FastAPI(title="FastAPI com SQLAlchemy", version="0.1")
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,log_config="info", reload=True)
