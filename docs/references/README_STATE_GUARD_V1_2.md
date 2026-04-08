
# HREVN State Guard v1.2

## Qué añade respecto a v1.1
- manifest de artefactos por ejecución
- receipt schema JSON
- naming más estable para handoff
- contrato todavía más claro para sustituir mocks por runners reales

## Archivos
- `HREVN_STATE_GUARD_V1_2.py`
- `HREVN_STATE_GUARD_V1_2_TESTS.py`
- `HREVN_STATE_GUARD_RECEIPT_SCHEMA_V1_2.json`
- `README.md`

## Ejecución demo
```bash
python HREVN_STATE_GUARD_V1_2.py success
python HREVN_STATE_GUARD_V1_2.py failure
python HREVN_STATE_GUARD_V1_2.py strict-block
python HREVN_STATE_GUARD_V1_2.py all
```

## Tests
```bash
python HREVN_STATE_GUARD_V1_2_TESTS.py
```

## Idea
Esta versión ya está pensada para acercarse al handoff a Codex:
- baseline runner reemplazable
- sign runner reemplazable
- artefactos estables
- schema de receipt
