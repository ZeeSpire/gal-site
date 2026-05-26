#!/usr/bin/env python3
"""One-shot static-site generator for galdc.ro.

Emits every HTML page with depth-aware relative paths so that the site works
both under ``file://`` and on GitHub Pages. Run once, commit the output, then
delete this folder if desired -- nothing about hosting or running the site
depends on it.

Usage:
    python3 _tools/build.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TITLE = "GALDC - Grupul de Actiune Locala Dobrogea Centrala"
DESCRIPTION = (
    "Grupul de Actiune Locala Dobrogea Centrala este un parteneriat public "
    "privat constituit conform programului LEADER"
)

# Bumped manually whenever CSS or JS changes — busts the browser cache so users
# don't keep the prior stylesheet after a redeploy.
ASSET_VERSION = "2026-05-26-5"


def head(prefix: str) -> str:
    return f"""<!doctype html>
<html lang="ro" data-theme="corporate">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESCRIPTION}">
<link rel="icon" href="{prefix}favicon.ico" type="image/x-icon">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,700;1,100;1,300;1,400;1,700&display=swap">
<link rel="stylesheet" href="{prefix}assets/css/site.css?v={ASSET_VERSION}">
</head>
<body>
"""


def header(prefix: str) -> str:
    """Header with navbar + hero strip. ``prefix`` is the depth-aware path prefix."""

    p = prefix
    return f"""<header>
  <div class="container navbar">
    <div class="navbar-start">
      <a href="{p}acasa/index.html"><img src="{p}helper/gal-logo-new.jpg" alt="gal logo" width="250" height="139"></a>
    </div>
    <nav class="navbar-center" aria-label="Navigație principală">
      <ul class="menu-horizontal">
        <li><a href="{p}acasa/index.html">Acasa</a></li>
        <li class="dropdown">
          <button class="dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false">GAL<span class="dropdown-caret" aria-hidden="true"></span></button>
          <ul class="dropdown-content">
            <li><a href="{p}details-of-organisations/index.html">Details of organisation</a></li>
            <li><a href="{p}implementarea-sdl-prin-leader/index.html">Implementarea SDL prin LEADER</a></li>
            <li><a href="https://ec.europa.eu/enrd/leader-clld_en.html" target="_blank" rel="noopener">Informatii generale</a></li>
          </ul>
        </li>
        <li><a href="{p}teritoriul-microregiunii/index.html">Teritoriul Microregiunii</a></li>
        <li><a href="{p}strategia-de-dezvoltare-locala/SDL_GAL_DOBROGEA_CENTRALA.pdf" target="_blank" rel="noopener">Strategia de dezvoltare locala</a></li>
        <li class="dropdown">
          <button class="dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false">Interventii FEADR<span class="dropdown-caret" aria-hidden="true"></span></button>
          <ul class="dropdown-content">
            <li><a href="{p}interventii/1-durabilitatea-mediului-in-satul-dobrogean.pdf">Durabilitatea mediului in satul dobrogean</a></li>
            <li><a href="{p}interventii/2-investitii-in-domeniul-sanatatii.pdf">Investitii in domeniul sănătăţii</a></li>
            <li><a href="{p}interventii/3-investitii-si-servicii-de-baza-destinate-comunitatii.pdf">Investiţii şi servicii de baza destinate comunității</a></li>
            <li><a href="{p}interventii/4-investitii-colective-in-domeniul-agricol.pdf">Investitii colective in domeniul agricol</a></li>
            <li><a href="{p}interventii/5-start-up-neagricol.pdf">Start-up neagricol</a></li>
            <li><a href="{p}interventii/6-activitati-neagricole-in-satul-dobrogean.pdf">Activitati neagricole in satul dobrogean</a></li>
            <li><a href="{p}interventii/7-cooperare-inter-teritoriala.pdf">Cooperare inter-teritoriala pentru agricultura si turism</a></li>
          </ul>
        </li>
        <li class="dropdown">
          <button class="dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false">Media<span class="dropdown-caret" aria-hidden="true"></span></button>
          <ul class="dropdown-content">
            <li><a href="{p}media/actiuni-animare/index.html">Actiuni animare</a></li>
            <li><a href="{p}media/calendar-animare-tr2-an-2.pdf" target="_blank" rel="noopener">Calendar</a></li>
            <li><a href="{p}media/comunicate/index.html">Comunicate</a></li>
            <li><a href="{p}acasa/index.html">Comunicari: AM, RRN, AFIR</a></li>
            <li><a href="{p}media/materiale-publicitare/index.html">Materiale publicitare</a></li>
          </ul>
        </li>
        <li class="dropdown">
          <button class="dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false">Finantare proiecte<span class="dropdown-caret" aria-hidden="true"></span></button>
          <ul class="dropdown-content">
            <li><a href="{p}finantare-proiecte/calendar-apeluri-selectie/index.html">Calendar apeluri selectie</a></li>
            <li><a href="{p}finantare-proiecte/apeluri-selectie/index.html">Apeluri selectie</a></li>
            <li><a href="{p}finantare-proiecte/rapoarte-selectie/index.html">Rapoarte selectie</a></li>
            <li><a href="{p}acasa/index.html">Proiecte finalizate</a></li>
          </ul>
        </li>
        <li><a href="{p}arhiva/index.html">Arhiva</a></li>
        <li><a href="{p}contact/index.html">Contact</a></li>
      </ul>
    </nav>
    <div class="mobile-menu-wrap">
      <button class="navbar-toggle" type="button" data-mobile-toggle aria-label="Meniu" aria-expanded="false">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h16M4 12h8m-8 6h16"/></svg>
      </button>
      <ul class="mobile-menu" data-mobile-menu>
        <li><a href="{p}acasa/index.html">Acasa</a></li>
        <li>
          <span class="menu-title">GAL</span>
          <ul>
            <li><a href="{p}details-of-organisations/index.html">Details of organisation</a></li>
            <li><a href="{p}implementarea-sdl-prin-leader/index.html">Implementarea SDL prin LEADER</a></li>
            <li><a href="https://ec.europa.eu/enrd/leader-clld_en.html" target="_blank" rel="noopener">Informatii generale</a></li>
          </ul>
        </li>
        <li><a href="{p}teritoriul-microregiunii/index.html">Teritoriul Microregiunii</a></li>
        <li><a href="{p}strategia-de-dezvoltare-locala/SDL_GAL_DOBROGEA_CENTRALA.pdf" target="_blank" rel="noopener">Strategia de dezvoltare locala</a></li>
        <li>
          <span class="menu-title">Interventii FEADR</span>
          <ul>
            <li><a href="{p}interventii/1-durabilitatea-mediului-in-satul-dobrogean.pdf">Durabilitatea mediului in satul dobrogean</a></li>
            <li><a href="{p}interventii/2-investitii-in-domeniul-sanatatii.pdf">Investitii in domeniul sănătăţii</a></li>
            <li><a href="{p}interventii/3-investitii-si-servicii-de-baza-destinate-comunitatii.pdf">Investiţii şi servicii de baza destinate comunității</a></li>
            <li><a href="{p}interventii/4-investitii-colective-in-domeniul-agricol.pdf">Investitii colective in domeniul agricol</a></li>
            <li><a href="{p}interventii/5-start-up-neagricol.pdf">Start-up neagricol</a></li>
            <li><a href="{p}interventii/6-activitati-neagricole-in-satul-dobrogean.pdf">Activitati neagricole in satul dobrogean</a></li>
            <li><a href="{p}interventii/7-cooperare-inter-teritoriala.pdf">Cooperare inter-teritoriala pentru agricultura si turism</a></li>
          </ul>
        </li>
        <li>
          <span class="menu-title">Media</span>
          <ul>
            <li><a href="{p}media/actiuni-animare/index.html">Actiuni animare</a></li>
            <li><a href="{p}media/calendar-animare-tr2-an-2.pdf" target="_blank" rel="noopener">Calendar</a></li>
            <li><a href="{p}media/comunicate/index.html">Comunicate</a></li>
            <li><a href="{p}acasa/index.html">Comunicari: AM, RRN, AFIR</a></li>
            <li><a href="{p}media/materiale-publicitare/index.html">Materiale publicitare</a></li>
          </ul>
        </li>
        <li>
          <span class="menu-title">Finantare proiecte</span>
          <ul>
            <li><a href="{p}finantare-proiecte/calendar-apeluri-selectie/index.html">Calendar apeluri selectie</a></li>
            <li><a href="{p}finantare-proiecte/apeluri-selectie/index.html">Apeluri selectie</a></li>
            <li><a href="{p}finantare-proiecte/rapoarte-selectie/index.html">Rapoarte selectie</a></li>
            <li><a href="{p}acasa/index.html">Proiecte finalizate</a></li>
          </ul>
        </li>
        <li><a href="{p}arhiva/index.html">Arhiva</a></li>
        <li><a href="{p}contact/index.html">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="hero-strip">
    <img src="{p}helper/IMG_20200920_125334-small.jpg" alt="Hero background" width="2000" height="800">
  </div>
</header>
"""


def sidebar() -> str:
    return """<aside class="sidebar">
  <div class="card">
    <h2>Noutăți</h2>
    <p>Noutati GAL</p>
  </div>
</aside>
"""


def footer(prefix: str) -> str:
    return """<footer class="site-footer">
  <div class="container">
    <a href="https://www.zeespire.com" target="_blank" rel="noopener noreferrer" title="Visit ZeeSpire Software 2025">ZeeSpire Software 2025</a>
  </div>
</footer>
"""


def banner(prefix: str) -> str:
    return f"""<div class="container page-banner">
  <img src="{prefix}helper/banner-gal.jpg" alt="banner gal" width="1280" height="170">
</div>
"""


def page(prefix: str, body: str, *, with_layout: bool = True) -> str:
    """Wrap ``body`` in the standard header/banner/main+sidebar/footer layout."""

    if not with_layout:
        return f"{head(prefix)}{body}\n<script src=\"{prefix}assets/js/site.js\" defer></script>\n</body>\n</html>\n"

    return (
        f"{head(prefix)}"
        f"<div class=\"flex-col-min-screen\">\n"
        f"{header(prefix)}"
        f"{banner(prefix)}"
        f"<div class=\"container page-body\">\n"
        f"<main>\n{body}\n</main>\n"
        f"{sidebar()}"
        f"</div>\n"
        f"{footer(prefix)}"
        f"</div>\n"
        f"<script src=\"{prefix}assets/js/site.js\" defer></script>\n"
        f"</body>\n</html>\n"
    )


# ---------- Pages ----------

INDEX_HTML = head("") + """<main>
  <div class="chooser" style="background-image: url('helper/IMG_20200920_125334.jpg');">
    <div class="chooser-logo">
      <a href="index.html"><img src="helper/gal-logo-new.png" alt="gal logo" width="300" height="166"></a>
    </div>
    <div class="chooser-grid">
      <div class="chooser-card">
        <img src="helper/leader.png" alt="leader 2023-2027 logo" width="293" height="83">
        <a href="acasa/index.html"><h1>LEADER 2023-2027</h1></a>
        <p>Strategia de dezvoltare locala a teritoriului GAL Dobrogea Centrala aferenta perioadei 2023 – 2027</p>
        <a class="btn btn-blue" href="acasa/index.html">Viziteaza pagina proiectului</a>
      </div>
      <div class="chooser-card">
        <img src="helper/leader-old.png" alt="leader 2014-2020" width="150" height="150">
        <a href="https://old.galdc.ro"><h1>LEADER 2014-2020</h1></a>
        <p>Strategia de dezvoltare locala a teritoriului GAL Dobrogea Centrala aferenta perioadei 2014 – 2020</p>
        <a class="btn btn-green" href="https://old.galdc.ro">Viziteaza pagina proiectului</a>
      </div>
    </div>
    <div class="chooser-credit">
      <a href="https://www.zeespire.com" target="_blank" rel="noopener noreferrer" title="Visit ZeeSpire Software 2025">ZeeSpire Software 2025</a>
    </div>
  </div>
</main>
<script src="assets/js/site.js?v=""" + ASSET_VERSION + """" defer></script>
</body>
</html>
"""


ACASA_BODY = """<p class="text-center">JUD CONSTANTA</p>
<p class="text-center">COMUNA TORTOMAN</p>
<p class="text-center">STR 1 DECEMBRIE 1918, NR 32</p>
<p class="text-center">PROGRAM DE LUCRU:  LUNI – VINERI  - 13.00-17.00 </p>"""


CONTACT_BODY = """<h1>Contact</h1>
<p>sediul social din teritoriu GALDC:  Str 1 Decembrie 1918, nr. 32, Tortoman</p>
<p> Program lucru luni - vineri 13.00-17.00</p>
<br>
<p>sediul administrativ:  Str Podgoriilor, nr 1, Medgidia </p>
<p>Program lucru luni – vineri 9.00 – 17.00</p>
<br>
<p>Telefon; 0762286145, 0723185714</p>
<br>
<p>E-MAIL: galmedg@yahoo.com, livadariu_g@yahoo.com</p>
<br>
<p>www.galdc.ro</p>
<br>
<p>social media: linkedin.com/in/galdc-medgidia-009542341</p>
<p>https://www.facebook.com/livadariu.constantin.16?locale=ro_RO</p>"""


DETAILS_BODY = """<h1>Details of organisations</h1>

<h2>D.2 Partner Organisation</h2>
<div class="table-wrap">
<table>
  <thead>
    <tr><th>Information</th><th>Details</th></tr>
  </thead>
  <tbody>
    <tr><td>PIC - ID</td><td>936824837</td></tr>
    <tr><td>Organisation ID</td><td>E10029768</td></tr>
    <tr><td>Full legal name (National Language)</td><td>GRUPUL DE ACTIUNE LOCALA DOBROGEA CENTRALA</td></tr>
    <tr><td>Full legal name (Latin characters)</td><td>LOCAL ACTION GROUP DOBROGEA CENTRALA</td></tr>
    <tr><td>Acronym</td><td>GALDC</td></tr>
    <tr><td>National ID</td><td>304377892</td></tr>
    <tr><td>Department (if applicable)</td><td></td></tr>
    <tr><td>Address</td><td>Str Decebal nr 35</td></tr>
    <tr><td>Country</td><td>Romania</td></tr>
    <tr><td>Region</td><td>RO02</td></tr>
    <tr><td>P.O. Box</td><td>905600</td></tr>
    <tr><td>CEDEX</td><td></td></tr>
    <tr><td>City</td><td>Medgidia</td></tr>
    <tr><td>Website</td><td><a class="link" href="http://www.galdc.ro">www.galdc.ro</a></td></tr>
    <tr><td>Email</td><td><a class="link" href="mailto:galmedg@yahoo.com">galmedg@yahoo.com</a>, <a class="link" href="mailto:livadariu_g@yahoo.com">livadariu_g@yahoo.com</a></td></tr>
    <tr><td>Telephone 1</td><td>0040762286145</td></tr>
    <tr><td>Telephone 2</td><td>0040723185714</td></tr>
    <tr><td>Fax</td><td>-</td></tr>
  </tbody>
</table>
</div>

<h2>D.2.1 Profile</h2>
<div class="table-wrap">
<table>
  <tbody>
    <tr><td>Type of Organisation</td><td>Legal NGO</td></tr>
    <tr><td>Is the partner organisation a public body?</td><td></td></tr>
    <tr><td>Is the partner organisation a non-profit?</td><td>X</td></tr>
  </tbody>
</table>
</div>

<h2>Presentation of Partner Organisation</h2>
<p>Local Action Group Dobrogea Centrala is a public-private associative group which operates in accordance with EC Regulation 1303/2013 Article 34. GALDC brings together 17 rural communities located in the south-east of Romania in Constanta and Tulcea counties. LAGDC provide some of the resources necessary to enable local partners to direct and actively engage in the local development of their area, through a community-led local development (CLLD).</p>
<p>Local Action Group Dobrogea Centrala operates as territorial management unit at subregional level for National Rural Development Plan 2023-2027, LAGDC financing projects under European development priorities identified in UE Regulation 2021/2115. </p>

<p>ACTIONS</p>
<ul>
  <li>1. Environmental sustainability</li>
  <li>2. Investments in the field of health.</li>
  <li>3. Operations with an economic purpose whose direct beneficiaries are women.</li>
  <li>4. Operations with an economic purpose whose direct beneficiaries are people past retirement age.</li>
  <li>5. Smart agriculture, smart farming and smart tourism.</li>
  <li>6. Specific vocational education</li>
</ul>
<p>Through its activities, LAGDC influence local political environment in actions attending the economic development of the territory. This approach is performed by mobilizing local and county education sector and by organization of continuing education courses and counseling sessions for rural communities members.</p>
<p>Awareness local population to attend courses is done through organization of local meetings and events. LAGDC experts are responsible of professional events in the territory and are bearers of messages that role in educating its population to participate at local decision, social life and rural economic development. Through these events, courses and counseling sessions are formed core competencies, specific technical and social skills.</p>
<p>LAGDC experts monitors personal evolution of grant holders by observing the participation in training courses, professional events for personal satisfaction, economic and social increase of communities and transferability of good practices.</p>
<p>LAG Dobrogea Centrala staff is part of the National Committee for monitoring the implementation of the PNS (National Strategic Plan) and is a founding member of the National Network for Rural Development.</p>
<p>In its territorial approach LAGDC relies on the expertise of 18 persons specialized in education, agriculture, environment, rural and urban economy, management and managing European projects, local and regional governance.</p>
<p>All LAGDC experts hold certificates attesting trainer for adults, assessor professional competence, provide didactic and pedagogical experience. LAG Central Dobrogea is a member of the European Network of Local Action Groups and the National Federation of Local Action Groups.</p>

<div class="table-wrap">
<table>
  <tbody>
    <tr><td colspan="4">Have you participated in a European Union granted project in the 3 years preceeding this apprlication? ( no need to write your projects before 2016)</td></tr>
    <tr><td colspan="2">YES</td><td>YES/NO</td></tr>
    <tr><td>EU PROGRAMME</td><td>YEAR</td><td>Project Identification Number</td><td>Applicant – Beneficiary Organisation</td></tr>
    <tr><td>FEADR</td><td>2016 -2020</td><td>C19400163011621418292</td><td>GAL Dobrogea Centrala</td></tr>
    <tr><td>FEADR</td><td>2023-2027</td><td>C19100000012321400017</td><td>GAL Dobrogea Centrala</td></tr>
    <tr><td>ERASMUS +</td><td>2016-2019</td><td>2016-1-IE01-KA202-016898</td><td>Limeric Institut for Technologies</td></tr>
    <tr><td>EUROPA 2020</td><td>2017-2022</td><td>COASTAL 773782</td><td>Valmese Instelling</td></tr>
  </tbody>
</table>
</div>

<h2>D2.3 Legal Representative</h2>
<p>Important:- Please also provide a one-side A4 letter (with institutional stamp) from the Legal Representative that acknowledges their interest in becoming a partner. Please scan and email.</p>
<div class="table-wrap">
<table>
  <tbody>
    <tr><td>Title</td><td>Manager</td></tr>
    <tr><td>Gender</td><td>MDM</td></tr>
    <tr><td>First Name</td><td>GABRIELA</td></tr>
    <tr><td>Family Name</td><td>LIVADARIU</td></tr>
    <tr><td>Department</td><td>MANAGEMENT AND COORDONATION</td></tr>
    <tr><td>Position</td><td>MANAGER</td></tr>
    <tr><td>Email</td><td>Livadariu_g@yahoo.com</td></tr>
    <tr><td>Telephone</td><td>0040762286145</td></tr>
    <tr><td>Address</td><td>Str Victoriei, nr 10</td></tr>
    <tr><td>Country</td><td>ROMANIA</td></tr>
    <tr><td>Region</td><td>RO02</td></tr>
    <tr><td>P.O. Box</td><td></td></tr>
    <tr><td>CEDEX</td><td></td></tr>
    <tr><td>City</td><td>MEDGIDIA</td></tr>
    <tr><td>Website</td><td>www.galdc.ro</td></tr>
  </tbody>
</table>
</div>"""


IMPLEMENTAREA_BODY = """<h1>Implementarea SDL prin LEADER</h1>
<h2>Programul LEADER</h2>
<p>Programul LEADER reprezintă o abordare care oferă noi oportunităţi de dezvoltare rurală punând bazele identificării nevoilor locale, întăririi capacităţii de dezvoltare şi implementării strategiilor locale de dezvoltare în vederea conservării patrimoniului rural şi cultural, dezvoltării mediului economic şi îmbunătăţirii abilităţilor organizatorice ale comunităţilor locale. Schimbările din sectorul agricol, ca rezultat al reformei Politicii Agricole Comune, creşterea cererii consumatorilor, presiunile asupra mediului înconjurător, răspândirea rapidă a noilor tehnologii, îmbătrânirea populaţiei şi depopularea rurală sunt numai o parte din  factorii care afectează zona rurală şi care solicită implementarea unui program orientat spre construirea de parteneriate public-private şi valorificarea resurselor locale (fizice, umane şi financiare) pentru elaborarea şi punerea în practică a unor strategii de dezvoltare locală.</p>
<h3>Scurt istoric</h3>
<p>La nivel european, necesitatea Programului LEADER a apărut în 1990, când, programele publice pentru dezvoltare rurală din multe ţări erau limitate, în ceea ce priveşte obiectivul intervenţiilor lor, fiind administrate într-un mod tradiţional de sus în jos (de la nivel central spre cel local). În perioada 1991-1994 la nivel comunitar s-a derulat LEADER I, „Faza de iniţiere”, în cadrul căreia au fost constituite 217 Grupuri Locale de Acţiune (GAL).  În cadrul LEADER II (1994-1999), Faza de generalizare, s-au format 1000 GAL-uri.  În cadrul LEADER (2000-2006), Faza de consolidare, au fost selectate 896 GAL-uri, în zonele rurale din toate statele membre.</p>
<h3>Caracteristicile Programului LEADER</h3>
<p>Programul LEADER se bazează pe combinarea a 7 caracteristici, astfel:</p>
<ul class="list-disc">
  <li>abordare teritorială (utilizarea eficientă a resurselor locale din cadrul unei zone teritoriale specifice, desfăşurarea de activităţi integrate şi crearea unei viziuni comune),</li>
  <li>abordare partenerială (realizarea unui parteneriat public-privat interesat în dezvoltarea zonei, denumit Grup de Acţiune Locală),</li>
  <li>abordare de jos în sus (participarea activă a populaţiei locale la planificarea, luarea deciziilor şi implementarea strategiilor necesare dezvoltării zonei), </li>
  <li>abordarea integrată şi multisectorială a strategiilor bazate pe interacţiunea partenerilor din toate sectoarele economiei locale, pentru a planifica şi pune în comun problemele din mediul rural,</li>
  <li>accent deosebit pe inovaţie şi experimentare (căutarea de răspunsuri noi la problemele existente ale dezvoltării rurale),</li>
  <li>implementarea proiectelor de cooperare,</li>
  <li>interconectarea parteneriatelor locale.</li>
</ul>
<h3>Cine sunt beneficiarii Programului LEADER?</h3>
<p>Beneficiarii Programului LEADER sunt Grupurile de Acţiune Locală (GAL) care îşi desfăşoară activitatea pe un teritoriu rural, cu o populaţie cuprinsă între 10.000 – 100.000 locuitori şi densitatea de maximum 150 de locuitori pe km2.</p>
<p>Grupurile de Acţiune Locală reprezintă parteneriate constituite din diverşi reprezentanţi ai sectorului socio-economic din teritoriul respectiv. La nivel de decizie, partenerii sociali şi economici şi reprezentanţii societăţii civile, precum agricultorii, femeile, tinerii din spaţiul rural şi asociaţiile  acestora trebuie să reprezinte cel puţin 50% din parteneriatul local.</p>
<p>În statele membre, GAL-urile au diferite structuri legale: asociaţii non-profit, asociaţii/fundaţii, autorităţi locale sau regionale, societăţi comerciale, cooperative.</p>
<p>GAL-urile reprezintă interesele locuitorilor şi comunităţii rurale – motorul de funcţiune al Programului LEADER.</p>
<p>GAL-urile elaborează o strategie de dezvoltare rurală locală integrată şi sunt responsabile de implementarea acesteia.</p>
<p>Astfel, GAL-urile aleg proiectele care vor fi finanţate în cadrul strategiei. De asemenea, pot selecta proiecte de cooperare.</p>
<p>Criterii de identificare a teritoriilor LEADER</p>
<ul class="list-disc">
  <li>Dimensiune redusă</li>
  <li>Caracter rural</li>
  <li>Omogenitate</li>
  <li>Resurse suficiente</li>
  <li>Densitate redusă a populaţiei (maxim 150 locuitori/ km2)</li>
  <li>Identitate locală</li>
  <li>Populaţie între 10.000 – 100.000 locuitori</li>
</ul>
<h3>Avantaje ale Programului LEADER</h3>
<ul class="list-disc">
  <li>Răspunde nevoilor locale specifice;</li>
  <li>Valorifică resursele locale;</li>
  <li>Mobilizează actorii locali, reprezentanţi ai populaţiei rurale, de a se preocupa şi de a prelua controlul dezvoltării zonelor rurale prin întocmirea de strategii axate pe problemele identificate în comunităţile lor;</li>
  <li>Oferă zonelor rurale posibilitatea de colaborare  cu alte teritorii pentru schimb şi transfer de experienţă prin crearea de reţele;</li>
  <li>Prin caracterul său descentralizat, integrat şi de jos în sus este esenţial pentru dezvoltarea echilibrată teritorială.</li>
</ul>
<h3>Scopul Programului LEADER</h3>
<ul class="list-disc">
  <li>Construirea capacităţii locale de parteneriat, animare şi dobândirea de aptitudini pentru mobilizarea potenţialului local;</li>
  <li>Promovarea parteneriatelor public-private. LEADER va continua să deţină un rol important în încurajarea abordărilor inovative ale dezvoltării rurale şi în reunirea pe aceeaşi scenă a sectoarelor privat şi public;</li>
  <li>Promovarea cooperării şi inovaţiei;</li>
  <li>Îmbunătăţirea guvernării locale. LEADER favorizează dezvoltarea abordărilor inovative asigurând legătura între agricultură, silvicultură şi economia locală şi contribuind astfel la diversificarea bazei economice şi întărirea structurii socio-economice a zonelor rurale.</li>
</ul>
<h3>Acoperire geografică</h3>
<p>Sunt eligibile teritoriile (zonele) rurale si orasele mici cu populatie de sub 20000 de locuitori care dispun de suficiente resurse umane, financiare şi economice pentru sprijinirea unei strategii de dezvoltare viabilă.  De asemenea, teritoriile (zonele) eligibile sunt acele teritorii care, în conformitate cu definiţia OECD, sunt clasificate drept rurale. Definiţia OECD are la bază acea parte a populaţiei  care locuieşte în comune (cu mai puţin de 150 locuitori/km2). Această definiţie este unica recunoscută pe plan internaţional referitor la spaţiul rural.</p>

<br>
<p><b>Programul LEADER se finanţează</b> prin Programul Naţional de Dezvoltare Rurală, implementat de Agenţia pentru Finanţarea Investiţiilor Rurale, din subordinea Ministerului Agriculturii şi Dezvoltării Rurale. PNDR este finanţat de Uniunea Europeană şi Guvernul României prin Fondul European Agricol pentru Dezvoltare Rurală (FEADR).</p>"""


def teritoriul_body(prefix: str) -> str:
    p = prefix
    items = [
        ("1", "1-comuna-aliman.pdf", "COMUNA ALIMAN"),
        ("2", "2-comuna-ciocarlia.pdf", "COMUNA CIOCIRLIA"),
        ("3", "3-comuna-crucea.pdf", "COMUNA CRUCEA"),
        ("4", "4-comuna-garliciu.pdf", "COMUNA GARLICIU"),
        ("5", "5-comuna-ghindaresti.pdf", "COMUNA GHINDARESTI"),
        ("6", "6-comuna-horia.pdf", "COMUNA HORIA"),
        ("7", "7-comuna-mircea-voda.pdf", "COMUNA MIRCEA VODA"),
        ("8", "8-comuna-pestera.pdf", "COMUNA PESTERA"),
        ("9", "9-comuna-rasova.pdf", "COMUNA RASOVA"),
        ("10", "10-comuna-saligny.pdf", "COMUNA SALIGNY"),
        ("11", "11-comuna-saraiu.pdf", "COMUNA SARAIU"),
        ("12", "12-comuna-seimeni.pdf", "COMUNA SEIMENI"),
        ("13", "13-comuna-topalu.pdf", "COMUNA TOPALU"),
        ("14", "14-comuna-tortoman.pdf", "COMUNA TORTOMAN"),
        ("15", "15-comuna-ciobanu.pdf", "COMUNA CIOBANU"),
        ("16", "16-oras-harsova.pdf", "ORAS HIRSOVA"),
        ("17", "17-comuna-casimcea.pdf", "COMUNA CASIMCEA"),
    ]
    lis = "\n".join(
        f'  <li>{n}. <a class="link" href="{p}teritoriul-microregiunii/{fn}">{label}</a></li>'
        for n, fn, label in items
    )
    return f"""<h1>Teritoriul microregiunii</h1>
<a class="link" href="{p}media/raport-de-activitate-pentru-anul-1-DR-36.pdf">Raport de activitate pentru anul 1 DR 36</a>
<br><br>
<ul class="list-none">
{lis}
</ul>
<br>
<img src="{p}teritoriul-microregiunii/harta-microregiunii.png" alt="harta gal" width="628" height="748">"""


def apeluri_body(prefix: str) -> str:
    p = prefix
    return f"""<h1>Apeluri selecție</h1>
<a class="link" href="{p}media/apel_selectie_Interventia_1_Durabilitatea_mediului_in_satul_dobrogean.zip" target="_blank" rel="noopener">Apel selecție Intervenția 1 - Durabilitatea mediului în satul dobrogean</a><br>
<a class="link" href="{p}media/apel_selectie_interventia_3_Investitii_si_servicii_de_baza_destinate_comunitatii.zip" target="_blank" rel="noopener">Apel selecție Intervenția 3 - Investiții și servicii de bază destinate comunității</a><br>


<a class="link" href="https://www.afir.ro/domenii-de-interventie/detalii-si-anexe-dr-36/" target="_blank" rel="noopener">Detalii și anexe DR 36</a><br>
<a class="link" href="{p}media/anunt-erata-apel-selectie-I4.pdf" target="_blank" rel="noopener">Anunț erată la apel de selecție - I4</a><br>
<a class="link" href="{p}media/apel_selectie_interventia_5.rar" target="_blank" rel="noopener">Apel selecție Intervenția 5</a><br>
<a class="link" href="{p}media/apel_selectie_interventia_4.rar" target="_blank" rel="noopener">Apel selecție Intervenția 4</a><br>"""


def calendar_apeluri_body(prefix: str) -> str:
    p = prefix
    return f"""<h1>Calendar apeluri selectie</h1>
<ul class="list-none">
  <li><a class="link" href="{p}media/calendar%20estimativ%20DR%2036%20AN%202%20REVIZUIT.pdf" target="_blank" rel="noopener">CALENDAR ESTIMATIV DR 36 AN 2 REVIZUIT</a></li>
  <li><a class="link" href="{p}media/calendar-estimativ-DR-36-AN-2.pdf" target="_blank" rel="noopener">CALENDAR ESTIMATIV DR 36 AN 2</a></li>
</ul>"""


def rapoarte_body(prefix: str) -> str:
    p = prefix
    return f"""<h1>Rapoarte selecție</h1>
<ul class="list-none">
  <li><a class="link" href="{p}media/rapoarte-selectie/raport-selectie-intermediar-gal-dobrogea-centrala-devine-raport-final.pdf" target="_blank" rel="noopener">Raport selecție intermediar GAL Dobrogea Centrală care devine raport final</a></li>
</ul>"""


def actiuni_animare_body(prefix: str) -> str:
    p = prefix
    items = [
        ("1", "aliman", "COMUNA ALIMAN"),
        ("2", "ciocirlia", "COMUNA CIOCIRLIA"),
        ("3", "crucea", "COMUNA CRUCEA"),
        ("4", "garliciu", "COMUNA GARLICIU"),
        ("5", "ghindaresti", "COMUNA GHINDARESTI"),
        ("6", "horia", "COMUNA HORIA"),
        ("7", "mircea-voda", "COMUNA MIRCEA VODA"),
        ("8", "pestera", "COMUNA PESTERA"),
        ("9", "rasova", "COMUNA RASOVA"),
        ("10", "saligny", "COMUNA SALIGNY"),
        ("11", "saraiu", "COMUNA SARAIU"),
        ("12", "seimeni", "COMUNA SEIMENI"),
        ("13", "topalu", "COMUNA TOPALU"),
        ("14", "tortoman", "COMUNA TORTOMAN"),
        ("15", "ciobanu", "COMUNA CIOBANU"),
        ("16", "harsova", "ORAS HIRSOVA"),
        ("17", "casimcea", "COMUNA CASIMCEA"),
    ]
    lis = "\n".join(
        f'  <li>{n}. <a class="link" href="{p}media/actiuni-animare/anunturi-an-1-sem-4/anunt-{slug}.docx">{label}</a></li>'
        for n, slug, label in items
    )
    return f"""<h1>Actiuni animare</h1>
<a class="link" href="{p}media/plan-bune-practici.pdf">Plan de bune practici</a>
<h2>Anunturi - trimestrul al IV-lea - anul 1</h2>
<ul class="list-none">
{lis}
</ul>"""


def comunicate_body(prefix: str) -> str:
    p = prefix
    return f"""<h1>Comunicate</h1>
<a class="link" href="{p}media/comunicate/anunt-prelungire-interventia-1.rar">PRELUNGIRE APEL SELECTIE INTERVENTIA NR 1 - DURABILITATEA MEDIULUI IN SATUL DOBROGEAN</a><br><br>
<a class="link" href="{p}media/comunicate/anunt-prelungire-interventia-3.rar">PRELUNGIRE APEL SELECTIE INTERVENTIA NR 3 - INVESTITII SI SERVICII DE BAZA DESTINATE COMUNITATII</a><br><br>
<a class="link" href="{p}media/comunicate/NOTA-PRELUNGIRE-PERIOADA-DE-EVALUARE.pdf">NOTA PRELUNGIRE PERIOADA DE EVALUARE</a><br><br>
<a class="link" href="{p}media/comunicate/1-anunt-apel-interventia-5.docx">APEL SELECTIE INTERVENTIA NR 5 START-UP NONAGRICOL</a><br><br>
<a class="link" href="{p}media/comunicate/2-anunt-prelungire-interventia-5.docx">PRELUNGIRE APEL SELECTIE INTERVENTIA NR 5 START-UP NONAGRICOL</a>"""


def materiale_body(prefix: str) -> str:
    p = prefix
    afise = [
        ("1", "aliman", "COMUNA ALIMAN"),
        ("2", "ciocirlia", "COMUNA CIOCIRLIA"),
        ("3", "crucea", "COMUNA CRUCEA"),
        ("4", "garliciu", "COMUNA GARLICIU"),
        ("5", "ghindaresti", "COMUNA GHINDARESTI"),
        ("6", "horia", "COMUNA HORIA"),
        ("7", "mircea-voda", "COMUNA MIRCEA VODA"),
        ("8", "pestera", "COMUNA PESTERA"),
        ("9", "rasova", "COMUNA RASOVA"),
        ("10", "saligny", "COMUNA SALIGNY"),
        ("11", "saraiu", "COMUNA SARAIU"),
        ("12", "seimeni", "COMUNA SEIMENI"),
        ("13", "topalu", "COMUNA TOPALU"),
        ("14", "tortoman", "COMUNA TORTOMAN"),
        ("15", "ciobanu", "COMUNA CIOBANU"),
        ("16", "hirsova", "ORAS HIRSOVA"),
        ("17", "casimcea", "COMUNA CASIMCEA"),
    ]
    lis = "\n".join(
        f'  <li>{n}. <a class="link" href="{p}media/materiale-publicitare/afise/{slug}.pdf">{label}</a></li>'
        for n, slug, label in afise
    )
    return f"""<h1>Materiale publicitare</h1>
<img src="{p}media/materiale-publicitare/panou.jpg" alt="panou" width="943" height="641">
<img src="{p}media/materiale-publicitare/rollup.jpg" alt="rollup" width="943" height="1257">

<img src="{p}media/materiale-publicitare/altele/01-tortoman-sediu-gal.jpg" alt="sediu">
<img src="{p}media/materiale-publicitare/altele/02-tortoman-program.jpg" alt="program">
<img src="{p}media/materiale-publicitare/altele/ALIMAN.jpg" alt="aliman">
<img src="{p}media/materiale-publicitare/altele/CIOCIRLIA.jpg" alt="ciocarlia">
<img src="{p}media/materiale-publicitare/altele/PESTEREA.jpg" alt="pesterea">
<img src="{p}media/materiale-publicitare/altele/RASOVA.jpg" alt="rasova">
<img src="{p}media/materiale-publicitare/altele/SEIMENI.jpg" alt="seimeni">
<img src="{p}media/materiale-publicitare/altele/TOPALU.jpg" alt="topalu">
<img src="{p}media/materiale-publicitare/altele/TORTOMAN.jpg" alt="tortoman">

<h2>Afise</h2>
<ul class="list-none">
{lis}
</ul>"""


def _animare_list(prefix: str, folder: str, ext: str) -> str:
    items = [
        ("1", "aliman", "COMUNA ALIMAN"),
        ("2", "ciocirlia", "COMUNA CIOCIRLIA"),
        ("3", "crucea", "COMUNA CRUCEA"),
        ("4", "garliciu", "COMUNA GARLICIU"),
        ("5", "ghindaresti", "COMUNA GHINDARESTI"),
        ("6", "horia", "COMUNA HORIA"),
        ("7", "mircea-voda", "COMUNA MIRCEA VODA"),
        ("8", "pestera", "COMUNA PESTERA"),
        ("9", "rasova", "COMUNA RASOVA"),
        ("10", "saligny", "COMUNA SALIGNY"),
        ("11", "saraiu", "COMUNA SARAIU"),
        ("12", "seimeni", "COMUNA SEIMENI"),
        ("13", "topalu", "COMUNA TOPALU"),
        ("14", "tortoman", "COMUNA TORTOMAN"),
        ("15", "ciobanu", "COMUNA CIOBANU"),
        ("16", "harsova", "ORAS HIRSOVA"),
        ("17", "casimcea", "COMUNA CASIMCEA"),
    ]
    return "\n".join(
        f'  <li>{n}. <a class="link" href="{prefix}media/actiuni-animare/{folder}/anunt-{slug}.{ext}">{label}</a></li>'
        for n, slug, label in items
    )


def arhiva_body(prefix: str) -> str:
    p = prefix
    lis_reactualizat = _animare_list(p, "anunturi-an-1-sem-3-reactualizat", "pdf")
    lis_sem3 = _animare_list(p, "anunturi-an-1-sem-3", "pdf")
    lis_sem2 = _animare_list(p, "anunturi-an-1-sem-2", "pdf")
    lis_sem1 = _animare_list(p, "anunturi", "pdf")
    return f"""<h1>Arhiva</h1>
<h1>Apeluri selectie</h1>
<a class="link" href="{p}media/Raport-selectie-intermediar-I5-DC.pdf" target="_blank" rel="noopener">Raport-selectie-intermediar-I5-DC</a><br>
<a class="link" href="{p}media/documente-apel%20strat%20-%20up%2001.zip" target="_blank" rel="noopener">documente-apel strat - up 01</a><br>

<h1>Calendar apeluri selectie</h1>
<ul class="list-none">
  <li><a class="link" href="{p}media/calendar%20estimativ%20DR%2036%20AN%201%20trim%204%20r.jpg" target="_blank" rel="noopener">calendar-AM-estimativ-an-1-trim-IV-2025</a></li>
</ul>
<br>
<h1>Media - Calendar</h1>
<ul class="list-none">
  <li><a class="link" href="{p}media/calendar-animare-tr1-an-2.pdf" target="_blank" rel="noopener">CALENDARUL INTALNIRILOR DE ANIMARE IN PREAMBULUL LANSARII INTERVENTIILOR TRIMESTRUL 1/ AN 2</a></li>
  <li><a class="link" href="{p}media/calendar%20animare%20TR4.pdf" target="_blank" rel="noopener">CALENDARUL INTALNIRILOR DE ANIMARE IN PREAMBULUL LANSARII INTERVENTIILOR TRIMESTRUL 4/ 2025</a></li>
</ul>
<br>
<h2>Calendar apeluri selectie</h2>
<ul class="list-none">
  <li><a class="link" href="{p}media/calendar-estimativ-DR-36-AN-1.jpg" target="_blank" rel="noopener">calendar-estimativ-DR-36-AN-1</a></li>
  <li><a class="link" href="{p}media/calendar-AM-estimativ-an-1-trim-III-2025.pdf" target="_blank" rel="noopener">calendar-AM-estimativ-an-1-trim-III-2025</a></li>
  <li><a class="link" href="{p}media/calendar-AM-estimativ-an-1-trim-IV-2025.pdf" target="_blank" rel="noopener">calendar-AM-estimativ-an-1-trim-IV-2025</a></li>
</ul>
<a class="link" href="{p}media/calendar-trim-3_2.pdf" target="_blank" rel="noopener">Calendar reactualizat</a>

<h2>EVENIMENT DE ANIMARE A TERITORIULUI TRIM III COMUNA SARAIU</h2>
<ul class="list-none">
  <li>1. <a class="link" href="{p}media/actiuni-animare/anunturi-an-1-sem-3/afis-saraiu-trim-3.pdf">Afis comuna Saraiu</a></li>
</ul>
<h2>Anunturi - trimestrul al III-lea - reactualizate - anul 1</h2>
<ul class="list-none">
{lis_reactualizat}
</ul>

<h2>Anunturi - trimestrul al III-lea - anul 1</h2>
<ul class="list-none">
{lis_sem3}
</ul>
<h2>CALENDAR AN 1 TRIMESTRUL 3</h2>
<a class="link" href="{p}media/calendar-trim-3.pdf">Calendar</a>
<h2>CALENDAR AN 1 TRIMESTRUL 2</h2>
<a class="link" href="{p}media/calendar-trim-2.pdf">Calendar</a>
<h2>Anunturi - trimestrul 2 - anul 1</h2>
<ul class="list-none">
{lis_sem2}
</ul>
<br>
<hr>
<br>
<h2>CALENDAR AN 1 TRIMESTRUL 1</h2>
<a class="link" href="{p}media/calendar.pdf">Calendar</a>
<h2>ARHIVA ANUNTURI AN 1 TRIMESTRUL 1</h2>
<ul class="list-none">
{lis_sem1}
</ul>"""


NOT_FOUND_HTML = head("") + """<div class="prose">
  <h1>Pagina nu a fost gasita</h1>
  <p><a class="link" href="index.html">Click aici pentru a merge catre prima pagina</a></p>
</div>
<script src="assets/js/site.js?v=""" + ASSET_VERSION + """" defer></script>
</body>
</html>
"""


# ---------- Page registry ----------

PAGES = [
    ("index.html", INDEX_HTML),
    ("404.html", NOT_FOUND_HTML),
    ("acasa/index.html", page("../", ACASA_BODY)),
    ("contact/index.html", page("../", CONTACT_BODY)),
    ("details-of-organisations/index.html", page("../", DETAILS_BODY)),
    ("implementarea-sdl-prin-leader/index.html", page("../", IMPLEMENTAREA_BODY)),
    ("teritoriul-microregiunii/index.html", page("../", teritoriul_body("../"))),
    ("arhiva/index.html", page("../", arhiva_body("../"))),
    ("media/actiuni-animare/index.html", page("../../", actiuni_animare_body("../../"))),
    ("media/comunicate/index.html", page("../../", comunicate_body("../../"))),
    ("media/materiale-publicitare/index.html", page("../../", materiale_body("../../"))),
    ("finantare-proiecte/apeluri-selectie/index.html", page("../../", apeluri_body("../../"))),
    ("finantare-proiecte/calendar-apeluri-selectie/index.html", page("../../", calendar_apeluri_body("../../"))),
    ("finantare-proiecte/rapoarte-selectie/index.html", page("../../", rapoarte_body("../../"))),
]


SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://galdc.ro/</loc></url>
  <url><loc>https://galdc.ro/acasa/</loc></url>
  <url><loc>https://galdc.ro/arhiva/</loc></url>
  <url><loc>https://galdc.ro/contact/</loc></url>
  <url><loc>https://galdc.ro/details-of-organisations/</loc></url>
  <url><loc>https://galdc.ro/finantare-proiecte/apeluri-selectie/</loc></url>
  <url><loc>https://galdc.ro/finantare-proiecte/calendar-apeluri-selectie/</loc></url>
  <url><loc>https://galdc.ro/finantare-proiecte/rapoarte-selectie/</loc></url>
  <url><loc>https://galdc.ro/implementarea-sdl-prin-leader/</loc></url>
  <url><loc>https://galdc.ro/media/actiuni-animare/</loc></url>
  <url><loc>https://galdc.ro/media/comunicate/</loc></url>
  <url><loc>https://galdc.ro/media/materiale-publicitare/</loc></url>
  <url><loc>https://galdc.ro/teritoriul-microregiunii/</loc></url>
</urlset>
"""


ROBOTS = """User-agent: *
Allow: /
Sitemap: https://galdc.ro/sitemap.xml
"""


def write_all() -> None:
    for relpath, content in PAGES:
        out = ROOT / relpath
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"wrote {relpath}")

    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    print("wrote robots.txt")

    (ROOT / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    write_all()
