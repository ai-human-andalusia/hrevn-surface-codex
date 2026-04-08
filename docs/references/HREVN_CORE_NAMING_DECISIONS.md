# HREVN_CORE_NAMING_DECISIONS.md
## Consolidación de naming del núcleo técnico

### Decisión 1 — Antes de la acción
El output del pre-flight check debe llamarse:

**BaselineResult**

Se usa para:
- `profile_detected`
- `missing_required_blocks`
- `risk_flags`
- `readiness_level`
- `recommended_next_step`
- `remedy_payload`

### Decisión 2 — Después de la acción
El output post-acción visible al desarrollador debe llamarse:

**AER**  
(**Agentic Evidence Receipt**)

Internamente se puede mantener una clase como `ActionReceipt` o `AgenticEvidenceReceipt`
si facilita el tipado, pero de cara externa la nomenclatura recomendada es AER.

### Decisión 3 — Contextos internos del receipt
Mantener estos nombres:
- `agent_identity`
- `integrity_context`
- `action_context`
- `action_outcome`
- `metadata`

### Decisión 4 — Regla de consistencia
No usar indiscriminadamente:
- `receipt`
- `AER`
- `baseline result`

Fórmula correcta:
- **BaselineResult = antes**
- **AER = después**

### Decisión 5 — Multiplataforma
OpenAI, Anthropic y Google pueden cambiar el envoltorio, pero no el naming semántico del núcleo.
