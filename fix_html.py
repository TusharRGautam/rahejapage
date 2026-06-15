import re

html_content = """        <ol class="carousel-indicators">
            <li data-target="#home" data-slide-to="0" class="active"></li>
            <li data-target="#home" data-slide-to="1"></li>
            <li data-target="#home" data-slide-to="2"></li>
        </ol>
        
        <div class="carousel-inner blockimg" id="blockimg">
            <div class="carousel-item active">
                <div class="desktopview"> <img src="./assets/img/desk_ban_1.webp" alt="Raheja Prime Two World Trade Center Vashi NX" width="1920" height="900" class="d-block micro-main-slider-img" fetchpriority="high" decoding="async" /> </div>
                <div class="mobileview"> <img src="./assets/img/mob_ban_1.webp" alt="Raheja Prime Two World Trade Center Vashi NX" width="768" height="600" class="d-block micro-main-slider-img" fetchpriority="high" decoding="async" /> </div>
            </div>
            <div class="carousel-item">
                <div class="desktopview"> <img src="./assets/img/desk_ban_2.webp" alt="Raheja Prime Two Commercial Marvel" width="1920" height="900" class="d-block micro-main-slider-img" loading="lazy" decoding="async" /> </div>
                <div class="mobileview"> <img src="./assets/img/mob_ban_2.webp" alt="Raheja Prime Two Commercial Marvel" width="768" height="600" class="d-block micro-main-slider-img" loading="lazy" decoding="async" /> </div>
            </div>
            <div class="carousel-item">
                <div class="desktopview"> <img src="./assets/img/amenities/NEW.jpeg" alt="World Trade Center Navi Mumbai - Raheja Prime Two" width="1920" height="900" class="d-block micro-main-slider-img" loading="lazy" decoding="async" style="object-fit:cover;" /> </div>
                <div class="mobileview"> <img src="./assets/img/amenities/NEW.jpeg" alt="World Trade Center Navi Mumbai - Raheja Prime Two" width="768" height="600" class="d-block micro-main-slider-img" loading="lazy" decoding="async" style="object-fit:cover;" /> </div>
            </div>
        </div>
        <a class="carousel-control-prev" href="#home" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#home" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>

     <div class="info-box-wrapper">
         <div class="info-box-card">
            <div class="booking-open-badge">Booking Open: Limited Time Only</div>
            
            <h1 class="pro-title text-dark">Raheja Prime Two<br>World Trade Center</h1>
            
            <div class="pro-subtitle">
                At Juinagar By Raheja Universal<br>
                <img alt="Google Review" width="16" height="16" src="./assets/img/logo.png" style="vertical-align: middle; margin-right: 5px;">
                <span class="text-warning">★★★★<span style="display:inline-block; width:8px; overflow:hidden;">★</span></span>
                <span class="text-muted" style="font-size:12px;">4.6 Stars 75 Reviews</span>
            </div>
            
            <div class="property-grid bg-light">
                <div class="grid-row">
                    <span class="grid-label">Land Parcel</span>
                    <span class="grid-value">68 Acres</span>
                </div>
                <div class="grid-row">
                    <span class="grid-label">Floors</span>
                    <span class="grid-value">G + 39 Storeys</span>
                </div>
                <div class="grid-row">
                    <span class="grid-label">Possession</span>
                    <span class="grid-value">Dec 2026</span>
                </div>
            </div>
            
            <div class="offer-box">
                <div class="offer-bg-animation offer-inner">
                    Avail 25:25:20:20:10 Flexi Pay Plan<br>
                    Avail Spot Offer On Every Booking<br>
                    Book With Just ₹ 2 Lakhs*
                </div>
            </div>
            
            <div class="price-section">
                <div class="price-label">Luxurious <strong>Offices</strong> Starts At</div>
                <div class="price-amount text-dark">₹ 1.58 Cr <small>Onwards</small></div>
            </div>
            
            <button class="btn btn-info micro-form-btn enqModal effetMoveGradient w-100" data-form="lg" data-title="Download Brochure" data-btn="Download Now" data-enquiry="Download Brochure Left Panel" data-redirect="enquiry" data-toggle="modal" data-target="#enqModal">
                Download Brochure
            </button>
         </div>
     </div>

    <section class="section shadow-sm lazyload" id="overview">
    <h2 class="d-block section-heading color-primary text-capitalize">Welcome to Raheja Prime Two</h2>
    <p>
 Raheja Prime Two is Navi Mumbai's fastest-selling commercial marvel, situated in the iconic World Trade Center - Vashi NX. This striking 39-storey business landmark offers premium commercial units ranging from 526 CRPT to 3621 CRPT. The project is designed to give your business a global stature with a lavish 42-ft grand triple-height entrance lobby, outdoor restaurant, business lounge, and a modern gym & recreation hub. Experience work-life balance like never before with sports and leisure zones, including a net cricket zone, football turf, and games room.
</p>
<p><span class="more-cont" style="display: none;"><span class="d-block">
    Positioned in a highly strategic location, Raheja Prime Two offers unmatched location advantages. It is just an 8-minute walk from Juinagar Station, providing seamless connectivity to the rest of Navi Mumbai and Mumbai. The landmark business tower is surrounded by premium commercial developments, tech parks, financial institutions, and retail hotspots. Make the smartest move in Navi Mumbai's commercial landscape now and secure your space under our limited pre-launch offer.
</span></span> <a href="#!" class="btn btn-link btn-sm more">Read more</a></p>
    <button
        class="btn btn-info micro-form-btn effetMoveGradient enqModal download-brochure"
        data-form="md"
        data-title="Download Brochure"
        data-btn="Download Now"
        data-enquiry="Download Brochure Welcome Text"
        data-redirect="brochure"
        data-redirect-file="brochure.pdf"
        data-toggle="modal"
        data-target="#enqModal"
    >
<span class="d-inline-block mi mi-download mr-1 animated slideInDown infinite"></span> Download Brochure
    </button>
</section>

<section class="section shadow-sm lazyload" id="pricing">
            <span class="section-link"></span> 
 <h2 class="head text-capitalize">Raheja Prime Two Pricing and Carpet Area</h2>
	<div class="row">
		<div class="col-md-8">
			<table class="table table-striped table-borderless border micro-price-table table-pricing for-desktop">
				<thead>"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<ol class="carousel-indicators">.*?<thead>', re.DOTALL)
new_content = pattern.sub(html_content, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed HTML successfully!")
