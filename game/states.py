# A collection of game states
from __future__ import annotations
import attrs
import tcod.console
import tcod.event

import g
from game.components import Gold, Graphic, Position
from game.constants import DIRECTION_KEYS
from game.tags import IsItem, IsPlayer


# Primary in-game state
@attrs.define()
class InGame:
    # Handle events for the in-game state
    def on_event(self, event: tcod.event.Event) -> None:
        (player,) = g.world.Q.all_of(tags=[IsPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                player.components[Position] += DIRECTION_KEYS[sym]
                # Auto pickup gold
                for gold in g.world.Q.all_of(
                    components=[Gold], tags=[player.components[Position], IsItem]
                ):
                    player.components[Gold] += gold.components[Gold]
                    text = f"Picked up {gold.components[Gold]}g, total: {player.components[Gold]}g"
                    g.world[None].components[str] = text
                    gold.clear()

    # Draw the standard screen
    def on_draw(self, console: tcod.console.Console) -> None:
        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y < console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.y, pos.x] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(
                x=0,
                y=console.height - 1,
                string=text,
                fg=(255, 255, 255),
                bg=(0, 0, 0),
            )
