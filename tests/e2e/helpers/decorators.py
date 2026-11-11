"""
tests/e2e/helpers/decorators.py
Decorators for tagging E2E tests with Tier (1-4) and Feature (R1-R5).
"""
import functools
from typing import Any, Callable, List, Union

def tier(level: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Annotates a test method with its tier level (1, 2, 3, or 4)."""
    if level not in (1, 2, 3, 4):
        raise ValueError(f"Tier level must be 1, 2, 3, or 4; got {level}")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        setattr(func, "__tier__", level)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        setattr(wrapper, "__tier__", level)
        return wrapper

    return decorator

def feature(req: Union[str, List[str]]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Annotates a test method with requirement tags (e.g. 'r1', 'r2', 'r3', 'r4', 'r5', 'multi')."""
    reqs = [req] if isinstance(req, str) else list(req)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        setattr(func, "__feature__", reqs)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        setattr(wrapper, "__feature__", reqs)
        return wrapper

    return decorator
