import streamlit as st
import random
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Leo's Animal Kingdom", page_icon="🦁", layout="centered")

# --- MAXI DATABASE ANIMALI ESTESO (Oltre 120 animali da tutto il mondo) ---
ANIMALI = {
    # MAMMIFERI (Anche i più strani!)
    "Leone 🦁": "Mammifero", "Delfino 🐬": "Mammifero", "Pipistrello 🦇": "Mammifero",
    "Elefante 🐘": "Mammifero", "Balena 🐋": "Mammifero", "Cane 🐕": "Mammifero",
    "Gatto 🐈": "Mammifero", "Tigre 🐅": "Mammifero", "Orso 🐻": "Mammifero",
    "Giraffa 🦒": "Mammifero", "Zebra 🦓": "Mammifero", "Scimmia 🐒": "Mammifero",
    "Canguro 🦘": "Mammifero", "Koala 🐨": "Mammifero", "Panda 🐼": "Mammifero",
    "Ornitorinco 🦦🦆": "Mammifero", "Capibara 🟤": "Mammifero", "Pipistrello della Frutta 🦇🍌": "Mammifero",
    "Bradipo 🦥": "Mammifero", "Lontra 🦦": "Mammifero", "Castoro 🦫": "Mammifero",
    "Puzzola 🦨": "Mammifero", "Tasso 🦡": "Mammifero", "Procione 🦝": "Mammifero",
    "Lama 🦙": "Mammifero", "Alpaca 🦙": "Mammifero", "Iena 🤎": "Mammifero",
    "Ghepardo 🐆": "Mammifero", "Pantera 🐈‍⬛": "Mammifero", "Lemure 🐒": "Mammifero",
    "Gorilla 🦍": "Mammifero", "Orango 🦧": "Mammifero", "Alce 🫎": "Mammifero",
    "Cervo 🦌": "Mammifero", "Bisonte 🦬": "Mammifero", "Cinghiale 🐗": "Mammifero",
    "Formichiere 🐜👅": "Mammifero", "Foca 🦭": "Mammifero", "Tricheco 🦭": "Mammifero",
    "Leone Marino 🦭": "Mammifero", "Orca 🐋": "Mammifero", "Narvalo 🐳🦄": "Mammifero",
    "Beluga 🐳": "Mammifero", "Suricato 🦦": "Mammifero", "Armadillo 🪖": "Mammifero",
    "Porcellino d'India 🐹": "Mammifero", "Criceto 🐹": "Mammifero", "Lupo 🐺": "Mammifero",
    "Volpe 🦊": "Mammifero", "Pangolino 🛡️": "Mammifero", "Vombato 🐻⬇️": "Mammifero",

    # UCCELLI
    "Aquila 🦅": "Uccello", "Pinguino 🐧": "Uccello", "Pappagallo 🦜": "Uccello",
    "Gufo 🦉": "Uccello", "Gallina 🐔": "Uccello", "Cigno 🦢": "Uccello",
    "Anatra 🦆": "Uccello", "Fenicottero 🦩": "Uccello", "Pavone 🦚": "Uccello",
    "Gabbiano 🕊️": "Uccello", "Tacchino 🦃": "Uccello", "Piccione 🐦": "Uccello",
    "Kiwi 🥝🐦": "Uccello", "Struzzo 🦅🏃": "Uccello", "Emù 🦅": "Uccello",
    "Pellicano 🦢🐟": "Uccello", "Tucano 🦜": "Uccello", "Colibrì 🐦✨": "Uccello",
    "Picchio 🐦🪵": "Uccello", "Falco 🦅": "Uccello", "Avvoltoio 🦅": "Uccello",
    "Corvo 🐦‍⬛": "Uccello", "Pettirosso 🐦": "Uccello", "Rondine 🐦": "Uccello",
    
    # RETTILI
    "Serpente 🐍": "Rettile", "Coccodrillo 🐊": "Rettile", "Tartaruga 🐢": "Rettile",
    "Camaleonte 🦎": "Rettile", "Iguana 🦎": "Rettile", "Lucertola 🦎": "Rettile",
    "Anaconda 🐍": "Rettile", "Pitone 🐍": "Rettile", "Cobra 🐍": "Rettile",
    "Alligatore 🐊": "Rettile", "Geco 🦎": "Rettile", "Drago di Komodo 🐉": "Rettile",
    
    # PESCI
    "Squalo 🦈": "Pesce", "Pesce Pagliaccio 🐠": "Pesce", "Salmone 🐟": "Pesce",
    "Pesce Palla 🐡": "Pesce", "Cavalluccio Marino 🌊🐎": "Pesce", "Tonno 🐟": "Pesce",
    "Pesce Spada 🐟⚔️": "Pesce", "Piranha 🐟🦷": "Pesce", "Anguilla 🐟⚡": "Pesce",
    "Murena 🐟": "Pesce", "Carpa 🐟": "Pesce", "Razza 🦈": "Pesce",
    "Squalo Martello 🦈🔨": "Pesce", "Pesce Luna 🐟🌕": "Pesce",
    
    # ANFIBI
    "Rana 🐸": "Anfibio", "Rospo 🐸": "Anfibio", "Salamandra 🦎💧": "Anfibio",
    "Axolotl (Assolotto) 🦎🎀": "Anfibio", "Tritone 🦎💧": "Anfibio", "Raganella 🐸🌳": "Anfibio",
    "Rana Freccia Velenosa 🐸⚠️": "Anfibio",
    
    # INSETTI
    "Farfalla 🦋": "Insetto", "Ape 🐝": "Insetto", "Coccinella 🐞": "Insetto",
    "Formica 🐜": "Insetto", "Zanzara 🦟": "Insetto", "Mosca 🪰": "Insetto",
    "Grillo 🦗": "Insetto", "Cavalletta 🦗": "Insetto", "Scarafaggio 🪳": "Insetto",
    "Mantide Religiosa 🦗🙏": "Insetto", "Scarabeo 🪲": "Insetto", "Lucciola 🪲✨": "Insetto",
    "Libellula 🦟✨": "Insetto", "Vespa 🐝": "Insetto", "Calabrone 🐝": "Insetto",
    "Falena 🦋🌙": "Insetto",
    
    # INVERTEBRATI
    "Polpo 🐙": "Invertebrato", "Granchio 🦀": "Invertebrato", "Aragosta 🦞": "Invertebrato",
    "Gambero 🦐": "Invertebrato", "Calamaro 🦑": "Invertebrato", "Chiocciola 🐌": "Invertebrato",
    "Stella Marina 🌟": "Invertebrato", "Medusa 🪼": "Invertebrato", "Ragno 🕷️": "Invertebrato",
    "Scorpione 🦂": "Invertebrato", "Verme 🪱": "Invertebrato", "Lombrico 🪱": "Invertebrato",
    "Millepiedi 🐛": "Invertebrato", "Sanguisuga 🪱🩸": "Invertebrato", "Tarantola 🕷️🕸️": "Invertebrato",
    "Ostrica 🦪": "Invertebrato", "Riccio di Mare 🦔🌊": "Invertebrato", "Corallo 🪸": "Invertebrato",
    "Spugna di Mare 🧽": "Invertebrato"
}

LISTA_CATEGORIE = list(set(ANIMALI.values()))

# --- STILE CSS (Tema Giungla) ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 3.5rem !important; 
        max-width: 500px !important;
    }
    .main { background-color: #0e1117; color: #ffffff; }
    .titolo-game {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF00;
        text-align: center;
        text-shadow: 2px 2px #ff00ff;
        font-size: 32px !important;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .domanda-box {
        background: linear-gradient(45deg, #2b580c, #639a67);
        padding: 25px;
        border-radius: 20px;
        border: 4px solid #a3c9a8;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 15px;
        box-shadow: 0px 5px 20px rgba(99, 154, 103, 0.3);
    }
    div.stButton > button {
        width: 100%;
        height: 75px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        background-color: #3e3e3e !important;
        color: white !important;
        border: 2px solid #555 !important;
    }
    .ripasso-box {
        background-color: #1e1e1e;
        border-left: 5px solid #ffcc00;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
        text-align: left;
    }
    @media (max-width: 600px) {
        .block-container { padding-top: 2.8rem !important; }
        .titolo-game { font-size: 26px !important; }
        .domanda-box { padding: 15px !important; }
        .domanda-box p:last-child { font-size: 38px !important; }
        div.stButton > button { height: 65px !important; font-size: 18px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGICA DEL GIOCO ---
TOTAL_DOMANDE = 15
TEMPO_LIMITE = 7.0

if 'stato_ani' not in st.session_state:
    st.session_state.stato_ani = 'inizio'
if 'punteggio_ani' not in st.session_state:
    st.session_state.punteggio_ani = 0
if 'round_ani' not in st.session_state:
    st.session_state.round_ani = 1
if 'msg_ani' not in st.session_state:
    st.session_state.msg_ani = ""
if 'lista_errori' not in st.session_state:
    st.session_state.lista_errori = []

def genera_domanda_animale():
    animale = random.choice(list(ANIMALI.keys()))
    categoria_giusta = ANIMALI[animale]
    
    st.session_state.animale_corrente = animale
    st.session_state.categoria_giusta = categoria_giusta
    
    categorie_errate = random.sample([c for c in LISTA_CATEGORIE if c != categoria_giusta], 2)
    
    opzioni = [categoria_giusta] + categorie_errate
    random.shuffle(opzioni)
    st.session_state.opzioni_ani = opzioni
    st.session_state.tempo_inizio_ani = time.time()

def verifica_ani(scelta):
    tempo_risposta = time.time() - st.session_state.tempo_inizio_ani
    giusta = st.session_state.categoria_giusta
    
    # Rimuove le emoji solo per il messaggio in basso
    parti_nome = st.session_state.animale_corrente.split(" ")
    animale_puro = " ".join(parti_nome[:-1]) if len(parti_nome) > 1 else parti_nome[0]
    
    if tempo_risposta > TEMPO_LIMITE:
        st.session_state.msg_ani = f"⏱️ TEMPO SCADUTO! Era: {giusta}"
        st.session_state.tipo_msg_ani = "error"
        st.session_state.lista_errori.append({"animale": st.session_state.animale_corrente, "risposta": "Tempo Scaduto ⏳", "giusta": giusta})
    elif scelta == giusta:
        st.session_state.msg_ani = f"🚀 BRAVO! Il {animale_puro} è un {giusta}!"
        st.session_state.punteggio_ani += 1
        st.session_state.tipo_msg_ani = "success"
    else:
        st.session_state.msg_ani = f"👾 OPS! Il {animale_puro} è un {giusta}!"
        st.session_state.tipo_msg_ani = "error"
        st.session_state.lista_errori.append({"animale": st.session_state.animale_corrente, "risposta": scelta, "giusta": giusta})
        
    st.session_state.round_ani += 1
    if st.session_state.round_ani > TOTAL_DOMANDE:
        st.session_state.stato_ani = 'fine'
    else:
        genera_domanda_animale()

# --- INTERFACCIA ---
st.markdown('<p class="titolo-game">LEO\'S ANIMAL KINGDOM</p>', unsafe_allow_html=True)

if st.session_state.stato_ani == 'inizio':
    st.markdown(f"<div style='text-align: center; margin-bottom: 20px;'>A quale famiglia appartiene questo animale?<br>Hai <b>{int(TEMPO_LIMITE)} secondi</b> per rispondere!</div>", unsafe_allow_html=True)
    if st.button("🌿 INIZIA L'ESPLORAZIONE", use_container_width=True):
        st.session_state.punteggio_ani = 0
        st.session_state.round_ani = 1
        st.session_state.msg_ani = ""
        st.session_state.lista_errori = [] 
        st.session_state.stato_ani = 'in_corso'
        genera_domanda_animale()
        st.rerun()

elif st.session_state.stato_ani == 'in_corso':
    st.progress((st.session_state.round_ani - 1) / TOTAL_DOMANDE)
    
    if st.session_state.msg_ani:
        if st.session_state.tipo_msg_ani == "success":
            st.success(st.session_state.msg_ani)
        else:
            st.error(st.session_state.msg_ani)
    else:
        st.write("")

    st.markdown(f"""
    <div class="domanda-box">
        <p style='margin: 0; opacity: 0.8; font-size: 16px; color: white;'>CHE ANIMALE È...</p>
        <p style='margin: 0; font-weight: bold; font-family: "Courier New"; color: white;'>{st.session_state.animale_corrente}</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i in range(3):
        opzione = st.session_state.opzioni_ani[i]
        if st.button(opzione, key=f"ani_{i}", use_container_width=True):
            verifica_ani(opzione)
            st.rerun()

elif st.session_state.stato_ani == 'fine':
    st.balloons()
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.header("ESPLORAZIONE COMPLETATA! 🏁")
    st.markdown(f"<h1>Punteggio: {st.session_state.punteggio_ani}/{TOTAL_DOMANDE}</h1>", unsafe_allow_html=True)
    
    if st.session_state.punteggio_ani == TOTAL_DOMANDE:
        st.success("SEI UN VERO ZOOLOGO! Punteggio Perfetto! 🦁🏆")
    else:
        # SEZIONE RIPASSO DEGLI ERRORI
        st.markdown("<h3 style='color: #ffcc00; margin-top: 20px;'>📝 Ripasso per il prossimo Safari:</h3>", unsafe_allow_html=True)
        for errore in st.session_state.lista_errori:
            st.markdown(f"""
            <div class="ripasso-box">
                <b>{errore['animale']}</b><br>
                Hai risposto: <span style='color: #ff4b4b;'>{errore['risposta']}</span> ❌<br>
                Categoria giusta: <span style='color: #00ff00;'>{errore['giusta']}</span> ✅
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎮 RIGIOCA", use_container_width=True):
        st.session_state.stato_ani = 'inizio'
        st.session_state.msg_ani = ""
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
