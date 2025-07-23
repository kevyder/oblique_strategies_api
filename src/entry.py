from fastapi import FastAPI


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
