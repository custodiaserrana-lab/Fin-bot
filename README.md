# 📊 FinBot AR — Agente Financiero Geopolítico

> **Analizá tu dinero con inteligencia real. Contexto argentino. Datos en tiempo real. Decisiones tuyas.**

[![GitHub Pages](https://img.shields.io/badge/Live-GitHub%20Pages-brightgreen)](https://custodiaserrana-lab.github.io/Fin-bot/)
[![Versión](https://img.shields.io/badge/Versión-5.2-blue)]()
[![Licencia](https://img.shields.io/badge/Licencia-Personal-lightgrey)]()

---

## ¿Qué es FinBot AR?

FinBot AR es un agente financiero personal desarrollado como herramienta de análisis para el ahorrista argentino. No es una app bancaria ni un servicio de inversión — es un **sistema de inteligencia financiera** que cruza datos en tiempo real con contexto geopolítico, histórico y macroeconómico para ayudarte a tomar mejores decisiones con tu dinero.

Fue diseñado especialmente para perfiles conservadores — jubilados, ahorristas, inversores no profesionales — que necesitan información clara, honesta y sin jerga innecesaria.

> *"Los datos matan relato."* — Principio rector del sistema.

---

## 🚀 Demo en vivo

👉 **[https://custodiaserrana-lab.github.io/Fin-bot/](https://custodiaserrana-lab.github.io/Fin-bot/)**

No requiere instalación. Funciona en cualquier browser, celular o computadora.

---

## ✨ Funcionalidades principales

### 💬 Chat con Analista AI
- Motor dual **Groq (LLaMA 3.3 70B)** + **Anthropic (Claude Sonnet)** con fallback automático
- Chat libre — preguntá cualquier cosa sobre finanzas argentinas
- 45 preguntas predefinidas en 7 categorías
- 40 fuentes documentales activas y personalizables
- Memoria de sesión — el analista aprende tus correcciones

### 📡 Panel Live AR — Datos en Tiempo Real
- **Tipos de cambio** — Oficial, Blue, MEP, CCL, Turista, Santander (vía Bluelytics API)
- **Indicadores BCRA** — Reservas, Riesgo País, Tasas (vía API oficial BCRA)
- **8 indicadores adelantados globales** — VIX, DXY, Oro, Brent, S&P 500, Treasury 10Y, EEM, Curva EE.UU.
- **Panel Crypto** — Bitcoin, Ethereum, USDT/AR, BNB con termómetro de dolarización informal
- **Calendario económico semanal** — 10 eventos con impacto alto/medio/bajo

### 🧠 Modelo Predictivo
- Probabilidades a 30 días: 🟢 Normal / 🟡 Alerta / 🔴 Extremo
- Score de riesgo basado en 4 indicadores cruzados
- Precedentes históricos 1973-2026 incorporados al modelo

### ⚠️ Monitor de Umbrales Críticos
- 6 umbrales con barra de progreso visual y estado en tiempo real
- Riesgo País · Brent · Brecha MEP · VIX · DXY · Reservas BCRA
- Punto rojo en navegación cuando hay umbrales en alerta

### 📊 Gráficos Históricos
- 4 indicadores: Riesgo País · Brent · Brecha MEP · Dólar MEP
- Períodos: 30 · 60 · 90 días
- Zona visual del período del conflicto bélico marcada automáticamente
- Stats: Actual · Variación · Mínimo · Máximo

### ⏱️ Calculadora de Liquidez y Parking
- Grilla de tiempos de liquidación de todos los instrumentos
- Calculadora de parking MEP con feriados argentinos 2026 incluidos
- Alerta automática si hay alta volatilidad + fin de semana próximo
- Regla de incompatibilidad 90 días MEP/Oficial

### 💸 Calculadora de Costos Reales
- Costo neto de cada operación en Cocos: MEP, CEDEARs, Bonos, FCI, Opciones
- Comparativa de 6 brokers argentinos (Cocos, IOL, Balanz, Bull Market, PPI, Santander)
- FCI Cocos con rendimiento **neto de management fee** — lo que el broker no publica

### 🥥 Tablero Cocos Capital
- Semáforo de condición de mercado: Normal / Alerta / Extrema / Bélico / Inflación
- 7 fondos catalogados con rendimiento, liquidez y perfil de riesgo
- 14 CEDEARs de usuario monitoreados
- 5 botones de escenario rápido

### 🔔 Alertas Push + Modo Autónomo
- Notificaciones push al celular cuando cruza un umbral crítico
- Modo autónomo: monitorea cada 15 minutos sin intervención
- Cooldown de 30 minutos para evitar spam

---

## 🗺️ Base de conocimiento incorporada

| Categoría | Contenido |
|---|---|
| **Shocks petroleros históricos** | 1973 · 1979 · 1990 · 2008 · 2022 · 2026 con causas, magnitud y consecuencias |
| **Paradoja Argentina 2026** | Primera vez exportadora neta en un shock — análisis de doble impacto |
| **Comportamiento del ahorrista** | Patrones documentados en cada crisis: MEP, bonos, CEDEARs, fondos |
| **Crypto en Argentina** | USDT como dolarización informal, correlaciones con blue y MEP |
| **Refugios del inversor americano** | Oro, Tesoro, DXY, acciones de defensa — y cómo replicarlos desde AR |
| **Tarifario Cocos actualizado** | Comisiones reales con IVA, management fees, comparativa de brokers |
| **Regulación BCRA vigente** | Parking MEP, incompatibilidad 90 días, banda cambiaria |

---

## 🔧 Configuración

El bot requiere al menos una API key para activar el analista AI:

| API | Costo | Dónde obtener |
|---|---|---|
| **Groq** (recomendada) | 100% gratis, sin tarjeta | [console.groq.com](https://console.groq.com/keys) |
| **Anthropic** (respaldo) | USD 5 crédito inicial | [console.anthropic.com](https://console.anthropic.com) |
| **Twelve Data** (cotizaciones) | 800 llamadas/día gratis | [twelvedata.com](https://twelvedata.com) |

Las keys se guardan en `localStorage` de tu browser — **nunca salen de tu dispositivo**.

---

## 📱 Cómo usar

1. Abrí la URL en tu browser
2. Al primer acceso configurá tu Groq API key (gratis, 2 minutos)
3. Navegá por los tabs: 💬 Chat · 🔔 Alertas · ❓ Preguntas · 📡 Fuentes · 🧠 Memoria · 🥥 Cocos · 📡 Live AR
4. En el tab **📡 Live AR** activá las alertas push para recibir notificaciones en el celular

---

## 🏗️ Arquitectura técnica

```
FinBot AR
├── Motor AI dual (Groq + Anthropic con fallback automático)
├── APIs de datos gratuitas
│   ├── Bluelytics API → tipos de cambio AR
│   ├── BCRA API oficial → reservas, riesgo país, tasas
│   └── CoinGecko API → precios crypto
├── Twelve Data API → cotizaciones globales (opcional)
├── Base de conocimiento embebida (~15.000 tokens)
├── Modelo predictivo heurístico (4 indicadores cruzados)
└── Sistema de alertas push (Web Notifications API)
```

**Stack:** HTML5 · CSS3 · JavaScript vanilla · Canvas API (gráficos sin dependencias)

**Sin frameworks. Sin build. Sin servidor.** Un solo archivo HTML que funciona en cualquier browser.

---

## 📊 Contexto de creación

Desarrollado durante el conflicto bélico EE.UU.+Israel vs Irán (iniciado 28-Feb-2026) con el Estrecho de Ormuz cerrado al tráfico comercial y el Brent superando los USD 104 por barril (+35% en 8 días).

El sistema nació de una necesidad concreta: el ahorrista argentino conservador no tiene herramientas que crucen datos globales con el mercado local y le den una lectura clara de qué hacer con su dinero en tiempo de crisis.

---

## ⚠️ Disclaimer

Este bot es una herramienta de análisis e información. **No constituye asesoramiento financiero profesional.** Toda decisión de inversión es responsabilidad exclusiva del usuario. Verificá siempre la información con fuentes oficiales y tu broker antes de operar.

---

## 📄 Licencia

Uso personal. No autorizado para distribución comercial sin consentimiento del autor.

---

*Desarrollado con 🧠 + ☕ + datos que matan relato.*
