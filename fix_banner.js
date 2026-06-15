const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the broken section: from the phone icon line that got corrupted to end of amenity-card CSS
// The file has the navbar phone icon line corrupted - it needs to be restored
// The problem: TargetContent was found inside the navbar phone button area

// Step 1: Fix the corrupted navbar section by finding the broken join and fixing it
// The line `<a href="tel:+912246180880" ...>` should be followed by phone icon, not style CSS
html = html.replace(
  /(<a href="tel:\+912246180880"[^>]+>)\s*\n\s*overflow: hidden;\s*\n\s*box-shadow: 0 4px 12px rgba\(0,0,0,0\.12\);\s*\n\s*background: #f0f0f0;\s*\n\s*\}\s*\n\s*\.amenity-card img \{[\s\S]*?@media \(max-width: 576px\) \{\s*\n\s*\.amenity-card img \{ height: 180px; \}\s*\n\s*\}\s*\n<\/style>/,
  `$1
                        <i class="fa-solid fa-phone mr-2 text-white"></i> +912246180880
                    </a>
                </div>
            </nav>
        </header>
<main class="pload">
    <style>
  .card-d-custom{ width: 95%; justify-content: center; text-align: center; margin: 0 auto 15px; }

  /* ===== Fix: hide mobileview on desktop by default ===== */
  .mobileview { display: none; }
  @media only screen and (max-width: 768px) {
    .mobileview { display: block; margin-top: 65px; }
    .desktopview { display: none; }
  }

  /* ===== Desktop Banner: show full image, no crop ===== */
  @media only screen and (min-width: 769px) {
    .desktopview { margin-top: 0 !important; }
    .banner-desktop-img {
      width: 100%;
      height: auto;
      max-height: 89vh;
      object-fit: contain;
      object-position: center;
      background: #000;
      display: block;
    }
    .micro-main-slider .carousel-item img.banner-desktop-img {
      height: auto !important;
    }
  }

  /* ===== Amenity Cards ===== */
  .amenity-card {
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    background: #f0f0f0;
  }
  .amenity-card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    object-position: center;
    display: block;
    transition: transform 0.3s ease;
  }
  .amenity-card:hover img {
    transform: scale(1.04);
  }
  .amenity-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.75));
    color: #fff;
    padding: 18px 14px 12px;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  @media (max-width: 576px) {
    .amenity-card img { height: 180px; }
  }
</style>`
);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Done. Characters written:', html.length);
