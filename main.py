from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

import g
import game.states
import game.world_tools


def main() -> None:
    # Entry point function
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png",
        columns=16,
        rows=16,
        charmap=tcod.tileset.CHARMAP_CP437,
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 50)
    state = game.states.InGame()
    g.world = game.world_tools.new_world()
    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while True:
            console.clear()
            state.on_draw(console)
            g.context.present(console)
            for event in tcod.event.wait():
                print(event)
                state.on_event(event)  # Pass events to the state


if __name__ == "__main__":
    main()
