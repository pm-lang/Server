import os

assets_dir = r"d:\Experiences\skillizee\creating an ad Activity\assets"
os.makedirs(assets_dir, exist_ok=True)

svgs = {
    "img_chocolate.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="chocBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#3D1E16" /><stop offset="100%" stop-color="#1B0A06" />
      </linearGradient>
      <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#683824" /><stop offset="100%" stop-color="#38180E" />
      </linearGradient>
      <linearGradient id="goldFoil" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFDF73" /><stop offset="50%" stop-color="#FFA800" /><stop offset="100%" stop-color="#D97706" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#chocBg)" />
    <circle cx="150" cy="90" r="70" fill="#FFA800" opacity="0.15" />
    <path d="M 70 120 L 120 40 L 230 75 L 180 155 Z" fill="url(#goldFoil)" />
    <g transform="rotate(-15 150 90)">
      <rect x="110" y="45" width="100" height="80" rx="6" fill="url(#barGrad)" stroke="#8B4513" stroke-width="2" />
      <rect x="118" y="53" width="40" height="30" rx="3" fill="#4A2518" stroke="#8B4513" />
      <rect x="164" y="53" width="40" height="30" rx="3" fill="#4A2518" stroke="#8B4513" />
      <rect x="118" y="88" width="40" height="30" rx="3" fill="#4A2518" stroke="#8B4513" />
      <rect x="164" y="88" width="40" height="30" rx="3" fill="#4A2518" stroke="#8B4513" />
    </g>
    <path d="M 40 140 Q 90 110 140 145 Q 200 120 260 140" stroke="#FFA800" stroke-width="2.5" fill="none" opacity="0.6" />
  </svg>""",

    "img_soft_drink.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="sodaBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#08203E" /><stop offset="100%" stop-color="#0A0F1D" />
      </linearGradient>
      <linearGradient id="canGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#E63D17" /><stop offset="50%" stop-color="#FF5A36" /><stop offset="100%" stop-color="#B91C1C" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#sodaBg)" />
    <circle cx="150" cy="90" r="65" fill="#2D68FF" opacity="0.2" />
    <g transform="rotate(12 150 90)">
      <rect x="120" y="40" width="60" height="100" rx="10" fill="url(#canGrad)" />
      <ellipse cx="150" cy="40" rx="30" ry="8" fill="#D1D5DB" />
      <ellipse cx="150" cy="140" rx="30" ry="8" fill="#9CA3AF" />
      <path d="M 130 65 Q 150 90 170 65" stroke="#FFF" stroke-width="4" fill="none" opacity="0.8" />
    </g>
    <rect x="75" y="105" width="28" height="28" rx="4" fill="rgba(255,255,255,0.25)" stroke="#93C5FD" stroke-width="1.5" transform="rotate(20 89 119)" />
    <rect x="195" y="55" width="24" height="24" rx="4" fill="rgba(255,255,255,0.25)" stroke="#93C5FD" stroke-width="1.5" transform="rotate(-15 207 67)" />
    <circle cx="100" cy="70" r="4" fill="#93C5FD" opacity="0.8" />
    <circle cx="210" cy="120" r="5" fill="#93C5FD" opacity="0.8" />
    <circle cx="130" cy="30" r="3" fill="#FFF" opacity="0.9" />
  </svg>""",

    "img_shampoo.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="shampBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#064E3B" /><stop offset="100%" stop-color="#0B1B15" />
      </linearGradient>
      <linearGradient id="bottleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#10B981" /><stop offset="50%" stop-color="#6EE7B7" /><stop offset="100%" stop-color="#047857" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#shampBg)" />
    <circle cx="150" cy="90" r="65" fill="#10B981" opacity="0.2" />
    <path d="M 40 30 Q 120 90 200 40 Q 260 70 280 150" stroke="#FBBF24" stroke-width="3" fill="none" opacity="0.4" />
    <rect x="130" y="50" width="40" height="95" rx="14" fill="url(#bottleGrad)" />
    <rect x="142" y="35" width="16" height="15" rx="3" fill="#D1D5DB" />
    <ellipse cx="150" cy="85" rx="12" ry="22" fill="#FFF" opacity="0.25" />
    <circle cx="110" cy="110" r="8" fill="rgba(255,255,255,0.3)" stroke="#A7F3D0" stroke-width="1.5" />
    <circle cx="185" cy="120" r="12" fill="rgba(255,255,255,0.3)" stroke="#A7F3D0" stroke-width="1.5" />
    <circle cx="190" cy="75" r="6" fill="rgba(255,255,255,0.3)" stroke="#A7F3D0" stroke-width="1" />
  </svg>""",

    "img_noodles.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="noodleBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#7C2D12" /><stop offset="100%" stop-color="#180A05" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#noodleBg)" />
    <circle cx="150" cy="100" r="60" fill="#FFA800" opacity="0.2" />
    <ellipse cx="150" cy="115" rx="65" ry="35" fill="#DC2626" />
    <ellipse cx="150" cy="110" rx="60" ry="30" fill="#FEF08A" />
    <path d="M 85 115 Q 150 165 215 115 Z" fill="#B91C1C" />
    <path d="M 105 105 Q 120 95 135 105 Q 150 115 165 105 Q 180 95 195 105" stroke="#F59E0B" stroke-width="4" fill="none" />
    <path d="M 115 115 Q 130 105 145 115 Q 160 125 175 115" stroke="#F59E0B" stroke-width="4" fill="none" />
    <line x1="110" y1="35" x2="195" y2="120" stroke="#78350F" stroke-width="4" stroke-linecap="round" />
    <line x1="130" y1="30" x2="205" y2="115" stroke="#78350F" stroke-width="4" stroke-linecap="round" />
    <path d="M 135 75 Q 130 55 140 40" stroke="rgba(255,255,255,0.6)" stroke-width="2.5" stroke-linecap="round" fill="none" />
    <path d="M 165 70 Q 170 50 160 35" stroke="rgba(255,255,255,0.6)" stroke-width="2.5" stroke-linecap="round" fill="none" />
  </svg>""",

    "img_phone.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="phoneBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1E1B4B" /><stop offset="100%" stop-color="#09081E" />
      </linearGradient>
      <linearGradient id="screenGlow" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#6366F1" /><stop offset="50%" stop-color="#EC4899" /><stop offset="100%" stop-color="#3B82F6" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#phoneBg)" />
    <circle cx="150" cy="90" r="65" fill="#6366F1" opacity="0.25" />
    <rect x="115" y="30" width="70" height="125" rx="14" fill="#1E293B" stroke="#64748B" stroke-width="3" />
    <rect x="120" y="36" width="60" height="113" rx="10" fill="url(#screenGlow)" />
    <rect x="138" y="40" width="24" height="8" rx="4" fill="#0F172A" />
    <circle cx="145" cy="44" r="2" fill="#10B981" />
    <circle cx="225" cy="70" r="20" stroke="#EC4899" stroke-width="1.5" fill="none" opacity="0.5" />
    <circle cx="75" cy="120" r="15" stroke="#3B82F6" stroke-width="1.5" fill="none" opacity="0.5" />
  </svg>""",

    "img_car.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="carBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#18181B" /><stop offset="100%" stop-color="#09090B" />
      </linearGradient>
      <linearGradient id="carBody" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#EF4444" /><stop offset="50%" stop-color="#F87171" /><stop offset="100%" stop-color="#991B1B" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#carBg)" />
    <line x1="20" y1="145" x2="280" y2="145" stroke="#FFA800" stroke-width="2" opacity="0.4" />
    <line x1="50" y1="155" x2="250" y2="155" stroke="#FF5A36" stroke-width="1.5" opacity="0.3" />
    <path d="M 60 125 L 80 95 Q 120 70 170 70 L 220 90 L 250 110 L 250 130 L 60 130 Z" fill="url(#carBody)" />
    <path d="M 105 95 L 135 76 L 175 76 L 195 95 Z" fill="#0F172A" />
    <path d="M 240 110 L 250 112" stroke="#FDE047" stroke-width="4" stroke-linecap="round" />
    <circle cx="95" cy="130" r="16" fill="#0F172A" stroke="#94A3B8" stroke-width="4" />
    <circle cx="215" cy="130" r="16" fill="#0F172A" stroke="#94A3B8" stroke-width="4" />
  </svg>""",

    "img_soap.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="soapBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0E7490" /><stop offset="100%" stop-color="#083344" />
      </linearGradient>
      <linearGradient id="barSoap" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#F0FDFA" /><stop offset="100%" stop-color="#CCFBF1" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#soapBg)" />
    <circle cx="150" cy="90" r="65" fill="#06B6D4" opacity="0.2" />
    <rect x="90" y="65" width="120" height="65" rx="22" fill="url(#barSoap)" stroke="#99F6E4" stroke-width="3" />
    <path d="M 120 95 Q 150 105 180 95" stroke="#5EEAD4" stroke-width="2.5" fill="none" />
    <circle cx="80" cy="60" r="12" fill="rgba(255,255,255,0.45)" stroke="#A5F3FC" stroke-width="1.5" />
    <circle cx="215" cy="55" r="16" fill="rgba(255,255,255,0.45)" stroke="#A5F3FC" stroke-width="1.5" />
    <circle cx="230" cy="90" r="9" fill="rgba(255,255,255,0.45)" stroke="#A5F3FC" stroke-width="1" />
    <circle cx="70" cy="100" r="7" fill="rgba(255,255,255,0.45)" stroke="#A5F3FC" stroke-width="1" />
  </svg>""",

    "img_cookies.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <defs>
      <linearGradient id="cookieBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#451A03" /><stop offset="100%" stop-color="#1C0B02" />
      </linearGradient>
      <linearGradient id="cookieGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#D97706" /><stop offset="100%" stop-color="#92400E" />
      </linearGradient>
    </defs>
    <rect width="300" height="180" fill="url(#cookieBg)" />
    <circle cx="150" cy="90" r="65" fill="#D97706" opacity="0.2" />
    <circle cx="140" cy="95" r="45" fill="url(#cookieGrad)" stroke="#78350F" stroke-width="2" />
    <circle cx="125" cy="75" r="6" fill="#291206" />
    <circle cx="155" cy="80" r="5" fill="#291206" />
    <circle cx="140" cy="105" r="6" fill="#291206" />
    <circle cx="120" cy="115" r="5" fill="#291206" />
    <circle cx="160" cy="115" r="5.5" fill="#291206" />
    <circle cx="210" cy="65" r="26" fill="url(#cookieGrad)" stroke="#78350F" stroke-width="1.5" />
    <circle cx="205" cy="58" r="3.5" fill="#291206" />
    <circle cx="220" cy="68" r="4" fill="#291206" />
    <circle cx="75" cy="70" r="5" fill="#FFF" opacity="0.8" />
    <circle cx="90" cy="120" r="3.5" fill="#FFF" opacity="0.8" />
  </svg>""",

    "img_jingle.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#1E1B4B" />
    <circle cx="150" cy="90" r="60" fill="#8B5CF6" opacity="0.3" />
    <circle cx="150" cy="90" r="40" fill="#0F172A" stroke="#A78BFA" stroke-width="3" />
    <circle cx="150" cy="90" r="12" fill="#EF4444" />
    <rect x="50" y="80" width="6" height="20" rx="3" fill="#C084FC" />
    <rect x="65" y="65" width="6" height="50" rx="3" fill="#C084FC" />
    <rect x="80" y="55" width="6" height="70" rx="3" fill="#C084FC" />
    <rect x="215" y="55" width="6" height="70" rx="3" fill="#C084FC" />
    <rect x="230" y="65" width="6" height="50" rx="3" fill="#C084FC" />
    <rect x="245" y="80" width="6" height="20" rx="3" fill="#C084FC" />
  </svg>""",

    "img_tagline.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#18181B" />
    <circle cx="150" cy="90" r="60" fill="#F59E0B" opacity="0.2" />
    <rect x="50" y="40" width="200" height="100" rx="16" fill="#27272A" stroke="#F59E0B" stroke-width="2.5" />
    <text x="150" y="98" fill="#FFF" font-family="sans-serif" font-weight="800" font-size="22" text-anchor="middle" letter-spacing="2">“JUST DO IT.”</text>
  </svg>""",

    "img_story.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#0F172A" />
    <circle cx="150" cy="90" r="60" fill="#3B82F6" opacity="0.25" />
    <rect x="70" y="45" width="160" height="90" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="2.5" />
    <polygon points="135,75 175,95 135,115" fill="#38BDF8" />
    <line x1="70" y1="65" x2="230" y2="65" stroke="#38BDF8" stroke-width="2" />
  </svg>""",

    "img_pen.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#1E1B4B" />
    <line x1="60" y1="140" x2="240" y2="40" stroke="#F59E0B" stroke-width="12" stroke-linecap="round" />
    <polygon points="240,40 260,30 250,55" fill="#FDE047" />
    <line x1="100" y1="118" x2="105" y2="115" stroke="#FFF" stroke-width="4" />
  </svg>""",

    "img_flask.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#064E3B" />
    <rect x="125" y="45" width="50" height="100" rx="14" fill="#10B981" stroke="#6EE7B7" stroke-width="3" />
    <rect x="137" y="30" width="26" height="15" rx="4" fill="#D1D5DB" />
    <line x1="137" y1="75" x2="163" y2="75" stroke="#065F46" stroke-width="3" />
  </svg>""",

    "img_notebook.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#451A03" />
    <rect x="95" y="35" width="110" height="115" rx="8" fill="#92400E" stroke="#F59E0B" stroke-width="3" />
    <line x1="115" y1="35" x2="115" y2="150" stroke="#78350F" stroke-width="4" />
    <line x1="130" y1="65" x2="180" y2="65" stroke="#FDE047" stroke-width="2.5" />
    <line x1="130" y1="85" x2="180" y2="85" stroke="#FDE047" stroke-width="2.5" />
  </svg>""",

    "img_brand_mcdonalds.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#DC2626" />
    <path d="M 105 135 C 105 70 135 60 150 100 C 165 60 195 70 195 135" stroke="#FBBF24" stroke-width="16" stroke-linecap="round" fill="none" />
  </svg>""",

    "img_brand_apple.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#0F172A" />
    <path d="M 150 145 C 120 145 110 110 110 90 C 110 65 130 55 145 55 C 158 55 168 62 175 62 C 182 62 195 55 205 55 C 215 55 230 60 235 75 C 215 85 215 115 235 125 C 225 145 210 145 200 145 C 190 145 180 138 175 138 C 170 138 160 145 150 145 Z" fill="#F8FAFC" />
    <path d="M 175 52 C 175 40 185 30 195 28 C 195 40 185 50 175 52 Z" fill="#F8FAFC" />
  </svg>""",

    "img_brand_coke.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#B91C1C" />
    <path d="M 30 120 Q 150 50 270 110" stroke="#FFF" stroke-width="8" fill="none" stroke-linecap="round" />
    <path d="M 40 135 Q 160 70 260 125" stroke="#FFF" stroke-width="3" fill="none" opacity="0.6" />
  </svg>""",

    "img_brand_adidas.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#18181B" />
    <polygon points="100,135 115,135 145,85 130,85" fill="#FFF" />
    <polygon points="135,135 150,135 180,60 165,60" fill="#FFF" />
    <polygon points="170,135 185,135 215,35 200,35" fill="#FFF" />
  </svg>""",

    "img_brand_nike.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#09090B" />
    <path d="M 60 95 Q 140 145 250 45 Q 150 120 90 90 Q 65 75 60 95 Z" fill="#F97316" />
  </svg>""",

    "img_brand_starbucks.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#064E3B" />
    <circle cx="150" cy="90" r="50" fill="none" stroke="#FFF" stroke-width="5" />
    <circle cx="150" cy="85" r="16" fill="#FFF" />
    <polygon points="142,65 150,55 158,65" fill="#FFF" />
    <path d="M 125 110 Q 150 130 175 110" stroke="#FFF" stroke-width="4" fill="none" />
  </svg>""",

    "img_water.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#0369A1" />
    <path d="M 150 35 C 130 75 110 95 110 120 C 110 145 128 160 150 160 C 172 160 190 145 190 120 C 190 95 170 75 150 35 Z" fill="#38BDF8" stroke="#E0F2FE" stroke-width="3" />
  </svg>""",

    "img_plastic.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#0F766E" />
    <circle cx="150" cy="90" r="45" fill="none" stroke="#2DD4BF" stroke-width="4" stroke-dasharray="10 5" />
    <path d="M 120 90 L 180 90" stroke="#F43F5E" stroke-width="6" stroke-linecap="round" />
    <path d="M 130 65 L 170 115" stroke="#F43F5E" stroke-width="5" stroke-linecap="round" />
  </svg>""",

    "img_designer.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#312E81" />
    <path d="M 70 130 Q 150 30 230 130" stroke="#EC4899" stroke-width="4" fill="none" />
    <circle cx="150" cy="80" r="8" fill="#F43F5E" />
    <line x1="120" y1="80" x2="180" y2="80" stroke="#60A5FA" stroke-width="2" />
  </svg>""",

    "img_copywriter.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#1C1917" />
    <rect x="70" y="45" width="160" height="90" rx="8" fill="#292524" stroke="#F59E0B" stroke-width="2" />
    <text x="150" y="98" fill="#FDE047" font-family="monospace" font-weight="700" font-size="20" text-anchor="middle">HELLO WORLD</text>
  </svg>""",

    "img_director.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#1E1B4B" />
    <rect x="80" y="55" width="100" height="70" rx="10" fill="#312E81" stroke="#818CF8" stroke-width="3" />
    <polygon points="190,70 230,55 230,125 190,110" fill="#818CF8" />
  </svg>""",

    "img_creative_dir.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="100%">
    <rect width="300" height="180" fill="#431407" />
    <circle cx="150" cy="85" r="30" fill="#F59E0B" opacity="0.4" />
    <path d="M 135 95 C 135 70 165 70 165 95 L 158 115 L 142 115 Z" fill="#FDE047" />
    <line x1="140" y1="122" x2="160" y2="122" stroke="#FFF" stroke-width="3" />
  </svg>"""
}

for fname, content in svgs.items():
    fpath = os.path.join(assets_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(svgs)} assets successfully.")
