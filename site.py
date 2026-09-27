"""Generate the dependency-free Astral site for GitHub Pages."""
from pathlib import Path
from html import escape
import os

ROOT = Path(__file__).parent
OUT = ROOT / "dist"

# Fill these values when BALAN's Discord application and support contact are ready.
BOT_CLIENT_ID = os.environ.get("BALAN_CLIENT_ID", "").strip()
SUPPORT_EMAIL = os.environ.get("ASTRAL_SUPPORT_EMAIL", "").strip()

FEATURES = [
    ("01", "Moderation", "Keep conversations orderly with practical moderation controls."),
    ("02", "Security", "Protect your server with configurable safeguards."),
    ("03", "Tickets", "Give members a clear way to ask for help."),
    ("04", "Temporary Voice", "Make room for conversations when they happen."),
    ("05", "Levels", "Recognize activity across your community."),
    ("06", "Giveaways", "Run community events with less manual work."),
    ("07", "Self Roles", "Let members choose how they participate."),
    ("08", "Logging", "Keep a record of the actions that matter."),
]

def icon():
    return '<svg class="symbol" viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M20 3 35.5 30.5H4.5L20 3Z" stroke="currentColor" stroke-width="1.3"/><path d="M20 12 28.6 27H11.4L20 12Z" fill="currentColor"/></svg>'

def link(path, prefix):
    return prefix + path

def shell(title, description, section, body, prefix="", page=""):
    nav = [("Home", ""), ("Bots", "bots/"), ("Status", "status/"), ("Docs", "docs/"), ("Legal", "legal/")]
    menu = "".join(f'<a href="{link(p,prefix)}" {"aria-current=page" if page == p else ""}>{label}</a>' for label,p in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#090d12"><meta name="description" content="{escape(description, quote=True)}"><title>{escape(title)} — ASTRAL</title>
<link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg"><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a><div class="site-wrap">
<header class="header"><a class="brand" href="{prefix}" aria-label="Astral home">{icon()}<span>ASTRAL<span class="brand-dot">.</span></span></a><nav aria-label="Main navigation">{menu}</nav><a class="header-bot" href="{prefix}bots/balan/">Explore BALAN <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">Menu <span aria-hidden="true">+</span></button></header>
<main id="main">{body}</main>
<footer><div class="footer-top"><div class="brand">{icon()}<span>ASTRAL<span class="brand-dot">.</span></span></div><p>Infrastructure for better communities.</p></div><div class="footer-bottom"><span>© 2026 Astral</span><div><a href="{prefix}bots/">Bots</a><a href="{prefix}docs/">Docs</a><a href="{prefix}legal/privacy/balan/">Privacy</a><a href="{prefix}legal/terms/balan/">Terms</a></div></div></footer></div><script src="{prefix}assets/site.js" defer></script></body></html>'''

def button_invite(prefix):
    if BOT_CLIENT_ID.isdigit():
        href = f"https://discord.com/oauth2/authorize?client_id={BOT_CLIENT_ID}&scope=bot%20applications.commands"
        return f'<a class="button primary" href="{href}" target="_blank" rel="noopener noreferrer">Add to Discord <span aria-hidden="true">↗</span></a>'
    return '<span class="button disabled" title="Invite link will be enabled when the Discord application ID is configured">Invite link coming soon</span>'

def eyebrow(index, text):
    return f'<div class="eyebrow"><span class="index">{index}</span><span>{text}</span></div>'

def bot_card(prefix):
    return f'''<article class="bot-card"><div class="bot-card-top"><div class="bot-mark">B<span class="tiny-star">✳</span></div><span class="micro">01 / ASTRAL BOTS</span></div>
    <div class="bot-card-body"><p class="muted-kicker">COMMUNITY &amp; MODERATION</p><h3>BALAN<span class="brand-dot">.</span></h3><p>All the essentials for a better run community, in one considered bot.</p></div>
    <div class="tags"><span>Security</span><span>Levels</span><span>Tickets</span><span>Voice Rooms</span><span>Giveaways</span></div>
    <div class="bot-card-bottom"><span class="status unverified"><span class="status-dot"></span>Status not connected</span><a class="text-link" href="{prefix}bots/balan/">View bot <span aria-hidden="true">↗</span></a></div></article>'''

home = f'''<section class="hero"><div class="hero-copy">{eyebrow('001', 'DISCORD TOOLS, CONSIDERED')}<h1>Better spaces<br>start <em>here.</em></h1><p class="hero-description">Powerful tools for the communities you care about. Simple setup. A calmer way to manage what matters.</p><a class="button primary" href="bots/">Explore bots <span aria-hidden="true">↗</span></a></div><div class="hero-art" aria-hidden="true"><div class="orbit orbit-outer"></div><div class="orbit orbit-mid"></div><div class="orbit orbit-inner"></div><div class="core">{icon()}</div><div class="orbit-label orbit-label-top">ASTRAL / 001</div><div class="orbit-label orbit-label-bottom">BUILD BETTER TOGETHER</div></div></section>
<section class="bots-section">{eyebrow('002','THE COLLECTION')}<div class="section-heading"><h2>Our bots<span class="brand-dot">.</span></h2><p>Purposeful tools, built to make everyday community life easier.</p></div><div class="bots-grid">{bot_card('')}<div class="next-card"><span class="asterisk">✳</span><div><span class="micro">WHAT'S NEXT</span><h3>More on<br>the horizon.</h3><p>The Astral collection is just beginning.</p></div><span class="next-index">02 — ∞</span></div></div></section>'''

bots = f'''<section class="page-intro">{eyebrow('001','THE COLLECTION')}<h1>Made for<br><em>your community.</em></h1><p>Meet the tools behind Astral. Start with BALAN, built around the day-to-day work of running a Discord server.</p></section><section class="bots-section compact"><div class="bots-grid">{bot_card('../')}<div class="next-card"><span class="asterisk">✳</span><div><span class="micro">WHAT'S NEXT</span><h3>More on<br>the horizon.</h3><p>More bots coming soon.</p></div><span class="next-index">02 — ∞</span></div></div></section>'''

feature_tiles = ''.join(f'<article class="feature"><span class="feature-number">{n}</span><h3>{name}</h3><p>{desc}</p></article>' for n,name,desc in FEATURES)
balan = f'''<section class="bot-hero"><div>{eyebrow('001','AN ASTRAL BOT')}<div class="bot-hero-title"><div class="bot-mark big">B<span class="tiny-star">✳</span></div><h1>BALAN<span class="brand-dot">.</span></h1></div><p class="bot-tagline">Community management,<br><em>without the clutter.</em></p><p class="bot-description">A single place for moderation, member support and the little things that make a server feel like home.</p><div class="hero-actions">{button_invite('../../')}<a class="button outline" href="../../docs/balan/">Documentation <span aria-hidden="true">↗</span></a></div></div><aside class="bot-console" aria-label="BALAN module overview"><div class="console-head"><span>ASTRAL / BALAN</span><span class="status unverified"><span class="status-dot"></span>Status not connected</span></div><div class="console-title"><span class="console-glyph">✳</span><span>Community toolkit</span></div><div class="console-rows"><div><span>01</span> MODERATION <b>↗</b></div><div><span>02</span> SECURITY <b>↗</b></div><div><span>03</span> TICKETS <b>↗</b></div><div><span>04</span> TEMPORARY VOICE <b>↗</b></div><div><span>05</span> LEVELS <b>↗</b></div></div><div class="console-foot">TOOLS FOR EVERYDAY COMMUNITIES <span>01 / 08</span></div></aside></section><section class="feature-section">{eyebrow('002','THE TOOLKIT')}<div class="section-heading"><h2>Everything in<br>its right place<span class="brand-dot">.</span></h2><p>Explore the areas BALAN is designed to cover.</p></div><div class="feature-grid">{feature_tiles}</div></section><section class="bot-end"><span>READY WHEN YOU ARE</span><h2>Make room for<br>better communities.</h2><div class="hero-actions">{button_invite('../../')}<a class="text-link" href="../../legal/privacy/balan/">How BALAN handles data ↗</a></div></section>'''

status = '''<section class="page-intro narrow">''' + eyebrow('001','SERVICE STATUS') + '''<h1>Operational<br><em>visibility.</em></h1><p>Live monitoring has not been connected yet. This page will show service health when a verified status source is available.</p></section><section class="content-panel"><div class="panel-row"><div><h2>BALAN</h2><p>Discord bot</p></div><span class="status unverified"><span class="status-dot"></span>Monitoring unavailable</span></div><p class="note">This is not an indication that the bot is offline. No uptime or incident data is currently reported here.</p></section>'''

docs = '''<section class="page-intro narrow">''' + eyebrow('001','DOCUMENTATION') + '''<h1>Find your<br><em>way around.</em></h1><p>Documentation for the Astral collection.</p></section><section class="link-list"><a href="balan/"><span>01</span><strong>BALAN</strong><span>Overview and setup notes</span><b>↗</b></a></section>'''
docs_balan = f'''<section class="page-intro narrow">{eyebrow('001','BALAN / DOCUMENTATION')}<h1>Getting started<br><em>with BALAN.</em></h1><p>A quick look at the bot and its modules. Detailed command instructions will be added once the configuration is verified.</p></section><section class="content-panel prose"><h2>Invite the bot</h2><p>Use the invite button on the <a href="../../bots/balan/">BALAN page</a> once it becomes available. A server administrator must approve the requested permissions in Discord.</p><h2>What BALAN is designed to do</h2><p>Moderation, security, tickets, temporary voice channels, levels, giveaways, self roles and logging. Which modules are available and their commands depend on the deployed bot version.</p><h2>Before you enable a module</h2><p>Review the bot permissions, choose the channels and roles it needs, and consult the <a href="../../legal/privacy/balan/">BALAN privacy policy</a> and <a href="../../legal/terms/balan/">terms</a>. Documentation for each module will follow the verified release.</p></section>'''

legal = '''<section class="page-intro narrow">''' + eyebrow('001','LEGAL') + '''<h1>Clear by<br><em>design.</em></h1><p>Each Astral bot can have its own privacy policy and terms, tailored to what it actually does.</p></section><section class="link-list"><a href="privacy/balan/"><span>01</span><strong>BALAN / Privacy</strong><span>Data handling</span><b>↗</b></a><a href="terms/balan/"><span>02</span><strong>BALAN / Terms</strong><span>Conditions of use</span><b>↗</b></a></section>'''

contact = f'<a href="mailto:{escape(SUPPORT_EMAIL,quote=True)}">{escape(SUPPORT_EMAIL)}</a>' if SUPPORT_EMAIL else '<strong>[Insert verified contact address before publication]</strong>'
privacy = f'''<section class="legal-heading">{eyebrow('LEGAL / 01','BALAN')}<h1>Privacy policy<span class="brand-dot">.</span></h1><p>Draft for BALAN · Requires verification against the running bot before use in Discord Developer Portal.</p><div class="legal-meta">Last drafted: 27 September 2026 <span>•</span> ASTRAL / BALAN</div></section><div class="legal-layout"><aside class="legal-toc"><span>ON THIS PAGE</span><a href="#who">01 / Who operates BALAN</a><a href="#data">02 / Data processed</a><a href="#purpose">03 / Purpose and basis</a><a href="#storage">04 / Storage and sharing</a><a href="#rights">05 / Your choices</a><a href="#changes">06 / Changes</a></aside><article class="legal-prose"><div class="draft-banner"><strong>Publication checklist</strong><p>Verify the operator identity, every data category, legal basis, hosting location, retention period, third-party recipients, contact address and deletion process. Remove this notice only after the text matches the deployed bot.</p></div><section id="who"><h2>01 / Who operates BALAN</h2><p>BALAN is a Discord application in the Astral collection. Operator: <strong>[insert legal name and address]</strong>. Privacy contact: {contact}.</p></section><section id="data"><h2>02 / Data processed</h2><p>Depending on the modules you enable, BALAN may need Discord server IDs, user IDs, role and channel IDs, moderation actions, ticket content or metadata, voice channel activity, and level or giveaway activity. <strong>[Confirm exactly which fields the running bot receives, stores and deletes, including any message content or attachments.]</strong></p></section><section id="purpose"><h2>03 / Purpose and legal basis</h2><p>These data categories would be used to provide the modules requested by server administrators, respond to support requests and protect the service. <strong>[Specify the applicable GDPR legal basis for each actual processing purpose, including any legitimate interests assessment where relevant.]</strong></p></section><section id="storage"><h2>04 / Storage, retention and sharing</h2><p><strong>[Specify hosting provider and country, access controls, exact retention periods or criteria, backups, deletion deadlines, and any subprocessors or international transfers. State whether data are shared beyond Discord and infrastructure providers.]</strong></p></section><section id="rights"><h2>05 / Your choices and rights</h2><p>Server administrators can choose which modules to enable and can remove the bot from their server. For access, correction, deletion or other applicable data protection requests, contact {contact}. <strong>[Explain identity verification, response process and limits where records involve other members.]</strong> You may also contact the relevant data protection authority.</p></section><section id="changes"><h2>06 / Changes</h2><p>This policy will be updated when BALAN's features or data practices change. A dated published version should always reflect the live service.</p></section></article></div>'''

terms = f'''<section class="legal-heading">{eyebrow('LEGAL / 02','BALAN')}<h1>Terms of service<span class="brand-dot">.</span></h1><p>Draft for BALAN · Requires operator and service details before use in Discord Developer Portal.</p><div class="legal-meta">Last drafted: 27 September 2026 <span>•</span> ASTRAL / BALAN</div></section><div class="legal-layout"><aside class="legal-toc"><span>ON THIS PAGE</span><a href="#operator">01 / Operator</a><a href="#use">02 / Using the bot</a><a href="#admins">03 / Administrator choices</a><a href="#availability">04 / Availability</a><a href="#liability">05 / Responsibility</a><a href="#contact">06 / Contact</a></aside><article class="legal-prose"><div class="draft-banner"><strong>Publication checklist</strong><p>Confirm the operator, contact, applicable law, actual service behavior and any limits of liability with appropriate legal review before publishing these terms.</p></div><section id="operator"><h2>01 / Operator</h2><p>BALAN is offered by <strong>[insert legal name and address]</strong> as part of Astral. Contact: {contact}.</p></section><section id="use"><h2>02 / Using the bot</h2><p>You must follow Discord's applicable terms and community rules. Do not use BALAN to abuse users, break the law, or interfere with the service. The person installing BALAN must have permission to manage the relevant Discord server.</p></section><section id="admins"><h2>03 / Administrator choices</h2><p>Server administrators are responsible for selecting suitable permissions, configuring modules and informing their members where necessary. Features may require access to server information. See the <a href="../../privacy/balan/">BALAN privacy policy</a> for data practices once verified.</p></section><section id="availability"><h2>04 / Availability and changes</h2><p>Features may change, pause or become unavailable. We may restrict access where needed to protect the service or respond to misuse. <strong>[Define any support commitments, pricing or subscription terms if applicable.]</strong></p></section><section id="liability"><h2>05 / Responsibility</h2><p>BALAN is a tool to assist with community management. Server administrators remain responsible for their moderation decisions. <strong>[Insert reviewed warranty, liability and governing law terms appropriate to the operator and users.]</strong></p></section><section id="contact"><h2>06 / Contact and updates</h2><p>Questions about these terms can be sent to {contact}. Publish the date and notify users of material changes when these terms are finalized.</p></section></article></div>'''

pages = [
    ("", "Home", "Astral builds considered tools for Discord communities.", home, ""),
    ("bots/", "Bots", "Explore bots in the Astral collection, starting with BALAN.", bots, "../"),
    ("bots/balan/", "BALAN", "Community management with moderation, tickets, levels and more.", balan, "../../"),
    ("status/", "Status", "Service status for Astral bots.", status, "../"),
    ("docs/", "Docs", "Documentation for Astral bots.", docs, "../"),
    ("docs/balan/", "BALAN documentation", "Getting started with BALAN.", docs_balan, "../../"),
    ("legal/", "Legal", "Policies and terms for Astral bots.", legal, "../"),
    ("legal/privacy/balan/", "BALAN privacy policy", "Privacy information for BALAN.", privacy, "../../../"),
    ("legal/terms/balan/", "BALAN terms of service", "Terms of service for BALAN.", terms, "../../../"),
]

for path, title, desc, body, prefix in pages:
    target = OUT / path / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shell(title, desc, path, body, prefix, path), encoding="utf-8")

print(f"Generated {len(pages)} Astral pages in {OUT}")
