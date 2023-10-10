from __future__ import annotations

from typing import Any

from lark import Transformer, v_args, Discard
from lark.tree import Meta

__all__ = ("PhysthonParser",)

@v_args(inline=True, meta=True)
class PhysthonParser(Transformer):
    WS = lambda *_: Discard

    def module(self, _: Meta, *items: Any) -> None:
        ...
