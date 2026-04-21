"""Unit tests for SinksRunner."""

from agentforge_sinks.agents.sinks_test_agent.runner import SinksRunner


def test_runner_returns_sinks_ok() -> None:
    runner = SinksRunner()
    assert runner.run() == "sinks:ok"
