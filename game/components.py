# Collection of common components
from __future__ import annotations

from typing import Final, Self

import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity


@attrs.define(frozen=True)
class Position:
    # An entities position
    x: int
    y: int

    # Add a vector to this position
    def __add__(self, direction: tuple[int, int]) -> Self:
        x, y = direction
        return self.__class__(self.x + x, self.y + y)


# Mirror position components as a tag
@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changes(
    entity: Entity, old: Position | None, new: Position | None
) -> None:
    if old == new:
        return
    if old is not None:  # entity.tags is outdated and must be removed
        entity.tags.discard(old)
    if new is not None:  # new is the up-to-date value to be tracked by entity.tags
        entity.tags.add(new)


@attrs.define(frozen=True)
class Graphic:
    # An entities icon and color
    ch: int = ord("!")
    fg: tuple[int, int, int] = (255, 255, 255)


# Amount of gold
Gold: Final = ("Gold", int)
