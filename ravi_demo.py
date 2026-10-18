from pathlib import Path
from shutil import copy2
from favicon import icon_links


def build_ravi_dental_demo(P, origin):
    """Build a single independent, noindex prospect concept for Ravi Dental Care."""
    destination = P / "demos" / "ravi-dental-care"
    destination.mkdir(parents=True, exist_ok=True)
    source_image = Path("assets/ravi-dental-hero.png")
    copy2(source_image, destination / source_image.name)

    css = r'''
:root { --ink:#0c1113; --mist:#c8dcec; --paper:#f8f7f3; --line:rgba(12,17,19,.15); --soft:#eaf1f6; }
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { margin:0; color:var(--ink); background:var(--paper); font-family:"DM Sans",Arial,sans-serif; }
a { color:inherit; }
.ravi-skip { position:absolute; left:-999px; top:0; background:white; color:black; padding:12px; z-index:10; }
.ravi-skip:focus { left:12px; }
.ravi-banner { display:flex; justify-content:space-between; gap:20px; align-items:center; padding:10px 5vw; color:#31424e; background:#e8f0f5; border-bottom:1px solid rgba(12,17,19,.1); font-size:12px; letter-spacing:.04em; }
.ravi-banner a { text-underline-offset:3px; }
.ravi-page { max-width:1600px; margin:0 auto; padding:16px clamp(14px,3vw,44px) 44px; }
.ravi-hero { min-height:790px; overflow:hidden; position:relative; padding:26px clamp(22px,4vw,64px) 36px; background:var(--mist); border-radius:30px; }
.ravi-nav { display:flex; align-items:center; justify-content:space-between; position:relative; z-index:3; gap:28px; }
.ravi-brand { display:flex; align-items:center; gap:10px; text-decoration:none; font-weight:700; letter-spacing:-.04em; font-size:20px; }
.ravi-mark { display:grid; place-items:center; width:34px; height:34px; color:white; background:var(--ink); border-radius:9px; font-size:20px; font-family:Georgia,serif; }
.ravi-links { display:flex; align-items:center; justify-content:center; gap:clamp(14px,2vw,34px); font-size:14px; }
.ravi-links a { text-decoration:none; }
.ravi-links a:hover { text-decoration:underline; text-underline-offset:5px; }
.ravi-action, .ravi-button { display:inline-flex; align-items:center; justify-content:center; gap:10px; padding:14px 19px; background:var(--ink); color:white; text-decoration:none; border:1px solid var(--ink); font:600 14px/1 "DM Sans",Arial,sans-serif; cursor:pointer; transition:transform .2s ease, background .2s ease; }
.ravi-action { border-radius:4px; padding:12px 17px; }
.ravi-button:hover, .ravi-action:hover { background:#27373f; transform:translateY(-2px); }
.ravi-button.ghost { background:transparent; color:var(--ink); border-color:var(--ink); }
.ravi-button.ghost:hover { background:white; }
.ravi-availability { position:absolute; right:clamp(22px,4vw,64px); top:133px; text-align:right; color:#365064; font-size:13px; line-height:1.35; }
.ravi-availability strong { display:block; color:var(--ink); font-weight:500; }
.ravi-hero h1 { position:relative; z-index:1; max-width:1080px; margin:112px 0 0; font:400 clamp(54px,8.4vw,138px)/.82 "DM Sans",Arial,sans-serif; letter-spacing:-.075em; }
.ravi-hero h1 em { font-style:normal; color:#f8fafb; }
.ravi-subtitle { width:min(360px,100%); margin:31px 0 0; color:#304553; line-height:1.45; font-size:16px; }
.ravi-hero-buttons { display:flex; flex-wrap:wrap; gap:10px; margin-top:26px; }
.ravi-art { position:absolute; z-index:2; width:clamp(320px,42vw,650px); right:5%; bottom:-2px; filter:drop-shadow(0 25px 24px rgba(28,53,73,.14)); pointer-events:none; }
.ravi-art img { width:100%; height:auto; display:block; }
.ravi-orbit { position:absolute; right:13%; bottom:194px; width:min(45vw,650px); height:215px; border:1px solid rgba(255,255,255,.75); border-radius:50%; transform:rotate(-7deg); }
.ravi-chip { position:absolute; z-index:3; padding:9px 11px; background:rgba(249,252,255,.76); border:1px solid rgba(255,255,255,.8); box-shadow:0 8px 25px rgba(55,89,110,.09); color:#486373; font-size:11px; backdrop-filter:blur(8px); }
.ravi-chip.one { right:38%; top:54%; } .ravi-chip.two { right:10%; top:64%; }
.ravi-supersize { position:absolute; bottom:-31px; left:0; color:rgba(90,133,164,.18); font-size:clamp(112px,19vw,300px); line-height:.7; font-weight:600; letter-spacing:-.11em; user-select:none; }
.ravi-public { display:grid; grid-template-columns:repeat(4,1fr); margin:28px 4vw 0; padding:28px 0; border-bottom:1px solid var(--line); }
.ravi-public div { display:flex; align-items:baseline; gap:11px; padding:0 clamp(12px,2.5vw,42px); border-right:1px solid var(--line); }
.ravi-public div:last-child { border:none; }
.ravi-public strong { font-size:clamp(31px,3.4vw,54px); letter-spacing:-.07em; font-weight:500; }
.ravi-public span { color:#74828b; font-size:12px; line-height:1.1; max-width:100px; }
.ravi-section { padding:clamp(78px,11vw,160px) clamp(8px,4vw,64px); }
.ravi-section-head { display:grid; grid-template-columns:1fr 370px; gap:40px; align-items:end; }
.ravi-kicker { display:block; margin-bottom:20px; color:#75838b; letter-spacing:.07em; font-size:11px; font-weight:700; }
.ravi-section h2 { max-width:730px; margin:0; font:400 clamp(42px,5.6vw,84px)/.92 "DM Sans",Arial,sans-serif; letter-spacing:-.065em; }
.ravi-section-head > p { margin:0 0 8px; color:#53636c; font-size:16px; line-height:1.45; }
.ravi-dark { margin:0 clamp(0px,2vw,28px); padding:clamp(30px,5vw,74px); color:#f7f7f1; background:var(--ink); border-radius:26px; }
.ravi-dark .ravi-kicker { color:#a5b6c1; }
.ravi-dark h2 { max-width:660px; }
.ravi-journey { display:grid; grid-template-columns:repeat(3,1fr); gap:15px; margin-top:55px; padding-top:18px; border-top:1px solid rgba(255,255,255,.15); }
.ravi-journey article { min-height:285px; padding:19px; border-radius:18px; background:#20292d; }
.ravi-journey figure { height:120px; margin:0 0 23px; border-radius:12px; overflow:hidden; background:linear-gradient(135deg,#7699b3,#b8d0df); }
.ravi-journey article:nth-child(2) figure { background:radial-gradient(circle at 60% 35%,#f5f7f7 0 7%,transparent 8%), linear-gradient(135deg,#253941,#94b7c6); }
.ravi-journey article:nth-child(3) figure { background:linear-gradient(120deg,#dbe8ef 0 40%,#7598ae 40% 100%); }
.ravi-journey h3 { margin:0 0 10px; font-size:24px; font-weight:500; letter-spacing:-.06em; }
.ravi-journey p { margin:0; color:#bdc7cc; line-height:1.45; font-size:14px; }
.ravi-location { display:grid; grid-template-columns:1.05fr .95fr; gap:clamp(34px,7vw,110px); align-items:start; }
.ravi-location-text p { max-width:530px; color:#53636c; line-height:1.55; font-size:18px; }
.ravi-address { margin-top:36px; padding-top:21px; border-top:1px solid var(--line); }
.ravi-address p { margin:0; color:#28353a; font-size:16px; line-height:1.5; }
.ravi-address a { display:inline-block; margin-top:12px; font-size:14px; text-underline-offset:4px; }
.ravi-map { min-height:430px; position:relative; overflow:hidden; border-radius:23px; background:linear-gradient(135deg,#dbe8ee,#c1d6df); }
.ravi-map::before, .ravi-map::after { content:""; position:absolute; background:rgba(255,255,255,.48); }
.ravi-map::before { width:135%; height:18px; left:-20%; top:44%; transform:rotate(-18deg); }
.ravi-map::after { width:18px; height:130%; right:43%; top:-20%; transform:rotate(18deg); }
.ravi-pin { position:absolute; z-index:1; top:46%; left:53%; display:grid; place-items:center; width:58px; height:58px; color:white; background:var(--ink); border:7px solid white; border-radius:50% 50% 50% 0; transform:rotate(-45deg); box-shadow:0 10px 18px rgba(20,45,55,.22); }
.ravi-pin span { transform:rotate(45deg); font-size:16px; }
.ravi-map-note { position:absolute; z-index:1; right:20px; bottom:20px; max-width:210px; padding:13px; color:#344a56; background:rgba(255,255,255,.78); font-size:12px; line-height:1.35; backdrop-filter:blur(8px); }
.ravi-cta { margin:20px 0 0; padding:clamp(34px,5vw,74px); color:var(--ink); background:var(--mist); border-radius:26px; }
.ravi-cta-inner { display:flex; align-items:end; justify-content:space-between; gap:36px; }
.ravi-cta h2 { max-width:760px; margin:0; font:400 clamp(44px,6vw,92px)/.88 "DM Sans",Arial,sans-serif; letter-spacing:-.065em; }
.ravi-cta p { max-width:330px; color:#375060; line-height:1.45; }
.ravi-footer { display:flex; justify-content:space-between; gap:25px; padding:30px 10px 5px; color:#68767d; font-size:12px; line-height:1.45; }
.ravi-footer p { max-width:580px; margin:0; }
@media (max-width:800px) { .ravi-banner { align-items:flex-start; flex-direction:column; gap:5px; } .ravi-page { padding:8px 8px 26px; } .ravi-hero { min-height:710px; border-radius:20px; padding:20px; } .ravi-links { display:none; } .ravi-hero h1 { margin-top:90px; max-width:620px; font-size:clamp(53px,15vw,95px); } .ravi-availability { right:20px; top:99px; font-size:11px; } .ravi-art { width:min(106vw,520px); right:-11%; bottom:-8px; } .ravi-orbit { width:103vw; right:-28%; bottom:170px; } .ravi-chip.one { right:40%; top:55%; } .ravi-chip.two { display:none; } .ravi-public { grid-template-columns:1fr 1fr; margin:18px 18px 0; gap:20px 0; } .ravi-public div:nth-child(2) { border:none; } .ravi-public div:nth-child(n+3) { padding-top:18px; border-top:1px solid var(--line); } .ravi-public strong { font-size:36px; } .ravi-section { padding:82px 20px; } .ravi-section-head, .ravi-location { grid-template-columns:1fr; } .ravi-journey { grid-template-columns:1fr; margin-top:38px; } .ravi-journey article { min-height:auto; } .ravi-map { min-height:310px; } .ravi-cta { border-radius:20px; } .ravi-cta-inner, .ravi-footer { align-items:flex-start; flex-direction:column; } }
@media (max-width:430px) { .ravi-brand { font-size:17px; } .ravi-action { padding:10px 12px; font-size:12px; } .ravi-hero h1 { letter-spacing:-.09em; } .ravi-subtitle { font-size:14px; max-width:280px; } .ravi-hero-buttons { margin-top:20px; } .ravi-button { width:100%; } }
'''

    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">{icon_links()}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>RAVI Dental Care — independent website concept</title>
<meta name="description" content="An independent one-page website concept for RAVI Dental Care in Varanasi. Not the clinic's official website.">
<meta name="robots" content="noindex,follow"><link rel="canonical" href="{origin}/demos/ravi-dental-care/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/demos/ravi-dental-care/ravi-demo.css"></head>
<body><a class="ravi-skip" href="#main">Skip to content</a>
<div class="ravi-banner"><span>Independent concept preview for RAVI Dental Care · Not an official clinic website</span><a href="/">Made by SiteSutra ↗</a></div>
<div class="ravi-page"><main id="main">
<section class="ravi-hero"><nav class="ravi-nav" aria-label="Concept navigation">
<a class="ravi-brand" href="#main"><span class="ravi-mark">R</span><span>RAVI<br>Dental Care</span></a>
<div class="ravi-links"><a href="#visit">Visit us</a><a href="#prepare">Before you visit</a><a href="#contact">Contact</a></div>
<a class="ravi-action" href="tel:+918209417262">Call the clinic <span aria-hidden="true">↗</span></a></nav>
<div class="ravi-availability"><strong>RAVI DENTAL CARE</strong>Jagatganj, Varanasi</div>
<h1>A clearer way<br>to begin your <em>dental visit.</em></h1>
<p class="ravi-subtitle">A calm, useful first stop for finding the clinic, speaking with the team, and planning your next step.</p>
<div class="ravi-hero-buttons"><a class="ravi-button" href="tel:+918209417262">Call RAVI Dental Care <span aria-hidden="true">↗</span></a><a class="ravi-button ghost" href="#visit">Get directions <span aria-hidden="true">↓</span></a></div>
<div class="ravi-orbit" aria-hidden="true"></div><span class="ravi-chip one">Call before visiting<br>for current availability</span><span class="ravi-chip two">Jagatganj, Varanasi</span>
<picture class="ravi-art"><img src="/demos/ravi-dental-care/ravi-dental-hero.png" alt="Original 3D porcelain tooth artwork on a silver pedestal"></picture><span class="ravi-supersize" aria-hidden="true">RAVI</span>
</section>
<section class="ravi-public" aria-label="Public clinic information, checked 18 October 2026"><div><strong>5.0</strong><span>Google Maps rating</span></div><div><strong>461</strong><span>Public Google reviews</span></div><div><strong>01</strong><span>Clinic location in Jagatganj</span></div><div><strong>Call</strong><span>Direct public contact number</span></div></section>
<section class="ravi-section ravi-dark" id="prepare"><span class="ravi-kicker">BEFORE YOU VISIT</span><h2>A simple path from a question to the right next step.</h2>
<div class="ravi-journey"><article><figure aria-hidden="true"></figure><h3>01 · Start with a call</h3><p>Use the published number to ask about the concern you want to discuss and the current appointment process.</p></article><article><figure aria-hidden="true"></figure><h3>02 · Confirm the details</h3><p>Confirm clinic hours, available treatments, fees, and any preparation needed directly with the clinic team.</p></article><article><figure aria-hidden="true"></figure><h3>03 · Plan your visit</h3><p>Use the map link below for directions to the Jagatganj location before you leave.</p></article></div>
</section>
<section class="ravi-section" id="visit"><div class="ravi-location"><div class="ravi-location-text"><span class="ravi-kicker">FIND THE CLINIC</span><h2>Close by when you need a next step.</h2><p>RAVI Dental Care is listed in Jagatganj, Varanasi. Use the public map listing for directions and call the clinic to confirm current hours before visiting.</p><div class="ravi-address"><p>C-27/1-A, Sanskrit University Rd, near Sampurnanand, Jagatganj, Chaukaghat, Varanasi, Uttar Pradesh 221002</p><a href="https://www.google.com/maps/search/?api=1&amp;query=Ravi+Dental+Care+Jagatganj+Varanasi" target="_blank" rel="noopener">Open in Google Maps ↗</a></div></div><a class="ravi-map" href="https://www.google.com/maps/search/?api=1&amp;query=Ravi+Dental+Care+Jagatganj+Varanasi" target="_blank" rel="noopener" aria-label="Open RAVI Dental Care location in Google Maps"><span class="ravi-pin"><span>R</span></span><span class="ravi-map-note">Directions open in Google Maps. Confirm the exact location before travel.</span></a></div></section>
<section class="ravi-cta" id="contact"><div class="ravi-cta-inner"><div><span class="ravi-kicker">RAVI DENTAL CARE · VARANASI</span><h2>Ready to speak with the clinic?</h2></div><div><p>Call directly to ask about your visit. The clinic can confirm services, fees, hours, and appointment availability.</p><a class="ravi-button" href="tel:+918209417262">Call 082094 17262 <span aria-hidden="true">↗</span></a></div></div></section>
</main><footer class="ravi-footer"><span>RAVI Dental Care · independent concept preview</span><p>Public address, phone, rating, and review count were referenced from Google Maps on 18 October 2026. This page is not endorsed by or affiliated with the clinic. Verify all care, availability, prices, and hours directly with the clinic.</p></footer></div></body></html>'''
    (destination / "ravi-demo.css").write_text(css)
    (destination / "index.html").write_text(html)
