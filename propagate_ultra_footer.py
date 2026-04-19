import os
import re

new_footer = """    <footer aria-label="Site Footer" class="relative pb-16 pt-8 overflow-hidden font-sans" id="footer" itemscope itemtype="https://schema.org/WPFooter">
        <!-- Main Footer Container (Rounded & Centered) -->
        <div class="max-w-[1250px] mx-auto px-6 sm:px-10 md:px-16 py-16 sm:py-20 bg-gradient-to-b from-[#0a0a0a] to-[#050505] rounded-[28px] relative overflow-hidden shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] border border-white/5">
            
            <!-- Glassmorphism & Aurora Glow Effects -->
            <div class="absolute inset-0 pointer-events-none">
                <!-- Top Aurora Streak -->
                <div class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-purple-500/40 to-transparent"></div>
                <!-- Star-like Particles (Using Radial Gradient Grid) -->
                <div class="absolute inset-0 opacity-[0.15]" style="background-image: radial-gradient(circle, white 0.5px, transparent 0.5px); background-size: 32px 32px;"></div>
                <!-- Colorful Aurora Glows -->
                <div class="absolute -top-24 -left-24 w-96 h-96 bg-purple-600/10 blur-[100px] rounded-full"></div>
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-blue-500/5 blur-[120px] rounded-full"></div>
                <div class="absolute -bottom-24 -right-24 w-96 h-96 bg-orange-500/5 blur-[100px] rounded-full"></div>
            </div>

            <div class="relative z-10">
                <!-- Main Grid: 5 Columns -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-12 lg:gap-8 mb-16">
                    
                    <!-- Column 1: Brand Section -->
                    <div class="flex flex-col gap-6 items-center lg:items-start text-center lg:text-left">
                        <a href="/" class="flex items-center gap-3 group">
                            <div class="w-10 h-10 bg-white rounded-lg flex items-center justify-center transform group-hover:rotate-6 transition-all duration-300 shadow-[0_0_15px_rgba(255,255,255,0.1)]">
                                <img src="/assets/img/logo.webp" alt="KAKOKI Logo" class="h-7 w-auto">
                            </div>
                            <span class="text-xl font-bold tracking-tight text-white uppercase italic">KAKOKI</span>
                        </a>
                        <p class="text-[#7a7a7a] text-sm leading-relaxed max-w-[240px]">
                            Architecting modern digital brands with precision and creative excellence.
                        </p>
                        <div class="flex gap-4 pt-2">
                            <a href="https://facebook.com/kakokicreative" class="w-9 h-9 rounded-full border border-white/10 flex items-center justify-center text-[#9a9a9a] hover:text-white hover:bg-white/5 hover:border-white/20 transition-all duration-300" aria-label="Facebook"><i class="fa-brands fa-facebook-f text-sm"></i></a>
                            <a href="https://github.com/farhanmubeenk" class="w-9 h-9 rounded-full border border-white/10 flex items-center justify-center text-[#9a9a9a] hover:text-white hover:bg-white/5 hover:border-white/20 transition-all duration-300" aria-label="GitHub"><i class="fa-brands fa-github text-sm"></i></a>
                            <a href="https://instagram.com/kakokicreative" class="w-9 h-9 rounded-full border border-white/10 flex items-center justify-center text-[#9a9a9a] hover:text-white hover:bg-white/5 hover:border-white/20 transition-all duration-300" aria-label="Instagram"><i class="fa-brands fa-instagram text-sm"></i></a>
                            <a href="https://linkedin.com/in/farhanmubeenk" class="w-9 h-9 rounded-full border border-white/10 flex items-center justify-center text-[#9a9a9a] hover:text-white hover:bg-white/5 hover:border-white/20 transition-all duration-300" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in text-sm"></i></a>
                        </div>
                    </div>

                    <!-- Column 2: Services -->
                    <div class="flex flex-col gap-6 items-center lg:items-start text-center lg:text-left">
                        <h4 class="text-[11px] font-bold text-[#cfcfcf] uppercase tracking-[0.2em]">Services</h4>
                        <nav class="flex flex-col gap-4">
                            <a href="/web-design-malappuram/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Web Design</a>
                            <a href="/branding-areekode/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Branding</a>
                            <a href="/creative-agency-kerala/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">UI/UX Design</a>
                            <a href="/gulf-nri-web-design/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">NRI Projects</a>
                        </nav>
                    </div>

                    <!-- Column 3: About -->
                    <div class="flex flex-col gap-6 items-center lg:items-start text-center lg:text-left">
                        <h4 class="text-[11px] font-bold text-[#cfcfcf] uppercase tracking-[0.2em]">About</h4>
                        <nav class="flex flex-col gap-4">
                            <a href="/farhan-mubeen/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Our Story</a>
                            <a href="/#team" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Team</a>
                            <a href="/contact/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Partners</a>
                            <a href="/sitemap.xml" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">FAQs</a>
                        </nav>
                    </div>

                    <!-- Column 4: Community -->
                    <div class="flex flex-col gap-6 items-center lg:items-start text-center lg:text-left">
                        <h4 class="text-[11px] font-bold text-[#cfcfcf] uppercase tracking-[0.2em]">Community</h4>
                        <nav class="flex flex-col gap-4">
                            <a href="/blog/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Blog</a>
                            <a href="/#portfolio" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Events</a>
                            <a href="/creative-agency-kerala/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Press</a>
                            <a href="/contact/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Forum</a>
                            <a href="/branding-areekode/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Merch Store</a>
                        </nav>
                    </div>

                    <!-- Column 5: Solutions -->
                    <div class="flex flex-col gap-6 items-center lg:items-start text-center lg:text-left">
                        <h4 class="text-[11px] font-bold text-[#cfcfcf] uppercase tracking-[0.2em]">Solutions</h4>
                        <nav class="flex flex-col gap-4">
                            <a href="/contact/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Pricing</a>
                            <a href="/contact/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Contact Sales</a>
                            <a href="/contact/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Help & Support</a>
                            <a href="/farhan-mubeen/" class="text-[#9a9a9a] hover:text-white text-sm transition-colors duration-300">Invest</a>
                        </nav>
                    </div>
                </div>

                <!-- Bottom Section: Centered Copyright -->
                <div class="pt-10 border-t border-white/5 flex flex-col items-center gap-4">
                    <p class="text-[10px] font-medium text-[#7a7a7a] uppercase tracking-[0.4em] text-center">
                        &copy; 2026 KAKOKI CREATIVE CO. ALL RIGHTS RESERVED.
                    </p>
                </div>
            </div>
        </div>
    </footer>"""

files = [
    "index.html",
    "web-design-tirur/index.html",
    "web-design-perinthalmanna/index.html",
    "web-design-manjeri/index.html",
    "web-design-malappuram/index.html",
    "web-design-kozhikode/index.html",
    "service-areas-malappuram/index.html",
    "gulf-nri-web-design/index.html",
    "contact/index.html",
    "creative-agency-kondotty/index.html",
    "farhan-mubeen/index.html",
    "branding-areekode/index.html",
    "blog/why-every-business-in-malappuram-needs-a-professional-website-2026/index.html",
    "blog/index.html",
    "areekode/index.html",
    "creative-agency-kerala/index.html"
]

for file_path in files:
    if not os.path.exists(file_path):
        continue
    
    content = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Match from <footer to </footer> including attributes and content
    # Using re.DOTALL to match across lines
    pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_footer, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find footer in {file_path}")
