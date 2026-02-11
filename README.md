# CW Script Manager

Proyecto dedicado a crear, gestionar y exportar scripts de sexting para Chatting Wizard.

## Estructura

```
scripts/framework/    → Framework maestro de scripts (reglas, psicologia, formato)
scripts/models/       → Scripts por modelo (1 carpeta por modelo)
exports/              → Archivos exportados listos para Infloww
tools/                → Scripts de automatizacion (generador, exportador)
cursor_context/       → Contexto para que el agente de Cursor opere bien
.cursor/rules/        → Reglas del agente Script Manager
```

## Como funciona

1. Dile al agente que modelo y que content set quieres.
2. El agente genera el script completo siguiendo el framework.
3. Exporta a Excel en formato Infloww.
4. Lo subes a Infloww.
