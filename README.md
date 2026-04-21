# agentforge-sinks-plugin

Test-rig plugin for AgentForge event sinks (TAP-771).

Provides a deterministic `/api/sinks-test/emit` endpoint that fires events
onto the host app's `TopicBus`, letting the core smoke test verify that
`PostgresEventSinkProvider` and `TappsBrainEventSinkProvider` receive and
process events correctly.

## Structure

```
agentforge_sinks/
  __init__.py               # __version__ = "1.0.0"
  plugin.json               # plugin manifest
  plugin.py                 # register(app) — mounts router + loads agent
  routes.py                 # POST /api/sinks-test/emit
  agents/
    sinks_test_agent/
      AGENT.md
      runner.py             # SinksRunner.run() → "sinks:ok"
tests/
  test_runner.py
```

## Usage

Install into the AgentForge dev environment:

```bash
uv pip install -e /path/to/agentforge-sinks-plugin
```

The core smoke tests live in `backend/tests/test_sinks_smoke.py` and run
without the plugin installed. The route-level test
(`test_emit_route_triggers_sink`) is skipped automatically when the plugin
is not installed.
