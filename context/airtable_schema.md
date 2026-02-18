# Airtable Schema — Chatting Wizard

> Base ID: `appy0qGaMEfyDz9LZ`
> Última actualización: 2026-02-14
> Total de tablas: 36

---

## Índice por Área Funcional

| Área | Tablas |
|------|--------|
| **Core (Personas y Equipos)** | Chatter, Team, Recruitment |
| **Clientes y Modelos** | Clients, Models |
| **Performance y KPIs** | Chatter Performance, Chatter Score, KPIs, Daily Performance |
| **Coaching y Desarrollo** | Chatters Call, Chatters Performance, Chatters improvement plan, Coaching Log |
| **Reportes Operativos** | Shift Report, 🔵CHM Shift Report, 🔵CHM Weekly Report, 🟡TL Live Assistance Report, 🟡TL Week Report, 🟣SM Weekly Shift Report, 🟠Weekly Checklist, 🟠AM Client Calls, Content Manager Report |
| **Quality Assurance** | Quality Control |
| **Contenido y Operaciones** | Custom, Content Request, Content Management, Scripts Management |
| **Tracking y Tareas** | Hubstaff, Task Form |
| **Análisis de Modelos** | Deep Dive, 🟠Weekly Checklist |
| **Formación y Testing** | New MasterClass Test, Editor Form |
| **Email / Recruitment Marketing** | Email, Email Serbia, Email editors |
| **Test / Inactivo** | _test_perms |

---

## Mapa de Relaciones Central

```
Recruitment ──sync──► Chatter ◄──── Team
                         │              │
        ┌────────────────┼──────────────┼──────────────┐
        │                │              │              │
        ▼                ▼              ▼              ▼
  Chatter Score    Shift Report    Models ◄──── Clients
        │                │           │
        │                ▼           ▼
        │          Quality Control  Custom
        │                          Content Request
        ▼                          Content Management
  Chatter Performance              Scripts Management
  Chatters Performance
  Chatters Call
  Chatters improvement plan
  Coaching Log
  KPIs
  Daily Performance
  Hubstaff
```

La tabla **Chatter** es el hub central. Casi todas las demás tablas se vinculan a ella.

---

## 1. CORE — Personas y Equipos

### Chatter
- **ID**: `tblBrbCZyL5ub48zc`
- **Registros**: 100+ | **Campos**: 47
- **Última actividad detectada**: Sin fecha directa (siempre activa, es la tabla principal)
- **Función**: Tabla maestra de TODOS los miembros del equipo (chatters, TLs, CHM, QA, VA, CEO, COO, etc.)
- **Campos clave**:
  - `Full Name` (text) — Nombre completo
  - `⚡️Status` (select): Active, Dropped, Fired, Declined, Probation, inflow mail
  - `⚡️Rol` (select): CEO, COO, Chatter, Team Leader, Chatter Manager, VA, QA, Content Manager, Hiring Manager, Account Manager
  - `👫Team` → link a **Team**
  - `Favorite Shift` / `Second Favorite Shift` (select): 3 turnos UTC (00-08, 08-16, 16-00)
  - `Chatter ID` → link a **Recruitment** (origen del chatter)
  - `User` (collaborator) — Usuario Airtable asociado
- **Links salientes (a otras tablas)**:
  - `💬Hubstaff` → Hubstaff
  - `👩🏻 Custom` / `👩🏻 Custom copy` → Custom
  - `🧾Shift Report` → Shift Report
  - `📈Quality Control` → Quality Control
  - `📈Chatters Performance` → Chatters Performance
  - `📈Chatters improvement plan` → Chatters improvement plan
  - `📈Chatters Call` → Chatters Call
  - `🧾Supervisor Report` → TL Live Assistance Report
  - `💬Chatter Score` → Chatter Score
  - `🧾Content Manager Report` → Content Manager Report
  - `Task Form` → Task Form
  - `KPIs` → KPIs
  - `Chatter Performance` → Chatter Performance
  - `Chatter Manager Shift Report` → 🔵CHM Shift Report
  - `Chatter Manager Weekly Report` → 🔵CHM Weekly Report
  - `Script Manager Weekly Shift Report` → 🟣SM Weekly Shift Report
  - `TL Week Repor (Team Leader)` → 🟡TL Week Report
- **Campos de reportes** (text, links de visualización por rol):
  - Chatter Report, Chatter Report 2/3/4, COO Report, Team Leader Report, Content VA Report, Ops Assistant Report, Chatter Manager Report, Script Manager Report, Hiring Manager Report, Account Manager Report, Content Manager Report
- **Métricas calculadas**: Last Week Points, This Week Points, Score Bonus (fórmulas que tiran de Chatter Score)

### Team
- **ID**: `tblGTOPvVCQTbEHsW`
- **Registros**: 29 | **Campos**: 6
- **Función**: Define los equipos. Cada equipo tiene un nombre (ej: "Team Danilyn"), modelos asignadas y chatters asignados.
- **Campos clave**:
  - `Equipo` (text) — Nombre del equipo (Team Danilyn, Team Huckle, Team Ezekiel, etc.)
  - `Creators` → link a **Models**
  - `Chatter` → link a **Chatter**
  - `💬Chatter Performance 2` → link a **Chatter Performance**
- **Nota**: El nombre del Team Leader es el nombre del equipo (Team Danilyn = TL Danilyn)

### Recruitment
- **ID**: `tblL7aNq9GftQhm7V`
- **Registros**: 100+ | **Campos**: 59
- **Función**: Pipeline completo de recruiting. Desde aplicación hasta contratación.
- **Campos clave**:
  - `Chatter ID` (fórmula) — ID del candidato
  - `Status` (select): Interview, Training, Declined, Probation, Hired
  - `First Name`, `Last Name`, `Age`, `Email`, `Nationality`, `Timezone`, `Discord Handle`
  - `Profile Score`, `Interview score` (ratings)
  - `Training score D1` a `D6`, `Examen final` (ratings) — puntuaciones día a día del training
  - `Elite Hiring` (checkbox) — candidatos premium
  - `Flexibility`, `Experience` — disponibilidad y experiencia previa
  - Skills ratings: Sales Skills, Computer Navigation Speed, Problem-solving, Stress control, Commitment
  - `Test MasterClass + Guía de Chatting` (text) — link al test
  - `Sync` → link a **Chatter** (cuando pasan a contratados)
  - `Imported table` → link a **New MasterClass Test**

---

## 2. Clientes y Modelos

### Clients
- **ID**: `tblkawE86Yxsu5fIr`
- **Registros**: 47 | **Campos**: 18
- **Última actividad**: 2026-02-09 ✅ ACTIVA
- **Función**: Dueños de las cuentas de OnlyFans. Cada cliente tiene una o más modelos.
- **Campos clave**:
  - `Full Name`, `Status` (Active/Inactive/On Hold)
  - `Telegram ID`, `Telegram` — contacto Telegram del cliente
  - `Infloww Name`, `Infloww Email` — datos de Infloww (CRM)
  - `Business Name`, `Tax Number`, `Address` — datos de facturación
  - `Creators` → link a **Models**
  - `Account Manager Calls` → link a **🟠AM Client Calls**
  - `Customer ID`, `ClientID` (fórmula)

### Models
- **ID**: `tbl97sE9V8wbcgjAJ`
- **Registros**: 100+ | **Campos**: 63
- **Última actividad**: 2026-02-09 ✅ ACTIVA
- **Función**: Perfiles detallados de cada creadora de OF. La tabla más grande y detallada.
- **Campos clave — Identidad**:
  - `Model Name`, `Status` (Dead/On hold/Live/Pending Invoice), `Page Type` (Paid/Free/Mixed)
  - `Start Date`, `Location`, `Nationality`, `Age`, `Birthday`
  - `Profile Picture` (attachment)
  - `Bio`, `Notes`, `Price Guide`
  - `Scripts` (URL) — link al script de la modelo
  - `Branding Guideline` (rich text) — guía de marca
  - `Niche` (multi-select): MILF, Gym, Gamer, Lifestyle, etc.
- **Campos clave — Físico** (para chatting/sexting):
  - `Height`, `Weight`, `Boobs Size`, `Shoe Size`, `Hair Color and Type`, `Eye Color`, `Tattoos`, `Surgeries`
- **Campos clave — Servicios** (Yes/No selects):
  - `Masturbation`, `Anal`, `Squirting`, `B/G`, `G/G`, `Custom`, `Video Calls`
  - `VC Medium` (select): Instagram, Telegram, WhatsApp, Snapchat, Otros
- **Campos clave — Personal**:
  - `Smoking`, `Drinking`, `Partner`, `Children`, `Countries Visited`, `Previous Job`, `Current Job`, `Favorite Food`, `Sports`, `Instagram Link`
- **Campos clave — Negocio**:
  - `Traffic` (multi-select): Instagram/TikTok, Dating Apps, Paid Promo, Reddit, OFTV, Twitter/X
  - `CHATBOT` (select): Active/Inactive — si tiene chatbot activo
  - `RECORD_ID` (fórmula), `Client Name` (fórmula)
- **Links**:
  - `👫Team` → Team
  - `Client` → Clients
  - `.Custom` → Custom
  - `👩🏻OF Feed` → Content Management
  - `Content Request` → Shift Report (nota: nombre confuso, realmente tira de Shift Report)
  - `Scripts Management` → Scripts Management
  - `Deep Dive` → Deep Dive
  - `Weekly Checklist` → 🟠Weekly Checklist

---

## 3. Performance y KPIs

### Chatter Performance
- **ID**: `tbl97bJZ3ngHiQx1w`
- **Registros**: 100+ | **Campos**: 33
- **Función**: Métricas detalladas por turno/periodo de cada chatter. La tabla MÁS IMPORTANTE para medir rendimiento.
- **Campos clave**:
  - `⚡️Start date`, `⚡️End date` (fechas), `⚡️Duration` (duración)
  - `⚡️Chatter` (text) — nombre del chatter
  - `Chatter` → link a **Chatter**
  - `Team` → link a **Team**
  - `Rol` (multi-select): mismo que Chatter.⚡️Rol
  - `Week` (text) — identificador de semana
  - **Métricas de ventas**: `⚡️Sales` ($), `💰Sales/hr` ($/hr), `Sales/Fan` ($)
  - **Métricas de mensajes**: `⚡️Messages` (#), `💰Messages/Hr`, `⚡️Characters`, `Characters/Message`, `Messages/Fan`
  - **Métricas de PPV**: `⚡️PPV` (#), `⚡️Unlocked` (#), `💰Avg. PPV Price` ($), `⚡️Golden Ratio` (%), `⚡️Unlock Ratio` (%), `PPV Ratio` (fórmula)
  - **Métricas de fans**: `⚡️Fans Chatted` (#), `⚡️Fans who spent money` (#), `Fan CVR` (%), `Fans/Hr` (#)
  - **Métricas de velocidad**: `⚡️Reply Time` (text)
  - **Gamificación**: `Performance Points` (fórmula), `Player Level` (fórmula)

### Chatter Score
- **ID**: `tbljQun5AMLAfFtzX`
- **Registros**: 100+ | **Campos**: 18
- **Función**: Sistema de puntos (+/-) por comportamiento. Puntos positivos (asistencia, cubrir turnos) y negativos (llegar tarde, AFK, no-show).
- **Campos clave**:
  - `Chatter` → link a **Chatter**
  - `Date` (fecha)
  - `Type` (select): Manager Call Attendance (+), Covering ≥ 4h (+), Covering < 4h (+), Feedback Implemented (+), Late to Shift (-), AFK over 5 min (-), No Show (-), No reply Slack (-), Chatter Report not delivered (-), Manager Call Incidence (-)
  - `Reply Time` (select): rangos de 00:00 a 04:00+
  - `No Shift Incidence`, `All Reports Sent` (checkboxes)
  - `Points`, `Weekly Points`, `Total Points` (fórmulas)
  - `Week`, `Is Previous Week` (fórmulas)

### KPIs
- **ID**: `tblb8JHkQYUDZ3xDb`
- **Registros**: 32 | **Campos**: 14
- **Función**: Resumen semanal de KPIs por empleado. Usado para dashboards y reportes semanales.
- **Campos clave**:
  - `Start Date`, `End Date` — rango semanal
  - `Employee` → link a **Chatter**
  - `Sales` ($), `Sales x Hour`, `Messages x Hour`, `Golden Ratio`, `Unlock Rate`, `CVR`, `Reply Time`, `Average Chatter Score`, `C-Player Recurrence` (todos text excepto Sales)
- **Nota**: Muchos campos son text en vez de number, lo que dificulta cálculos automáticos.

### Daily Performance
- **ID**: `tbltaM187ka2UNOsi`
- **Registros**: 100+ | **Campos**: 15
- **Función**: Rendimiento diario por chatter. Tabla nueva del Coaching System.
- **Campos clave**:
  - `Date`, `Chatter` (text, no link), `Team` (text, no link)
  - `Sales`, `Sales/hr`, `CVR`, `Unlock Rate`, `Golden Ratio`, `Msg/hr` (numbers)
  - `Reply Time` (text)
  - `Hours Worked`, `Messages Sent`, `PPVs Sent`, `PPVs Unlocked`, `Fans Chatted` (numbers)
- **Nota**: No tiene links a Chatter ni Team, usa texto plano. Diseñada para inserción rápida por scripts.

---

## 4. Coaching y Desarrollo

### Chatters Call
- **ID**: `tblXv6uXkrctmm9FZ`
- **Registros**: 100+ | **Campos**: 19
- **Última actividad**: 2025-10-04 ⚠️ SIN USO DESDE OCTUBRE 2025
- **Función**: Log de llamadas de coaching usando modelo GROW (Goal, Reality, Options, Will).
- **Campos clave**:
  - `Date`, `Chatter` → link a Chatter
  - `Type of Call` (multi-select): Last chance, Improvement, Support, Explanation, Other
  - `Goal`, `Reality`, `Options` (rich text) — modelo GROW
  - `Will (When I check it back)` (fecha) — fecha de seguimiento
  - `Call Description` (rich text)
  - `Solution` (multi-select): Completed, In progress, Not completed, Not answered
  - `Call Channel` (multi-select): Slack Group/Individual, Discord, Telegram, Written, Meet
  - `Engagement` (rating 1-5)
  - `Duration` (number)

### Chatters Performance (evaluaciones)
- **ID**: `tblN6PZxXDpmDBExw`
- **Registros**: 100+ | **Campos**: 14
- **Función**: Evaluaciones cualitativas del chatter por parte del TL/CHM.
- **Campos clave**:
  - `Chatter` → link a Chatter
  - `Date`, `Description`
  - `Chatting` / `Involvement` / `Progress` (ratings 1-5)
  - `Chatting Personality` (multi-select): Aggro, Lovely, Dominant, Submissive, Creative
  - `Chatting Speed` (select): Slow, Medium, Fast
  - `Best role` (select): Closer, Setter, Training

### Chatters improvement plan
- **ID**: `tbl8d1DWrwTqDrS6x`
- **Registros**: 100+ | **Campos**: 10
- **Función**: Planes de mejora asignados a chatters con problemas.
- **Campos clave**:
  - `Chatter` → link a Chatter
  - `Starting Date`, `End Date`
  - `Improvement plan` (rich text)
  - `Type` (select): Fan engagement, Sexting, Ortography, Submission, Various, Priority, Notes/lists, Implication
  - `Actual Status` (select): Completed, Not Completed, With Incidences, In progress

### Coaching Log
- **ID**: `tbl2vOAqIIpyseVIg`
- **Registros**: 19 | **Campos**: 14
- **Función**: Tabla NUEVA del Coaching System. Log detallado de cada sesión de coaching.
- **Campos clave**:
  - `Date` (fecha)
  - `Team Leader` (select): Huckle, Danilyn, Ezekiel, Rycel
  - `Chatter` (select): lista de chatters activos
  - `Team` (select): Team Huckle, Team Danilyn, Team Ezekiel
  - `Coaching Notes`, `KPI Issues`, `Observations`, `Action Items` (text)
  - `Method` (select): Voice Chat, Message, Video Call, Slack Call
  - `Engagement` (number), `Duration (min)` (number)
  - `Focus KPI` (select): Sales/hr, CVR, Unlock Rate, Golden Ratio, Msg/hr, Reply Time
  - `Target Value`, `Baseline Value` (numbers)
- **Nota**: Los campos Team Leader y Chatter son selects simples, NO links a la tabla Chatter. Esto limita relaciones automáticas.

---

## 5. Reportes Operativos

### Shift Report (Chatters)
- **ID**: `tblHRpUH8WUQqSJOr`
- **Registros**: 100+ | **Campos**: 22
- **Última actividad**: 2026-02-14 ✅ MUY ACTIVA
- **Función**: Reporte que cada chatter llena al final de su turno. Control de calidad operativo.
- **Campos clave**:
  - `Chatter` → link a Chatter
  - `👩🏻Modelo` → link a Models
  - `Notas` (select: Yes/Partial/No), `Notas no hechas` (select)
  - `Listas` (select: Yes/Partial/No), `Listas no añadidas` (select)
  - `Tráfico` (select: High/Moderate/Low)
  - `Activar tráfico` (multi-select): General Massive Message, Message to online fans, Message specific fans, Ask for MM, I did nothing
  - `Report` (text) — reporte libre del chatter
  - `Contenido` (text) — notas sobre contenido
  - `Revisado` (checkbox), `Revisado por` (modified by), `Fecha Revisado`
  - `Are you a chatter in probation?`, `How many hours did you work?`
  - `Have you received any guidance or help from supervisor?` + descripción

### 🔵CHM Shift Report (Chatter Manager)
- **ID**: `tblBn3cpMeGd5gIia`
- **Registros**: 13 | **Campos**: 7
- **Última actividad**: 2026-02-10 ✅ ACTIVA
- **Función**: Reporte de turno del Chatter Manager (Rycel).
- **Campos**: Date, Chatter Manager → Chatter, Key Achievements, Red Flags, Pending Follow-Ups

### 🔵CHM Weekly Report (Chatter Manager)
- **ID**: `tblcs9ApKMdaMgMxy`
- **Registros**: 3 | **Campos**: 10
- **Última actividad**: 2026-02-10 ✅ ACTIVA
- **Función**: Reporte semanal del CHM con resumen de coaching, low-performers, KPIs, plan de siguiente semana.
- **Campos**: Week Start Date, Coaching Summary, Low-Performer Alerts, URL to KPI Excel Sheet, Weekly Summary, Upcoming Week, Others

### 🟡TL Live Assistance Report (Team Leaders)
- **ID**: `tblzj0mONmQUvuQqI`
- **Registros**: 100+ | **Campos**: 9
- **Última actividad**: 2026-02-14 ✅ MUY ACTIVA
- **Función**: Cada vez que un TL ayuda a un chatter en vivo, lo registra aquí. Evidencia de supervisión real.
- **Campos**: Date, Team Leader → Chatter, Chatter → Chatter, Evidence (attachment), Assistance Method (Voice Chat/Message), Resolution Message (attachment), Resolution (text)

### 🟡TL Week Report (Team Leaders)
- **ID**: `tblWyDJqqr1butruo`
- **Registros**: 4 | **Campos**: 8
- **Última actividad**: Sin fecha ⚠️ POCO USADO
- **Función**: Reporte semanal del TL con resumen de chatters, recomendaciones, necesidades de coaching.
- **Campos**: Week Start Date, Team Leader → Chatter, Chatter Summary, Recommendations for improvements, Coaching Needs, Others

### 🟣SM Weekly Shift Report (Script Manager)
- **ID**: `tblgvuX0ooeopfEUY`
- **Registros**: 3 | **Campos**: 11
- **Última actividad**: Sin fecha ⚠️ POCO USADO
- **Función**: Reporte semanal del Script Manager con performance de scripts, A/B tests, mejoras.
- **Campos**: Date, Script Manager → Chatter, Best/Weak-Performing Sequences, Common Funnel Drop-off Points, Improvements for Next Week, New Scripts Done, URL to AB Tests

### 🟠Weekly Checklist (Account Manager)
- **ID**: `tblQi3eOw0VHKoEwU`
- **Registros**: 100+ | **Campos**: 15
- **Última actividad**: Sin fecha
- **Función**: Checklist semanal por modelo con revenue, subs, tips, refunds, warnings.
- **Campos**: Starting Date, Ending Date, Model → Models, New Subs, Total Revenue, Messages ($), Tips ($), Refunds ($), Warnings, Pending Custom Content, Additional Observations, Week (fórmula), Total LTV, Sales LTV

### 🟠AM Client Calls (Account Manager)
- **ID**: `tblDMhJdfF6z8wb3j`
- **Registros**: 6 | **Campos**: 11
- **Última actividad**: Sin fecha ⚠️ POCO USADO
- **Función**: Log de llamadas con clientes (dueños de modelos).
- **Campos**: Call Title, Date of Call, Client → Clients, Call Type, Duration, Call Summary, Next Steps, Follow-Up Needed, Follow-Up Date, Call Recording Link, Client Mood (rating)

### Content Manager Report
- **ID**: `tbltQf1uEt5YKuMLV`
- **Registros**: 4 | **Campos**: 11
- **Última actividad**: Sin fecha ⚠️ POCO USADO
- **Función**: Checklist diario del Content Manager (posts, stories, PPV mass messages, SfS, Drive, etc.)
- **Campos**: Date, Content Manager → Chatter, 7 preguntas Yes/No sobre tareas completadas, Observations

---

## 6. Quality Assurance

### Quality Control
- **ID**: `tblBXoAhJc3IEHvSr`
- **Registros**: 100+ | **Campos**: 13
- **Última actividad**: 2025-11-12 ⚠️ SIN USO DESDE NOVIEMBRE 2025
- **Función**: Feedback y errores detectados por QA en los chats de los chatters.
- **Campos clave**:
  - `Chatter` → link a Chatter
  - `Feedback` (text) — descripción del error/feedback
  - `Type` (multi-select): Spelling/Vocabulary, Speed, Chat Error, Others, Positive Feedback, Important, Shift Incidents
  - `Screenshot` (attachment) — evidencia
  - `Reviewed` (checkbox), `Communicated to Chatter` (select: Yes/No)
  - `Created By`, `Created`, `Last Modified By`, `Last Modified`

---

## 7. Contenido y Operaciones

### Custom (Pedidos Custom)
- **ID**: `tblSRIKj7Qm1E6yM4`
- **Registros**: 100+ | **Campos**: 27
- **Función**: Registro de cada pedido custom (video, fotos, videollamada, audio) vendido a un fan.
- **Campos clave**:
  - `Model` → Models, `Chatter` → Chatter, `Team Leader` → Chatter
  - `Custom` (select): Custom Video, Custom Pictures, Videocall, Audio
  - `Status` (select): Sent, Cancelled, Notified, VC Confirmed
  - `Sub Name`, `Username` — datos del fan
  - `Price` ($), `Prepaid` ($), `Duration (minutes)`, `Número de Fotos`
  - `Content Description`, `Capture` (attachment)
  - `VC medium` (select): WhatsApp, Telegram, Instagram, Snapchat
  - `VC Username` — contacto para videollamada

### Content Request
- **ID**: `tblS5R1Zes8P7FzUi`
- **Registros**: 100 | **Campos**: 13
- **Función**: Peticiones de contenido a las modelos (posts, stories, sexting, audios).
- **Campos clave**:
  - `Model` → Models
  - `Type` (select): OF Post, OF Story, Sexting, Audio, Others
  - `Status` (select): Sent, Cancelled, Notified, VC Confirmed
  - `Content Description`, `Notes`

### Content Management
- **ID**: `tblabiWymhYwy4u9w`
- **Registros**: 100+ | **Campos**: 14
- **Última actividad**: 2025-11-18 ⚠️ SIN USO RECIENTE
- **Función**: Calendario de contenido. Qué tipo de contenido se programa para cada modelo.
- **Campos clave**:
  - `Model` → Models
  - `Scheduled Date` (fecha)
  - `Type` (select): Post/Story Content Management, Post/Story Posting, Sexting Management, Mass PPV Management, Scripts Creation, Vault Management, Smart Messages Management
  - `Quantity` (number), `Notes`
  - `Expected Minutes/Hours` (fórmulas)

### Scripts Management
- **ID**: `tblGlj7w3lzXT5riz`
- **Registros**: 100+ | **Campos**: 10
- **Función**: Tracking de creación de scripts por modelo. Relacionado con el proyecto CW-ScriptManager.
- **Campos clave**:
  - `Model` → Models
  - `Date`, `Script name` (text)
  - `Status` (select): Ready to be scripted, In progress, Done, Reviewed by Manager
  - `Created by`, `Last update`

---

## 8. Tracking y Tareas

### Hubstaff
- **ID**: `tblQBmYPfjOmeVAiH`
- **Registros**: 100+ | **Campos**: 8
- **Función**: Registro de horas trabajadas via Hubstaff. Usado para verificar que chatters cumplen turnos.
- **Campos**: Start Date, End Date, Duración (fórmula), Chatter → Chatter, Descripción, Pruebas (attachment), Approved (checkbox), Week (fórmula)

### Task Form
- **ID**: `tblUegBA9paITpJCy`
- **Registros**: 15 | **Campos**: 13
- **Función**: Sistema interno de tareas por departamento.
- **Campos**: Created By → Chatter, Department (Chatting/Content/Scripts/Clients/QA), Status (Cancelled/In progress/Paused/Done), Instructions, Observations, Deadline, Priority (Low/Medium/High/Critical)

---

## 9. Análisis de Modelos

### Deep Dive
- **ID**: `tblGcCLgC7KQ6mti0`
- **Registros**: 3 | **Campos**: 12
- **Última actividad**: Sin fecha ⚠️ POCO USADO
- **Función**: Análisis profundo de revenue por modelo (subs, tips, messages, avg spend).
- **Campos**: Start/End Date, Model → Models, New Subs, Tips ($), Messages ($), Sales (fórmula), Subs Income ($), Avg Spend per Spender ($), Avg Spend per Transaction ($), Sales LTV, Total LTV (fórmulas)

---

## 10. Formación y Testing

### New MasterClass Test
- **ID**: `tblFOpnzu7RInU3NL`
- **Registros**: 100+ | **Campos**: 37
- **Última actividad**: 2025-11-16
- **Función**: Examen de 30 preguntas sobre chatting, ventas y psicología que hacen los candidatos durante el proceso de hiring.
- **Campos**: Name, Recruiter → Recruitment, Q1 a Q30 (selects con 4 opciones cada una), Score (fórmula), Passed (fórmula)
- **Temas del examen**: Psicología de ventas, técnicas de sexting, manejo de objeciones, aftercare, upselling, modelo GROW, vocabulario OF

### Editor Form
- **ID**: `tblpbgfbPPXFIGzvQ`
- **Registros**: 3 | **Campos**: 13
- **Función**: Formulario de aplicación para editores de video.
- **Campos**: Name ID (fórmula), Status (Accepted/Declined), First/Last Name, Email, Telegram Username, Nationality, English Level, Bio, Portfolio, Best Video (attachment), Extra Attachment, Extra Comments

---

## 11. Email / Recruitment Marketing

### Email
- **ID**: `tblvEEprkuUaI4ZRk`
- **Registros**: 100+ | **Última actividad**: 2026-02-14 ✅ ACTIVA
- **Función**: Lista principal de emails de candidatos para recruiting.
- **Campos**: Email, Send Form (checkbox), Created, Full Name

### Email Serbia
- **ID**: `tblAWLmtQVI44iW8y`
- **Registros**: 12 | **Última actividad**: 2025-12-06
- **Función**: Lista de emails específica para recruiting en Serbia.
- **Campos**: Igual que Email.

### Email editors
- **ID**: `tbl340X0SwC2StBhc`
- **Registros**: 100+ | **Última actividad**: 2025-12-23
- **Función**: Lista de emails de candidatos a editor.
- **Campos**: Igual que Email.

---

## 12. Test / Inactivo

### _test_perms
- **ID**: `tblW7JZquZZJcZq42`
- **Registros**: 0 | **Campos**: 1
- **Función**: Tabla de prueba (vacía). Se puede eliminar.

---

## Resumen de Actividad

| Estado | Tablas |
|--------|--------|
| ✅ **Muy activa** (Feb 2026) | Shift Report, TL Live Assistance Report, Email, 🔵CHM Shift Report, 🔵CHM Weekly Report, Clients, Models |
| ⚠️ **Inactiva 1-3 meses** | Email editors (Dic 2025), Email Serbia (Dic 2025), Content Management (Nov 2025), New MasterClass Test (Nov 2025), Quality Control (Nov 2025) |
| ⚠️ **Inactiva 4+ meses** | Chatters Call (Oct 2025) |
| ❓ **Sin fecha detectada** | Chatter, Team, Recruitment, Chatter Performance, Hubstaff, Chatter Score, Task Form, Custom, Scripts Management, Content Request, 🟡TL Week Report, 🟣SM Weekly Shift Report, 🟠Weekly Checklist, 🟠AM Client Calls, Content Manager Report, Chatters Performance, Chatters improvement plan, Deep Dive, KPIs, Coaching Log, Daily Performance, _test_perms, Editor Form |

> **Nota**: "Sin fecha detectada" NO significa inactiva. Muchas tablas no tienen campo `Created` o `Date` que permita detectar actividad automáticamente. La tabla Chatter, por ejemplo, se usa constantemente pero no tiene campo de fecha directa.

---

## Relaciones entre Tablas (IDs)

| Tabla Origen | Campo | Tabla Destino (ID) |
|---|---|---|
| Chatter | 👫Team | Team (`tblGTOPvVCQTbEHsW`) |
| Chatter | Chatter ID | Recruitment (`tblL7aNq9GftQhm7V`) |
| Chatter | 💬Hubstaff | Hubstaff (`tblQBmYPfjOmeVAiH`) |
| Chatter | 👩🏻 Custom | Custom (`tblSRIKj7Qm1E6yM4`) |
| Chatter | 🧾Shift Report | Shift Report (`tblHRpUH8WUQqSJOr`) |
| Chatter | 📈Quality Control | Quality Control (`tblBXoAhJc3IEHvSr`) |
| Chatter | 📈Chatters Performance | Chatters Performance (`tblN6PZxXDpmDBExw`) |
| Chatter | 📈Chatters improvement plan | Chatters improvement plan (`tbl8d1DWrwTqDrS6x`) |
| Chatter | 📈Chatters Call | Chatters Call (`tblXv6uXkrctmm9FZ`) |
| Chatter | 🧾Supervisor Report | TL Live Assistance Report (`tblzj0mONmQUvuQqI`) |
| Chatter | 💬Chatter Score | Chatter Score (`tbljQun5AMLAfFtzX`) |
| Chatter | 🧾Content Manager Report | Content Manager Report (`tbltQf1uEt5YKuMLV`) |
| Chatter | Task Form | Task Form (`tblUegBA9paITpJCy`) |
| Chatter | KPIs | KPIs (`tblb8JHkQYUDZ3xDb`) |
| Chatter | Chatter Performance | Chatter Performance (`tbl97bJZ3ngHiQx1w`) |
| Chatter | Chatter Manager Shift Report | 🔵CHM Shift Report (`tblBn3cpMeGd5gIia`) |
| Chatter | Chatter Manager Weekly Report | 🔵CHM Weekly Report (`tblcs9ApKMdaMgMxy`) |
| Chatter | Script Manager Weekly Shift Report | 🟣SM Weekly Shift Report (`tblgvuX0ooeopfEUY`) |
| Chatter | TL Week Repor (Team Leader) | 🟡TL Week Report (`tblWyDJqqr1butruo`) |
| Team | Creators | Models (`tbl97sE9V8wbcgjAJ`) |
| Team | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Team | 💬Chatter Performance 2 | Chatter Performance (`tbl97bJZ3ngHiQx1w`) |
| Recruitment | Imported table | New MasterClass Test (`tblFOpnzu7RInU3NL`) |
| Recruitment | Sync | Chatter (`tblBrbCZyL5ub48zc`) |
| Clients | Creators | Models (`tbl97sE9V8wbcgjAJ`) |
| Clients | Account Manager Calls | 🟠AM Client Calls (`tblDMhJdfF6z8wb3j`) |
| Models | 👫Team | Team (`tblGTOPvVCQTbEHsW`) |
| Models | Client | Clients (`tblkawE86Yxsu5fIr`) |
| Models | .Custom | Custom (`tblSRIKj7Qm1E6yM4`) |
| Models | 👩🏻OF Feed | Content Management (`tblabiWymhYwy4u9w`) |
| Models | Scripts Management | Scripts Management (`tblGlj7w3lzXT5riz`) |
| Models | Deep Dive | Deep Dive (`tblGcCLgC7KQ6mti0`) |
| Models | Weekly Checklist | 🟠Weekly Checklist (`tblQi3eOw0VHKoEwU`) |
| Chatter Performance | Team | Team (`tblGTOPvVCQTbEHsW`) |
| Chatter Performance | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Chatter Score | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| KPIs | Employee | Chatter (`tblBrbCZyL5ub48zc`) |
| Chatters Call | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Chatters Performance | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Chatters improvement plan | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Shift Report | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Shift Report | 👩🏻Modelo | Models (`tbl97sE9V8wbcgjAJ`) |
| TL Live Assistance Report | Team Leader | Chatter (`tblBrbCZyL5ub48zc`) |
| TL Live Assistance Report | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| 🟡TL Week Report | Team Leader | Chatter (`tblBrbCZyL5ub48zc`) |
| 🔵CHM Shift Report | Chatter Manager | Chatter (`tblBrbCZyL5ub48zc`) |
| 🔵CHM Weekly Report | Chatter Manager | Chatter (`tblBrbCZyL5ub48zc`) |
| 🟣SM Weekly Shift Report | Script Manager | Chatter (`tblBrbCZyL5ub48zc`) |
| 🟠Weekly Checklist | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| 🟠AM Client Calls | Client | Clients (`tblkawE86Yxsu5fIr`) |
| Content Manager Report | Content Manager | Chatter (`tblBrbCZyL5ub48zc`) |
| Quality Control | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Custom | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| Custom | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Custom | Team Leader | Chatter (`tblBrbCZyL5ub48zc`) |
| Content Request | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| Content Management | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| Scripts Management | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| Hubstaff | Chatter | Chatter (`tblBrbCZyL5ub48zc`) |
| Task Form | Created By | Chatter (`tblBrbCZyL5ub48zc`) |
| Deep Dive | Model | Models (`tbl97sE9V8wbcgjAJ`) |
| New MasterClass Test | Recruiter | Recruitment (`tblL7aNq9GftQhm7V`) |

---

## Problemas Detectados

1. **Coaching Log usa selects simples** en vez de links a Chatter → no se puede cruzar datos automáticamente con KPIs ni performance. Debería linkearse.
2. **Daily Performance usa texto plano** para Chatter y Team → misma limitación. Diseñada para inserción rápida pero pierde trazabilidad.
3. **KPIs tiene muchos campos como texto** (Sales x Hour, Golden Ratio, etc.) → no se puede hacer cálculos directos. Debería ser number/percent.
4. **Quality Control inactiva desde Nov 2025** → ¿Se ha dejado de usar QA? Riesgo operativo alto.
5. **Chatters Call inactiva desde Oct 2025** → No se están registrando coaching calls en esta tabla (se creó Coaching Log como reemplazo parcial).
6. **Content Management inactiva desde Nov 2025** → ¿Se gestiona contenido fuera de Airtable ahora?
7. **Tablas duplicadas de email** (Email, Email Serbia, Email editors) → Podrían consolidarse en una sola con un campo "Source" o "Type".
8. **_test_perms vacía** → Se puede eliminar.
