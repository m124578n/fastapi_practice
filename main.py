import uvicorn

from src.main import app

uvicorn.run(
    app,
    host="0.0.0.0",
    port=8000,
    # use_colors=True,
    # log_level="warning",
)
