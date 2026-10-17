<!-- .agents/rules/agent-behavior.md -->
# Agent Behavior, Workflow & Antigravity Optimizations

This document describes the operational workflow, autonomy limits, and delivery standards for AI coding agents in this project.

---

## 1. Core Principles (Outcome-over-Process)

1. **No Mandatory Upfront Plan Mode**:
   - For well-scoped tasks, begin implementation immediately based on a clear brief (Goal + Constraints + Definition of Done).
   - Forcing `/plan` introduces unnecessary friction; steering focuses on final outcomes and automated verification.
2. **Definition of Done is a Deterministic Check**:
   - Work is complete only when `make check` (linters, format check, and pytest suite) succeeds with exit code 0.
   - The agent always proves delivery with concrete command output rather than textual assertions.
3. **Hard Boundaries in Hooks, Not Prompts**:
   - Shouting instructions ("NEVER", "IMPORTANT") in prompts is unreliable.
   - Safety constraints (such as blocking autonomous `git commit` or `git push`) and quality rules (auto-formatting) are strictly enforced via deterministic scripts in `.agents/hooks.json`.
4. **Lean Context & Indexing**:
   - Root instructions (`AGENTS.md`) remain compact (< 50 lines). Deep context is loaded modularly on-demand via `.agents/rules/` or scoped subdirectories (`src/app/domain/AGENTS.md`).
5. **Skills Policy**:
   - Only build an Agent Skill in `.agents/skills/` when a specific recurring workflow cannot be handled autonomously by the model. Prevent skill bloat.

---

## 2. Gemini 3.8 Flash & Google Models in Antigravity

These guidelines are optimized for Gemini 3.8 Flash within the Google Antigravity environment:

### A. Speed, Token Efficiency & Thinking Defaults
- **No "Think Harder" Prompts**: Keep reasoning and effort settings at recommended defaults. Meta-prompts waste tokens and slow execution.
- **Concise & Direct**: Keep answers to-the-point (< 15 lines of explanation outside code blocks). Avoid conversational filler, apologies, or restating the prompt.

### B. Bounded Autonomy & Escalation (Retry Limit)
- **Focus**: Respect no-go zones; do not touch files outside the explicit task scope.
- **Max 3 Retries**: When encountering persistent failures during `make check` or tests, the agent attempts **at most 3 autonomous retries**. If unresolved after 3 attempts: stop immediately, display the literal error, and align with the user.

### C. Subagent Governance
- **Controlled Delegation**: Use subagents strictly for heavy parallel research or browser testing (`/browser`).
- **Context Isolation**: Subagents run in isolated contexts and return only a concise synthesis to prevent context poisoning and token quota drain.

### D. Delivery & Evidence (Tiered Proof Model)
- **Standard / Incremental Changes**: Provide terminal proof directly (`make check` output with passing tests and 0 warnings).
- **Structural / Architectural Changes**: Produce a **Walkthrough Artifact** containing:
  1. A concise Mermaid architecture or flow diagram.
  2. A summary of assumptions and architectural trade-offs.
  3. Deterministic verification output (`make check`).

---

## 3. Multi-Model Readiness (Future LLMs)
This configuration serves as the foundational standard. If switching to alternative models in the future (e.g. Claude Sonnet or Grok), model-specific nuances (such as unique tool-calling behaviors or prompt sensitivities) can be added as dedicated profile sections without disrupting the core architecture.
