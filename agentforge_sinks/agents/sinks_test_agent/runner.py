"""Deterministic runner for sinks-test-agent. No side effects."""

from __future__ import annotations


class SinksRunner:
    def run(self) -> str:
        return "sinks:ok"
