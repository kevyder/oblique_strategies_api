import asgi

from typing import Optional

from fastapi import FastAPI, HTTPException, Query

from strategies.in_memory import InMemoryStrategyProvider

# Singleton instance of the strategy provider
strategy_provider = InMemoryStrategyProvider()


async def on_fetch(request, env):
    return await asgi.fetch(app, request, env)


app = FastAPI(title="Oblique Strategies API")


@app.get("/")
async def home():
    return {
        "title": "Oblique Strategies API",
        "description": "An API based on Brian Eno and Peter Schmidt's Oblique Strategies",
        "endpoints": ["/random", "/strategies", "/strategies/{id}"],
    }


@app.get("/random")
async def random_strategy(lang: Optional[str] = Query("en", enum=["en", "es"])):
    """Get a random strategy in the specified language"""
    strategy = strategy_provider.get_random()
    if not strategy:
        raise HTTPException(status_code=404, detail="No strategies available")
    return {"id": strategy.id, "strategy": strategy.get_text(lang)}


@app.get("/strategies")
async def list_strategies(lang: Optional[str] = Query("en", enum=["en", "es"])):
    """Get all strategies in the specified language"""
    strategies = strategy_provider.get_all()
    return {
        "total": len(strategies),
        "strategies": [{"id": s.id, "strategy": s.get_text(lang)} for s in strategies],
    }


@app.get("/strategies/{id}")
async def get_strategy(id: int, lang: Optional[str] = Query("en", enum=["en", "es"])):
    """Get a specific strategy by ID in the specified language"""
    strategy = strategy_provider.get_by_id(id)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return {"id": strategy.id, "strategy": strategy.get_text(lang)}
