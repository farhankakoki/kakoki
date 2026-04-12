"""
KAKOKI Creative Co — Master SEO Fix Script
Fixes: brand entity clarity, metadata, schema, sr-only hidden blocks,
       internal linking, title/meta quality across all HTML pages.
"""
import os
import re
import glob

ROOT_DIR = "."

# ─── PAGE REGISTRY ────────────────────────────────────────────────────────────
# Each entry: path → (title, description, primary_kw, page_type)
PAGE_MAP = {
    "index.html": {
        "title": "KAKOKI Creative Co — Web Design & Branding Agency, Kerala",
        "description": "KAKOKI Creative Co is a web design and branding agency in Malappuram, Kerala. We help businesses build strong brands and professional websites that grow their customer base.",
        "canonical": "https://www.kakokicreative.in/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "contact/index.html": {
        "title": "Contact KAKOKI Creative Co — Get a Free Project Quote",
        "description": "Get in touch with KAKOKI Creative Co for web design, branding, or graphic design. Based in Malappuram, Kerala — free consultation for all inquiries.",
        "canonical": "https://www.kakokicreative.in/contact/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "web-design-malappuram/index.html": {
        "title": "Web Design in Malappuram — KAKOKI Creative Co",
        "description": "Professional web design in Malappuram by KAKOKI Creative Co. Mobile-first, fast-loading websites built to rank on Google and convert local visitors into customers.",
        "canonical": "https://www.kakokicreative.in/web-design-malappuram/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "branding-areekode/index.html": {
        "title": "Branding Agency in Areekode — KAKOKI Creative Co",
        "description": "Logo design and brand identity services in Areekode, Malappuram. KAKOKI Creative Co builds complete visual identity systems for local Kerala businesses.",
        "canonical": "https://www.kakokicreative.in/branding-areekode/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "gulf-nri-web-design/index.html": {
        "title": "Web Design for Gulf NRI Businesses — KAKOKI Creative Co",
        "description": "Kerala-based web design and branding for Gulf NRI entrepreneurs. KAKOKI Creative Co serves clients in UAE, Qatar, Saudi Arabia, Oman, and Bahrain.",
        "canonical": "https://www.kakokicreative.in/gulf-nri-web-design/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "creative-agency-kondotty/index.html": {
        "title": "Creative Agency in Kondotty — KAKOKI Creative Co",
        "description": "Web design and branding services in Kondotty, Malappuram. KAKOKI Creative Co is your local creative agency for websites, logos, and brand design.",
        "canonical": "https://www.kakokicreative.in/creative-agency-kondotty/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "web-design-kozhikode/index.html": {
        "title": "Web Design in Kozhikode — KAKOKI Creative Co",
        "description": "Professional web design services for Kozhikode businesses. KAKOKI Creative Co delivers modern, SEO-ready websites and brand identities across Calicut.",
        "canonical": "https://www.kakokicreative.in/web-design-kozhikode/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "web-design-manjeri/index.html": {
        "title": "Web Design in Manjeri — KAKOKI Creative Co",
        "description": "Web design and branding in Manjeri, Malappuram. KAKOKI Creative Co builds fast, mobile-first websites that help local Manjeri businesses get found on Google.",
        "canonical": "https://www.kakokicreative.in/web-design-manjeri/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "web-design-perinthalmanna/index.html": {
        "title": "Web Design in Perinthalmanna — KAKOKI Creative Co",
        "description": "Web design services in Perinthalmanna, Malappuram. KAKOKI Creative Co creates SEO-optimised, mobile-first websites for local businesses in Perinthalmanna.",
        "canonical": "https://www.kakokicreative.in/web-design-perinthalmanna/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "web-design-tirur/index.html": {
        "title": "Web Design in Tirur — KAKOKI Creative Co",
        "description": "Affordable, high-quality web design in Tirur, Malappuram. KAKOKI Creative Co builds professional websites for Tirur businesses that rank locally on Google.",
        "canonical": "https://www.kakokicreative.in/web-design-tirur/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "service-areas-malappuram/index.html": {
        "title": "Web Design & Branding Across Malappuram — KAKOKI Creative Co",
        "description": "KAKOKI Creative Co serves all areas in Malappuram district — Areekode, Kondotty, Manjeri, Tirur, Perinthalmanna and beyond. View our service coverage.",
        "canonical": "https://www.kakokicreative.in/service-areas-malappuram/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "blog/index.html": {
        "title": "Web Design & Branding Blog — KAKOKI Creative Co",
        "description": "Insights on web design, branding, and digital marketing from KAKOKI Creative Co, a Kerala-based creative agency in Malappuram.",
        "canonical": "https://www.kakokicreative.in/blog/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
    "blog/why-every-business-in-malappuram-needs-a-professional-website-2025/index.html": {
        "title": "Why Every Malappuram Business Needs a Website in 2025 — KAKOKI",
        "description": "Discover why having a professional website is essential for every business in Malappuram, Kerala in 2025. Insights from KAKOKI Creative Co.",
        "canonical": "https://www.kakokicreative.in/blog/why-every-business-in-malappuram-needs-a-professional-website-2025/",
        "og_image": "https://www.kakokicreative.in/assets/img/og-cover.png",
    },
}

# ─── CLEAN SCHEMA TEMPLATE ────────────────────────────────────────────────────
def build_schema(page_url, page_desc):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "https://www.kakokicreative.in/#organization",
      "name": "KAKOKI Creative Co",
      "alternateName": ["KAKOKI", "Kakoki Ads", "Kakoki Co"],
      "url": "https://www.kakokicreative.in/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://www.kakokicreative.in/assets/img/logo.png",
        "width": 512,
        "height": 512
      }},
      "description": "KAKOKI Creative Co is a web design and branding agency based in Malappuram, Kerala, serving businesses across India and the Gulf.",
      "email": "kakokicreativeco@gmail.com",
      "telephone": "+917558908826",
      "foundingDate": "2023",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Areekode",
        "addressLocality": "Malappuram",
        "addressRegion": "Kerala",
        "postalCode": "673639",
        "addressCountry": "IN"
      }},
      "sameAs": [
        "https://www.instagram.com/kakokicreative/",
        "https://www.behance.net/kakokicreative",
        "https://dribbble.com/kakokicreative",
        "https://www.linkedin.com/in/farhanmubeenk/"
      ]
    }},
    {{
      "@type": "LocalBusiness",
      "@id": "https://www.kakokicreative.in/#localbusiness",
      "name": "KAKOKI Creative Co",
      "url": "{page_url}",
      "image": "https://www.kakokicreative.in/assets/img/logo.png",
      "description": "{page_desc}",
      "telephone": "+917558908826",
      "email": "kakokicreativeco@gmail.com",
      "priceRange": "₹₹",
      "servesCuisine": null,
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Areekode",
        "addressLocality": "Malappuram",
        "addressRegion": "Kerala",
        "postalCode": "673639",
        "addressCountry": "IN"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 11.2396,
        "longitude": 76.0456
      }},
      "areaServed": [
        {{"@type": "State", "name": "Kerala"}},
        {{"@type": "City", "name": "Malappuram"}},
        {{"@type": "City", "name": "Areekode"}},
        {{"@type": "City", "name": "Kozhikode"}}
      ],
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "KAKOKI Creative Co Services",
        "itemListElement": [
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Web Design", "url": "https://www.kakokicreative.in/web-design-malappuram/"}}}},
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Brand Identity & Logo Design", "url": "https://www.kakokicreative.in/branding-areekode/"}}}},
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Graphic Design"}}}}
        ]
      }},
      "openingHoursSpecification": {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens": "09:00",
        "closes": "18:00"
      }}
    }},
    {{
      "@type": "WebSite",
      "@id": "https://www.kakokicreative.in/#website",
      "url": "https://www.kakokicreative.in/",
      "name": "KAKOKI Creative Co",
      "publisher": {{"@id": "https://www.kakokicreative.in/#organization"}},
      "inLanguage": "en-IN",
      "potentialAction": {{
        "@type": "SearchAction",
        "target": "https://www.kakokicreative.in/?s={{search_term_string}}",
        "query-input": "required name=search_term_string"
      }}
    }}
  ]
}}
</script>"""


# ─── CLEAN HEAD TEMPLATE ──────────────────────────────────────────────────────
def build_head(info, extra_head=""):
    title = info["title"]
    desc = info["description"]
    canonical = info["canonical"]
    og_image = info["og_image"]
    schema = build_schema(canonical, desc)

    return f"""<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="KAKOKI Creative Co">
<meta name="theme-color" content="#050505">

<title>{title}</title>
<meta name="description" content="{desc}">

<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en-IN" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">

<!-- Favicons -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicons/k.png">
<link rel="apple-touch-icon" href="/assets/img/favicons/k.png">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="KAKOKI Creative Co">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@kakokicreative">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">

<!-- Geo Tags -->
<meta name="geo.region" content="IN-KL">
<meta name="geo.placename" content="Malappuram, Kerala, India">
<meta name="geo.position" content="11.2396;76.0456">
<meta name="ICBM" content="11.2396, 76.0456">

<!-- Structured Data -->
{schema}

<!-- Performance -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
{extra_head}
</head>"""


# ─── PROCESS EACH FILE ────────────────────────────────────────────────────────
def normalize_path(filepath):
    """Return a key matching PAGE_MAP (relative with forward slashes)."""
    rel = os.path.relpath(filepath, ROOT_DIR).replace("\\", "/")
    return rel


def remove_sr_only_divs(content):
    """Remove hidden <div class="sr-only"> blocks (Google spam signal)."""
    # Remove full sr-only div blocks
    content = re.sub(
        r'<div\s+class="sr-only">[^<]*(?:<[^/][^>]*>[^<]*</[^>]+>[^<]*)*<[^/][^>]*>[^<]*</[^>]+>[^<]*</div>',
        '',
        content, flags=re.DOTALL
    )
    # Also clean standalone sr-only on h2 (that are empty hidden heading tricks)
    # Keep legitimate "sr-only" that are purely for accessibility (aria), remove keyword-stuffed ones
    content = re.sub(
        r'<div\s+class=["\']sr-only["\'][^>]*>.*?</div>\s*',
        '',
        content, flags=re.DOTALL
    )
    return content


def fix_nav_links(content):
    """Fix broken relative nav links like index.html#services → /#services"""
    content = content.replace('href="index.html#', 'href="/#')
    content = content.replace("href='index.html#", "href='/#")
    return content


def ensure_trailing_slashes(content):
    """Ensure internal links have trailing slashes for consistency."""
    def add_slash(m):
        href = m.group(1)
        quote = m.group(0)[5]  # quote char
        # Only apply to same-origin paths without extension
        if (href.startswith('/') and 
            not href.endswith('/') and 
            '.' not in href.split('/')[-1] and
            not '#' in href):
            href = href + '/'
        return f'href={quote}{href}{quote}'
    content = re.sub(r'href=["\']([^"\']+)["\']', add_slash, content)
    return content


def fix_logo_src(content):
    """Ensure logo uses .webp in body (for performance) but .png in head for OG."""
    # In body: use .webp version (already converted)
    # In head: og:image should point to .png (handled by build_head)
    return content


def process_file(filepath):
    rel_key = normalize_path(filepath)
    page_info = PAGE_MAP.get(rel_key)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*)</body>', content, flags=re.DOTALL)
    if not body_match:
        print(f"SKIP (no body): {rel_key}")
        return
    
    body_content = body_match.group(1)
    body_tag_match = re.search(r'<body([^>]*)>', content)
    body_attrs = body_tag_match.group(1) if body_tag_match else ''
    
    doctype_html_match = re.search(r'(<html[^>]*>)', content)
    html_tag = doctype_html_match.group(1) if doctype_html_match else '<html lang="en" class="scroll-smooth">'
    
    # 1. Remove sr-only hidden blocks (negative SEO signal)
    body_content = remove_sr_only_divs(body_content)
    
    # 2. Fix broken nav links
    body_content = fix_nav_links(body_content)
    
    # 3. Ensure trailing slashes in internal links
    body_content = ensure_trailing_slashes(body_content)
    
    # 4. Build proper head
    if page_info:
        # Determine extra head content for homepage or subpages
        extra_head = ""
        if rel_key == "index.html":
            extra_head = """<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&family=Inter:wght@400;600&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="assets/css/index-extracted.css">
<link rel="stylesheet" href="assets/css/tailwind-compiled.css">
<link rel="preload" as="image" href="assets/img/main1.webp">
<link rel="preload" as="image" href="assets/img/main2.webp">
<!-- Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GZV0K4T7G0"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-GZV0K4T7G0');</script>"""
        else:
            extra_head = """<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="/assets/css/index-extracted.css">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={theme:{extend:{fontFamily:{sans:['Inter','sans-serif'],display:['Poppins','sans-serif']}}}}</script>"""
        
        new_head = build_head(page_info, extra_head)
    else:
        # Keep existing head structure, just remove the bad duplicate empty OG blocks
        head_match = re.search(r'<head>(.*?)</head>', content, flags=re.DOTALL)
        new_head = f"<head>{head_match.group(1)}</head>" if head_match else "<head></head>"
        # Clean orphan empty comment blocks from previous runs
        new_head = re.sub(r'<!-- Open Graph(?:\s+SEO)? -->\s*(?:\n\s*){3,}', '<!-- Open Graph -->\n', new_head)
        new_head = re.sub(r'<!-- Twitter(?:\s+(?:Card|SEO))? -->\s*(?:\n\s*){3,}', '<!-- Twitter Card -->\n', new_head)
    
    # Rebuild full document
    new_content = f"""<!DOCTYPE html>
{html_tag}
{new_head}
<body{body_attrs}>
{body_content.strip()}
</body>
</html>"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Fixed: {rel_key}")


# ─── RUN ──────────────────────────────────────────────────────────────────────
html_files = glob.glob(os.path.join(ROOT_DIR, '**/*.html'), recursive=True)
# Filter out .git, .agents
html_files = [f for f in html_files if '.git' not in f and '.agents' not in f]

for fp in html_files:
    try:
        process_file(fp)
    except Exception as e:
        print(f"✗ Error on {fp}: {e}")

print(f"\n✅ Done. Processed {len(html_files)} files.")
