import streamlit as st
import random
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Leo's Game Center", page_icon="🕹️", layout="centered")

# ==========================================
# 1. DATABASE DEI GIOCHI
# ==========================================

# Database Animali (Puoi incollare qui la lista gigante da 120 animali se vuoi!)
ANIMALI = {
    "Leone 🦁": "Mammifero", "Delfino 🐬": "Mammifero", "Pipistrello 🦇": "Mammifero",
    "Elefante 🐘": "Mammifero", "Canguro 🦘": "Mammifero", "Ornitorinco 🦦🦆": "Mammifero",
    "Aquila 🦅": "Uccello", "Pinguino 🐧": "Uccello", "Pappagallo 🦜": "Uccello",
    "Serpente 🐍": "Rettile", "Coccodrillo 🐊": "Rettile", "Tartaruga 🐢": "Rettile",
    "Squalo 🦈": "Pesce", "Pesce Pagliaccio 🐠": "Pesce", "Cavalluccio Marino 🌊🐎": "Pesce",
    "Rana 🐸": "Anfibio", "Axolotl 🦎🎀": "Anfibio",
    "Farfalla 🦋": "Insetto", "Ape 🐝": "Insetto",
    "Polpo 🐙": "Invertebrato", "Granchio 🦀": "Invertebrato", "Ragno 🕷️": "Invertebrato"
}
LISTA_CATEGORIE_ANI = list(set(ANIMALI.values()))

# Database Bandiere (Paese: Codice ISO)
PAESI_MONDO = {
    "Italia": "it", "Francia": "fr", "Spagna": "es", "Germania": "de", 
    "Regno Unito": "gb", "Stati Uniti": "us", "Brasile": "br", "Giappone": "jp",
    "Argentina": "ar", "Canada": "ca", "Australia": "au", "Cina": "cn"
}

# Database Parole (Anagrammi)
PAROLE_ANAGRAMMI = [
    "GATTO", "CANE", "SOLE", "MARE", "TAVOLO", "SCUOLA", "PIZZA", "CALCIO", 
    "LIBRO", "MATITA", "ZAINO", "GELATO", "STELLA", "LUNA", "AEREO", "TRENO"
]

# Database Italia (Capoluogo: Regione)
MAPPA_ITALIA = {
    "Torino": "Piemonte", "Milano": "Lombardia", "Venezia": "Veneto", "Genova": "Liguria",
    "Bologna": "Emilia-Romagna", "Firenze": "Toscana", "Roma": "Lazio", "Napoli": "Campania",
    "Bari": "Puglia", "Palermo": "Sicilia", "Cagliari": "Sardegna", "Aosta": "Valle d'Aosta"
}
LISTA_REGIONI = list(set(MAPPA_ITALIA.values()))


# ==========================================
# 2. STILE CSS UNIFICATO E IMPOSTAZIONI
# ==========================================
TOTAL_DOMANDE = 15
TEMPO_LIMITE = 7.0

st.markdown("""
    <style>
    .block-container { padding-top: 2rem !important; max-width: 500px !important; }
    .main { background-color: #0e1117; color: #ffffff; }
    
    .titolo-game {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF00;
        text-align: center;
        text-shadow: 2px 2px #ff00ff;
        font-size: 32px !important;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .domanda-box {
        background: linear-gradient(45deg, #182848, #4b6cb7);
        padding: 20px;
        border-radius: 20px;
        border: 4px solid #00d2ff;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 5px 20px rgba(0, 210, 255, 0.3);
    }
    .immagine-box {
        background: white; padding: 10px; border-radius: 15px;
        border: 4px solid #00d2ff; text-align: center; margin-bottom: 15px;
    }
    div.stButton > button {
        width: 100%; height: 70px !important; font-size: 20px !important;
        font-weight: bold !important; border-radius: 15px !important;
        background-color: #3e3e3e !important; color: white !important;
        border: 2px solid #555 !important;
    }
    .btn-menu > div > button {
        height: 80px !important; font-size: 22px !important; 
        border-color: #00FF00 !important; margin-bottom: 10px;
    }
    @media (max-width: 600px) {
        .titolo-game { font-size: 26px !important; }
        .domanda-box { padding: 15px !important; }
        .domanda-box p:last-child { font-size: 35px !important; }
        div.stButton > button { height: 60px !important; font-size: 16px !important; }
        .btn-menu > div > button { height: 70px !important; font-size: 18px !important; }
    }
    </style>
    """, unsafe_allow_html=True)


# ==========================================
# 3. GESTORE DELLE SCHERMATE (ROUTER)
# ==========================================
if 'schermata' not in st.session_state:
    st.session_state.schermata = 'menu'

# Funzione universale per tornare al menu
def torna_al_menu():
    st.session_state.schermata = 'menu'
    st.rerun()

# ==========================================
# FUNZIONI DI SUPPORTO PER I GIOCHI
# ==========================================
def inizializza_gioco(prefisso):
    st.session_state[f'stato_{prefisso}'] = 'inizio'
    st.session_state[f'punteggio_{prefisso}'] = 0
    st.session_state[f'round_{prefisso}'] = 1
    st.session_state[f'msg_{prefisso}'] = ""

def controlla_tempo(prefisso, giusta):
    tempo = time.time() - st.session_state[f'tempo_inizio_{prefisso}']
    if tempo > TEMPO_LIMITE:
        st.session_state[f'msg_{prefisso}'] = f"⏱️ TEMPO SCADUTO! Era: {giusta}"
        st.session_state[f'tipo_msg_{prefisso}'] = "error"
        return False
    return True

# --- GIOCO 1: TABELLINE (prefisso 'tab') ---
if 'stato_tab' not in st.session_state: inizializza_gioco('tab')
def genera_tab():
    st.session_state.f1 = random.randint(2, 10)
    st.session_state.f2 = random.randint(2, 10)
    giusta = st.session_state.f1 * st.session_state.f2
    opzioni = {giusta, giusta + random.randint(1,5), giusta - random.randint(1,5)}
    while len(opzioni) < 3: opzioni.add(giusta + random.randint(6,10))
    st.session_state.opz_tab = list(opzioni)
    random.shuffle(st.session_state.opz_tab)
    st.session_state.tempo_inizio_tab = time.time()
def verifica_tab(scelta):
    giusta = st.session_state.f1 * st.session_state.f2
    if controlla_tempo('tab', giusta):
        if scelta == giusta:
            st.session_state.msg_tab = "🚀 BOOM! Esatto!"
            st.session_state.punteggio_tab += 1
            st.session_state.tipo_msg_tab = "success"
        else:
            st.session_state.msg_tab = f"👾 OPS! Era {giusta}"
            st.session_state.tipo_msg_tab = "error"
    st.session_state.round_tab += 1
    if st.session_state.round_tab > TOTAL_DOMANDE: st.session_state.stato_tab = 'fine'
    else: genera_tab()

# --- GIOCO 2: ANIMALI (prefisso 'ani') ---
if 'stato_ani' not in st.session_state: inizializza_gioco('ani')
def genera_ani():
    animale = random.choice(list(ANIMALI.keys()))
    st.session_state.animale_corr = animale
    st.session_state.cat_giusta = ANIMALI[animale]
    errate = random.sample([c for c in LISTA_CATEGORIE_ANI if c != st.session_state.cat_giusta], 2)
    st.session_state.opz_ani = [st.session_state.cat_giusta] + errate
    random.shuffle(st.session_state.opz_ani)
    st.session_state.tempo_inizio_ani = time.time()
def verifica_ani(scelta):
    giusta = st.session_state.cat_giusta
    nome_puro = st.session_state.animale_corr.split(" ")[0]
    if controlla_tempo('ani', giusta):
        if scelta == giusta:
            st.session_state.msg_ani = f"🚀 BRAVO! È un {giusta}!"
            st.session_state.punteggio_ani += 1
            st.session_state.tipo_msg_ani = "success"
        else:
            st.session_state.msg_ani = f"👾 OPS! Il {nome_puro} è un {giusta}!"
            st.session_state.tipo_msg_ani = "error"
    st.session_state.round_ani += 1
    if st.session_state.round_ani > TOTAL_DOMANDE: st.session_state.stato_ani = 'fine'
    else: genera_ani()

# --- GIOCO 3: BANDIERE (prefisso 'ban') ---
if 'stato_ban' not in st.session_state: inizializza_gioco('ban')
def genera_ban():
    paese = random.choice(list(PAESI_MONDO.keys()))
    st.session_state.paese_corr = paese
    errate = random.sample([p for p in PAESI_MONDO.keys() if p != paese], 2)
    st.session_state.opz_ban = [paese] + errate
    random.shuffle(st.session_state.opz_ban)
    st.session_state.tempo_inizio_ban = time.time()
def verifica_ban(scelta):
    giusta = st.session_state.paese_corr
    if controlla_tempo('ban', giusta):
        if scelta == giusta:
            st.session_state.msg_ban = f"🚀 ESATTO! È la {giusta}!"
            st.session_state.punteggio_ban += 1
            st.session_state.tipo_msg_ban = "success"
        else:
            st.session_state.msg_ban = f"👾 OPS! Era la {giusta}!"
            st.session_state.tipo_msg_ban = "error"
    st.session_state.round_ban += 1
    if st.session_state.round_ban > TOTAL_DOMANDE: st.session_state.stato_ban = 'fine'
    else: genera_ban()

# --- GIOCO 4: ANAGRAMMI (prefisso 'ana') ---
if 'stato_ana' not in st.session_state: inizializza_gioco('ana')
def rimescola(parola):
    l = list(parola)
    random.shuffle(l)
    res = "".join(l)
    return res if res != parola else rimescola(parola)
def genera_ana():
    parola = random.choice(PAROLE_ANAGRAMMI)
    st.session_state.parola_corr = parola
    st.session_state.parola_mix = rimescola(parola)
    errate = random.sample([p for p in PAROLE_ANAGRAMMI if p != parola], 2)
    st.session_state.opz_ana = [parola] + errate
    random.shuffle(st.session_state.opz_ana)
    st.session_state.tempo_inizio_ana = time.time()
def verifica_ana(scelta):
    giusta = st.session_state.parola_corr
    if controlla_tempo('ana', giusta):
        if scelta == giusta:
            st.session_state.msg_ana = f"🚀 SUPER DETECTIVE! Era {giusta}"
            st.session_state.punteggio_ana += 1
            st.session_state.tipo_msg_ana = "success"
        else:
            st.session_state.msg_ana = f"👾 OPS! Era {giusta}"
            st.session_state.tipo_msg_ana = "error"
    st.session_state.round_ana += 1
    if st.session_state.round_ana > TOTAL_DOMANDE: st.session_state.stato_ana = 'fine'
    else: genera_ana()

# --- GIOCO 5: ITALIA (prefisso 'ita') ---
if 'stato_ita' not in st.session_state: inizializza_gioco('ita')
def genera_ita():
    capoluogo = random.choice(list(MAPPA_ITALIA.keys()))
    st.session_state.capoluogo_corr = capoluogo
    st.session_state.regione_giusta = MAPPA_ITALIA[capoluogo]
    errate = random.sample([r for r in LISTA_REGIONI if r != st.session_state.regione_giusta], 2)
    st.session_state.opz_ita = [st.session_state.regione_giusta] + errate
    random.shuffle(st.session_state.opz_ita)
    st.session_state.tempo_inizio_ita = time.time()
def verifica_ita(scelta):
    giusta = st.session_state.regione_giusta
    if controlla_tempo('ita', giusta):
        if scelta == giusta:
            st.session_state.msg_ita = f"🚀 BRAVISSIMO! {st.session_state.capoluogo_corr} è in {giusta}"
            st.session_state.punteggio_ita += 1
            st.session_state.tipo_msg_ita = "success"
        else:
            st.session_state.msg_ita = f"👾 OPS! Si trova in {giusta}"
            st.session_state.tipo_msg_ita = "error"
    st.session_state.round_ita += 1
    if st.session_state.round_ita > TOTAL_DOMANDE: st.session_state.stato_ita = 'fine'
    else: genera_ita()


# ==========================================
# INTERFACCIA GRAFICA (IL ROUTER)
# ==========================================

st.markdown('<p class="titolo-game">🕹️ LEO\'S GAME CENTER 🕹️</p>', unsafe_allow_html=True)

# ----------------- MENU PRINCIPALE -----------------
if st.session_state.schermata == 'menu':
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Scegli la tua missione:</h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="btn-menu">', unsafe_allow_html=True)
    if st.button("✖️ MATH CHALLENGE (Tabelline)", use_container_width=True):
        st.session_state.schermata = 'tabelline'
        inizializza_gioco('tab')
        st.rerun()
    if st.button("🌿 ANIMAL KINGDOM (Scienze)", use_container_width=True):
        st.session_state.schermata = 'animali'
        inizializza_gioco('ani')
        st.rerun()
    if st.button("🌍 WORLD EXPLORER (Bandiere)", use_container_width=True):
        st.session_state.schermata = 'bandiere'
        inizializza_gioco('ban')
        st.rerun()
    if st.button("🕵️‍♂️ WORD DETECTIVE (Anagrammi)", use_container_width=True):
        st.session_state.schermata = 'anagrammi'
        inizializza_gioco('ana')
        st.rerun()
    if st.button("🇮🇹 ITALY EXPLORER (Geografia)", use_container_width=True):
        st.session_state.schermata = 'italia'
        inizializza_gioco('ita')
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- GIOCHI -----------------
else:
    # Pulsante universale per tornare indietro (sempre in cima a ogni gioco)
    if st.button("🏠 Torna al Menu Principale", use_container_width=True):
        torna_al_menu()
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)

    # --- 1. TABELLINE ---
    if st.session_state.schermata == 'tabelline':
        if st.session_state.stato_tab == 'inizio':
            st.markdown("<div style='text-align: center;'>Sfida le tabelline in 7 secondi!</div><br>", unsafe_allow_html=True)
            if st.button("🚀 INIZIA", use_container_width=True):
                st.session_state.stato_tab = 'in_corso'
                genera_tab()
                st.rerun()
        elif st.session_state.stato_tab == 'in_corso':
            st.progress((st.session_state.round_tab - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_tab:
                if st.session_state.tipo_msg_tab == "success": st.success(st.session_state.msg_tab)
                else: st.error(st.session_state.msg_tab)
            st.markdown(f"<div class='domanda-box'><p style='margin:0;'>QUANTO FA...</p><p style='margin:0;font-size:60px;font-weight:bold;'>{st.session_state.f1} × {st.session_state.f2}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(str(st.session_state.opz_tab[i]), key=f"t_{i}", use_container_width=True): verifica_tab(st.session_state.opz_tab[i]); st.rerun()
        elif st.session_state.stato_tab == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_tab}/{TOTAL_DOMANDE}")

    # --- 2. ANIMALI ---
    elif st.session_state.schermata == 'animali':
        if st.session_state.stato_ani == 'inizio':
            st.markdown("<div style='text-align: center;'>A quale famiglia appartiene? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🌿 INIZIA", use_container_width=True):
                st.session_state.stato_ani = 'in_corso'
                genera_ani()
                st.rerun()
        elif st.session_state.stato_ani == 'in_corso':
            st.progress((st.session_state.round_ani - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ani:
                if st.session_state.tipo_msg_ani == "success": st.success(st.session_state.msg_ani)
                else: st.error(st.session_state.msg_ani)
            st.markdown(f"<div class='domanda-box' style='background: linear-gradient(45deg, #2b580c, #639a67);'><p style='margin:0;'>CHE ANIMALE È...</p><p style='margin:0;font-size:45px;font-weight:bold;'>{st.session_state.animale_corr}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ani[i], key=f"a_{i}", use_container_width=True): verifica_ani(st.session_state.opz_ani[i]); st.rerun()
        elif st.session_state.stato_ani == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ani}/{TOTAL_DOMANDE}")

    # --- 3. BANDIERE ---
    elif st.session_state.schermata == 'bandiere':
        if st.session_state.stato_ban == 'inizio':
            st.markdown("<div style='text-align: center;'>Di quale paese è questa bandiera? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🌍 INIZIA", use_container_width=True):
                st.session_state.stato_ban = 'in_corso'
                genera_ban()
                st.rerun()
        elif st.session_state.stato_ban == 'in_corso':
            st.progress((st.session_state.round_ban - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ban:
                if st.session_state.tipo_msg_ban == "success": st.success(st.session_state.msg_ban)
                else: st.error(st.session_state.msg_ban)
            url = f"https://flagcdn.com/w320/{PAESI_MONDO[st.session_state.paese_corr]}.png"
            st.markdown('<div class="immagine-box">', unsafe_allow_html=True); st.image(url, use_container_width=True); st.markdown('</div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ban[i], key=f"b_{i}", use_container_width=True): verifica_ban(st.session_state.opz_ban[i]); st.rerun()
        elif st.session_state.stato_ban == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ban}/{TOTAL_DOMANDE}")

    # --- 4. ANAGRAMMI ---
    elif st.session_state.schermata == 'anagrammi':
        if st.session_state.stato_ana == 'inizio':
            st.markdown("<div style='text-align: center;'>Riordina le lettere! (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🔎 INIZIA", use_container_width=True):
                st.session_state.stato_ana = 'in_corso'
                genera_ana()
                st.rerun()
        elif st.session_state.stato_ana == 'in_corso':
            st.progress((st.session_state.round_ana - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ana:
                if st.session_state.tipo_msg_ana == "success": st.success(st.session_state.msg_ana)
                else: st.error(st.session_state.msg_ana)
            st.markdown(f"<div class='domanda-box'><p style='margin:0;'>RIORDINA...</p><p style='margin:0;font-size:45px;letter-spacing:5px;font-weight:bold;'>{st.session_state.parola_mix}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ana[i], key=f"n_{i}", use_container_width=True): verifica_ana(st.session_state.opz_ana[i]); st.rerun()
        elif st.session_state.stato_ana == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ana}/{TOTAL_DOMANDE}")

    # --- 5. ITALIA ---
    elif st.session_state.schermata == 'italia':
        if st.session_state.stato_ita == 'inizio':
            st.markdown("<div style='text-align: center;'>In quale regione si trova il capoluogo? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🇮🇹 INIZIA", use_container_width=True):
                st.session_state.stato_ita = 'in_corso'
                genera_ita()
                st.rerun()
        elif st.session_state.stato_ita == 'in_corso':
            st.progress((st.session_state.round_ita - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ita:
                if st.session_state.tipo_msg_ita == "success": st.success(st.session_state.msg_ita)
                else: st.error(st.session_state.msg_ita)
            st.markdown(f"<div class='domanda-box'><p style='margin:0;'>IN QUALE REGIONE SI TROVA...</p><p style='margin:0;font-size:45px;font-weight:bold;'>{st.session_state.capoluogo_corr}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ita[i], key=f"i_{i}", use_container_width=True): verifica_ita(st.session_state.opz_ita[i]); st.rerun()
        elif st.session_state.stato_ita == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ita}/{TOTAL_DOMANDE}")
            
