"""
===============================================================================
Car-Sev C.A. — Moldes de Goma para Estampado de Pisos y Pavimentos Decorativos
Aplicación Web de Presentación, Catálogo Completo (14 Moldes), PWA & Valencia
Optimizado para Navegación Móvil (iOS / Android) y Despliegue en Render
===============================================================================
"""

import base64
import urllib.parse
from pathlib import Path
import streamlit as st

# --- TÍTULO DE LA PESTAÑA DEL NAVEGADOR ---
st.set_page_config(
    page_title="CAR-SEV C.A. - Moldes y Filtros",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
...        
        /* Botón de la barra lateral visible y en tono dorado */
        [data-testid="collapsedControl"] {
            display: flex !important;
            visibility: visible !important;
            z-index: 999999 !important;
            background-color: rgba(212, 175, 55, 0.9) !important;
            border-radius: 6px;
            padding: 6px !important;
            margin: 6px !important;
        }
        [data-testid="collapsedControl"] svg {
            fill: #1a1a1a !important;
            color: #1a1a1a !important;
        }
    </style>
""", unsafe_allow_html=True)                                                                                                                                  # ── 2. RUTAS RELATIVAS SEGURAS (RENDER & LOCAL) ──────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# Número oficial de WhatsApp de Car-Sev C.A. (+58 0416-6481679)
WHATSAPP_NUMBER = "584166481679"
WHATSAPP_DISPLAY = "+58 (416) 648-1679"
WHATSAPP_BASE = f"https://wa.me/{WHATSAPP_NUMBER}"


# ── 3. MOTOR DE IMÁGENES EN BASE64 CON CACHÉ ─────────────────────────────────
@st.cache_data(show_spinner=False)
def img_b64(filename: str) -> str:
    """Carga de forma segura y convierte imágenes de assets/ a Data-URI Base64."""
    try:
        p = ASSETS_DIR / filename
        if not p.exists() or not p.is_file():
            return ""
        suffix = p.suffix.lower()
        mime_map = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
            ".svg": "image/svg+xml"
        }
        mime = mime_map.get(suffix, "image/jpeg")
        data = p.read_bytes()
        encoded = base64.b64encode(data).decode("utf-8")
        return f"data:{mime};base64,{encoded}"
    except Exception:
        return ""


# ── 4. ESTILOS CSS PERSONALIZADOS & PWA METADATA ─────────────────────────────────────────────────
def inject_custom_css_and_pwa():
    # Metadatos PWA y manifiesto
    st.markdown("""
    <meta name="google" content="notranslate">
    <meta name="theme-color" content="#8B0000">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Car-Sev C.A.">
    <link rel="manifest" href="/static/manifest.json">
    <link rel="apple-touch-icon" href="/static/logo-192.png">
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    :root {
        --bg-main: #FFFFFF;
        --bg-alt: #FAFAF8;
        --gold-primary: #D4AF37;f
        --gold-light: #FFE57F;
        --gold-dark: #AA820A;
        --chic-red: #8B0000;
        --text-main: #1A1A1A;
        --text-muted: #555555;
        --card-border: rgba(212, 175, 55, 0.35);
        --shadow-gold: 0 8px 24px rgba(212, 175, 55, 0.14);
    }

    /* Ajustes Globales de la App */
    html, body, .stApp {
        background-color: var(--bg-alt) !important;
        background-image:
            radial-gradient(at 0% 0%, rgba(212,175,55,0.05) 0, transparent 50%),
            radial-gradient(at 100% 100%, rgba(139,0,0,0.04) 0, transparent 50%);
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif !important;
        color: var(--text-main) !important;
    }

    /* Ocultar elementos predeterminados innecesarios pero mantener control de navegación */
    #MainMenu, footer { visibility: hidden !important; }
    [data-testid="stDecoration"] { display: none !important; }
    [data-testid="stStatusWidget"] { display: none !important; }

    /* Header transparente para integrar el botón flotante en móviles */
    [data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 99999 !important;
    }

    /* BOTÓN HAMBURGUESA / COLAPSO DEL SIDEBAR REFORZADO */
    [data-testid="collapsedControl"], [data-testid="stSidebarCollapseButton"] button {
        background: linear-gradient(135deg, #FFE57F 0%, #D4AF37 50%, #AA820A 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #AA820A !important;
        border-radius: 50px !important;
        padding: 6px 14px !important;
        box-shadow: 0 4px 14px rgba(212, 175, 55, 0.45) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    [data-testid="collapsedControl"] svg, [data-testid="stSidebarCollapseButton"] svg {
        fill: #FFFFFF !important;
        color: #FFFFFF !important;
        width: 22px !important;
        height: 22px !important;
    }

    [data-testid="collapsedControl"]:hover, [data-testid="stSidebarCollapseButton"] button:hover {
        transform: scale(1.06) !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important;
    }

    /* TRANSICIÓN Y ESTILO DEL SIDEBAR (CERO AZUL) */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid var(--gold-primary) !important;
        box-shadow: 4px 0 25px rgba(212, 175, 55, 0.18) !important;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Eliminación total del color azul predeterminado de Streamlit en radio buttons */
    [data-testid="stSidebar"] .stRadio label {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        color: #1A1A1A !important;
        font-size: 0.92rem !important;
        padding: 10px 14px !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
        white-space: nowrap !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(212, 175, 55, 0.12) !important;
        color: var(--gold-dark) !important;
    }

    div[role="radiogroup"] label[aria-checked="true"] {
        background: linear-gradient(135deg, rgba(255,229,127,0.25) 0%, rgba(212,175,55,0.2) 100%) !important;
        color: #8B0000 !important;
        border-left: 4px solid #D4AF37 !important;
        font-weight: 700 !important;
    }

    div[role="radiogroup"] label[aria-checked="true"] p {
        color: #8B0000 !important;
        font-weight: 700 !important;
    }

    div[role="radiogroup"] input[type="radio"]:checked + div {
        border-color: #D4AF37 !important;
        background-color: #8B0000 !important;
    }

    /* Ajustes de Contenedores */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1240px !important;
    }

    /* Tarjetas de Lujo (Luxury Cards) */
    .luxury-card {
        background: #FFFFFF !important;
        border: 2px solid var(--gold-primary) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: var(--shadow-gold) !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        margin-bottom: 24px !important;
    }

    .luxury-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(170, 130, 10, 0.22) !important;
        border-color: var(--gold-dark) !important;
    }

    .card-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: var(--text-main) !important;
        margin-bottom: 8px !important;
    }

    .card-subtitle {
        font-size: 0.82rem !important;
        color: var(--gold-dark) !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.12em !important;
        margin-bottom: 12px !important;
    }

    .card-text {
        font-size: 0.88rem !important;
        color: var(--text-muted) !important;
        line-height: 1.6 !important;
    }

    /* Botón Dorado Personalizado */
    .btn-gold {
        background: linear-gradient(135deg, #FFE57F 0%, #D4AF37 50%, #AA820A 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #AA820A !important;
        padding: 12px 24px !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        border-radius: 30px !important;
        cursor: pointer !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        width: 100% !important;
        text-decoration: none !important;
        box-shadow: 0 4px 12px rgba(170, 130, 10, 0.25) !important;
        transition: all 0.25s ease !important;
    }

    .btn-gold:hover {
        opacity: 0.95 !important;
        box-shadow: 0 6px 18px rgba(212, 175, 55, 0.45) !important;
        transform: translateY(-2px) !important;
    }

    /* Badges y Adornos */
    .ornament-gold {
        font-size: 0.72rem !important;
        letter-spacing: 0.22em !important;
        color: var(--gold-primary) !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
    }

    .divider-gold {
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--gold-primary), transparent);
        max-width: 300px;
        margin: 32px auto;
    }

    /* Estilo para las métricas del Cotizador */
    .metric-box {
        background: #FFFFFF !important;
        border-left: 4px solid var(--gold-primary) !important;
        border-radius: 8px !important;
        padding: 16px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04) !important;
        margin-bottom: 12px !important;
    }

    .metric-value {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        color: var(--gold-dark) !important;
    }

    .metric-label {
        font-size: 0.78rem !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }

    /* OPTIMIZACIONES ESPECÍFICAS PARA PANTALLAS MÓVILES (MAX-WIDTH: 768PX) */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 3.8rem !important;
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
        }

        [data-testid="collapsedControl"] {
            position: fixed !important;
            top: 12px !important;
            left: 12px !important;
            z-index: 999999 !important;
        }

        [data-testid="stSidebar"] {
            width: 85vw !important;
            max-width: 320px !important;
        }

        .mobile-notice {
            background: #FFFFFF !important;
            border: 1px solid #D4AF37 !important;
            border-left: 4px solid #D4AF37 !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
            margin-bottom: 20px !important;
            font-size: 0.84rem !important;
            color: #1A1A1A !important;
            box-shadow: 0 4px 12px rgba(212, 175, 55, 0.15) !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Banner Flotante PWA
    st.markdown("""
    <div id="pwa-install-banner" style="display:none; position:fixed; bottom:20px; right:20px; z-index:999999; background:#FFFFFF; border:2px solid #D4AF37; border-radius:16px; padding:16px 20px; box-shadow:0 10px 30px rgba(139,0,0,0.2); max-width:320px; font-family:'Montserrat',sans-serif;">
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
        <span style="font-family:'Playfair Display',serif; font-size:1rem; font-weight:700; color:#8B0000;">Car-Sev C.A. App</span>
        <button onclick="dismissPWAInstall()" style="background:none; border:none; color:#999; font-size:1.1rem; cursor:pointer;">✕</button>
      </div>
      <p style="font-size:0.75rem; color:#555; margin:0 0 12px 0; line-height:1.4;">Instala nuestra aplicación oficial en tu pantalla de inicio.</p>
      <button id="pwa-install-btn" onclick="installPWAApp()" class="btn-gold" style="margin:0 !important; width:100% !important;">
        ✦ Instalar App Car-Sev
      </button>
    </div>

    <script>
      (function() {
        if (window.__pwa_script_loaded) return;
        window.__pwa_script_loaded = true;

        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
          e.preventDefault();
          deferredPrompt = e;
          const banner = document.getElementById('pwa-install-banner');
          if (banner) banner.style.display = 'block';
        });

        window.installPWAApp = function() {
          if (deferredPrompt) {
            deferredPrompt.prompt();
            deferredPrompt.userChoice.then(() => {
              deferredPrompt = null;
              window.dismissPWAInstall();
            });
          }
        };

        window.dismissPWAInstall = function() {
          const banner = document.getElementById('pwa-install-banner');
          if (banner) banner.style.display = 'none';
        };

        if ('serviceWorker' in navigator) {
          window.addEventListener('load', function() {
            navigator.serviceWorker.register('/static/sw.js').catch(function(err) {
              console.log('SW error:', err);
            });
          });
        }
      })();
    </script>
    """, unsafe_allow_html=True)


inject_custom_css_and_pwa()

# Aviso Móvil Responsivo
st.markdown("""
<div class="mobile-notice">
    💡 <b>¿Nos visitas desde el celular?</b> Toca el botón dorado <b>☰</b> en la esquina superior izquierda para desplegar el menú de navegación y explorar los 14 moldes.
</div>
""", unsafe_allow_html=True)


# ── 5. HELPER: BOTÓN DE WHATSAPP INTERACTIVO ─────────────────────────────────
def wa_button(msg: str, label: str = "✦ Solicitar por WhatsApp") -> str:
    """Genera un botón dorado de WhatsApp codificando el mensaje en el enlace."""
    url = f"{WHATSAPP_BASE}?text={urllib.parse.quote(msg)}"
    return f"""
    <a href="{url}" target="_blank" rel="noopener noreferrer" style="text-decoration:none; display:block; width:100%;">
      <div class="btn-gold">
        <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12.031 21c-1.603 0-3.14-.407-4.498-1.182l-.322-.184-3.344.877.893-3.26-.202-.32A8.932 8.932 0 013.06 12.03C3.06 7.086 7.085 3.06 12.031 3.06c4.945 0 8.97 4.025 8.97 8.97 0 4.945-4.025 8.97-8.97 8.97zm4.83-6.338c-.264-.132-1.563-.771-1.805-.859-.242-.088-.418-.132-.594.132s-.682.859-.836 1.035c-.154.176-.308.198-.572.066-.264-.132-1.114-.41-2.122-1.308-.784-.699-1.313-1.562-1.467-1.826-.154-.264-.016-.407.116-.539.119-.118.264-.308.396-.462.132-.154.176-.264.264-.44.088-.176.044-.33-.022-.462-.066-.132-.594-1.43-.814-1.958-.214-.514-.432-.443-.594-.451l-.506-.009a.97.97 0 00-.704.33c-.242.264-.924.903-.924 2.201s.946 2.553 1.078 2.729c.132.176 1.861 2.84 4.509 3.982.63.272 1.122.434 1.506.556.633.201 1.209.173 1.664.105.507-.075 1.563-.639 1.783-1.257.22-.617.22-1.146.154-1.257-.066-.11-.242-.176-.506-.308z"/>
        </svg>
        <span>{label}</span>
      </div>
    </a>"""


# ── 6. CATÁLOGO COMPLETO DE 14 MOLDES DE GOMA CAR-SEV ───────────────────────
CATALOG = [
    {
        "id": "laja_san_roman",
        "file": "molde_piedra_laja.jpg",
        "name": "Molde Piedra Laja San Román",
        "category": "Piedras & Lajas",
        "dimensions": "60 x 60 cm",
        "hardness": "Shore A 70",
        "price_usd": 200.00,
        "caption": "Grabado profundo de laja rústica natural. Ideal para patios, terrazas residenciales y zonas de piscina.",
        "msg": "Hola Car-Sev C.A.! Estoy interesado en el Molde Piedra Laja San Román ($200 USD)."
    },
    {
        "id": "adoquin_romano",
        "file": "molde_adoquin_romano.jpg",
        "name": "Molde Adoquín Español Rústico",
        "category": "Adoquines",
        "dimensions": "60 x 60 cm",
        "hardness": "Shore A 75",
        "price_usd": 200.00,
        "caption": "Diseño en abanico continuo de alta resistencia. Perfecto para avenidas, estacionamientos y calzadas vehiculares.",
        "msg": "Hola Car-Sev C.A.! Me interesa el Molde Adoquín Español Rústico ($200 USD)."
    },
    {
        "id": "madera_veteada",
        "file": "molde_madera_rustica.jpg",
        "name": "Molde Tabla de Madera Veteada",
        "category": "Maderas",
        "dimensions": "120 x 30 cm",
        "hardness": "Shore A 80",
        "price_usd": 110.00,
        "caption": "Juego de moldes con textura de vetas de pino rústico. Excelente para decks, bordes de piscina y fachadas.",
        "msg": "Hola Car-Sev C.A.! Quisiera cotizar el Molde Tabla de Madera Veteada ($110 USD)."
    },
    {
        "id": "ashlar_slate",
        "file": "molde3_piedra_ashlar_slate.jpg",
        "name": "Molde Piedra Ashlar Slate",
        "category": "Piedras & Lajas",
        "dimensions": "60 x 60 cm",
        "hardness": "Shore A 85",
        "price_usd": 240.00,
        "caption": "Patrón Geométrico Ashlar Slate de textura refinada. Diseñado para áreas comerciales y entradas señoriales.",
        "msg": "Hola Car-Sev C.A.! Quisiera cotizar el Molde Piedra Ashlar Slate ($240 USD)."
    },
    {
        "id": "ashlar_hilera",
        "file": "goma5_piedra_ashlar_en_hilera.jpg",
        "name": "Molde Piedra Ashlar en Hilera Continuous",
        "category": "Piedras & Lajas",
        "dimensions": "60 x 45 cm",
        "hardness": "Shore A 80",
        "price_usd": 170.00,
        "caption": "Diseño rectilíneo en hileras continúas que imitan mampostería tradicional tallada a mano.",
        "msg": "Hola Car-Sev C.A.! Me interesa el Molde Piedra Ashlar en Hilera ($170 USD)."
    },
    {
        "id": "adoquin_tipo_h",
        "file": "molde6_adoquin_tipo_h.jpg",
        "name": "Molde Adoquín Intertrabado Tipo H",
        "category": "Adoquines",
        "dimensions": "75 x 45 cm",
        "hardness": "Shore A 80",
        "price_usd": 200.00,
        "caption": "Patrón industrial intertrabado en forma de H de encastre perfecto para pavimentación vehicular intensiva.",
        "msg": "Hola Car-Sev C.A.! Quisiera información del Molde Adoquín Tipo H ($200 USD)."
    },
    {
        "id": "madera_liston",
        "file": "molde7_madera_rustica.jpg",
        "name": "Molde Madera Rústica Listón Real",
        "category": "Maderas",
        "dimensions": "90 x 22 cm",
        "hardness": "Shore A 80",
        "price_usd": 150.00,
        "caption": "Textura profunda de tableros de madera rústica envejecida con relieve acentuado.",
        "msg": "Hola Car-Sev C.A.! Me interesa el Molde Madera Rústica Listón Real ($150 USD)."
    },
    {
        "id": "adoquin_abanico",
        "file": "molde8_adoquin_en_abanico.jpg",
        "name": "Molde Adoquín en Abanico Real",
        "category": "Adoquines",
        "dimensions": "110 x 90 cm",
        "hardness": "Shore A 75",
        "price_usd": 500.00,
        "caption": "Estampado clásico europeo en arcos de abanico, ideal para boulevards y plazas elegantes.",
        "msg": "Hola Car-Sev C.A.! Solícito información del Molde Adoquín en Abanico Real ($500 USD)."
    },
    {
        "id": "piedra_grid",
        "file": "molde9_piedra_cuadrada_texturizada_grid.jpg",
        "name": "Molde Piedra Cuadrada Grid Modular",
        "category": "Piedras & Lajas",
        "dimensions": "50 x 50 cm",
        "hardness": "Shore A 80",
        "price_usd": 200.00,
        "caption": "Formato ortogonal de baldosas de piedra texturizada en cuadrícula para acabados contemporáneos.",
        "msg": "Hola Car-Sev C.A.! Quisiera adquirir el Molde Piedra Cuadrada Grid Modular ($200 USD)."
    },
    {
        "id": "ladrillo_tableta",
        "file": "molde10_ladrillo_tableta_rustica_en_tiras.jpg",
        "name": "Molde Ladrillo Tableta Rústica en Tiras",
        "category": "Adoquines",
        "dimensions": "95 x 22 cm",
        "hardness": "Shore A 65",
        "price_usd": 160.00,
        "caption": "Reproducción de hileras de ladrillos artesanales quemados al horno con bordes rústicos.",
        "msg": "Hola Car-Sev C.A.! Me interesa el Molde Ladrillo Tableta Rústica ($160 USD)."
    },
    {
        "id": "ashlar_cardenas",
        "file": "molde11_piedra_ashlar_rectangular.jpg",
        "name": "Molde Piedra Ashlar Rectangular Cárdenas",
        "category": "Piedras & Lajas",
        "dimensions": "60 x 60 cm",
        "hardness": "Shore A 85",
        "price_usd": 238.00,
        "caption": "Bloques rectangulares asimétricos con juntas definidas y relieve tridimensional.",
        "msg": "Hola Car-Sev C.A.! Solícito cotización del Molde Piedra Ashlar Rectangular ($238 USD)."
    },
    {
        "id": "grand_valley",
        "file": "molde12_piedra_grand_valley.jpg",
        "name": "Molde Piedra Grand Valley Exclusivo",
        "category": "Piedras & Lajas",
        "dimensions": "75 x 75 cm",
        "hardness": "Shore A 80",
        "price_usd": 240.00,
        "caption": "Moldura de gran formato con textura volcánica rocosa para áreas residenciales y comerciales de lujo.",
        "msg": "Hola Car-Sev C.A.! Quisiera información del Molde Piedra Grand Valley Exclusivo ($240 USD)."
    },
    {
        "id": "mosaico_colonial",
        "file": "mosaico1_de_pisos.jpg",
        "name": "Molde Mosaico Colonial Rústico",
        "category": "Piedras & Lajas",
        "dimensions": "00 x 00 cm",
        "hardness": "Shore A 00",
        "price_usd": 00.00,
        "caption": "Diseño en mosaico con piedras entrelazadas de estilo colonial para patios y caminerías de jardín.",
        "msg": "Hola Car-Sev C.A.! Me interesa el Molde Mosaico Colonial Rústico ($00 USD)."
    },
    {
        "id": "mosaico_pavimento",
        "file": "mosaico2_de_pisos.jpg",
        "name": "Molde Mosaico Pavimento Real",
        "category": "Piedras & Lajas",
        "dimensions": "00 x 00 cm",
        "hardness": "Shore A 00",
        "price_usd": 00.00,
        "caption": "Combinación simétrica de adoquín y piedra plana para pavimentos exteriores resistentes.",
        "msg": "Hola Car-Sev C.A.! Quisiera cotizar el Molde Mosaico Pavimento Real ($00 USD)."
    }
]


# ── 7. NAVEGACIÓN Y MENÚ LATERAL PERSISTENTE (CERO AZUL) ──────────────────────
with st.sidebar:
    logo_src_main = img_b64("logo1_original.png") or img_b64("logo_original.png") or img_b64("logo_192.png")
    if logo_src_main:
        st.markdown(
            '<div style="text-align:center; padding-top:10px; padding-bottom:6px;">'
            '<img src="' + logo_src_main + '" alt="Car-Sev C.A." style="max-width:240px; height:auto; display:block; margin:0 auto;">'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("""
    <div style="text-align: center; padding: 12px 0 16px 0;">
        <span class="ornament-gold">✦ FABRICACIÓN DE EXCELENCIA ✦</span>
        <h2 style="font-family:'Playfair Display', serif; color:#8B0000; font-size:1.6rem; margin:6px 0 2px 0;">CAR-SEV C.A.</h2>
        <p style="font-size:0.75rem; color:#AA820A; font-weight:600; letter-spacing:0.1em;">MOLDES DE GOMA PARA ESTAMPADO</p>
    </div>
    <div style="height: 2px; background: linear-gradient(90deg, transparent, #D4AF37, transparent); margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)

    menu_option = st.radio(
        "Navegación Principal",
        [
            "🏠  Inicio / Presentación",
            "🧩  Catálogo de Moldes (14)",
            "🧮  Cotizador / Pedidos",
            "📍  Contacto & Ubicación"
        ],
        index=0
    )

    st.markdown("""
    <div style="margin-top: 30px; padding: 16px; background: rgba(212,175,55,0.06); border: 1px solid #D4AF37; border-radius: 12px; text-align: center;">
        <p class="ornament-gold" style="font-size:0.65rem;">DOCUMENTACIÓN TÉCNICA</p>
        <p style="font-size:0.8rem; font-weight:700; color:#1A1A1A; margin:4px 0 10px 0;">Ficha de Rendimientos</p>
    """, unsafe_allow_html=True)

    pdf_file_path = ASSETS_DIR / "carsev_rendimiento_material.pdf"
    if pdf_file_path.exists():
        st.download_button(
            label="📄 Descargar PDF Rendimiento",
            data=pdf_file_path.read_bytes(),
            file_name="carsev_rendimiento_material.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown(f"""
        <div style="margin-top:16px;">
            <p class="ornament-gold" style="font-size:0.65rem;">ATENCIÓN DIRECTA</p>
            <p style="font-size:0.85rem; font-weight:700; color:#1A1A1A; margin:4px 0;">{WHATSAPP_DISPLAY}</p>
            <p style="font-size:0.75rem; color:#555555; margin-bottom:10px;">Valencia / Envíos a Nivel Nacional</p>
        </div>
 """, unsafe_allow_html=True)

    st.markdown(wa_button("Hola Car-Sev C.A.! Quisiera asesoría rápida sobre moldes de goma.", "💬 WhatsApp Directo"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ── 8. SECCIÓN 1: INICIO / PRESENTACIÓN ──────────────────────────────────────
if "Inicio" in menu_option:
    # Logotipo principal (logo1_original.png = alta resolución)
    logo_inicio = img_b64("logo1_original.png") or img_b64("logo_original.png") or img_b64("logo_192.png")
    if logo_inicio:
       # --- CAMPO DE TEXTO ---
# Usamos text_input para que funcione fluido en todos lados
        requerimiento = st.text_input(
        label="¿En qué podemos ayudarte?",
        placeholder="Hola Car-Sev C.A.! Quisiera asesoría rápida sobre...",
        key="campo_texto_usuario"
    )
        

    # Encabezado Principal Hero
    st.markdown("""
    <div style="text-align: center; padding: 10px 10px 10px 10px;">
        <span class="ornament-gold">✦ MOLDES DE POLIURETANO DE ALTA DENSIDAD ✦</span>
        <h1 style="font-family:'Playfair Display', serif; font-size: clamp(2.2rem, 5vw, 3.6rem); color: #1A1A1A; margin: 12px 0 8px 0; font-weight:700;">
            CAR-SEV C.A.
        </h1>
        <p style="font-size: 1.05rem; color: #555555; max-width: 780px; margin: 0 auto 24px auto; line-height: 1.6;">
            Líderes en la fabricación industrial de moldes de goma y poliuretano elastomérico para el estampado profesional de pisos, pavimentos y superficies decorativas en concreto. Producción en Valencia, Venezuela.
        </p>
    </div>
    <div class="divider-gold"></div>
    """, unsafe_allow_html=True)

  # --- LOGO EN LA PARTE CENTRAL ---
col_logo1, col_logo_centro, col_logo2 = st.columns([1, 2, 1]) 
with col_logo_centro:
    st.image("logo1_original.png", use_column_width=True)

# Ventajas Clave / Pilares
col1, col2, col3 = st.columns(3)

with col1:
        st.markdown("""
        <div class="luxury-card" style="text-align:center; height:100%;">
            <div style="font-size: 2.2rem; margin-bottom: 10px;">🛡️</div>
            <div class="card-subtitle">Máxima Durabilidad</div>
            <div class="card-title">Goma Indeformable</div>
            <div class="card-text">
                Formulados con resinas elastoméricas de alta densidad (Shore A 60-70) resistentes al desgarro, fricción continua y químicos desmoldantes.
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
        st.markdown("""
        <div class="luxury-card" style="text-align:center; height:100%;">
            <div style="font-size: 2.2rem; margin-bottom: 10px;">🎨</div>
            <div class="card-subtitle">Detalle Hiper-Realista</div>
            <div class="card-title">Grabado 3D Natural</div>
            <div class="card-text">
                Copiado milimétrico de vetas de madera, piedras rústicas, adoquines y lajas para lograr acabados estéticos de categoría lujo.
            </div>
        </div>
        """, unsafe_allow_html=True)

with col3:
        st.markdown("""
        <div class="luxury-card" style="text-align:center; height:100%;">
            <div style="font-size: 2.2rem; margin-bottom: 10px;">⚡</div>
            <div class="card-subtitle">Alto Rendimiento</div>
            <div class="card-title">Productividad en Obra</div>
            <div class="card-text">
                Encastres perfectos entre moldes que evitan rebabas de concreto, acelerando los metros cuadrados estampados por jornada de vaciado.
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    # 📹 SECCIÓN DESTACADA DE VIDEO DE YOUTUBE INTERACTIVO
st.markdown("""
    <div style="text-align: center; margin-bottom: 24px;">
        <span class="ornament-gold">✦ DEMOSTRACIÓN EN OBRA & TALLER ✦</span>
        <h2 style="font-family:'Playfair Display', serif; font-size: clamp(1.8rem, 4vw, 2.6rem); color: #1A1A1A; margin: 8px 0;">
            El Arte del Estampado de Pisos
        </h2>
        <p style="font-size: 0.9rem; color: #6B6B6B; max-width: 650px; margin: 0 auto 16px auto;">
            Mira nuestro video explicativo en alta definición para observar todo el proceso técnico: desde la fabricación de la goma hasta la aplicación en concreto fresco, desmoldeo y sellado final.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Reproductor de Video Streamlit integrado                                                                                                                  v_col1, v_col2, v_col3 = st.columns([1, 8, 1])
      with v_col2:
      st.video("https://www.youtube.com/watch?v=g1pTvoL8Q10")

    # Paso a Paso del Estampado
    st.markdown("""
    <div style="margin-top: 36px; padding: 28px; background: #FFFFFF; border: 2px solid #D4AF37; border-radius: 16px; box-shadow: 0 4px 20px rgba(212,175,55,0.12);">
        <h3 style="font-family:'Playfair Display', serif; color: #8B0000; font-size: 1.4rem; text-align: center; margin-bottom: 20px;">
            Proceso Estándar de Estampado de Pavimentos
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px;">
            <div style="padding: 12px; border-left: 3px solid #D4AF37;">
                <p style="font-weight: 700; color: #AA820A; font-size: 0.8rem;">PASO 1</p>
                <p style="font-weight: 600; color: #1A1A1A;">Vaciado & Nivelado</p>
                <p style="font-size: 0.82rem; color: #555555;">Colocación del concreto con resistencia óptima y enrase de la superficie.</p>
            </div>
            <div style="padding: 12px; border-left: 3px solid #D4AF37;">
                <p style="font-weight: 700; color: #AA820A; font-size: 0.8rem;">PASO 2</p>
                <p style="font-weight: 600; color: #1A1A1A;">Color & Desmoldante</p>
                <p style="font-size: 0.82rem; color: #555555;">Esparcido de endurecedor de color y capa desmoldante protectora.</p>
            </div>
            <div style="padding: 12px; border-left: 3px solid #D4AF37;">
                <p style="font-weight: 700; color: #AA820A; font-size: 0.8rem;">PASO 3</p>
                <p style="font-weight: 600; color: #1A1A1A;">Estampado Car-Sev</p>
                <p style="font-size: 0.82rem; color: #555555;">Presión continua con moldes rígidos y ajuste de remates con moldes flex.</p>
            </div>
            <div style="padding: 12px; border-left: 3px solid #D4AF37;">
                <p style="font-weight: 700; color: #AA820A; font-size: 0.8rem;">PASO 4</p>
                <p style="font-weight: 600; color: #1A1A1A;">Lavado & Sellado Lujo</p>
                <p style="font-size: 0.82rem; color: #555555;">Lavado a presión de excesos y aplicación de sellador acrílico protector brillante.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── 9. SECCIÓN 2: CATÁLOGO COMPLETO DE 14 MOLDES ─────────────────────────────
elif "Catálogo" in menu_option:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 10px 0;">
        <span class="ornament-gold">✦ GALERÍA DE 14 MODELOS EXCLUSIVOS ✦</span>
        <h2 style="font-family:'Playfair Display', serif; font-size: clamp(2rem, 4vw, 2.8rem); color: #1A1A1A; margin: 8px 0;">
            Catálogo Completo de Moldes de Goma
        </h2>
        <p style="font-size: 0.9rem; color: #6B6B6B; max-width: 650px; margin: 0 auto 20px auto;">
            Explora nuestra colección completa de 14 diseños exclusivos fabricados con goma de poliuretano industrial de alta resistencia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Filtro por Categoría
    categories = ["Todos (14)", "Piedras & Lajas", "Adoquines", "Maderas"]
    selected_cat = st.selectbox("Filtrar por Categoría:", categories, index=0)

    st.markdown('<div class="divider-gold"></div>', unsafe_allow_html=True)

    # Filtrar productos
    filtered_catalog = CATALOG if selected_cat == "Todos (14)" else [p for p in CATALOG if p["category"] == selected_cat]

    # Despliegue en Grilla de 3 Columnas
    cols = st.columns(3)
    for idx, product in enumerate(filtered_catalog):
        with cols[idx % 3]:
            b64_src = img_b64(product["file"])

            if b64_src:
                img_element = f'<img src="{b64_src}" alt="{product["name"]}" style="width:100%; height:210px; object-fit:cover; display:block;">'
            else:
                img_element = f'''
                <div style="height:210px; background:#F5F0E8; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#D4AF37;">
                    <span style="font-size:2.5rem;">🧩</span>
                    <span style="font-size:0.78rem; font-weight:600; margin-top:6px;">{product["name"]}</span>
                </div>
                '''

            card_html = f"""
            <div class="luxury-card" style="padding:0; overflow:hidden;">
                <div style="position:relative; aspect-ratio:4/3; overflow:hidden;">
                    {img_element}
                    <div style="position:absolute; top:12px; right:12px; background:rgba(26,26,26,0.85); color:#FFE57F; padding:4px 10px; border-radius:20px; font-size:0.72rem; font-weight:700; border:1px solid #D4AF37;">
                        {product['category']}
                    </div>
                </div>
                <div style="padding: 20px;">
                    <div class="card-title" style="font-size:1.15rem; margin-bottom:4px;">{product['name']}</div>
                    <div style="font-size:0.78rem; color:#AA820A; font-weight:700; margin-bottom:10px;">
                        Medidas: {product['dimensions']} | Dureza: {product['hardness']}
                    </div>
                    <div class="card-text" style="font-size:0.82rem; margin-bottom:16px;">
                        {product['caption']}
                    </div>
                    <div style="font-family:'Playfair Display',serif; font-size:1.25rem; font-weight:700; color:#1A1A1A; text-align:center; margin-bottom:14px;">
                        ${product['price_usd']:.2f} USD <span style="font-size:0.7rem; font-family:'Montserrat',sans-serif; color:#777;">/ unidad</span>
                    </div>
                    {wa_button(product['msg'], '✦ Cotizar este Molde')}
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)


# ── 10. SECCIÓN 3: COTIZADOR / PEDIDOS INTERACTIVO CON FICHA PDF ─────────────
elif "Cotizador" in menu_option:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 10px 0;">
        <span class="ornament-gold">✦ CALCULADORA DE PROYECTO & MATERIALES ✦</span>
        <h2 style="font-family:'Playfair Display',serif; font-size: clamp(2rem, 4vw, 2.8rem); color: #1A1A1A; margin: 8px 0;">
            Cotizador Interactivo de Moldes y Pisos
        </h2>
        <p style="font-size: 0.9rem; color: #6B6B6B; max-width: 680px; margin: 0 auto 20px auto;">
            Ingresa la extensión de tu obra en metros cuadrados ($m^2$) para obtener una estimación automatizada de los moldes y materiales recomendados.
        </p>
    </div>
    <div class="divider-gold"></div>
    """, unsafe_allow_html=True)

    # Botón prominente para descargar Ficha Técnica en PDF
    pdf_path = ASSETS_DIR / "carsev_rendimiento_material.pdf"
    if pdf_path.exists():
        st.download_button(
            label="📑 Descargar Tabla Oficial de Rendimiento de Materiales (PDF Car-Sev)",
            data=pdf_path.read_bytes(),
            file_name="carsev_rendimiento_material.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.markdown("<br>", unsafe_allow_html=True)

    c_col1, c_col2 = st.columns([1.1, 1], gap="large")

    with c_col1:
        st.markdown('<div class="luxury-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Parámetros del Proyecto</div>', unsafe_allow_html=True)

        m2_area = st.number_input("Área total a estampar (m²):", min_value=10, max_value=10000, value=120, step=10)

        mold_type = st.selectbox(
            "Selecciona el Diseño de Molde Principal (14 disponibles):",
            [p["name"] for p in CATALOG]
        )

        selected_mold_obj = next((p for p in CATALOG if p["name"] == mold_type), CATALOG[0])

        crew_size = st.selectbox(
            "Cantidad de Cuadrillas de Trabajo Simultáneas:",
            ["1 Cuadrilla (Estándar: 3-4 Moldes Rígidos)", "2 Cuadrillas (Obra Rápida: 6-8 Moldes Rígidos)"]
        )

        st.markdown("<p style='font-weight:700; color:#1A1A1A; margin-top:16px;'>Insumos Complementarios de Estampado:</p>", unsafe_allow_html=True)
        inc_color = st.checkbox("Endurecedor de Color en Polvo (5 kg/m²)", value=True)
        inc_release = st.checkbox("Desmoldante en Polvo Anti-Adherente (0.15 kg/m²)", value=True)
        inc_flex = st.checkbox("Incluir Molde Flex Ultra-Plegable para Remates de Paredes", value=True)
        inc_sealer = st.checkbox("Sellador Acrílico de Lujo Alto Brillo (0.20 L/m²)", value=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with c_col2:
        # CÁLCULOS TÉCNICOS AUTOMATIZADOS
        rigid_count = 4 if "1 Cuadrilla" in crew_size else 8
        flex_count = 1 if inc_flex else 0

        subtotal_molds = (rigid_count * selected_mold_obj["price_usd"]) + (flex_count * 55.00)

        # Insumos estimados
        kg_color = m2_area * 5.0 if inc_color else 0
        kg_release = m2_area * 0.15 if inc_release else 0
        liters_sealer = m2_area * 0.20 if inc_sealer else 0

        st.markdown("""
        <div class="luxury-card" style="background:#FAFAF8 !important;">
            <div class="card-subtitle">RESUMEN TÉCNICO DE REQUERIMIENTOS</div>
            <div class="card-title">Presupuesto Estimado de Equipamiento</div>
            <hr style="border:0; border-top:1px solid #D4AF37; margin:12px 0;">
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:16px;">
            <div class="metric-box">
                <div class="metric-label">Moldes Rígidos Requeridos</div>
                <div class="metric-value">{rigid_count} Unidades</div>
                <div style="font-size:0.75rem; color:#666;">{selected_mold_obj['name']}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Moldes Flex de Remate</div>
                <div class="metric-value">{flex_count} Unidad</div>
                <div style="font-size:0.75rem; color:#666;">Para esquinas y bordes</div>
            </div>
        </div>

        <div style="margin-bottom:16px; padding:12px; background:#FFFFFF; border-radius:8px; border:1px solid #E0E0E0;">
            <p style="font-weight:700; font-size:0.82rem; color:#1A1A1A; margin-bottom:6px;">Insumos Estimados para {m2_area} m²:</p>
            <ul style="font-size:0.8rem; color:#555555; padding-left:18px; margin:0;">
                <li>Colorante Endurecedor: <strong>{kg_color:.1f} kg</strong></li>
                <li>Desmoldante en Polvo: <strong>{kg_release:.1f} kg</strong></li>
                <li>Sellador Acrílico Lujo: <strong>{liters_sealer:.1f} Litros</strong></li>
            </ul>
        </div>

        <div style="text-align:center; padding:16px; background:#FFFFFF; border:2px solid #D4AF37; border-radius:12px; margin-bottom:16px;">
            <div style="font-size:0.78rem; color:#AA820A; font-weight:700; text-transform:uppercase;">Inversión Estimada en Moldes Car-Sev</div>
            <div style="font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; color:#8B0000; margin:4px 0;">
                ${subtotal_molds:.2f} USD
            </div>
            <div style="font-size:0.72rem; color:#777;">*Los precios de insumos químicos se confirman según disponibilidad de color.</div>
        </div>
        """, unsafe_allow_html=True)

        # Generador de mensaje listo para enviar a WhatsApp
        quote_msg = (
            f"Hola Car-Sev C.A.! Solícito cotización formal para un proyecto de estampado:\n\n"
            f"📌 Área Total: {m2_area} m²\n"
            f"🧩 Molde Elegido: {selected_mold_obj['name']}\n"
            f"🔢 Cantidad de Moldes: {rigid_count} Rígidos + {flex_count} Flex\n"
            f"🧪 Insumos Requeridos: Colorante ({kg_color:.0f}kg), Desmoldante ({kg_release:.1f}kg), Sellador ({liters_sealer:.0f}L)\n"
            f"💵 Subtotal Estimado Moldes: ${subtotal_molds:.2f} USD\n\n"
            f"Por favor indicarme tiempo de entrega y datos bancarios."
        )

        st.markdown(wa_button(quote_msg, "✦ Enviar Cotización por WhatsApp"), unsafe_allow_html=True)
        


# ── 11. SECCIÓN 4: CONTACTO & UBICACIÓN SATELITAL (VALENCIA, VENEZUELA) ───────
elif "Contacto" in menu_option:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 10px 0;">
        <span class="ornament-gold">✦ ATENCIÓN INSTITUCIONAL & ASESORÍA ✦</span>
        <h2 style="font-family:'Playfair Display',serif; font-size: clamp(2rem, 4vw, 2.8rem); color: #1A1A1A; margin: 8px 0;">
            Contacto & Planta de Producción
        </h2>
        <p style="font-size: 0.9rem; color: #6B6B6B; max-width: 650px; margin: 0 auto 20px auto;">
            Fabricacion Urbanizacion Parque Valencia en Valencia, Estado Carabobo, Venezuela. Envíos nacionales e internacionales.
        </p>
    </div>
    <div class="divider-gold"></div>
    """, unsafe_allow_html=True)

    ct_col1, ct_col2 = st.columns([1, 1], gap="large")
    
    with ct_col1:
        st.markdown(f"""
        <div style="margin-bottom:16px;">
            <div style="font-size:0.75rem; color:#AA820A; font-weight:700; text-transform:uppercase;">Planta Industrial & Sede Principal:</div>
            <div style="font-size:0.9rem; font-weight:600; color:#1A1A1A;">Fabricacion Urbanizacion Parque valencia Car-Sev C.A., Valencia, Estado Carabobo, Venezuela.</div>
        </div>

        <div style="margin-bottom:16px;">
            <div style="font-size:0.75rem; color:#AA820A; font-weight:700; text-transform:uppercase;">Teléfono Oficial & WhatsApp:</div>
            <div style="font-size:0.95rem; font-weight:700; color:#8B0000;">{WHATSAPP_DISPLAY}</div>
        </div>

        <div style="margin-bottom:16px;">
            <div style="font-size:0.75rem; color:#AA820A; font-weight:700; text-transform:uppercase;">Correo Electrónico:</div>
            <div style="font-size:0.9rem; font-weight:600; color:#1A1A1A;">sevillacarlos1@gmail.com</div>
        </div>

        <div style="margin-bottom:24px;">
            <div style="font-size:0.75rem; color:#AA820A; font-weight:700; text-transform:uppercase;">Horario de Atención Presencial:</div>
            <div style="font-size:0.88rem; color:#555555;">Lunes a Viernes: 8:00 AM – 5:00 PM | Sábados: 8:00 AM – 12:00 PM</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(wa_button("Hola Car-Sev C.A.! Quisiera coordinar una visita a la planta en Valencia o solicitar cotización.", "✦ Escribir a WhatsApp Oficial (+58 0416-6481679)"), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with ct_col2:
        st.markdown("""
        <div class="luxury-card" style="height:100%;">
            <div class="card-subtitle">UBICACIÓN GEOGRÁFICA SATELITAL</div>
            <div class="card-title">Valencia, Carabobo, Venezuela</div>
            <p class="card-text" style="margin-bottom:16px;">
                La Fabricacion se encuentra en el corazón industrial de Valencia para un despacho rápido a todo el territorio nacional.
            </p>
        """, unsafe_allow_html=True)

        # Mapa interactivo — Parque Valencia, Carabobo, Venezuela
        st.markdown("""
        <div style="width:100%; height:280px; border-radius:12px; overflow:hidden; border:2px solid #D4AF37; margin-bottom:8px;">
            <iframe
                width="100%"
                height="100%"
                frameborder="0"
                scrolling="no"
                marginheight="0"
                marginwidth="0"
                src="https://www.openstreetmap.org/export/embed.html?bbox=-68.0136%2C10.1421%2C-67.9736%2C10.1821&layer=mapnik&marker=10.1621%2C-67.9936"
                style="border:0;"
                allowfullscreen=""
                loading="lazy">
            </iframe>
        </div>
        <div style="text-align:right; margin-bottom:16px;">
            <a href="https://www.openstreetmap.org/?mlat=10.1621&mlon=-67.9936#map=15/10.1621/-67.9936"
               target="_blank" rel="noopener noreferrer"
               style="font-size:0.72rem; color:#AA820A; font-weight:600; text-decoration:none;">
               &#128205; Ver mapa completo &rarr;
            </a>
        </div>
        """, unsafe_allow_html=True)

       # 1. Estilos CSS optimizados para el Formulario
    st.markdown("""
    <style>
        /* Contenedor del formulario */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
        }

        /* Estilo para los Labels (Títulos de los campos) */
        div[data-testid="stForm"] label {
            color: #1A1A1A !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            margin-bottom: 4px !important;
        }

        /* Campos de texto y área de texto: Fondo claro, bordes limpios y texto oscuro */
        div.stTextInput > div > div > input, 
        div.stTextArea > div > div > textarea {
            background-color: #FAFAFA !important;
            color: #1A1A1A !important;
            border: 1px solid #D1D5DB !important;
            border-radius: 8px !important;
            padding: 12px !important;
            font-family: 'Montserrat', sans-serif !important;
        }

        /* Focus en los campos (al hacer clic) */
        div.stTextInput > div > div > input:focus, 
        div.stTextArea > div > div > textarea:focus {
            border-color: #AA820A !important;
            box-shadow: 0 0 0 1px #AA820A !important;
        }

        /* Botón de envío Industrial/Dorado personalizado */
        div.stFormSubmitButton > button {
            background: linear-gradient(135deg, #D4AF37 0%, #AA820A 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid #8E6B08 !important;
            border-radius: 8px !important;
            padding: 14px 20px !important;
            font-weight: 700 !important;
            font-size: 0.9rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            cursor: pointer !important;
        }

        div.stFormSubmitButton > button:hover {
            background: #8E6B08 !important;
            box-shadow: 0 4px 15px rgba(170, 130, 10, 0.35) !important;
            transform: translateY(-1px) !important;
            color: #FFFFFF !important;
        }
    </style>
    """, unsafe_allow_html=True)

   # 2. Bloque único del Formulario de Contacto
    with st.form("form_valencia"):
        user_name = st.text_input("Nombre Completo:", placeholder="Ej. Carlos Sevilla")
        user_phone = st.text_input("Teléfono / WhatsApp:", placeholder="Ej. 04166481679")
        user_city = st.text_input("Ciudad / Estado:", placeholder="Ej. Valencia, Carabobo")
        user_msg = st.text_area("Detalles de tu consulta:", placeholder="Escribe aquí los detalles de tu requerimiento...")
        
        submit_btn = st.form_submit_button("Enviar Mensaje a Planta Valencia")

        if submit_btn:
            if user_name and user_phone:
                st.success("¡Gracias por contactar a Car-Sev C.A.! Tu mensaje ha sido enviado a nuestra planta en Valencia. Un asesor te responderá a la brevedad.")
            else:
                st.warning("Por favor completa tu Nombre y Teléfono para procesar el mensaje.")

    st.markdown("</div>", unsafe_allow_html=True)

# ── 12. PIE DE PÁGINA PROFESIONAL (FOOTER) ──────────────────────────────────
st.markdown("""
<div class="divider-gold" style="max-width:100%; margin:40px 0 10px 0;"></div>
<footer style="text-align:center; padding: 20px 10px 30px 10px;">
    <p style="font-family:'Playfair Display',serif; font-size:1.4rem; font-weight:700; color:#8B0000; letter-spacing:0.15em; margin-bottom:4px;">
        CAR-SEV C.A.    </p>
    <p class="ornament-gold" style="font-size:0.7rem; margin-bottom:8px;">
        © 2026 CAR-SEV C.A. · TODOS LOS DERECHOS RESERVADOS · VALENCIA, CARABOBO, VENEZUELA
    </p>
    <p style="font-size:0.75rem; color:#777777;">
        Fabricación Industrial de Moldes de Goma y Pavimentos Decorativos de Alta Resistencia
    </p>
</footer>
""", unsafe_allow_html=True)