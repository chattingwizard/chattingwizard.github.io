# CW Script Manager — Context

## Operator
- **Pau Lopez** — COO, Chatting Wizard
- No sabe programar, instrucciones paso a paso
- Usa Wispr Flow (voz a texto), priorizar intencion
- Respuestas cortas, claras, sin fluff
- Siempre critico: proponer la mejor opcion aunque contradiga a Pau

## Company: Chatting Wizard
- OnlyFans chatting agency
- ~100 freelancers (chatters, QCs, supervisors, content managers)
- Revenue: ~$150k/month
- Clients: OF management agencies (15-20% of sales generated)
- Legal: Only Elite Marketing LLC (Delaware)
- Tools: Slack, Google Sheets, Notion, Infloww (CRM), Excel, Airtable (base de modelos)

## This Project
- Objetivo: crear, gestionar y exportar scripts de sexting para todas las modelos
- El framework maestro esta en `scripts/framework/script-framework-v1.md`
- Cada modelo tiene su carpeta en `scripts/models/[nombre]/`
- Los scripts se exportan a Excel para importar en Infloww
- Vision: automatizar al maximo la creacion de scripts para reducir dependencia del Script Manager humano

## Modelos
- Base de datos de modelos en Airtable (acceso pendiente via API)
- De momento, scripts se crean cuando Pau da el perfil de la modelo
- Modelo de ejemplo: Putri (ver `scripts/models/putri/`)
