import json

fonts_data = [
    # Category 1: Swiss Neo-Grotesque & Clean Geometric Sans (1-20)
    {
        "num": "01",
        "name": "Neue Haas Grotesk",
        "foundry": "Linotype / Christian Schwartz",
        "category": "Swiss Neo-Grotesque",
        "license": "Commercial (Adobe Fonts)",
        "license_type": "commercial",
        "css_font": "'Neue Haas Grotesk Display Pro', 'Switzer', -apple-system, sans-serif",
        "headline_weight": 700,
        "role": "Hero Headline & Capsule Drop Titles",
        "pairing": "Space Mono (400) + Switzer (400)",
        "desc": "The purest digital realization of original 1957 Helvetica. Razor-sharp terminal cuts, closed apertures, tight tracking. The quintessential high-fashion streetwear base."
    },
    {
        "num": "02",
        "name": "PP Neue Montreal",
        "foundry": "Pangram Pangram Foundry",
        "category": "Contemporary Swiss Grotesque",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Neue Montreal', 'General Sans', sans-serif",
        "headline_weight": 700,
        "role": "Top Navigation Bar & Floating Pills",
        "pairing": "PP Editorial New (Italic) + General Sans",
        "desc": "Contemporary Swiss grotesque icon. Tightened rhythm, circular curves, bold confident presence favored by Represent, Fear of God, and modern lookbooks."
    },
    {
        "num": "03",
        "name": "Söhne",
        "foundry": "Klim Type Foundry (Kris Sowersby)",
        "category": "Rationalist Akzidenz-Grotesk",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Sohne', 'Switzer', -apple-system, sans-serif",
        "headline_weight": 700,
        "role": "Product Card Titles & PDP Pricing",
        "pairing": "Söhne Mono / JetBrains Mono (400)",
        "desc": "Captures Akzidenz-Grotesk through late-20th-century typesetting machines. Clinical, architectural, and effortlessly cool Scandinavian/Japanese aesthetic."
    },
    {
        "num": "04",
        "name": "General Sans",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Modernist Neutral Grotesque",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'General Sans', sans-serif",
        "headline_weight": 700,
        "role": "Primary UI Body, Accordions & Size Guide Specs",
        "pairing": "Unbounded (900) + Space Mono (400)",
        "desc": "Neutral, authoritative modern grotesque with subtle geometric tension. Vertical terminals, clean interior counters, exceptional screen rendering."
    },
    {
        "num": "05",
        "name": "Forma DJR",
        "foundry": "DJR (David Jonathan Ross)",
        "category": "Soft Neo-Grotesque",
        "license": "Commercial (Adobe Fonts)",
        "license_type": "commercial",
        "css_font": "'Forma DJR Display', 'Satoshi', sans-serif",
        "headline_weight": 700,
        "role": "Store Locator & Flagship Boutique Addresses",
        "pairing": "Druk Wide / Monument Extended",
        "desc": "Revival of Aldo Novarese's 1968 Italian neo-grotesque. Rounded micro-corners subtly soften the mechanical grid, evoking subtle Prada/Jil Sander luxury."
    },
    {
        "num": "06",
        "name": "Satoshi",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Geometric Neo-Grotesque",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'Satoshi', sans-serif",
        "headline_weight": 700,
        "role": "Primary CTA Buttons, Bag Bar & Badges",
        "pairing": "Inter Tight + Anton",
        "desc": "Modernist neo-grotesque infused with crisp geometric architecture. Sharp apex on uppercase 'A', geometric bowls, and clean horizontal strokes."
    },
    {
        "num": "07",
        "name": "Switzer",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Contemporary Neo-Grotesque",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'Switzer', sans-serif",
        "headline_weight": 800,
        "role": "UNTLD Global System Base Font",
        "pairing": "Switzer Text + DM Mono (400)",
        "desc": "Precise, unpretentious Swiss neo-grotesque directly channeling Max Miedinger's original drawings. Extremely reliable across mobile and desktop viewports."
    },
    {
        "num": "08",
        "name": "Inter Tight",
        "foundry": "Google Fonts (Rasmus Andersson)",
        "category": "High-Density Screen Grotesque",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Inter Tight', sans-serif",
        "headline_weight": 700,
        "role": "High-Density Card Titles & Filter Bars",
        "pairing": "Inter Regular (400) + Unbounded",
        "desc": "Tighter tracking and narrower proportions than standard Inter, optimized for dense editorial grids, lookbook captioning, and luxury e-commerce navigation."
    },
    {
        "num": "09",
        "name": "Cabinet Grotesk",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Wide Quirky Brutalist Grotesque",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'Cabinet Grotesk', sans-serif",
        "headline_weight": 800,
        "role": "Capsule Badges, Drop Teasers & Labels",
        "pairing": "Instrument Sans (400) + Space Mono",
        "desc": "Post-modern grotesque with flared terminals, eccentric curves, and heavyweight impact. A staple of avant-garde graphic posters and Pinterest pins."
    },
    {
        "num": "10",
        "name": "Space Grotesk",
        "foundry": "Google Fonts (Florian Karsten)",
        "category": "Proportional Tech Grotesque",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Space Grotesk', sans-serif",
        "headline_weight": 700,
        "role": "Garment Detail Accents & Drop Highlights",
        "pairing": "Neue Haas Grotesk + Space Mono",
        "desc": "Proportional version of Space Mono. Idiosyncratic deep horizontal cuts and mechanical angles, ideal for high-tech streetwear drops."
    },
    {
        "num": "11",
        "name": "Suisse Int'l",
        "foundry": "Swiss Typefaces",
        "category": "Ultra-Pure Swiss Rationalist",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Suisse Int\\'l', 'Switzer', sans-serif",
        "headline_weight": 700,
        "role": "Global Editorial Masthead & Lookbook Spread",
        "pairing": "Suisse Int'l Mono / Space Mono",
        "desc": "The gold standard of minimalist graphic studios across Zurich, Paris, and Tokyo. Stark, utilitarian, and razor-sharp without distraction."
    },
    {
        "num": "12",
        "name": "Neue Haas Unica",
        "foundry": "Monotype / Team '77",
        "category": "Hybrid Grotesque-Neo",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Neue Haas Unica', 'Plus Jakarta Sans', sans-serif",
        "headline_weight": 700,
        "role": "'About UNTLD' Brand Manifesto Prose",
        "pairing": "Integral CF / Unbounded (900)",
        "desc": "The legendary 1980 hybrid of Helvetica, Univers, and Akzidenz-Grotesk. Softer curves and wider apertures give it natural readability and understated poise."
    },
    {
        "num": "13",
        "name": "FK Grotesk",
        "foundry": "Florian Karsten",
        "category": "Tactile Modernist Grotesque",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'FK Grotesk', 'Space Grotesk', sans-serif",
        "headline_weight": 700,
        "role": "Product Spec Drawer & Fabric Breakdown",
        "pairing": "Neue Haas Grotesk + DM Mono",
        "desc": "Engineered with subtle ink traps and robust stroke consistency. Bridges Swiss discipline with technical streetwear engineering."
    },
    {
        "num": "14",
        "name": "ABC Whyte",
        "foundry": "Dinamo (Johannes Breyer & Fabian Harb)",
        "category": "Smooth Swiss Grotesque",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'ABC Whyte', 'Plus Jakarta Sans', sans-serif",
        "headline_weight": 700,
        "role": "Micro-Copy, SKU Tags & Breadcrumbs",
        "pairing": "ABC Whyte Inktrap / Clash Display",
        "desc": "Smooth, warm grotesque with intentional curved transitions. Highly versatile, widely used in Balenciaga and Highsnobiety campaign collateral."
    },
    {
        "num": "15",
        "name": "Basis Grotesk",
        "foundry": "Colophon Foundry",
        "category": "Raw Utilitarian Grotesque",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Basis Grotesk', 'Switzer', sans-serif",
        "headline_weight": 700,
        "role": "SKU Badges, Product Codes & Card Prices",
        "pairing": "Instrument Serif (Italic) + Inter",
        "desc": "Based on early grotesque models, stripped of decoration. Honest, disciplined, and raw, creating an authentic industrial streetwear identity."
    },
    {
        "num": "16",
        "name": "Plus Jakarta Sans",
        "foundry": "Google Fonts (Tokotype)",
        "category": "Geometric Modernist Sans",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Plus Jakarta Sans', sans-serif",
        "headline_weight": 700,
        "role": "Mobile Navigation Drawer & Checkout UI",
        "pairing": "Anton + JetBrains Mono",
        "desc": "Modern geometric neo-grotesque with clean Swiss modernist rhythm and contemporary warmth. Stellar high-resolution legibility."
    },
    {
        "num": "17",
        "name": "Instrument Sans",
        "foundry": "Google Fonts (Instrument)",
        "category": "Refined Screen Grotesque",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Instrument Sans', sans-serif",
        "headline_weight": 600,
        "role": "Size Filter Pills (XS, S, M, L, XL)",
        "pairing": "Instrument Serif (Italic)",
        "desc": "Inspired by Christian Schwartz's neo-grotesque tradition, engineered specifically for contemporary screens. Highly disciplined vertical terminal cuts."
    },
    {
        "num": "18",
        "name": "Geist Sans",
        "foundry": "Vercel & Basement Studio",
        "category": "Ultra-Precise Developer Grotesque",
        "license": "100% Free Open Source (Geist)",
        "license_type": "free",
        "css_font": "'Geist Sans', -apple-system, sans-serif",
        "headline_weight": 700,
        "role": "Garment Technical Spec Sheets & GSM Tags",
        "pairing": "Geist Mono (400) + Unbounded",
        "desc": "The modern benchmark of geometric Swiss precision. Razor-sharp micro-details, tabular alignment, vertical terminal cuts, zero ornamentation."
    },
    {
        "num": "19",
        "name": "PP Telegraf",
        "foundry": "Pangram Pangram Foundry",
        "category": "Clipped Angle Grotesque",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Telegraf', 'Space Grotesk', sans-serif",
        "headline_weight": 700,
        "role": "Capsule Teasers & Lookbook Slide Counters",
        "pairing": "General Sans + Space Mono",
        "desc": "Characterized by distinctive clipped internal angles, bridging brutalist telegraphic communication with high-end Swiss geometry."
    },
    {
        "num": "20",
        "name": "Univers Next",
        "foundry": "Linotype (Adrian Frutiger)",
        "category": "Rationalist Swiss System",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Univers Next', 'Switzer', sans-serif",
        "headline_weight": 700,
        "role": "Drop Category Tabs ('VAULT', 'CORE')",
        "pairing": "Syne (800) + DM Mono",
        "desc": "The archetype of 1957 rationalist Swiss design. Strictly uniform and architectural, providing an unemotional, ultra-disciplined high-fashion canvas."
    },

    # Category 2: Extended Geometric & Brutalist Display (21-35)
    {
        "num": "21",
        "name": "Druk Wide",
        "foundry": "Commercial Type (Berton Hasebe)",
        "category": "Ultra-Wide Heavyweight Display",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Druk Wide', 'Unbounded', sans-serif",
        "headline_weight": 900,
        "role": "Hero Drop Banners & Giant Billboards",
        "pairing": "Neue Haas Grotesk + Space Mono",
        "desc": "Monumental extended letterforms engineered for extreme horizontal scale. The definitive luxury streetwear headline font across Pinterest boards."
    },
    {
        "num": "22",
        "name": "Monument Extended",
        "foundry": "Pangram Pangram (Mat Desjardins)",
        "category": "Extended Monumental Sans",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'Monument Extended', 'Panchang', sans-serif",
        "headline_weight": 800,
        "role": "Sticky Top Navigation Brand Wordmark",
        "pairing": "Switzer (500) + Geist Mono",
        "desc": "Radical horizontal expansion with sharp geometric corners. Unmistakable streetwear authority and architectural presence."
    },
    {
        "num": "23",
        "name": "PP Formula",
        "foundry": "Pangram Pangram Foundry",
        "category": "Modular Variable Grotesque",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Formula', 'Clash Display', sans-serif",
        "headline_weight": 800,
        "role": "Watermark Backgrounds & Sub-Collection Badges",
        "pairing": "Satoshi (400) + Söhne Buch",
        "desc": "Massive width-spectrum font inspired by vintage racing and industrial packaging. Squarish circular counters and monumental impact."
    },
    {
        "num": "24",
        "name": "Unbounded",
        "foundry": "Google Fonts (NaN Foundry)",
        "category": "Ultra-Black Geometric Extended",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Unbounded', sans-serif",
        "headline_weight": 900,
        "role": "Current Approved UNTLD Hero Title Face",
        "pairing": "General Sans (400) + Inter",
        "desc": "Generous horizontal expansion, sharp mechanical joints, tight tracking. The exact typeface powering UNTLD's 'THE DENIM VAULT' hero title."
    },
    {
        "num": "25",
        "name": "Clash Display",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Brutalist Geometric Display",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'Clash Display', sans-serif",
        "headline_weight": 700,
        "role": "Lookbook Video Statement Titles",
        "pairing": "Cabinet Grotesk + Satoshi",
        "desc": "Brutalist high-contrast display face with narrow apertures and surprising sharp geometric quirks. Commands immediate attention."
    },
    {
        "num": "26",
        "name": "Integral CF",
        "foundry": "Connary Fagen",
        "category": "Extra-Bold Monumental Titling",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Integral CF', 'Panchang', sans-serif",
        "headline_weight": 800,
        "role": "Full-Screen Drop Reveal & Master Callouts",
        "pairing": "Space Grotesk + Inter",
        "desc": "Aggressive, heavyweight, unapologetic titling face. Pure structural mass and industrial confidence."
    },
    {
        "num": "27",
        "name": "Akira Expanded",
        "foundry": "Twicolabs Font Foundry",
        "category": "Extended Brutalist Display",
        "license": "Free Demo / Commercial",
        "license_type": "commercial",
        "css_font": "'Akira Expanded', 'Panchang', sans-serif",
        "headline_weight": 800,
        "role": "Archival Capsule Release IDs ('LOT 001')",
        "pairing": "Neue Haas Grotesk + Switzer",
        "desc": "Bold geometric expanded block font with stark horizontal momentum. Very popular in underground streetwear and Japanese lookbooks."
    },
    {
        "num": "28",
        "name": "Thunder",
        "foundry": "Rajesh Rajput",
        "category": "Ultra-Condensed Brutalist Display",
        "license": "100% Free Commercial",
        "license_type": "free",
        "css_font": "'Thunder', 'Anton', sans-serif",
        "headline_weight": 800,
        "role": "Vertical Lookbook Tickers & Side Marquees",
        "pairing": "Unbounded + Panchang",
        "desc": "Towering vertical proportions with razor-sharp compressed width. Creates massive visual height without consuming horizontal real estate."
    },
    {
        "num": "29",
        "name": "PP Pangram Sans",
        "foundry": "Pangram Pangram Foundry",
        "category": "Extended Geometric Sans",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Pangram Sans', 'Switzer', sans-serif",
        "headline_weight": 800,
        "role": "Main Brand Lockup & Cart Summary Header",
        "pairing": "PP Neue Montreal + Inter",
        "desc": "Geometric sans with extended widths, circular geometry, and authoritative street-luxury stance."
    },
    {
        "num": "30",
        "name": "Syne (800 Extra Bold)",
        "foundry": "Google Fonts (Bonjour Monde)",
        "category": "Sculptural Avant-Garde Sans",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Syne', sans-serif",
        "headline_weight": 800,
        "role": "Seasonal Campaign Narrative Headlines",
        "pairing": "Syne Regular (400) + Space Grotesk",
        "desc": "Sculptural geometric letterforms with unexpected character. Designed originally for French art centers, widely adopted by avant-garde luxury fashion."
    },
    {
        "num": "31",
        "name": "Bebas Neue Pro",
        "foundry": "Dharma Type (Ryoichi Tsunekawa)",
        "category": "Extended & Condensed System",
        "license": "Commercial (Std free on Google)",
        "license_type": "commercial",
        "css_font": "'Bebas Neue', sans-serif",
        "headline_weight": 700,
        "role": "Fit Matrix ('OVERSIZED SILHOUETTE GUIDE')",
        "pairing": "Forma DJR Text + Inter Tight",
        "desc": "The Pro version adds expanded horizontal cuts that transform the traditional poster font into a high-end architectural identity face."
    },
    {
        "num": "32",
        "name": "Panchang",
        "foundry": "Fontshare / Indian Type Foundry",
        "category": "Ultra-Wide Extended Brutalist",
        "license": "100% Free Commercial (Fontshare)",
        "license_type": "free",
        "css_font": "'Panchang', sans-serif",
        "headline_weight": 800,
        "role": "Extended Slogans & Category Banners",
        "pairing": "General Sans (400) + Satoshi",
        "desc": "Pure ultra-wide geometric brutalism. Indian Type Foundry origin gives it authentic cultural resonance with UNTLD's Mumbai luxury identity."
    },
    {
        "num": "33",
        "name": "Right Grotesk",
        "foundry": "Pangram Pangram (Alex Slobzheninov)",
        "category": "Inktrap Brutalist Display",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'Right Grotesk', 'Clash Display', sans-serif",
        "headline_weight": 800,
        "role": "Limited Drop Release Tags ('SOLD OUT')",
        "pairing": "Switzer + Inter",
        "desc": "Brutalist post-modern grotesk with deep angular inktraps and gouges. Extreme favorite across Pinterest graphic design moodboards."
    },
    {
        "num": "34",
        "name": "Eurostile Bold Extended",
        "foundry": "Linotype (Aldo Novarese, 1962)",
        "category": "Mid-Century Technical Squircle",
        "license": "Commercial (Adobe Fonts)",
        "license_type": "commercial",
        "css_font": "'Eurostile', 'Michroma', sans-serif",
        "headline_weight": 700,
        "role": "Heavyweight Outerwear Titles & GPS Coordinates",
        "pairing": "Neue Haas Grotesk + Inter",
        "desc": "The undisputed godfather of mid-century technical brutalism and luxury streetwear (Helmut Lang, Undercover). Distinctive squircle letterforms."
    },
    {
        "num": "35",
        "name": "Anton",
        "foundry": "Google Fonts (Vernon Adams)",
        "category": "Heavyweight Compressed Display",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Anton', sans-serif",
        "headline_weight": 400,
        "role": "Marquee Scrolling Ticker Ribbons",
        "pairing": "Neue Haas Grotesk + General Sans",
        "desc": "Reworked advertising grotesk with geometric proportions, tight apertures, and crushing visual weight. Used live on bluorng.com."
    },

    # Category 3: High-Fashion Editorial Serifs & Technical Monospace (36-50)
    {
        "num": "36",
        "name": "PP Editorial New",
        "foundry": "Pangram Pangram Foundry",
        "category": "High-Fashion Editorial Serif",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Editorial New', 'Instrument Serif', serif",
        "headline_weight": 400,
        "is_italic": True,
        "role": "Lookbook Quotes & Capsule Narratives",
        "pairing": "Neue Haas Grotesk + Inter",
        "desc": "The gold standard of contemporary luxury fashion typography on Pinterest. Narrow proportions, ultra-high contrast hairlines, dramatic italics."
    },
    {
        "num": "37",
        "name": "Instrument Serif",
        "foundry": "Google Fonts (Instrument)",
        "category": "Transitional Display Serif",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Instrument Serif', serif",
        "headline_weight": 400,
        "is_italic": True,
        "role": "Italic Capsule Subtitles & Photo Captions",
        "pairing": "Satoshi + Inter Tight",
        "desc": "Razor-sharp open-source transitional display serif with slender stems, sharp flat bracketed serifs, and graceful italic swashes."
    },
    {
        "num": "38",
        "name": "Ogg",
        "foundry": "Sharp Type (Lucas Sharp)",
        "category": "Calligraphic Roman Serif",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Ogg', 'Cormorant Garamond', serif",
        "headline_weight": 600,
        "role": "Isolated One-Word Accents & VIP Packaging",
        "pairing": "General Sans + Söhne",
        "desc": "Inspired by 20th-century book designer Oscar Ogg. Highly expressive calligraphic Roman serif with dramatic flourishing terminals."
    },
    {
        "num": "39",
        "name": "Cormorant Garamond",
        "foundry": "Google Fonts (Christian Thalmann)",
        "category": "High-Contrast Neoclassical Serif",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Cormorant Garamond', serif",
        "headline_weight": 600,
        "role": "Textile Origin Storytelling & Heritage Specs",
        "pairing": "Switzer + Neue Haas Grotesk",
        "desc": "High-contrast neoclassical distillation of Garamond. Whisper-thin hairlines, sculpted terminals, and royal verticality."
    },
    {
        "num": "40",
        "name": "Canela",
        "foundry": "Commercial Type (Miguel Reyes)",
        "category": "Flared Stone-Carved Display",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Canela', 'Cinzel', serif",
        "headline_weight": 600,
        "role": "Product Taxonomy Headers & High-Fashion Categories",
        "pairing": "Forma DJR + Inter Tight",
        "desc": "Neither pure serif nor pure sans. Flare-ended display face inspired by hand-carved stone inscriptions. Used by Bottega Veneta and Gentle Monster."
    },
    {
        "num": "41",
        "name": "Reckless Neue",
        "foundry": "Displaay Type Foundry",
        "category": "Renaissance Brutalist Serif",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Reckless Neue', 'Instrument Serif', serif",
        "headline_weight": 500,
        "role": "Capsule Manifesto Copy & Numbering",
        "pairing": "PP Neue Montreal + Space Grotesk",
        "desc": "Renaissance-rooted elegance colliding with Prague typographic brutalism. High x-height, blade-cut serifs, dramatic vertical stress."
    },
    {
        "num": "42",
        "name": "Playfair Display",
        "foundry": "Google Fonts (Claus Eggers Sørensen)",
        "category": "Transitional Editorial Serif",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Playfair Display', serif",
        "headline_weight": 700,
        "role": "Press Quotes & Private Salon Releases",
        "pairing": "Inter + Cabinet Grotesk",
        "desc": "Influenced by John Baskerville and Scotch Roman typefaces. High contrast, sharp serifs, and timeless editorial pedigree."
    },
    {
        "num": "43",
        "name": "GT Super",
        "foundry": "Grilli Type (Noël Leu)",
        "category": "1970s High-Drama Serif",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'GT Super', 'Playfair Display', serif",
        "headline_weight": 700,
        "role": "Video Headline Overlays & Date Stamps",
        "pairing": "Unbounded + Söhne",
        "desc": "Draws inspiration from display serifs of the 1970s and 80s (Trooper, Manhattan). Expressive, muscular, high-fashion personality."
    },
    {
        "num": "44",
        "name": "Space Mono",
        "foundry": "Google Fonts (Colophon Foundry)",
        "category": "Retro-Futuristic Monospace",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'Space Mono', monospace",
        "headline_weight": 700,
        "role": "Technical Denim Specs ('14.5 OZ SELVEDGE')",
        "pairing": "Unbounded + Neue Haas Grotesk",
        "desc": "Fixed-width geometric typeface designed for science fiction and technical literature. Perfect for garment weight badges and atelier coordinates."
    },
    {
        "num": "45",
        "name": "JetBrains Mono",
        "foundry": "Google Fonts (JetBrains)",
        "category": "Engineered Code Monospace",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'JetBrains Mono', monospace",
        "headline_weight": 600,
        "role": "Garment Measurement Tables & SKU Matrix",
        "pairing": "Inter + PP Neue Montreal",
        "desc": "Engineered for maximum optical clarity at micro sizes. Crisp pixel-level legibility, clear character distinctions, and industrial authority."
    },
    {
        "num": "46",
        "name": "PP Neue Machina",
        "foundry": "Pangram Pangram Foundry",
        "category": "Mechanical Inktrap Monospace",
        "license": "Commercial (Free demo)",
        "license_type": "commercial",
        "css_font": "'PP Neue Machina', 'Space Mono', monospace",
        "headline_weight": 700,
        "role": "Drop Timers & Hardware Engravings",
        "pairing": "Syne + Neue Haas Grotesk",
        "desc": "A powerhouse display monospace with unapologetic deep square inktraps and brutalist mechanical curves. Seen across Acronym and Techwear moodboards."
    },
    {
        "num": "47",
        "name": "GT America Mono",
        "foundry": "Grilli Type (Noël Leu)",
        "category": "Swiss-American Gothic Mono",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'GT America Mono', 'DM Mono', monospace",
        "headline_weight": 600,
        "role": "Woven Neck Tags & Care Labels",
        "pairing": "GT America + Söhne",
        "desc": "Builds a bridge between American 19th-century gothics and Swiss neo-grotesques. Pragmatic, understated, and exceptionally balanced."
    },
    {
        "num": "48",
        "name": "Apercu Mono",
        "foundry": "Colophon Foundry",
        "category": "Bespoke Cultural Monospace",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Apercu Mono', 'Space Mono', monospace",
        "headline_weight": 500,
        "role": "Authenticity Cards & Order Seals",
        "pairing": "Apercu + General Sans",
        "desc": "Conceived as an amalgam of Johnston, Gill Sans, and Neuzeit. Charming humanist nuances inside a disciplined fixed-pitch system."
    },
    {
        "num": "49",
        "name": "DM Mono",
        "foundry": "Google Fonts (Colophon)",
        "category": "Geometric Modernist Monospace",
        "license": "100% Free Open Source (Google)",
        "license_type": "free",
        "css_font": "'DM Mono', monospace",
        "headline_weight": 500,
        "role": "Fabric Composition Micro-Specs ('100% COTTON')",
        "pairing": "Switzer + Inter",
        "desc": "Geometric, low-contrast monospace designed for code and tabular listings. Minimalist, quiet, and razor-sharp."
    },
    {
        "num": "50",
        "name": "Pitch Sans",
        "foundry": "Klim Type Foundry (Kris Sowersby)",
        "category": "Typewriter Modernist Sans",
        "license": "Commercial",
        "license_type": "commercial",
        "css_font": "'Pitch Sans', 'Space Mono', monospace",
        "headline_weight": 600,
        "role": "Limited Edition Piece Numbering ('01/50')",
        "pairing": "Canela + Neue Haas Grotesk",
        "desc": "A tribute to the typewriter, modernized into a contemporary monospaced work of art. Refined proportions with mechanical charm."
    }
]

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>UNTLD — 50 Minimal Typography Fonts Specimen Book</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://api.fontshare.com">

  <!-- GOOGLE FONTS -->
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Cinzel:wght@600;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,700&family=DM+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600;700&family=Instrument+Serif:ital,wght@0,400;1,400&family=Inter+Tight:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Michroma&family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Syne:wght@600;700;800&family=Unbounded:wght@600;700;800;900&display=swap" rel="stylesheet">

  <!-- FONTSHARE CDN -->
  <link href="https://api.fontshare.com/v2/css?f[]=switzer@300,400,500,600,700,800,900&f[]=general-sans@400,500,600,700&f[]=satoshi@400,500,700,900&f[]=clash-display@500,600,700&f[]=panchang@600,700,800&f[]=cabinet-grotesk@500,700,800,900&display=swap" rel="stylesheet">

  <style>
    @page {
      size: A4 portrait;
      margin: 14mm 16mm 14mm 16mm;
      @bottom-right {
        content: counter(page);
        font-family: 'DM Mono', monospace;
        font-size: 9pt;
        color: #888888;
      }
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      background-color: #FFFFFF;
      color: #121212;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.45;
      font-size: 13px;
    }

    .page {
      width: 100%;
      max-width: 820px;
      margin: 0 auto 36px auto;
      padding: 24px;
      background: #FFFFFF;
    }

    @media print {
      body {
        background: #FFFFFF;
      }
      .page {
        margin: 0;
        padding: 0;
        max-width: 100%;
      }
      .page-break {
        page-break-before: always;
        break-before: page;
      }
      .no-break {
        page-break-inside: avoid;
        break-inside: avoid;
      }
    }

    /* COVER PAGE */
    .cover-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 20px;
      border-bottom: 2px solid #121212;
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #707070;
    }

    .cover-brand-pill {
      background: #121212;
      color: #FFFFFF;
      padding: 4px 10px;
      font-weight: 700;
      letter-spacing: 0.15em;
    }

    .cover-hero {
      padding: 60px 0 40px 0;
    }

    .cover-tag {
      font-family: 'DM Mono', monospace;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #8C887B;
      margin-bottom: 16px;
      display: block;
    }

    .cover-title {
      font-family: 'Unbounded', sans-serif;
      font-size: 42px;
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: -0.03em;
      text-transform: uppercase;
      color: #121212;
      margin-bottom: 20px;
    }

    .cover-subtitle {
      font-size: 18px;
      font-weight: 500;
      color: #555555;
      line-height: 1.4;
      max-width: 640px;
      margin-bottom: 32px;
    }

    .cover-meta-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      padding: 24px 0;
      border-top: 1px solid #E5E5E5;
      border-bottom: 1px solid #E5E5E5;
      margin-bottom: 40px;
    }

    .meta-item h4 {
      font-family: 'DM Mono', monospace;
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #888888;
      margin-bottom: 4px;
    }

    .meta-item p {
      font-size: 14px;
      font-weight: 600;
      color: #121212;
    }

    .cover-toc {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }

    .toc-card {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 20px;
      background: #F8F8F8;
      border-left: 3px solid #121212;
    }

    .toc-card h3 {
      font-size: 15px;
      font-weight: 700;
      color: #121212;
      margin-bottom: 2px;
    }

    .toc-card p {
      font-size: 12px;
      color: #707070;
    }

    .toc-count {
      font-family: 'DM Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: #121212;
    }

    /* SECTION HEADER */
    .section-banner {
      padding: 24px 0 16px 0;
      border-bottom: 2px solid #121212;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }

    .section-banner h2 {
      font-family: 'Unbounded', sans-serif;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
      text-transform: uppercase;
      color: #121212;
    }

    .section-banner span {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      color: #888888;
      letter-spacing: 0.1em;
    }

    /* SPECIMEN CARD */
    .specimen-card {
      padding: 20px 22px;
      background: #FFFFFF;
      border: 1px solid #E5E5E5;
      border-radius: 8px;
      margin-bottom: 18px;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid #F0F0F0;
    }

    .card-id-block {
      display: flex;
      align-items: baseline;
      gap: 10px;
    }

    .font-num {
      font-family: 'DM Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      color: #888888;
    }

    .font-name {
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: #121212;
    }

    .font-foundry {
      font-size: 11px;
      color: #888888;
      font-weight: 400;
    }

    .license-badge {
      font-family: 'DM Mono', monospace;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
    }

    .badge-free {
      background: #EBF8F2;
      color: #0E7044;
      border: 1px solid #C4EED9;
    }

    .badge-commercial {
      background: #F3F4F6;
      color: #4B5563;
      border: 1px solid #E5E7EB;
    }

    /* TYPOGRAPHIC SPECIMENS INSIDE CARD */
    .specimen-display {
      font-size: 32px;
      line-height: 1.1;
      letter-spacing: -0.02em;
      text-transform: uppercase;
      color: #121212;
      margin-bottom: 10px;
      overflow-wrap: break-word;
    }

    .specimen-sentence {
      font-size: 15px;
      line-height: 1.35;
      color: #262626;
      margin-bottom: 10px;
    }

    .specimen-charset {
      font-size: 11px;
      letter-spacing: 0.08em;
      color: #777777;
      line-height: 1.4;
      margin-bottom: 12px;
      padding: 8px 10px;
      background: #F9F9F9;
      border-radius: 4px;
    }

    /* CARD FOOTER META */
    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      border-top: 1px dashed #E5E5E5;
      font-size: 11px;
      color: #666666;
    }

    .footer-left {
      display: flex;
      gap: 16px;
    }

    .footer-tag {
      display: flex;
      gap: 4px;
    }

    .tag-label {
      font-family: 'DM Mono', monospace;
      color: #999999;
      text-transform: uppercase;
      font-size: 10px;
    }

    .tag-val {
      font-weight: 600;
      color: #121212;
    }

    /* END SUMMARY TABLE */
    .summary-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
      margin-top: 16px;
    }

    .summary-table th {
      background: #121212;
      color: #FFFFFF;
      font-family: 'DM Mono', monospace;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 8px 10px;
      text-align: left;
      font-size: 10px;
    }

    .summary-table td {
      padding: 7px 10px;
      border-bottom: 1px solid #EEEEEE;
    }

    .summary-table tr:nth-child(even) {
      background: #FAFAFA;
    }
  </style>
</head>
<body>

  <!-- ==================== COVER PAGE ==================== -->
  <div class="page">
    <div class="cover-header">
      <span class="cover-brand-pill">UNTLD ATELIER</span>
      <span>MUMBAI FLAGSHIP • ARCHIVE VOL. 2026</span>
      <span>EDITION: SPECIMEN 01</span>
    </div>

    <div class="cover-hero">
      <span class="cover-tag">PINTEREST MINIMAL TYPOGRAPHY COMPILATION</span>
      <h1 class="cover-title">50 Minimal Typography Fonts</h1>
      <p class="cover-subtitle">
        Curated specimen catalogue designed for UNTLD's luxury Mumbai streetwear aesthetic, high-contrast raw denim lookbooks, and clean Swiss architectural storefronts.
      </p>

      <div class="cover-meta-grid">
        <div class="meta-item">
          <h4>TOTAL TYPEFACES</h4>
          <p>50 Curated Fonts</p>
        </div>
        <div class="meta-item">
          <h4>OPEN SOURCE & FREE</h4>
          <p>27 Google / Fontshare Faces</p>
        </div>
        <div class="meta-item">
          <h4>COMMERCIAL LUXURY</h4>
          <p>23 Boutique Foundry Faces</p>
        </div>
      </div>

      <div class="cover-toc">
        <div class="toc-card">
          <div>
            <h3>Tier 1: Swiss Neo-Grotesque & Clean Geometric Sans</h3>
            <p>Clean base typography for navigation, product cards, pricing & editorial body</p>
          </div>
          <span class="toc-count">FONTS 01 — 20</span>
        </div>

        <div class="toc-card">
          <div>
            <h3>Tier 2: Extended Geometric & Brutalist Display</h3>
            <p>Monumental extended titling, hero banners, capsule IDs & marquee ribbons</p>
          </div>
          <span class="toc-count">FONTS 21 — 35</span>
        </div>

        <div class="toc-card">
          <div>
            <h3>Tier 3: High-Fashion Editorial Serifs & Technical Monospace</h3>
            <p>Lookbook pull quotes, raw denim fabric specs (GSM), coordinates & care tags</p>
          </div>
          <span class="toc-count">FONTS 36 — 50</span>
        </div>
      </div>
    </div>
  </div>

  <div class="page-break"></div>
"""

# Render fonts
current_category = ""
for idx, f in enumerate(fonts_data):
    cat = f["category"]
    cat_header = ""
    
    # Check if category banner needed
    if idx == 0:
        cat_header = """
  <div class="page">
    <div class="section-banner">
      <div>
        <span>CATEGORY 01</span>
        <h2>Swiss Neo-Grotesque & Clean Geometric Sans</h2>
      </div>
      <span>FONTS 01 — 20</span>
    </div>
"""
    elif idx == 20:
        cat_header = """
  </div>
  <div class="page-break"></div>
  <div class="page">
    <div class="section-banner">
      <div>
        <span>CATEGORY 02</span>
        <h2>Extended Geometric & Brutalist Display</h2>
      </div>
      <span>FONTS 21 — 35</span>
    </div>
"""
    elif idx == 35:
        cat_header = """
  </div>
  <div class="page-break"></div>
  <div class="page">
    <div class="section-banner">
      <div>
        <span>CATEGORY 03</span>
        <h2>High-Fashion Editorial Serifs & Technical Monospace</h2>
      </div>
      <span>FONTS 36 — 50</span>
    </div>
"""
    elif idx % 4 == 0:
        cat_header = """
  </div>
  <div class="page-break"></div>
  <div class="page">
"""

    italic_style = "font-style: italic;" if f.get("is_italic") else ""
    badge_cls = "badge-free" if f["license_type"] == "free" else "badge-commercial"

    card_html = f"""
    <!-- FONT {f['num']}: {f['name']} -->
    <div class="specimen-card no-break">
      <div class="card-top">
        <div class="card-id-block">
          <span class="font-num">[{f['num']}]</span>
          <span class="font-name">{f['name']}</span>
          <span class="font-foundry">{f['foundry']}</span>
        </div>
        <span class="license-badge {badge_cls}">{f['license']}</span>
      </div>

      <div class="specimen-display" style="font-family: {f['css_font']}; font-weight: {f['headline_weight']}; {italic_style}">
        THE DENIM VAULT®
      </div>

      <div class="specimen-sentence" style="font-family: {f['css_font']}; font-weight: 500; {italic_style}">
        Raw denim. Uncompromised fit. Built for the streets of Mumbai.
      </div>

      <div class="specimen-charset" style="font-family: {f['css_font']}; {italic_style}">
        ABCDEFGHIJKLMNOPQRSTUVWXYZ • abcdefghijklmnopqrstuvwxyz • 0123456789 • 14.5 OZ
      </div>

      <div class="card-footer">
        <div class="footer-left">
          <div class="footer-tag">
            <span class="tag-label">Role:</span>
            <span class="tag-val">{f['role']}</span>
          </div>
          <div class="footer-tag">
            <span class="tag-label">Pair With:</span>
            <span class="tag-val">{f['pairing']}</span>
          </div>
        </div>
        <div class="footer-tag">
          <span class="tag-label">Type:</span>
          <span class="tag-val">{f['category']}</span>
        </div>
      </div>
    </div>
"""
    html += cat_header + card_html

html += """
  </div>
  <div class="page-break"></div>

  <!-- ==================== RECOMMENDATIONS & CDN GUIDE ==================== -->
  <div class="page">
    <div class="section-banner">
      <div>
        <span>DEPLOYMENT GUIDE</span>
        <h2>Top 5 Recommended UNTLD Pairing Stacks</h2>
      </div>
      <span>100% READY FOR WEB</span>
    </div>

    <div style="margin-bottom: 24px;">
      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px;">1. The Raw Denim Blueprint (High-Contrast Utility)</h3>
      <p style="color: #555555; margin-bottom: 8px;">Unbounded 900 (Display Hero) + Switzer 400/600 (Product Grid & Body) + Space Mono 400 (Fabric Specs) + Instrument Serif Italic (Subtitles).</p>
      
      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px; margin-top: 18px;">2. Contemporary Mumbai Luxury Streetwear</h3>
      <p style="color: #555555; margin-bottom: 8px;">PP Neue Montreal 600 / General Sans 600 (Nav & Wordmark) + General Sans 400 (Body) + Instrument Serif Italic (Pull Quotes) + JetBrains Mono 400 (SKU Badges).</p>

      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px; margin-top: 18px;">3. High-Energy Flash Drop (Brutalist Streetwear)</h3>
      <p style="color: #555555; margin-bottom: 8px;">Anton 400 (Marquee Ribbon) + Panchang 700 (Category Headers) + Satoshi 700 (Pill Buttons) + Space Mono 700 (Countdown Timers).</p>

      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px; margin-top: 18px;">4. Pure Swiss Architectural Minimalist</h3>
      <p style="color: #555555; margin-bottom: 8px;">Neue Haas Grotesk 700 / Söhne (Headers) + Inter Tight 600 (Secondary Headings) + Switzer 400 (Body) + DM Mono 400 (Tabular Data).</p>

      <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 8px; margin-top: 18px;">5. 100% Free Open-Source Commercial Stack</h3>
      <p style="color: #555555; margin-bottom: 8px;">Unbounded (Google) + Instrument Serif (Google) + Switzer / General Sans (Fontshare CDN) + Space Mono / JetBrains Mono (Google).</p>
    </div>

    <div style="background: #F8F8F8; border-left: 3px solid #121212; padding: 16px; border-radius: 4px; margin-top: 24px;">
      <h4 style="font-family: 'DM Mono', monospace; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #121212; margin-bottom: 6px;">Copy-Paste Quick Webfont CDN Tag:</h4>
      <p style="font-family: 'DM Mono', monospace; font-size: 10px; color: #555555; word-break: break-all; line-height: 1.5;">
        &lt;link href="https://fonts.googleapis.com/css2?family=Anton&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400..800&family=JetBrains+Mono:wght@400..700&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@700;800&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet"&gt;<br>
        &lt;link href="https://api.fontshare.com/v2/css?f[]=switzer@400,600,700,800&f[]=general-sans@400,600,700&f[]=satoshi@500,700&f[]=panchang@700,800&display=swap" rel="stylesheet"&gt;
      </p>
    </div>
  </div>

</body>
</html>
"""

with open('/Users/speedyzyzz/UNTLD/typography_specimens.html', 'w') as f:
    f.write(html)

print("Saved /Users/speedyzyzz/UNTLD/typography_specimens.html")
