---
name: sinks-test-agent
namespace: project.sinks-test.sinks-test-agent
description: Test agent for AgentForge event sinks rig — emit events, verify sink delivery.
keywords: [sinks, events, test]
---

# Sinks Test Agent

Deterministic test fixture for the event sinks rig (TAP-771).

Exists to exercise `AgentLoader.load_external()`, namespace registration under
`project.sinks-test`, and the plugin registration surface without any LLM or
external service dependency.
