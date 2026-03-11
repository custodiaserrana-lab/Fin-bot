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

---

## 📋 Historial de cambios

### v6.0 — Marzo 2026 · Auditoría y salto de calidad

Esta versión fue el resultado de una auditoría externa del sistema evaluado como producto fintech real orientado a usuarios minoristas. El diagnóstico fue claro: la base era sólida en lectura de mercado, pero le faltaba convertirse en una **herramienta de decisión**. Estas son las mejoras implementadas.

---

#### 🔮 Algoritmo Crisis Argentina — nuevo módulo

Score 0-100 calibrado con los patrones de las tres últimas grandes crisis del mercado argentino: 2018, 2020 y 2023. Cruza seis variables con peso diferenciado — reservas BCRA, riesgo país, brecha cambiaria, shock externo (VIX + Brent), inflación y DXY — y muestra en tiempo real cuántas señales históricas de corrida están activas simultáneamente. Incluye comparativa visual de parecido con cada crisis pasada y dispara notificación push automática si el score supera 70/100.

---

#### 📉 Inflación real vs rendimiento — por instrumento

Panel que responde la pregunta que ningún banco ni broker publica claramente: ¿tu dinero en pesos está ganando o perdiendo contra la inflación? Muestra cada instrumento disponible — caja de ahorro, Súper Ahorro Santander, COCOA, Pesos Plus, Dólares Ahorro y Dólares Plus — con su rendimiento nominal, su rendimiento **real neto de inflación** y una barra de progreso visual que indica si cubre o no el índice de precios. Se actualiza automáticamente con la inflación anual estimada del contexto macroeconómico vigente.

---

#### 🧮 Simulador de capital

El usuario ingresa su capital actual y elige el horizonte temporal — 1, 3, 6 o 12 meses — y el sistema calcula automáticamente cuánto valdría ese dinero en cada instrumento, comparado con el efecto inflacionario estimado. Incluye botones rápidos de $500k, $1M, $2M y $5M, y emite una conclusión inteligente recomendando dolarización cuando ningún fondo en pesos cubre la inflación proyectada.

---

#### 🎯 Botón "¿Qué hago hoy con mi dinero?"

Motor de decisión diaria que toma los indicadores actuales del sistema — riesgo país, Brent, VIX, brecha, reservas e inflación — y los inyecta automáticamente en el chat con el analista AI, solicitando tres acciones concretas y priorizadas para el día. Diseñado para el perfil conservador del jubilado que no sigue el mercado minuto a minuto pero necesita una respuesta clara cuando abre el bot por la mañana.

---

#### 😱 Detector de pánico del ahorrista

Indicador 0-100 que cruza cuatro señales simultáneas — brecha cambiaria, VIX, riesgo país y Brent — para detectar cuándo el mercado está en modo fuga hacia el dólar. Score por encima de 75 dispara push al celular con alerta de pánico. Score bajo indica calma relativa sin necesidad de acción.

---

#### 💱 Presión cambiaria unificada

Indicador 0-100 dedicado exclusivamente al tipo de cambio, que combina brecha, reservas BCRA, riesgo país y shock externo en una sola lectura. Complementa al detector de pánico con foco específico en el riesgo de salto del dólar. Niveles: BAJA · MEDIA · ALTA · CRÍTICA con color y descripción contextual.

---

#### ⚡ Probabilidad de salto cambiario a 30 días

Modelo heurístico con cuatro factores ponderados — reservas (35%), brecha (30%), riesgo país (20%) y shock externo (15%) — calibrado con los datos previos a las devaluaciones de 2018, 2020 y 2023. No es una predicción, es una señal de convergencia de condiciones históricas que precedieron saltos cambiarios. Se presenta con barra de progreso, porcentaje y descripción del factor determinante.

---

#### 📐 UVA vs Inflación — rendimiento real comparado

Tabla completa que muestra el Plazo Fijo UVA, el Plazo Fijo tradicional y los principales fondos Cocos con su rendimiento nominal, rendimiento **real neto de inflación**, ajuste UVA anual y análisis de pros y contras. Responde la pregunta del jubilado que tiene opciones en el banco y no sabe cuál le conviene realmente.

---

#### 💸 Calculadora de costo real por operación

Ingresás el monto y el tipo de operación — MEP, CEDEAR, Bono, FCI u Opción — y el sistema calcula el desglose exacto: comisión, IVA, total pagado y tipo de cambio efectivo real. En contextos de alta volatilidad suma automáticamente el riesgo estimado de parking MEP al costo total.

---

#### 🏆 Comparativa de brokers argentinos

Tabla con seis brokers — Cocos Capital, IOL InvertirOnline, Balanz, Bull Market, PPI y Santander — comparando comisiones reales con IVA para MEP, CEDEARs y bonos, más custodia y rating de aplicación. Permite evaluar si Cocos es la mejor opción para cada tipo de operación.

---

#### 📊 FCI Cocos — rendimiento neto de management fee

Por primera vez visible en el sistema: el rendimiento de cada fondo Cocos **después de descontar el fee de administración**. El Dólar Plus que aparece como 7.5% bruto rinde efectivamente 6.70% neto. El COCOA que aparece como 25% rinde 24.5% neto. Información que el broker no publica en la portada.

---

#### ⏱️ Calculadora de parking MEP con feriados

Ingresás la fecha de compra del MEP y el sistema calcula exactamente qué día podés vender, saltando feriados nacionales (calendario 2026 completo incluido) y fines de semana. Incluye alerta automática si hay alta volatilidad y un feriado próximo que pueda extender el período de parking de forma inesperada.

---

#### 🔴 Alerta automática de parking en volatilidad

Si es jueves o viernes con VIX mayor a 25 o Brent mayor a 95 dólares, aparece automáticamente un panel rojo parpadeante advirtiendo que comprar MEP en ese momento implica quedar trabado durante el fin de semana mientras el tipo de cambio puede moverse libremente. Recomienda operar con instrumentos T+0 hasta que baje la volatilidad.

---

### Valoración post-auditoría

| Dimensión | Antes v5 | Después v6 |
|---|---|---|
| Arquitectura | 8.5/10 | 9/10 |
| Indicadores macro | 8/10 | 9.5/10 |
| Sistema de alertas | 8.5/10 | 9.5/10 |
| Utilidad para jubilados | 7/10 | **9.5/10** |
| Herramienta de decisión | 6/10 | **9.5/10** |

> *"El sistema ya era bueno para leer el mercado. Ahora también es bueno para decidir."*

---

*Última actualización: Marzo 2026 · 4.536 líneas de JavaScript · 299 KB · Sin frameworks · Sin servidor · Un solo archivo.*
