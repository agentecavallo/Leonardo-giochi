import streamlit as st
import random
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Leo's Game Center", page_icon="🕹️", layout="centered")

# ==========================================
# 1. I MEGA DATABASE DEI GIOCHI
# ==========================================

# --- DATABASE CUCINA (Il nuovo gioco!) ---
PIATTI_ITALIANI = {
    "Carbonara 🍝 (Lazio)": "Guanciale, Uova, Pecorino, Pepe Nero",
    "Amatriciana 🍝 (Lazio)": "Guanciale, Pomodoro, Pecorino, Peperoncino",
    "Cacio e Pepe 🍝 (Lazio)": "Pecorino Romano, Pepe Nero",
    "Pesto alla Genovese 🌿 (Liguria)": "Basilico, Pinoli, Aglio, Parmigiano, Olio",
    "Focaccia di Recco 🍞 (Liguria)": "Farina, Stracchino, Olio, Sale",
    "Risotto alla Milanese 🍚 (Lombardia)": "Riso, Zafferano, Midollo, Parmigiano",
    "Pizzoccheri 🍝 (Lombardia)": "Grano Saraceno, Verza, Patate, Formaggio Casera",
    "Cotoletta alla Milanese 🥩 (Lombardia)": "Costoletta di Vitello, Uovo, Pangrattato, Burro",
    "Tortellini in Brodo 🍲 (Emilia-Romagna)": "Pasta all'Uovo, Carne Mista, Parmigiano, Brodo",
    "Lasagne al Forno 🍝 (Emilia-Romagna)": "Pasta, Ragù, Besciamella, Parmigiano",
    "Ragù alla Bolognese 🍅 (Emilia-Romagna)": "Carne Macinata, Passata, Sedano, Carota, Cipolla",
    "Ribollita 🥣 (Toscana)": "Pane Raffermo, Fagioli, Cavolo Nero, Verdure",
    "Pappa al Pomodoro 🍅 (Toscana)": "Pane, Pomodoro, Aglio, Basilico, Olio",
    "Bistecca alla Fiorentina 🥩 (Toscana)": "Carne di Vitellone (Taglio spesso con l'osso)",
    "Arrosticini 🍢 (Abruzzo)": "Carne di Pecora a piccoli cubetti",
    "Olive Ascolane 🫒 (Marche)": "Olive, Carne Mista, Uovo, Pangrattato (Fritte)",
    "Vincisgrassi 🍝 (Marche)": "Pasta al Forno, Ragù di rigaglie, Besciamella",
    "Pizza Margherita 🍕 (Campania)": "Farina, Pomodoro, Mozzarella, Basilico",
    "Parmigiana di Melanzane 🍆 (Campania)": "Melanzane fritte, Pomodoro, Mozzarella, Parmigiano",
    "Insalata Caprese 🍅 (Campania)": "Mozzarella, Pomodoro, Basilico, Olio",
    "Spaghetti alle Vongole 🍝 (Campania)": "Spaghetti, Vongole, Aglio, Olio, Prezzemolo",
    "Babà 🧁 (Campania)": "Impasto lievitato, Sciroppo al Rum",
    "Orecchiette alle Cime di Rapa 🥦 (Puglia)": "Orecchiette, Cime di Rapa, Acciughe, Aglio",
    "Taralli 🥨 (Puglia)": "Farina, Olio, Vino Bianco, Semi di Finocchio",
    "Pasticciotto 🥧 (Puglia)": "Pasta Frolla, Crema Pasticcera",
    "Peperoni Cruschi 🌶️ (Basilicata)": "Peperoni rossi dolci essiccati e fritti",
    "Arancini/e 🍙 (Sicilia)": "Riso, Ragù, Piselli, Mozzarella (Fritti)",
    "Pasta alla Norma 🍝 (Sicilia)": "Maccheroni, Pomodoro, Melanzane fritte, Ricotta Salata",
    "Cannoli 🥐 (Sicilia)": "Cialda fritta, Ricotta di Pecora, Gocce di Cioccolato",
    "Caponata 🍆 (Sicilia)": "Melanzane, Sedano, Capperi, Olive, Salsa Agrodolce",
    "Malloreddus alla Campidanese 🍝 (Sardegna)": "Gnocchetti sardi, Salsiccia, Pomodoro, Zafferano",
    "Porceddu 🐖 (Sardegna)": "Maialino da latte arrosto profumato al mirto",
    "Seadas 🥞 (Sardegna)": "Pasta fritta, Formaggio fresco, Miele",
    "Pane Carasau 🫓 (Sardegna)": "Farina di semola, Acqua, Lievito, Sale (Sfoglia Croccante)",
    "Canederli 🥣 (Trentino-Alto Adige)": "Pane, Speck, Uova, Latte, Brodo",
    "Strudel di Mele 🍏 (Trentino-Alto Adige)": "Pasta sfoglia, Mele, Uvetta, Pinoli, Cannella",
    "Risi e Bisi 🍚 (Veneto)": "Riso, Piselli, Pancetta, Cipolla",
    "Tiramisù 🍰 (Veneto)": "Savoiardi, Mascarpone, Caffè, Uova, Cacao",
    "Frico 🧀 (Friuli-Venezia Giulia)": "Formaggio Montasio, Patate, Cipolle",
    "Bagna Cauda 🧄 (Piemonte)": "Aglio, Acciughe, Olio (Salsa calda per verdure crude)",
    "Agnolotti del Plin 🍝 (Piemonte)": "Piccola pasta ripiena di carne mista",
    "Fonduta 🧀 (Valle d'Aosta)": "Formaggio Fontina, Latte, Tuorli, Burro",
    "Torta al Testo 🫓 (Umbria)": "Focaccia piatta cotta su piano di ghisa, Salumi",
    "'Nduja 🌶️ (Calabria)": "Salame morbido piccante, Peperoncino, Grasso di maiale"
}
LISTA_INGREDIENTI = list(set(PIATTI_ITALIANI.values()))

# --- DATABASE ANIMALI ---
ANIMALI = {
    "Leone 🦁": "Mammifero", "Delfino 🐬": "Mammifero", "Pipistrello 🦇": "Mammifero",
    "Elefante 🐘": "Mammifero", "Balena 🐋": "Mammifero", "Cane 🐕": "Mammifero",
    "Gatto 🐈": "Mammifero", "Tigre 🐅": "Mammifero", "Orso 🐻": "Mammifero",
    "Giraffa 🦒": "Mammifero", "Zebra 🦓": "Mammifero", "Scimmia 🐒": "Mammifero",
    "Canguro 🦘": "Mammifero", "Koala 🐨": "Mammifero", "Panda 🐼": "Mammifero",
    "Ornitorinco 🦦🦆": "Mammifero", "Capibara 🟤": "Mammifero", "Pipistrello della Frutta 🦇🍌": "Mammifero",
    "Bradipo 🦥": "Mammifero", "Lontra 🦦": "Mammifero", "Castoro 🦫": "Mammifero",
    "Lupo 🐺": "Mammifero", "Volpe 🦊": "Mammifero", "Vombato 🐻⬇️": "Mammifero",
    "Aquila 🦅": "Uccello", "Pinguino 🐧": "Uccello", "Pappagallo 🦜": "Uccello",
    "Gufo 🦉": "Uccello", "Gallina 🐔": "Uccello", "Cigno 🦢": "Uccello",
    "Fenicottero 🦩": "Uccello", "Pavone 🦚": "Uccello", "Piccione 🐦": "Uccello",
    "Kiwi 🥝🐦": "Uccello", "Struzzo 🦅🏃": "Uccello", "Colibrì 🐦✨": "Uccello",
    "Serpente 🐍": "Rettile", "Coccodrillo 🐊": "Rettile", "Tartaruga 🐢": "Rettile",
    "Camaleonte 🦎": "Rettile", "Iguana 🦎": "Rettile", "Anaconda 🐍": "Rettile",
    "Squalo 🦈": "Pesce", "Pesce Pagliaccio 🐠": "Pesce", "Salmone 🐟": "Pesce",
    "Pesce Palla 🐡": "Pesce", "Cavalluccio Marino 🌊🐎": "Pesce", "Squalo Martello 🦈🔨": "Pesce",
    "Rana 🐸": "Anfibio", "Rospo 🐸": "Anfibio", "Salamandra 🦎💧": "Anfibio", "Axolotl 🦎🎀": "Anfibio",
    "Farfalla 🦋": "Insetto", "Ape 🐝": "Insetto", "Coccinella 🐞": "Insetto",
    "Formica 🐜": "Insetto", "Zanzara 🦟": "Insetto", "Mantide Religiosa 🦗🙏": "Insetto",
    "Polpo 🐙": "Invertebrato", "Granchio 🦀": "Invertebrato", "Aragosta 🦞": "Invertebrato",
    "Stella Marina 🌟": "Invertebrato", "Medusa 🪼": "Invertebrato", "Ragno 🕷️": "Invertebrato",
    "Scorpione 🦂": "Invertebrato", "Corallo 🪸": "Invertebrato"
}
LISTA_CATEGORIE_ANI = list(set(ANIMALI.values()))

# --- DATABASE BANDIERE ---
PAESI_MONDO = {
    "Italia": "it", "Francia": "fr", "Spagna": "es", "Germania": "de", "Regno Unito": "gb", 
    "Stati Uniti": "us", "Brasile": "br", "Giappone": "jp", "Argentina": "ar", "Canada": "ca", 
    "Australia": "au", "Cina": "cn", "Messico": "mx", "Egitto": "eg", "Grecia": "gr", 
    "Portogallo": "pt", "Olanda": "nl", "Svizzera": "ch", "Svezia": "se", "Belgio": "be",
    "Norvegia": "no", "Danimarca": "dk", "Finlandia": "fi", "Irlanda": "ie", "Austria": "at",
    "Polonia": "pl", "Corea del Sud": "kr", "Nuova Zelanda": "nz", "India": "in", "Sudafrica": "za"
}

# --- DATABASE ANAGRAMMI ---
PAROLE_ANAGRAMMI = [
    "AEREO", "ALBERO", "AMICO", "ANANAS", "ANCORA", "AQUILA", "ARANCIA", "ARMADIO", "ASTRONAUTA", 
    "AUTOBUS", "BALENA", "BAMBINO", "BANANA", "BARCA", "BICICLETTA", "BISCOTTO", "BOTTIGLIA", 
    "CALCIO", "CAMMELLO", "CANE", "CANGURO", "CAROTA", "CARTA", "CASA", "CAVALLO", "CHIAVE", 
    "CHITARRA", "CIOCCOLATO", "COCCODRILLO", "COMPUTER", "CONIGLIO", "DELFINO", "DINOSAURO", 
    "ELEFANTE", "ELICOTTERO", "FARFALLA", "FIORE", "FORMAGGIO", "FRAGOLA", "GATTO", "GELATO", 
    "GIRAFFA", "GIUNGLA", "LAVAGNA", "LEONE", "LIBRO", "LUNA", "MACCHINA", "MAESTRA", "MARE", 
    "MELA", "MONTAGNA", "MUCCA", "MUSICA", "NAVE", "NONNO", "NUVOLA", "OROLOGIO", "ORSO", 
    "PALLONCINO", "PAPPAGALLO", "PIANETA", "PINGUINO", "PIOGGIA", "PIPISTRELLO", "PIRATA", 
    "PIZZA", "RAGNO", "RAZZO", "ROBOT", "SCIMMIA", "SCUOLA", "SERPENTE", "SOLE", "SQUALO", 
    "STELLA", "STORIA", "TARTARUGA", "TAVOLO", "TELEFONO", "TIGRE", "TRENO", "UCCELLO", "ZAINO"
]

# --- DATABASE ITALIA ---
MAPPA_ITALIA = {
    "L'Aquila": "Abruzzo", "Pescara": "Abruzzo", "Potenza": "Basilicata", "Matera": "Basilicata",
    "Catanzaro": "Calabria", "Reggio Calabria": "Calabria", "Napoli": "Campania", "Salerno": "Campania",
    "Bologna": "Emilia-Romagna", "Parma": "Emilia-Romagna", "Rimini": "Emilia-Romagna", 
    "Trieste": "Friuli-Venezia Giulia", "Udine": "Friuli-Venezia Giulia",
    "Roma": "Lazio", "Latina": "Lazio", "Genova": "Liguria", "La Spezia": "Liguria",
    "Milano": "Lombardia", "Bergamo": "Lombardia", "Brescia": "Lombardia", "Como": "Lombardia",
    "Ancona": "Marche", "Pesaro": "Marche", "Campobasso": "Molise", "Torino": "Piemonte", 
    "Novara": "Piemonte", "Bari": "Puglia", "Lecce": "Puglia", "Taranto": "Puglia",
    "Cagliari": "Sardegna", "Sassari": "Sardegna", "Palermo": "Sicilia", "Catania": "Sicilia", 
    "Siracusa": "Sicilia", "Firenze": "Toscana", "Pisa": "Toscana", "Siena": "Toscana",
    "Trento": "Trentino-Alto Adige", "Bolzano": "Trentino-Alto Adige", "Perugia": "Umbria",
    "Aosta": "Valle d'Aosta", "Venezia": "Veneto", "Verona": "Veneto", "Padova": "Veneto"
}
LISTA_REGIONI = list(set(MAPPA_ITALIA.values()))

# ==========================================
# 2. STILE CSS UNIFICATO E IMPOSTAZIONI
# ==========================================
TOTAL_DOMANDE = 15
TEMPO_LIMITE_STANDARD = 7.0
TEMPO_LIMITE_LUNGO = 12.0 # Più tempo per leggere gli ingredienti!

st.markdown("""
    <style>
    .block-container { padding-top: 2rem !important; max-width: 500px !important; }
    .main { background-color: #0e1117; color: #ffffff; }
    .titolo-game {
        font-family: 'Courier New', Courier, monospace; color: #00FF00;
        text-align: center; text-shadow: 2px 2px #ff00ff;
        font-size: 32px !important; font-weight: bold; margin-bottom: 20px;
    }
    .domanda-box {
        background: linear-gradient(45deg, #182848, #4b6cb7);
        padding: 20px; border-radius: 20px; border: 4px solid #00d2ff;
        text-align: center; margin-bottom: 15px; box-shadow: 0px 5px 20px rgba(0, 210, 255, 0.3);
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
        height: 70px !important; font-size: 20px !important; 
        border-color: #00FF00 !important; margin-bottom: 5px;
    }
    .ripasso-box {
        background-color: #1e1e1e; border-left: 5px solid #ffcc00;
        padding: 15px; border-radius: 5px; margin-bottom: 10px; text-align: left;
    }
    @media (max-width: 600px) {
        .titolo-game { font-size: 26px !important; }
        .domanda-box { padding: 15px !important; }
        .domanda-box p:last-child { font-size: 35px !important; }
        div.stButton > button { height: 60px !important; font-size: 14px !important; }
        .btn-menu > div > button { height: 65px !important; font-size: 16px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. MOTORE DEI GIOCHI E GESTIONE ERRORI
# ==========================================
if 'schermata' not in st.session_state: st.session_state.schermata = 'menu'

def torna_al_menu():
    st.session_state.schermata = 'menu'
    st.rerun()

def inizializza_gioco(prefisso):
    st.session_state[f'stato_{prefisso}'] = 'inizio'
    st.session_state[f'punteggio_{prefisso}'] = 0
    st.session_state[f'round_{prefisso}'] = 1
    st.session_state[f'msg_{prefisso}'] = ""
    st.session_state[f'errori_{prefisso}'] = []

def controlla_tempo(prefisso, giusta, testo_domanda, tempo_max):
    tempo = time.time() - st.session_state[f'tempo_inizio_{prefisso}']
    if tempo > tempo_max:
        st.session_state[f'msg_{prefisso}'] = f"⏱️ TEMPO SCADUTO!"
        st.session_state[f'tipo_msg_{prefisso}'] = "error"
        st.session_state[f'errori_{prefisso}'].append({"domanda": testo_domanda, "risposta": "Tempo Scaduto ⏳", "giusta": giusta})
        return False
    return True

def mostra_ripasso(prefisso):
    errori = st.session_state[f'errori_{prefisso}']
    if errori:
        st.markdown("<h3 style='color: #ffcc00; margin-top: 20px;'>📝 Ripasso degli errori:</h3>", unsafe_allow_html=True)
        for err in errori:
            st.markdown(f"<div class='ripasso-box'><b>{err['domanda']}</b><br>Hai risposto: <span style='color: #ff4b4b;'>{err['risposta']}</span> ❌<br>Corretta: <span style='color: #00ff00;'>{err['giusta']}</span> ✅</div>", unsafe_allow_html=True)

# --- GIOCO 1: TABELLINE ---
if 'stato_tab' not in st.session_state: inizializza_gioco('tab')
def genera_tab():
    if random.random() < 0.3:
        st.session_state.f1 = random.randint(2, 10) * 10
        st.session_state.f2 = random.randint(2, 9)
    else:
        st.session_state.f1 = random.randint(2, 10)
        st.session_state.f2 = random.randint(2, 10)
    giusta = st.session_state.f1 * st.session_state.f2
    offset = 10 if giusta > 100 else 5
    opzioni = {giusta, giusta + random.randint(1, offset), giusta - random.randint(1, offset)}
    while len(opzioni) < 3: opzioni.add(giusta + random.randint(offset+1, offset+10))
    st.session_state.opz_tab = list(opzioni)
    random.shuffle(st.session_state.opz_tab)
    st.session_state.tempo_inizio_tab = time.time()
def verifica_tab(scelta):
    giusta = st.session_state.f1 * st.session_state.f2
    testo = f"{st.session_state.f1} × {st.session_state.f2}"
    if controlla_tempo('tab', giusta, testo, TEMPO_LIMITE_STANDARD):
        if int(scelta) == giusta:
            st.session_state.msg_tab = "🚀 BOOM! Esatto!"
            st.session_state.punteggio_tab += 1
            st.session_state.tipo_msg_tab = "success"
        else:
            st.session_state.msg_tab = f"👾 OPS! Era {giusta}"
            st.session_state.tipo_msg_tab = "error"
            st.session_state.errori_tab.append({"domanda": testo, "risposta": scelta, "giusta": giusta})
    st.session_state.round_tab += 1
    if st.session_state.round_tab > TOTAL_DOMANDE: st.session_state.stato_tab = 'fine'
    else: genera_tab()

# --- GIOCO 2: ANIMALI ---
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
    if controlla_tempo('ani', giusta, st.session_state.animale_corr, TEMPO_LIMITE_STANDARD):
        if scelta == giusta:
            st.session_state.msg_ani = f"🚀 BRAVO! È un {giusta}!"
            st.session_state.punteggio_ani += 1
            st.session_state.tipo_msg_ani = "success"
        else:
            st.session_state.msg_ani = f"👾 OPS! È un {giusta}!"
            st.session_state.tipo_msg_ani = "error"
            st.session_state.errori_ani.append({"domanda": st.session_state.animale_corr, "risposta": scelta, "giusta": giusta})
    st.session_state.round_ani += 1
    if st.session_state.round_ani > TOTAL_DOMANDE: st.session_state.stato_ani = 'fine'
    else: genera_ani()

# --- GIOCO 3: BANDIERE ---
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
    if controlla_tempo('ban', giusta, f"Bandiera (era {giusta})", TEMPO_LIMITE_STANDARD):
        if scelta == giusta:
            st.session_state.msg_ban = f"🚀 ESATTO! È la {giusta}!"
            st.session_state.punteggio_ban += 1
            st.session_state.tipo_msg_ban = "success"
        else:
            st.session_state.msg_ban = f"👾 OPS! Era la {giusta}!"
            st.session_state.tipo_msg_ban = "error"
            st.session_state.errori_ban.append({"domanda": f"Bandiera di {giusta}", "risposta": scelta, "giusta": giusta})
    st.session_state.round_ban += 1
    if st.session_state.round_ban > TOTAL_DOMANDE: st.session_state.stato_ban = 'fine'
    else: genera_ban()

# --- GIOCO 4: ANAGRAMMI ---
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
    testo = st.session_state.parola_mix
    if controlla_tempo('ana', giusta, testo, TEMPO_LIMITE_STANDARD):
        if scelta == giusta:
            st.session_state.msg_ana = f"🚀 SUPER DETECTIVE! Era {giusta}"
            st.session_state.punteggio_ana += 1
            st.session_state.tipo_msg_ana = "success"
        else:
            st.session_state.msg_ana = f"👾 OPS! Era {giusta}"
            st.session_state.tipo_msg_ana = "error"
            st.session_state.errori_ana.append({"domanda": f"Anagramma: {testo}", "risposta": scelta, "giusta": giusta})
    st.session_state.round_ana += 1
    if st.session_state.round_ana > TOTAL_DOMANDE: st.session_state.stato_ana = 'fine'
    else: genera_ana()

# --- GIOCO 5: ITALIA ---
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
    testo = st.session_state.capoluogo_corr
    if controlla_tempo('ita', giusta, testo, TEMPO_LIMITE_STANDARD):
        if scelta == giusta:
            st.session_state.msg_ita = f"🚀 BRAVISSIMO! È in {giusta}"
            st.session_state.punteggio_ita += 1
            st.session_state.tipo_msg_ita = "success"
        else:
            st.session_state.msg_ita = f"👾 OPS! Si trova in {giusta}"
            st.session_state.tipo_msg_ita = "error"
            st.session_state.errori_ita.append({"domanda": f"Dov'è {testo}?", "risposta": scelta, "giusta": giusta})
    st.session_state.round_ita += 1
    if st.session_state.round_ita > TOTAL_DOMANDE: st.session_state.stato_ita = 'fine'
    else: genera_ita()

# --- GIOCO 6: CUCINA ITALIANA ---
if 'stato_cuc' not in st.session_state: inizializza_gioco('cuc')
def genera_cuc():
    piatto = random.choice(list(PIATTI_ITALIANI.keys()))
    st.session_state.piatto_corr = piatto
    st.session_state.ingr_giusti = PIATTI_ITALIANI[piatto]
    errate = random.sample([i for i in LISTA_INGREDIENTI if i != st.session_state.ingr_giusti], 2)
    st.session_state.opz_cuc = [st.session_state.ingr_giusti] + errate
    random.shuffle(st.session_state.opz_cuc)
    st.session_state.tempo_inizio_cuc = time.time()
def verifica_cuc(scelta):
    giusta = st.session_state.ingr_giusti
    testo = st.session_state.piatto_corr
    if controlla_tempo('cuc', giusta, testo, TEMPO_LIMITE_LUNGO): # Tempo prolungato a 12 sec
        if scelta == giusta:
            st.session_state.msg_cuc = f"🚀 MASTERCHEF! Ricetta perfetta!"
            st.session_state.punteggio_cuc += 1
            st.session_state.tipo_msg_cuc = "success"
        else:
            st.session_state.msg_cuc = f"👾 OPS! Quegli ingredienti non vanno bene!"
            st.session_state.tipo_msg_cuc = "error"
            st.session_state.errori_cuc.append({"domanda": testo, "risposta": scelta, "giusta": giusta})
    st.session_state.round_cuc += 1
    if st.session_state.round_cuc > TOTAL_DOMANDE: st.session_state.stato_cuc = 'fine'
    else: genera_cuc()

# ==========================================
# 4. INTERFACCIA GRAFICA E MENU
# ==========================================

st.markdown('<p class="titolo-game">🕹️ LEO\'S GAME CENTER 🕹️</p>', unsafe_allow_html=True)

# ----------------- MENU PRINCIPALE -----------------
if st.session_state.schermata == 'menu':
    st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Scegli la tua missione:</h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="btn-menu">', unsafe_allow_html=True)
    if st.button("✖️ MATH CHALLENGE (Tabelline)", use_container_width=True):
        st.session_state.schermata = 'tabelline'; inizializza_gioco('tab'); st.rerun()
    if st.button("🌿 ANIMAL KINGDOM (Scienze)", use_container_width=True):
        st.session_state.schermata = 'animali'; inizializza_gioco('ani'); st.rerun()
    if st.button("🌍 WORLD EXPLORER (Bandiere)", use_container_width=True):
        st.session_state.schermata = 'bandiere'; inizializza_gioco('ban'); st.rerun()
    if st.button("🕵️‍♂️ WORD DETECTIVE (Anagrammi)", use_container_width=True):
        st.session_state.schermata = 'anagrammi'; inizializza_gioco('ana'); st.rerun()
    if st.button("🇮🇹 ITALY EXPLORER (Geografia)", use_container_width=True):
        st.session_state.schermata = 'italia'; inizializza_gioco('ita'); st.rerun()
    if st.button("🍕 MASTERCHEF ITALIA (Cucina)", use_container_width=True):
        st.session_state.schermata = 'cucina'; inizializza_gioco('cuc'); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------- I 6 GIOCHI -----------------
else:
    # Pulsante universale per tornare indietro
    if st.button("🏠 Torna al Menu Principale", use_container_width=True): torna_al_menu()
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)

    # --- 1. TABELLINE ---
    if st.session_state.schermata == 'tabelline':
        if st.session_state.stato_tab == 'inizio':
            st.markdown("<div style='text-align: center;'>Tabelline e magia dello zero in 7 secondi!</div><br>", unsafe_allow_html=True)
            if st.button("🚀 INIZIA", use_container_width=True): st.session_state.stato_tab = 'in_corso'; genera_tab(); st.rerun()
        elif st.session_state.stato_tab == 'in_corso':
            st.progress((st.session_state.round_tab - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_tab:
                if st.session_state.tipo_msg_tab == "success": st.success(st.session_state.msg_tab)
                else: st.error(st.session_state.msg_tab)
            st.markdown(f"<div class='domanda-box' style='background: linear-gradient(45deg, #4b6cb7, #182848);'><p style='margin:0;'>QUANTO FA...</p><p style='margin:0;font-size:60px;font-weight:bold;'>{st.session_state.f1} × {st.session_state.f2}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(str(st.session_state.opz_tab[i]), key=f"t_{i}", use_container_width=True): verifica_tab(st.session_state.opz_tab[i]); st.rerun()
        elif st.session_state.stato_tab == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_tab}/{TOTAL_DOMANDE}")
            mostra_ripasso('tab')

    # --- 2. ANIMALI ---
    elif st.session_state.schermata == 'animali':
        if st.session_state.stato_ani == 'inizio':
            st.markdown("<div style='text-align: center;'>A quale famiglia appartiene? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🌿 INIZIA", use_container_width=True): st.session_state.stato_ani = 'in_corso'; genera_ani(); st.rerun()
        elif st.session_state.stato_ani == 'in_corso':
            st.progress((st.session_state.round_ani - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ani:
                if st.session_state.tipo_msg_ani == "success": st.success(st.session_state.msg_ani)
                else: st.error(st.session_state.msg_ani)
            st.markdown(f"<div class='domanda-box' style='background: linear-gradient(45deg, #2b580c, #639a67);'><p style='margin:0;'>CHE ANIMALE È...</p><p style='margin:0;font-size:38px;font-weight:bold;'>{st.session_state.animale_corr}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ani[i], key=f"a_{i}", use_container_width=True): verifica_ani(st.session_state.opz_ani[i]); st.rerun()
        elif st.session_state.stato_ani == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ani}/{TOTAL_DOMANDE}")
            mostra_ripasso('ani')

    # --- 3. BANDIERE ---
    elif st.session_state.schermata == 'bandiere':
        if st.session_state.stato_ban == 'inizio':
            st.markdown("<div style='text-align: center;'>Di quale paese è questa bandiera? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🌍 INIZIA", use_container_width=True): st.session_state.stato_ban = 'in_corso'; genera_ban(); st.rerun()
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
            mostra_ripasso('ban')

    # --- 4. ANAGRAMMI ---
    elif st.session_state.schermata == 'anagrammi':
        if st.session_state.stato_ana == 'inizio':
            st.markdown("<div style='text-align: center;'>Riordina le lettere! (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🔎 INIZIA", use_container_width=True): st.session_state.stato_ana = 'in_corso'; genera_ana(); st.rerun()
        elif st.session_state.stato_ana == 'in_corso':
            st.progress((st.session_state.round_ana - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ana:
                if st.session_state.tipo_msg_ana == "success": st.success(st.session_state.msg_ana)
                else: st.error(st.session_state.msg_ana)
            st.markdown(f"<div class='domanda-box'><p style='margin:0;'>RIORDINA...</p><p style='margin:0;font-size:38px;letter-spacing:5px;font-weight:bold;'>{st.session_state.parola_mix}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ana[i], key=f"n_{i}", use_container_width=True): verifica_ana(st.session_state.opz_ana[i]); st.rerun()
        elif st.session_state.stato_ana == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ana}/{TOTAL_DOMANDE}")
            mostra_ripasso('ana')

    # --- 5. ITALIA ---
    elif st.session_state.schermata == 'italia':
        if st.session_state.stato_ita == 'inizio':
            st.markdown("<div style='text-align: center;'>In quale regione si trova il capoluogo? (7 secondi)</div><br>", unsafe_allow_html=True)
            if st.button("🇮🇹 INIZIA", use_container_width=True): st.session_state.stato_ita = 'in_corso'; genera_ita(); st.rerun()
        elif st.session_state.stato_ita == 'in_corso':
            st.progress((st.session_state.round_ita - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_ita:
                if st.session_state.tipo_msg_ita == "success": st.success(st.session_state.msg_ita)
                else: st.error(st.session_state.msg_ita)
            st.markdown(f"<div class='domanda-box' style='background: linear-gradient(45deg, #1d2671, #c33764);'><p style='margin:0;'>IN QUALE REGIONE SI TROVA...</p><p style='margin:0;font-size:45px;font-weight:bold;'>{st.session_state.capoluogo_corr}</p></div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            for i, c in enumerate([c1, c2, c3]):
                if c.button(st.session_state.opz_ita[i], key=f"i_{i}", use_container_width=True): verifica_ita(st.session_state.opz_ita[i]); st.rerun()
        elif st.session_state.stato_ita == 'fine':
            st.balloons(); st.success(f"Finito! Punteggio: {st.session_state.punteggio_ita}/{TOTAL_DOMANDE}")
            mostra_ripasso('ita')

    # --- 6. CUCINA ITALIANA (IL NUOVO GIOCO) ---
    elif st.session_state.schermata == 'cucina':
        if st.session_state.stato_cuc == 'inizio':
            st.markdown("<div style='text-align: center;'>Quali sono gli ingredienti giusti? Hai <b>12 secondi</b> per leggere bene!</div><br>", unsafe_allow_html=True)
            if st.button("🍕 ENTRA IN CUCINA", use_container_width=True): st.session_state.stato_cuc = 'in_corso'; genera_cuc(); st.rerun()
        elif st.session_state.stato_cuc == 'in_corso':
            st.progress((st.session_state.round_cuc - 1) / TOTAL_DOMANDE)
            if st.session_state.msg_cuc:
                if st.session_state.tipo_msg_cuc == "success": st.success(st.session_state.msg_cuc)
                else: st.error(st.session_state.msg_cuc)
            # Box con colori che ricordano il pomodoro e l'impasto della pizza
            st.markdown(f"<div class='domanda-box' style='background: linear-gradient(45deg, #d35400, #c0392b);'><p style='margin:0;'>INGREDIENTI PER...</p><p style='margin:0;font-size:32px;font-weight:bold;'>{st.session_state.piatto_corr}</p></div>", unsafe_allow_html=True)
            
            # Qui mettiamo i bottoni uno sotto l'altro perché gli ingredienti sono testi lunghi!
            for i in range(3):
                opz = st.session_state.opz_cuc[i]
                if st.button(opz, key=f"c_{i}", use_container_width=True): 
                    verifica_cuc(opz); st.rerun()
                    
        elif st.session_state.stato_cuc == 'fine':
            st.balloons(); st.success(f"Servizio Finito! Punteggio: {st.session_state.punteggio_cuc}/{TOTAL_DOMANDE}")
            mostra_ripasso('cuc')
                
