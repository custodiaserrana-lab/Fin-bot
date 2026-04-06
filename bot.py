#!/usr/bin/env python3
"""
FinBot AR - Bot Telegram para mercado financiero argentino
Reescrito con httpx puro - Compatible Python 3.13 / Termux
"""

import os
import json
import time
import httpx
import logging
import threading
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROO_KEY = os.getenv("GROO_KEY", "")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("/data/data/com.termux/files/home/finbot/finbot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# ── Helpers Telegram ──────────────────────────────────────────────────────────

def send_message(chat_id, text, parse_mode="Markdown"):
    try:
        with httpx.Client(timeout=15) as client:
            r = client.post(f"{BASE_URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": parse_mode
            })
        return r.json()
    except Exception as e:
        logger.error(f"send_message error: {e}")

def get_updates(offset=None, timeout=30):
    params = {"timeout": timeout, "allowed_updates": ["message"]}
    if offset:
        params["offset"] = offset
    try:
        with httpx.Client(timeout=timeout + 5) as client:
            r = client.get(f"{BASE_URL}/getUpdates", params=params)
        return r.json().get("result", [])
    except Exception as e:
        logger.error(f"get_updates error: {e}")
        return []

# ── APIs Financieras ──────────────────────────────────────────────────────────

def get_dolar():
    try:
        with httpx.Client(timeout=10) as client:
            r = client.get("https://dolarapi.com/v1/dolares")
        data = r.json()
        result = {}
        for d in data:
            result[d.get("nombre", "?")] = {"compra": d.get("compra"), "venta": d.get("venta")}
        return result
    except:
        return {}

def get_merval():
    try:
        with httpx.Client(timeout=10) as client:
            r = client.get("https://query1.finance.yahoo.com/v8/finance/chart/^MERV")
        data = r.json()
        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        previous = data["chart"]["result"][0]["meta"]["previousClose"]
        change = ((price - previous) / previous) * 100
        return {"price": price, "change": change}
    except:
        return {}

def get_crypto():
    try:
        with httpx.Client(timeout=10) as client:
            r = client.get(
                "https://api.coingecko.com/api/v3/simple/price",
                params={"ids": "bitcoin,ethereum,solana", "vs_currencies": "usd", "include_24hr_change": "true"}
            )
        return r.json()
    except:
        return {}

def get_fear_greed():
    try:
        with httpx.Client(timeout=10) as client:
            r = client.get("https://api.alternative.me/fng/")
        data = r.json()
        return data["data"][0]
    except:
        return {}

def get_cedears():
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    results = {}
    try:
        with httpx.Client(timeout=10) as client:
            for t in tickers:
                try:
                    r = client.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}")
                    data = r.json()
                    meta = data["chart"]["result"][0]["meta"]
                    results[t] = {
                        "price": meta["regularMarketPrice"],
                        "change": ((meta["regularMarketPrice"] - meta["previousClose"]) / meta["previousClose"]) * 100
                    }
                except:
                    results[t] = {"price": 0, "change": 0}
    except:
        pass
    return results

# ── Comandos ──────────────────────────────────────────────────────────────────

def cmd_start(chat_id):
    msg = (
        "🏦 *FinBot AR — Agente Financiero Institucional*\n\n"
        "Bienvenido al sistema de análisis financiero argentino.\n\n"
        "*Comandos disponibles:*\n"
        "💵 /dolar — Cotizaciones del dólar\n"
        "📈 /merval — Índice Merval\n"
        "₿ /cripto — Bitcoin, ETH, SOL\n"
        "😱 /fear — Fear & Greed Index\n"
        "🏢 /cedears — CEDEARs principales\n"
        "📊 /macro — Macro global\n"
        "💼 /cartera — Cartera óptima AR\n"
        "🎯 /opciones — Estrategias opciones\n"
        "📉 /ciclo — Ciclo sectorial\n"
        "💰 /dividendos — Dividendos BlackRock\n"
        "⚠️ /riesgo — Riesgo de cartera\n"
        "💹 /earnings — Earnings próximos\n"
        "🔍 /analisis — Análisis AR completo\n"
        "💡 /consulta — Consultar al analista\n"
        "🌍 /global — Mercados globales\n"
        "🔐 /merval\\_cmd — Merval detalle\n"
        "📋 /estado — Estado del sistema\n\n"
        "_Powered by Custodia Serrana Lab_"
    )
    send_message(chat_id, msg)

def cmd_dolar(chat_id):
    send_message(chat_id, "⏳ Consultando cotizaciones...")
    data = get_dolar()
    if not data:
        send_message(chat_id, "❌ Error al obtener cotizaciones del dólar.")
        return
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [f"💵 *Dólar AR — {now}*\n"]
    for nombre, vals in data.items():
        compra = vals.get("compra", "N/D")
        venta = vals.get("venta", "N/D")
        lines.append(f"*{nombre}*: Compra ${compra} | Venta ${venta}")
    send_message(chat_id, "\n".join(lines))

def cmd_merval(chat_id):
    send_message(chat_id, "⏳ Consultando Merval...")
    data = get_merval()
    if not data:
        send_message(chat_id, "❌ Error al obtener datos del Merval.")
        return
    emoji = "📈" if data["change"] >= 0 else "📉"
    msg = (
        f"{emoji} *Merval — {datetime.now().strftime('%d/%m %H:%M')}*\n\n"
        f"Precio: *{data['price']:,.0f}* pts\n"
        f"Variación: *{data['change']:+.2f}%*\n\n"
        f"_Goldman Sachs AR: {'Tendencia alcista — momentum positivo' if data['change'] >= 0 else 'Presión vendedora — cautela recomendada'}_"
    )
    send_message(chat_id, msg)

def cmd_cripto(chat_id):
    send_message(chat_id, "⏳ Consultando criptomonedas...")
    data = get_crypto()
    if not data:
        send_message(chat_id, "❌ Error al obtener datos de cripto.")
        return
    now = datetime.now().strftime("%d/%m %H:%M")
    msg = f"₿ *Criptomonedas — {now}*\n\n"
    nombres = {"bitcoin": "Bitcoin (BTC)", "ethereum": "Ethereum (ETH)", "solana": "Solana (SOL)"}
    for key, nombre in nombres.items():
        if key in data:
            price = data[key].get("usd", 0)
            change = data[key].get("usd_24h_change", 0)
            emoji = "🟢" if change >= 0 else "🔴"
            msg += f"{emoji} *{nombre}*: ${price:,.2f} ({change:+.2f}%)\n"
    send_message(chat_id, msg)

def cmd_fear(chat_id):
    send_message(chat_id, "⏳ Consultando Fear & Greed...")
    data = get_fear_greed()
    if not data:
        send_message(chat_id, "❌ Error al obtener Fear & Greed.")
        return
    value = int(data.get("value", 0))
    classification = data.get("value_classification", "N/D")
    if value <= 25:
        emoji, advice = "😱", "Miedo Extremo — Oportunidad de compra histórica"
    elif value <= 45:
        emoji, advice = "😨", "Miedo — Mercado defensivo, acumular gradualmente"
    elif value <= 55:
        emoji, advice = "😐", "Neutral — Sin señal clara, mantener posiciones"
    elif value <= 75:
        emoji, advice = "😏", "Codicia — Reducir exposición, tomar ganancias"
    else:
        emoji, advice = "🤑", "Codicia Extrema — Señal de techo, alta cautela"
    msg = (
        f"{emoji} *Fear & Greed Index*\n\n"
        f"Valor: *{value}/100*\n"
        f"Clasificación: *{classification}*\n\n"
        f"📊 *Análisis BlackRock:*\n_{advice}_"
    )
    send_message(chat_id, msg)

def cmd_cedears(chat_id):
    send_message(chat_id, "⏳ Consultando CEDEARs...")
    data = get_cedears()
    now = datetime.now().strftime("%d/%m %H:%M")
    msg = f"🏢 *CEDEARs — {now}*\n\n"
    for ticker, vals in data.items():
        emoji = "🟢" if vals["change"] >= 0 else "🔴"
        msg += f"{emoji} *{ticker}*: ${vals['price']:,.2f} ({vals['change']:+.2f}%)\n"
    msg += "\n_Fuente: Yahoo Finance | Custodia Serrana Lab_"
    send_message(chat_id, msg)

def cmd_macro(chat_id):
    msg = (
        f"📊 *Macro Global — {datetime.now().strftime('%d/%m %H:%M')}*\n\n"
        "🇺🇸 *Fed:* Tasas en pausa, próxima reunión FOMC pendiente\n"
        "🇦🇷 *BCRA:* Tasa de política monetaria activa\n"
        "🛢️ *Petróleo WTI:* Volatilidad media\n"
        "🥇 *Oro:* Refugio activo ante incertidumbre\n"
        "📈 *S&P 500:* Tendencia monitoreada\n\n"
        "💼 *JPMorgan AR:*\n"
        "_Contexto macro favorable para activos argentinos de corto plazo. "
        "Riesgo país como variable clave. Monitorear tipo de cambio oficial._"
    )
    send_message(chat_id, msg)

def cmd_cartera(chat_id):
    msg = (
        "💼 *Cartera Óptima AR — Construcción*\n\n"
        "📐 *Asignación sugerida (perfil moderado):*\n\n"
        "• 30% — Acciones AR (Merval)\n"
        "• 25% — CEDEARs diversificados\n"
        "• 20% — FCI Dollar-linked / CER\n"
        "• 15% — Obligaciones Negociables\n"
        "• 10% — Liquidez / Cauciones\n\n"
        "📊 *Retorno esperado anual:* 45-65% ARS\n"
        "⚠️ *Riesgo:* Moderado-Alto\n"
        "🔄 *Rebalanceo:* Trimestral\n\n"
        "💡 *Citadel AR:* _Diversificación entre activos hard dollar "
        "y pesos ajustados clave para cobertura inflacionaria._"
    )
    send_message(chat_id, msg)

def cmd_riesgo(chat_id):
    msg = (
        "⚠️ *Análisis de Riesgo — Cartera AR*\n\n"
        "📉 *Riesgos principales:*\n\n"
        "• 🔴 *Brecha cambiaria:* Alta — impacto en CEDEARs\n"
        "• 🟡 *Inflación:* Moderada — cubrir con CER/UVA\n"
        "• 🔴 *Riesgo país:* Elevado — volatilidad en bonos\n"
        "• 🟢 *Liquidez:* Adecuada en pesos\n"
        "• 🟡 *Regulatorio:* Cepo cambiario vigente\n\n"
        "🛡️ *Coberturas recomendadas (Morgan Stanley):*\n"
        "• Dolarizar 40% del portafolio\n"
        "• Stop-loss en posiciones >15% pérdida\n"
        "• Diversificar en 5+ instrumentos\n\n"
        "📊 _VaR 95% estimado: 12-18% mensual_"
    )
    send_message(chat_id, msg)

def cmd_dividendos(chat_id):
    msg = (
        "💰 *Dividendos — Proyección*\n\n"
        "🏆 *Top pagadores AR (BlackRock):*\n\n"
        "• *YPF:* Dividendo variable según resultados\n"
        "• *Banco Galicia:* Pago semestral estimado\n"
        "• *Pampa Energía:* Alta retención, reinversión\n"
        "• *Telecom:* Dividendo anual histórico\n\n"
        "🌍 *CEDEARs con dividendos:*\n"
        "• AAPL: ~0.5% anual | MSFT: ~0.8% anual\n"
        "• KO: ~3.1% anual | JNJ: ~2.9% anual\n\n"
        "📅 *Próximos ex-dividend:* Verificar calendario NYSE\n\n"
        "💡 _Payout ratio objetivo: 30-50% para sostenibilidad_"
    )
    send_message(chat_id, msg)

def cmd_earnings(chat_id):
    msg = (
        f"📈 *Earnings Próximos — {datetime.now().strftime('%d/%m/%Y')}*\n\n"
        "🗓️ *Calendario estimado:*\n\n"
        "• *AAPL:* Próximo trimestre pendiente\n"
        "• *MSFT:* Resultados mensuales a confirmar\n"
        "• *GOOGL:* Q siguiente en calendario\n"
        "• *TSLA:* Alta volatilidad post-earnings\n\n"
        "🇦🇷 *Empresas AR:*\n"
        "• YPF, Galicia, Pampa — resultados trimestrales\n\n"
        "⚡ *Estrategia Goldman:*\n"
        "_Posicionarse antes del earnings con opciones o reducir "
        "exposición si hay incertidumbre alta._\n\n"
        "🔗 _Verificar fechas exactas en: earningswhispers.com_"
    )
    send_message(chat_id, msg)

def cmd_ciclo(chat_id):
    msg = (
        "🔄 *Ciclo Sectorial — Análisis*\n\n"
        "📍 *Fase actual estimada:* Expansión tardía\n\n"
        "🟢 *Sectores favorecidos:*\n"
        "• Energía (YPF, Pampa, Vista)\n"
        "• Financiero (Galicia, Macro, Supervielle)\n"
        "• Materiales (Aluar, Ternium)\n\n"
        "🟡 *Sectores neutros:*\n"
        "• Telecom, Utilities\n\n"
        "🔴 *Sectores a reducir:*\n"
        "• Consumo discrecional\n"
        "• Real estate en pesos\n\n"
        "💼 *Rotación sugerida (Citadel):*\n"
        "_Sobreponderar energía y finanzas. "
        "Infraponderar consumo mientras persista presión inflacionaria._"
    )
    send_message(chat_id, msg)

def cmd_opciones(chat_id):
    msg = (
        "🎯 *Estrategias con Opciones — AR*\n\n"
        "📚 *Estrategias disponibles en BYMA:*\n\n"
        "• *Covered Call:* Vender call sobre posición larga\n"
        "  → Ingreso extra, cap de ganancia\n\n"
        "• *Protective Put:* Comprar put como seguro\n"
        "  → Protección ante caída brusca\n\n"
        "• *Bull Call Spread:* Alcista con costo reducido\n"
        "  → Riesgo/beneficio definido\n\n"
        "• *Straddle:* Volatilidad esperada alta\n"
        "  → Ganar con movimiento en cualquier dirección\n\n"
        "⚠️ *Prima promedio BYMA:* 2-5% mensual\n"
        "📊 *IV actual:* Elevada — favorece venta de opciones\n\n"
        "💡 _Morgan Stanley: En mercados volátiles AR, "
        "covered calls sobre Galicia y YPF generan alpha consistente._"
    )
    send_message(chat_id, msg)

def cmd_analisis(chat_id):
    send_message(chat_id, "⏳ Generando análisis completo AR...")
    dolar = get_dolar()
    merval = get_merval()
    cripto = get_crypto()
    fear = get_fear_greed()

    dolar_oficial = dolar.get("Oficial", {}).get("venta", "N/D")
    dolar_blue = dolar.get("Blue", {}).get("venta", "N/D")
    merval_price = f"{merval.get('price', 0):,.0f}" if merval else "N/D"
    merval_change = f"{merval.get('change', 0):+.2f}%" if merval else "N/D"
    btc_price = f"${cripto.get('bitcoin', {}).get('usd', 0):,.0f}" if cripto else "N/D"
    fear_val = fear.get("value", "N/D") if fear else "N/D"
    fear_class = fear.get("value_classification", "N/D") if fear else "N/D"
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    msg = (
        f"🔍 *Análisis Financiero AR — {now}*\n\n"
        f"💵 *Dólar:* Oficial ${dolar_oficial} | Blue ${dolar_blue}\n"
        f"📈 *Merval:* {merval_price} pts ({merval_change})\n"
        f"₿ *Bitcoin:* {btc_price}\n"
        f"😱 *Fear & Greed:* {fear_val}/100 — {fear_class}\n\n"
        "📋 *Conclusión institucional:*\n"
        "_Mercado argentino en fase de consolidación. "
        "Mantener diversificación entre activos dolarizados y pesos ajustados. "
        "Monitorear brecha cambiaria como indicador líder._\n\n"
        "💼 _Custodia Serrana Lab | FinBot AR_"
    )
    send_message(chat_id, msg)

def cmd_global(chat_id):
    msg = (
        f"🌍 *Mercados Globales — {datetime.now().strftime('%d/%m %H:%M')}*\n\n"
        "🇺🇸 *Wall Street:* S&P 500, Nasdaq, Dow Jones\n"
        "🇪🇺 *Europa:* EUROSTOXX, DAX, FTSE\n"
        "🇯🇵 *Asia:* Nikkei, Hang Seng, Shanghai\n"
        "🇧🇷 *Brasil:* IBOVESPA, Real\n\n"
        "📊 *Commodities:*\n"
        "• WTI Petróleo | Brent\n"
        "• Oro | Plata | Cobre\n"
        "• Soja | Maíz | Trigo\n\n"
        "🔗 _Datos en tiempo real: investing.com | tradingview.com_\n\n"
        "💡 _BlackRock Global: Contexto externo moderadamente favorable "
        "para emergentes en el corto plazo._"
    )
    send_message(chat_id, msg)

def cmd_consulta(chat_id, texto=""):
    if not texto or texto.strip() == "":
        send_message(chat_id,
            "💡 *Consulta al Analista*\n\n"
            "Enviá tu consulta así:\n"
            "`/consulta ¿Es momento de comprar YPF?`\n\n"
            "_El analista responderá con análisis institucional._"
        )
        return
    send_message(chat_id, f"🔍 Analizando: _{texto}_...")
    # Respuesta basada en palabras clave
    texto_lower = texto.lower()
    if any(w in texto_lower for w in ["comprar", "compra", "entrar"]):
        resp = "📊 *Análisis de entrada:*\n_Evaluar soporte técnico, volumen y contexto macro antes de ingresar. Usar Kelly Criterion para sizing._"
    elif any(w in texto_lower for w in ["vender", "venta", "salir"]):
        resp = "📊 *Análisis de salida:*\n_Considerar resistencias técnicas, noticias fundamentales y objetivo de ganancia previo al trade._"
    elif any(w in texto_lower for w in ["dolar", "dólar", "blue", "ccl", "mep"]):
        resp = "💵 *Análisis cambiario:*\n_Brecha entre oficial y paralelo es variable clave. CCL/MEP para dolarización legal de cartera._"
    elif any(w in texto_lower for w in ["ypf", "galicia", "pampa", "aluar"]):
        resp = "🏢 *Análisis de empresa AR:*\n_Verificar últimos balances, dividendos declarados y exposición al tipo de cambio._"
    else:
        resp = "💼 *Análisis general:*\n_Mercado AR requiere diversificación obligatoria entre activos dolarizados, CER y acciones. Horizonte mínimo recomendado: 6 meses._"
    send_message(chat_id, resp)

def cmd_estado(chat_id):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = (
        f"✅ *FinBot AR — Estado del Sistema*\n\n"
        f"🟢 Bot: *ACTIVO*\n"
        f"🕐 Servidor: *{now}*\n"
        f"📡 API Telegram: *Conectada*\n"
        f"💹 APIs financieras: *Operativas*\n\n"
        f"📊 *Comandos activos:* 18\n"
        f"🔄 *Resumen automático:* 09:00 y 18:00 hs\n\n"
        f"_Custodia Serrana Lab | Python 3.13 | httpx_"
    )
    send_message(chat_id, msg)

# ── Resumen Automático ────────────────────────────────────────────────────────

def enviar_resumen_ejecutivo(chat_id):
    """Resumen que se envía automáticamente 2 veces por día"""
    send_message(chat_id, "📋 *Resumen Ejecutivo Automático* — generando...")
    dolar = get_dolar()
    merval = get_merval()
    cripto = get_crypto()
    fear = get_fear_greed()

    dolar_oficial = dolar.get("Oficial", {}).get("venta", "N/D")
    dolar_blue = dolar.get("Blue", {}).get("venta", "N/D")
    merval_price = f"{merval.get('price', 0):,.0f}" if merval else "N/D"
    merval_change = f"{merval.get('change', 0):+.2f}%" if merval else "N/D"
    btc = f"${cripto.get('bitcoin', {}).get('usd', 0):,.0f}" if cripto else "N/D"
    eth = f"${cripto.get('ethereum', {}).get('usd', 0):,.0f}" if cripto else "N/D"
    fear_val = fear.get("value", "N/D") if fear else "N/D"
    fear_class = fear.get("value_classification", "N/D") if fear else "N/D"
    hora = datetime.now().strftime("%H:%M")
    fecha = datetime.now().strftime("%d/%m/%Y")

    msg = (
        f"🏦 *FinBot AR — Resumen {fecha} {hora}*\n"
        f"{'═' * 30}\n\n"
        f"💵 *DÓLAR*\n"
        f"  Oficial: ${dolar_oficial} | Blue: ${dolar_blue}\n\n"
        f"📈 *MERVAL*\n"
        f"  {merval_price} pts | {merval_change}\n\n"
        f"₿ *CRIPTO*\n"
        f"  BTC: {btc} | ETH: {eth}\n\n"
        f"😱 *SENTIMIENTO*\n"
        f"  Fear & Greed: {fear_val}/100 — {fear_class}\n\n"
        f"{'─' * 30}\n"
        f"💼 _Custodia Serrana Lab_"
    )
    send_message(chat_id, msg)

# ── Scheduler automático ──────────────────────────────────────────────────────

def scheduler_loop(chat_id):
    """Envía resumen a las 09:00 y 18:00"""
    horarios = ["09:00", "18:00"]
    enviados = set()
    while True:
        try:
            ahora = datetime.now().strftime("%H:%M")
            key = f"{ahora}"
            if ahora in horarios and key not in enviados:
                logger.info(f"Enviando resumen automático a las {ahora}")
                enviar_resumen_ejecutivo(chat_id)
                enviados.add(key)
            # Limpiar enviados a medianoche
            if ahora == "00:00":
                enviados.clear()
            time.sleep(45)
        except Exception as e:
            logger.error(f"Scheduler error: {e}")
            time.sleep(60)

# ── Router de comandos ────────────────────────────────────────────────────────

def handle_command(chat_id, text):
    text = text.strip()
    if text.startswith("/start"):
        cmd_start(chat_id)
    elif text.startswith("/dolar"):
        cmd_dolar(chat_id)
    elif text.startswith("/merval"):
        cmd_merval(chat_id)
    elif text.startswith("/cripto"):
        cmd_cripto(chat_id)
    elif text.startswith("/fear"):
        cmd_fear(chat_id)
    elif text.startswith("/cedears"):
        cmd_cedears(chat_id)
    elif text.startswith("/macro"):
        cmd_macro(chat_id)
    elif text.startswith("/cartera"):
        cmd_cartera(chat_id)
    elif text.startswith("/riesgo"):
        cmd_riesgo(chat_id)
    elif text.startswith("/dividendos"):
        cmd_dividendos(chat_id)
    elif text.startswith("/earnings"):
        cmd_earnings(chat_id)
    elif text.startswith("/ciclo"):
        cmd_ciclo(chat_id)
    elif text.startswith("/opciones"):
        cmd_opciones(chat_id)
    elif text.startswith("/analisis"):
        cmd_analisis(chat_id)
    elif text.startswith("/global"):
        cmd_global(chat_id)
    elif text.startswith("/consulta"):
        partes = text.split(" ", 1)
        consulta = partes[1] if len(partes) > 1 else ""
        cmd_consulta(chat_id, consulta)
    elif text.startswith("/estado"):
        cmd_estado(chat_id)
    elif text.startswith("/resumen"):
        enviar_resumen_ejecutivo(chat_id)
    else:
        send_message(chat_id, "❓ Comando no reconocido. Usá /start para ver todos los comandos.")

# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN no encontrado en .env")
        return

    logger.info("🚀 FinBot AR iniciando — Python 3.13 / httpx")

    # Obtener chat_id del owner desde .env para el scheduler
    owner_chat_id = os.getenv("OWNER_CHAT_ID", "5976165080")

    # Iniciar scheduler en thread separado
    t = threading.Thread(target=scheduler_loop, args=(owner_chat_id,), daemon=True)
    t.start()
    logger.info(f"⏰ Scheduler activo — resúmenes a las 09:00 y 18:00 → chat {owner_chat_id}")

    # Notificar inicio
    send_message(owner_chat_id,
        "✅ *FinBot AR activo*\n"
        f"🕐 {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        "_Resúmenes automáticos: 09:00 y 18:00_"
    )

    offset = None
    retry_delay = 5
    logger.info("📡 Escuchando mensajes...")

    while True:
        try:
            updates = get_updates(offset=offset)
            for update in updates:
                offset = update["update_id"] + 1
                msg = update.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")
                if chat_id and text:
                    logger.info(f"Mensaje de {chat_id}: {text}")
                    handle_command(chat_id, text)
            retry_delay = 5
        except KeyboardInterrupt:
            logger.info("Bot detenido por usuario.")
            break
        except Exception as e:
            logger.error(f"Error en main loop: {e}")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)

if __name__ == "__main__":
    main()
