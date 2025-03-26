# This module stores globally mutable variables use by this program.
from __future__ import annotations

import tcod.context
import tcod.ecs

context: tcod.context.Context  # The window manages by tcod.
world: tcod.ecs.Registry  # The active ECS registry and current session.
