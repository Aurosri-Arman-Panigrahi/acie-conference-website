import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from PIL import Image

output_pdf = "public/assets/brochure/ACIE-2027-Brochure.pdf"
PAGE_WIDTH = 849.75
PAGE_HEIGHT = 612.0
PANEL_WIDTH = PAGE_WIDTH / 3.0  # 283.25

c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

# Helper to draw wrapped text
def draw_text_lines(canv, text_lines, x, y, font="Helvetica", size=9, leading=12, fill=colors.black, align="left", width=260):
    canv.setFont(font, size)
    canv.setFillColor(fill)
    cur_y = y
    for line in text_lines:
        if align == "center":
            canv.drawCentredString(x + width/2.0, cur_y, line)
        elif align == "right":
            canv.drawRightString(x + width, cur_y, line)
        else:
            canv.drawString(x, cur_y, line)
        cur_y -= leading
    return cur_y

# =========================================================================
# PAGE 1: OUTSIDE COVERS (Left: Submissions & QR; Middle: Heritage; Right: Front Cover)
# =========================================================================

# Background
c.setFillColor(colors.HexColor("#f8fafc"))
c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

# Vertical fold guidelines (subtle dashed)
c.setStrokeColor(colors.HexColor("#cbd5e1"))
c.setLineWidth(0.5)
c.setDash(3, 3)
c.line(PANEL_WIDTH, 0, PANEL_WIDTH, PAGE_HEIGHT)
c.line(PANEL_WIDTH * 2, 0, PANEL_WIDTH * 2, PAGE_HEIGHT)
c.setDash([])

# ----------------- PANEL 1 (x: 0 -> 283.25): SUBMISSIONS & PORTAL ACCESS -----------------
# Header banner
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(0, PAGE_HEIGHT - 60, PANEL_WIDTH, 60, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 13)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 38, "ONLINE ACCESS & SUBMISSIONS")

# QR 1: Website
c.setFont("Helvetica-Bold", 10)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 85, "Scan to Visit Official Website")
c.setFont("Helvetica", 8)
c.setFillColor(colors.HexColor("#475569"))
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 98, "https://acieopen.com/")

qr_site = "brochure_extracted_assets/p1_img11.png"
if os.path.exists(qr_site):
    c.drawImage(qr_site, PANEL_WIDTH/2.0 - 45, PAGE_HEIGHT - 195, width=90, height=90, preserveAspectRatio=True)

# QR 2: Registration & Payments
c.setFont("Helvetica-Bold", 10)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 225, "Online Registration & Payment")
c.setFont("Helvetica", 8)
c.setFillColor(colors.HexColor("#475569"))
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 238, "https://forms.gle/eFNAa3H4Qg13kfyn8")

qr_pay = "brochure_extracted_assets/p1_img13.png"
if os.path.exists(qr_pay):
    c.drawImage(qr_pay, PANEL_WIDTH/2.0 - 45, PAGE_HEIGHT - 335, width=90, height=90, preserveAspectRatio=True)

# CMT Paper Submission Box
c.setFillColor(colors.HexColor("#eff6ff"))
c.setStrokeColor(colors.HexColor("#bfdbfe"))
c.setLineWidth(1)
c.roundRect(15, PAGE_HEIGHT - 475, PANEL_WIDTH - 30, 115, 6, fill=1, stroke=1)

c.setFont("Helvetica-Bold", 11)
c.setFillColor(colors.HexColor("#1d4ed8"))
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 380, "Microsoft CMT Submission")

cmt_text = [
    "Authors are invited to submit their original,",
    "unpublished research manuscripts via the",
    "official Microsoft CMT portal:",
    "",
    "https://cmt3.research.microsoft.com/ACIE2027",
    "",
    "All submissions undergo rigorous double-blind",
    "peer review by leading international experts."
]
draw_text_lines(c, cmt_text, 22, PAGE_HEIGHT - 398, font="Helvetica", size=7.5, leading=10, fill=colors.HexColor("#1e293b"), align="center", width=PANEL_WIDTH-44)

# Publication Indexing Card at bottom
c.setFillColor(colors.HexColor("#f1f5f9"))
c.setStrokeColor(colors.HexColor("#cbd5e1"))
c.roundRect(15, 20, PANEL_WIDTH - 30, 95, 6, fill=1, stroke=1)
c.setFont("Helvetica-Bold", 9)
c.setFillColor(colors.HexColor("#0f172a"))
c.drawCentredString(PANEL_WIDTH/2.0, 95, "Indexed in ACIE Open Access Journal")
pub_text = [
    "All accepted and presented conference papers will be",
    "considered for publication in ACIE: Advances in",
    "Computing, Intelligence and Engineering.",
    "",
    "ISSN: 2583-9985 | Peer-Reviewed Open Access",
    "Visit: https://acieopen.com/"
]
draw_text_lines(c, pub_text, 20, 80, font="Helvetica", size=7, leading=9.5, fill=colors.HexColor("#334155"), align="center", width=PANEL_WIDTH-40)


# ----------------- PANEL 2 (x: 283.25 -> 566.5): EXPERIENCE ODISHA'S HERITAGE -----------------
# Header
c.setFillColor(colors.HexColor("#0f766e"))
c.rect(PANEL_WIDTH, PAGE_HEIGHT - 60, PANEL_WIDTH, 60, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 13)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 1.5, PAGE_HEIGHT - 38, "EXPERIENCE ODISHA'S HERITAGE")

# 4 Heritage Frames in 2x2 grid
card_w = 115
card_h = 105
x_col1 = PANEL_WIDTH + 18
x_col2 = PANEL_WIDTH + 145

# Item 1: Lingaraj Temple
c.setFillColor(colors.white)
c.setStrokeColor(colors.HexColor("#e2e8f0"))
c.roundRect(x_col1, PAGE_HEIGHT - 195, card_w, card_h, 4, fill=1, stroke=1)
img_ling = "brochure_extracted_assets/p1_img17.jpeg"
if os.path.exists(img_ling):
    c.drawImage(img_ling, x_col1 + 5, PAGE_HEIGHT - 170, width=card_w - 10, height=72, preserveAspectRatio=True)
c.setFont("Helvetica-Bold", 8)
c.setFillColor(colors.HexColor("#0f172a"))
c.drawCentredString(x_col1 + card_w/2.0, PAGE_HEIGHT - 182, "Lingaraj Temple")
c.setFont("Helvetica", 6.5)
c.setFillColor(colors.HexColor("#64748b"))
c.drawCentredString(x_col1 + card_w/2.0, PAGE_HEIGHT - 191, "11th-Century Kalinga Jewel")

# Item 2: Konark Sun Temple
c.roundRect(x_col2, PAGE_HEIGHT - 195, card_w, card_h, 4, fill=1, stroke=1)
img_kon = "brochure_extracted_assets/p1_img18.jpeg"
if os.path.exists(img_kon):
    c.drawImage(img_kon, x_col2 + 5, PAGE_HEIGHT - 170, width=card_w - 10, height=72, preserveAspectRatio=True)
c.setFont("Helvetica-Bold", 8)
c.setFillColor(colors.HexColor("#0f172a"))
c.drawCentredString(x_col2 + card_w/2.0, PAGE_HEIGHT - 182, "Konark Sun Temple")
c.setFont("Helvetica", 6.5)
c.setFillColor(colors.HexColor("#64748b"))
c.drawCentredString(x_col2 + card_w/2.0, PAGE_HEIGHT - 191, "13th-Century UNESCO Wonder")

# Item 3: Dhauli Shanti Stupa
c.roundRect(x_col1, PAGE_HEIGHT - 325, card_w, card_h, 4, fill=1, stroke=1)
img_dhau = "brochure_extracted_assets/p1_img16.png"
if os.path.exists(img_dhau):
    c.drawImage(img_dhau, x_col1 + 5, PAGE_HEIGHT - 300, width=card_w - 10, height=72, preserveAspectRatio=True)
c.setFont("Helvetica-Bold", 8)
c.setFillColor(colors.HexColor("#0f172a"))
c.drawCentredString(x_col1 + card_w/2.0, PAGE_HEIGHT - 312, "Dhauli Peace Pagoda")
c.setFont("Helvetica", 6.5)
c.setFillColor(colors.HexColor("#64748b"))
c.drawCentredString(x_col1 + card_w/2.0, PAGE_HEIGHT - 321, "Historic Emperor Ashoka Stupa")

# Item 4: Chilika Lake
c.roundRect(x_col2, PAGE_HEIGHT - 325, card_w, card_h, 4, fill=1, stroke=1)
img_chi = "brochure_extracted_assets/p1_img20.jpeg"
if os.path.exists(img_chi):
    c.drawImage(img_chi, x_col2 + 5, PAGE_HEIGHT - 300, width=card_w - 10, height=72, preserveAspectRatio=True)
c.setFont("Helvetica-Bold", 8)
c.setFillColor(colors.HexColor("#0f172a"))
c.drawCentredString(x_col2 + card_w/2.0, PAGE_HEIGHT - 312, "Chilika Lake")
c.setFont("Helvetica", 6.5)
c.setFillColor(colors.HexColor("#64748b"))
c.drawCentredString(x_col2 + card_w/2.0, PAGE_HEIGHT - 321, "Asia's Largest Brackish Lagoon")

# Tourism narrative
c.setFillColor(colors.HexColor("#ffffff"))
c.setStrokeColor(colors.HexColor("#cbd5e1"))
c.roundRect(PANEL_WIDTH + 15, 20, PANEL_WIDTH - 30, 240, 6, fill=1, stroke=1)

c.setFont("Helvetica-Bold", 10.5)
c.setFillColor(colors.HexColor("#0f766e"))
c.drawCentredString(PANEL_WIDTH * 1.5, 242, "Discover Temple City Bhubaneswar")

tour_lines = [
    "Odisha, the land of vibrant art, architecture, and rich",
    "spiritual traditions, warmly welcomes international delegates.",
    "",
    "• Bhubaneswar: Renowned as the 'Temple City' with over",
    "  500 historic temples exemplifying ancient Kalinga craft.",
    "• Golden Triangle: Seamless road connectivity to Puri",
    "  (Jagannath Temple) and Konark (Sun Chariot).",
    "• Nature & Wildlife: Nandankanan Zoological Park,",
    "  famous for its white tigers and safari reserves.",
    "• Connectivity: Biju Patnaik International Airport (BBI)",
    "  operates direct flights to Delhi, Mumbai, Kolkata,",
    "  Bengaluru, Hyderabad, Chennai, and Kuala Lumpur.",
    "",
    "Campus Tour & Guided Heritage Excursion arranged for",
    "registered international & outstation delegates on Jan 24."
]
draw_text_lines(c, tour_lines, PANEL_WIDTH + 25, 225, font="Helvetica", size=7.5, leading=11, fill=colors.HexColor("#334155"), align="left", width=PANEL_WIDTH-50)


# ----------------- PANEL 3 (x: 566.5 -> 849.75): FRONT COVER -----------------
# Hero deep blue header block
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(PANEL_WIDTH * 2, PAGE_HEIGHT - 170, PANEL_WIDTH, 170, fill=1, stroke=0)

# University Logo
kiit_logo = "public/assets/images/logos/kiit-official-logo.webp"
if os.path.exists(kiit_logo):
    c.drawImage(kiit_logo, PANEL_WIDTH * 2 + 35, PAGE_HEIGHT - 65, width=PANEL_WIDTH - 70, height=45, preserveAspectRatio=True, mask='auto')

c.setFont("Helvetica-Bold", 11)
c.setFillColor(colors.HexColor("#fbbf24"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 82, "KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY")
c.setFont("Helvetica", 8)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 95, "Deemed to be University • Institution of Eminence")
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 106, "Bhubaneswar, Odisha, India")

c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(colors.HexColor("#93c5fd"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 128, "Organized By: School of Computer Engineering")

# Conference Title Announcement Badge
c.setFillColor(colors.HexColor("#2563eb"))
c.roundRect(PANEL_WIDTH * 2 + 15, PAGE_HEIGHT - 215, PANEL_WIDTH - 30, 36, 4, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 11)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 195, "1st INTERNATIONAL CONFERENCE")
c.setFont("Helvetica-Bold", 9)
c.setFillColor(colors.HexColor("#dbeafe"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 208, "ON ADVANCES IN COMPUTING, INTELLIGENCE & ENGG.")

# Main Acronym & Logo block
c.setFont("Helvetica-Bold", 26)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 260, "ACIE 2027")

c.setFont("Helvetica-Bold", 10.5)
c.setFillColor(colors.HexColor("#0284c7"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 280, "Hybrid Mode: In-Person & Virtual")

# Conference Campus Image
kiit_campus = "public/assets/images/kiit/kiit-convention-center.webp"
if not os.path.exists(kiit_campus):
    kiit_campus = "public/assets/images/kiit/kiit-campus-aerial.webp"
if os.path.exists(kiit_campus):
    c.drawImage(kiit_campus, PANEL_WIDTH * 2 + 20, PAGE_HEIGHT - 435, width=PANEL_WIDTH - 40, height=135, preserveAspectRatio=True)

# Important Dates on Front Cover
c.setFillColor(colors.HexColor("#eff6ff"))
c.setStrokeColor(colors.HexColor("#93c5fd"))
c.roundRect(PANEL_WIDTH * 2 + 15, PAGE_HEIGHT - 530, PANEL_WIDTH - 30, 80, 6, fill=1, stroke=1)

c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.HexColor("#b91c1c"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 460, "JANUARY 22 - 24, 2027")

c.setFont("Helvetica-Bold", 9)
c.setFillColor(colors.HexColor("#1e293b"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 480, "Venue: KIIT Convention Centre")
c.setFont("Helvetica", 8)
c.setFillColor(colors.HexColor("#475569"))
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 495, "Campus 6, KIIT Deemed to be University")
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 508, "Bhubaneswar, Odisha – 751024, India")

# Journal Brand Footer
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(PANEL_WIDTH * 2, 0, PANEL_WIDTH, 48, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 8.5)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 2.5, 30, "ACIE: Advances in Computing, Intelligence & Engg.")
c.setFont("Helvetica", 7.5)
c.setFillColor(colors.HexColor("#93c5fd"))
c.drawCentredString(PANEL_WIDTH * 2.5, 16, "An International Peer-Reviewed Open Access Journal | acieopen.com")

c.showPage()

# =========================================================================
# PAGE 2: INSIDE THREE PANELS (Left: About; Middle: Tracks & Committee; Right: Fees & Dates)
# =========================================================================

# Background
c.setFillColor(colors.HexColor("#f8fafc"))
c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

# Guidelines
c.setStrokeColor(colors.HexColor("#cbd5e1"))
c.setLineWidth(0.5)
c.setDash(3, 3)
c.line(PANEL_WIDTH, 0, PANEL_WIDTH, PAGE_HEIGHT)
c.line(PANEL_WIDTH * 2, 0, PANEL_WIDTH * 2, PAGE_HEIGHT)
c.setDash([])

# ----------------- PANEL 1 (x: 0 -> 283.25): ABOUT UNIVERSITY, SCHOOL & CONFERENCE -----------------
# Header
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(0, PAGE_HEIGHT - 45, PANEL_WIDTH, 45, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH/2.0, PAGE_HEIGHT - 28, "ABOUT KIIT & THE CONFERENCE")

# Section 1: About the University
c.setFont("Helvetica-Bold", 10)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawString(16, PAGE_HEIGHT - 65, "About KIIT Deemed to be University")

about_univ = [
    "Kalinga Institute of Industrial Technology (KIIT) Deemed to be",
    "University is globally recognized as an Institution of Eminence",
    "by the Ministry of Education, Govt. of India. Founded by celebrated",
    "educationist and philanthropist Prof. Achyuta Samanta, KIIT has",
    "emerged as one of India's premier multi-disciplinary universities.",
    "",
    "Accredited with NAAC 'A++' Grade and ranked within top global",
    "brackets by Times Higher Education (THE) and QS World Rankings,",
    "KIIT spans 25 green, Wi-Fi-enabled campuses housing 40,000+",
    "students from over 65 countries with ultra-modern laboratories,",
    "high-performance computing centres, and Olympic-grade sports."
]
draw_text_lines(c, about_univ, 16, PAGE_HEIGHT - 80, font="Helvetica", size=7, leading=9.5, fill=colors.HexColor("#334155"), align="left", width=PANEL_WIDTH-32)

# Section 2: About School of Computer Engineering
c.setFont("Helvetica-Bold", 10)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawString(16, PAGE_HEIGHT - 215, "About School of Computer Engineering")

about_school = [
    "The School of Computer Engineering (SCE) at KIIT is a pioneer",
    "in research and engineering education. Equipped with advanced",
    "research centres in Artificial Intelligence, Edge Computing, Cyber",
    "Security, Internet of Things, and Data Science, the school maintains",
    "deep collaborations with industry giants including Microsoft,",
    "IBM, Intel, Cisco, and Ericsson to produce industry-ready leaders."
]
draw_text_lines(c, about_school, 16, PAGE_HEIGHT - 230, font="Helvetica", size=7, leading=9.5, fill=colors.HexColor("#334155"), align="left", width=PANEL_WIDTH-32)

# Section 3: About Conference (ACIE 2027)
c.setFont("Helvetica-Bold", 10)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawString(16, PAGE_HEIGHT - 320, "About the Conference (ACIE 2027)")

about_conf = [
    "The 2027 International Conference on Advances in Computing,",
    "Intelligence and Engineering (ACIE 2027) provides an interdisciplinary",
    "international forum for leading scientists, researchers, engineers,",
    "and practitioners to present novel theories, algorithms, and",
    "applications in smart computing and artificial intelligence.",
    "",
    "The conference emphasizes translational AI solutions for industry,",
    "sustainable energy systems, automated governance, healthcare,",
    "and environmental preservation. High-quality papers will be indexed",
    "in the ACIE International Open Access Journal."
]
draw_text_lines(c, about_conf, 16, PAGE_HEIGHT - 335, font="Helvetica", size=7, leading=9.5, fill=colors.HexColor("#334155"), align="left", width=PANEL_WIDTH-32)

# Section 4: Founder's Vision Box
c.setFillColor(colors.HexColor("#fef3c7"))
c.setStrokeColor(colors.HexColor("#fde68a"))
c.roundRect(14, 15, PANEL_WIDTH - 28, 120, 6, fill=1, stroke=1)
c.setFont("Helvetica-Bold", 9)
c.setFillColor(colors.HexColor("#92400e"))
c.drawCentredString(PANEL_WIDTH/2.0, 118, "Founder & Visionary")
founder_lines = [
    "\"Education is the third eye of a human being. It empowers,",
    "transforms, and illuminates every corner of society.\"",
    "",
    "— Prof. Achyuta Samanta",
    "Founder, KIIT & KISS (Kalinga Institute of Social Sciences)",
    "",
    "KISS provides free education, accommodation, food, and",
    "healthcare to 80,000+ indigenous children from KG to PG."
]
draw_text_lines(c, founder_lines, 20, 102, font="Helvetica", size=6.8, leading=9.2, fill=colors.HexColor("#78350f"), align="center", width=PANEL_WIDTH-40)


# ----------------- PANEL 2 (x: 283.25 -> 566.5): TRACKS & COMMITTEE -----------------
# Header
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(PANEL_WIDTH, PAGE_HEIGHT - 45, PANEL_WIDTH, 45, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 1.5, PAGE_HEIGHT - 28, "CONFERENCE TRACKS & COMMITTEE")

# Tracks Header
c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(colors.HexColor("#0f766e"))
c.drawString(PANEL_WIDTH + 14, PAGE_HEIGHT - 65, "Call for Papers — 10 Indicative Tracks")

tracks = [
    "Track 1: Artificial Intelligence, Machine Learning & Deep Learning",
    "Track 2: IoT, Edge AI, Sensor Networks & Cyber-Physical Systems",
    "Track 3: Natural Language Processing, Computer Vision & Multimodal AI",
    "Track 4: AI in Healthcare, Medical Informatics & Bio-Engineering",
    "Track 5: AI for Smart Grids, Renewable Energy & Power Systems",
    "Track 6: AI-Driven Smart Manufacturing, Industry 4.0 & Robotics",
    "Track 7: Aerospace Systems, Autonomous Drones & Navigation",
    "Track 8: AI in Mining, Geological Modeling & Resource Exploration",
    "Track 9: Smart Governance, Cyber Security & Public Infrastructure",
    "Track 10: Green Computing, Environmental Intelligence & Sustainability"
]
draw_text_lines(c, tracks, PANEL_WIDTH + 14, PAGE_HEIGHT - 80, font="Helvetica", size=6.8, leading=10, fill=colors.HexColor("#1e293b"), align="left", width=PANEL_WIDTH-28)

c.setFont("Helvetica-Oblique", 6.2)
c.setFillColor(colors.HexColor("#64748b"))
c.drawString(PANEL_WIDTH + 14, PAGE_HEIGHT - 188, "Note: Indicative and non-exhaustive; related novel contributions welcome.")

# Committee Section
c.setStrokeColor(colors.HexColor("#e2e8f0"))
c.line(PANEL_WIDTH + 14, PAGE_HEIGHT - 198, PANEL_WIDTH * 2 - 14, PAGE_HEIGHT - 198)

c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(colors.HexColor("#1e3a8a"))
c.drawString(PANEL_WIDTH + 14, PAGE_HEIGHT - 215, "Organizing Committee Leadership")

comm_lines = [
    "Chief Patron:",
    "  • Prof. Achyuta Samanta, Founder, KIIT & KISS",
    "Patrons:",
    "  • Prof. N. L. Mitra, Chancellor, KIIT Deemed to be University",
    "  • Prof. Subrat Kumar Acharya, Pro-Chancellor, KIIT",
    "General Chairs:",
    "  • Prof. Saranjit Singh, Vice-Chancellor, KIIT",
    "  • Prof. Jnyana Ranjan Mohanty, Registrar, KIIT",
    "Honorary Chairs:",
    "  • Prof. Ganapati Panda, Ex-Director, IIT Bhubaneswar",
    "  • Prof. Ashutosh Dutta, Johns Hopkins University, USA",
    "  • Prof. Sukumar Mishra, Director, IIT Dhanbad",
    "Organizing Chairs:",
    "  • Prof. Ashok Kumar Tripathy, IEEE Bhubaneswar Section",
    "  • Prof. Debabrata Samanta, KIIT University",
    "Conference Secretaries:",
    "  • Prof. Sudhansu Kumar Samal, KIIT University",
    "  • Prof. Manoj Kumar Debnath, SOA University",
    "Sponsorship Coordinator:",
    "  • subhradebdas (Phone: 1234567890 | sponsorship@acieopen.com)"
]
draw_text_lines(c, comm_lines, PANEL_WIDTH + 14, PAGE_HEIGHT - 230, font="Helvetica", size=6.7, leading=8.8, fill=colors.HexColor("#1e293b"), align="left", width=PANEL_WIDTH-28)


# ----------------- PANEL 3 (x: 566.5 -> 849.75): FEES, DATES & CONTACT -----------------
# Header
c.setFillColor(colors.HexColor("#1e3a8a"))
c.rect(PANEL_WIDTH * 2, PAGE_HEIGHT - 45, PANEL_WIDTH, 45, fill=1, stroke=0)
c.setFont("Helvetica-Bold", 12)
c.setFillColor(colors.white)
c.drawCentredString(PANEL_WIDTH * 2.5, PAGE_HEIGHT - 28, "REGISTRATION FEES & SCHEDULE")

# Fees Header
c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(colors.HexColor("#0f766e"))
c.drawString(PANEL_WIDTH * 2 + 14, PAGE_HEIGHT - 65, "Fee Structure for Author / Attendee Registration")

# Fee Table using Platypus
fee_data = [
    ["Category", "India (IEEE)", "India (Non-IEEE)", "Abroad (IEEE)", "Abroad (Non-IEEE)"],
    ["Students", "INR 7,000", "INR 7,500", "$250", "$300"],
    ["Academia", "INR 8,000", "INR 9,000", "$300", "$350"],
    ["Industry", "INR 9,000", "INR 10,000", "$350", "$400"],
    ["Attendee", "INR 3,000", "INR 3,500", "$150", "$200"]
]
fee_table = Table(fee_data, colWidths=[55, 52, 54, 46, 49])
fee_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 6),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,1), (-1,-1), 6.5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f1f5f9")]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
fee_table.wrapOn(c, PANEL_WIDTH - 28, 100)
fee_table.drawOn(c, PANEL_WIDTH * 2 + 14, PAGE_HEIGHT - 175)

# Important Dates Table
c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(colors.HexColor("#b91c1c"))
c.drawString(PANEL_WIDTH * 2 + 14, PAGE_HEIGHT - 195, "Important Dates & Milestones")

date_data = [
    ["Event Milestone", "Adjusted January Timeline"],
    ["Paper Submission Begins", "15 March 2026"],
    ["Paper Submission Deadline", "15 October 2026"],
    ["Notification of Acceptance", "15 December 2026"],
    ["Camera-Ready Copy Deadline", "30 December 2026"],
    ["Last Date of Registration", "05 January 2027"],
    ["Date of Conference", "22 - 24 January 2027"]
]
date_table = Table(date_data, colWidths=[130, 126])
date_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#b91c1c")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 6.8),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,1), (-1,-1), 6.5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#fef2f2")]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#fecaca")),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
]))
date_table.wrapOn(c, PANEL_WIDTH - 28, 120)
date_table.drawOn(c, PANEL_WIDTH * 2 + 14, PAGE_HEIGHT - 335)

# Accommodation & Travel note
c.setFillColor(colors.HexColor("#f0fdf4"))
c.setStrokeColor(colors.HexColor("#bbf7d0"))
c.roundRect(PANEL_WIDTH * 2 + 14, PAGE_HEIGHT - 440, PANEL_WIDTH - 28, 95, 6, fill=1, stroke=1)

c.setFont("Helvetica-Bold", 8.5)
c.setFillColor(colors.HexColor("#15803d"))
c.drawString(PANEL_WIDTH * 2 + 22, PAGE_HEIGHT - 355, "Accommodation & Hostel Facilities")

acc_lines = [
    "• Student hostel accommodation available @ INR 400/day.",
    "• Working lunch provided on Jan 22, 23, and 24, 2027.",
    "• Nearby premium hotels: Vivanta Bhubaneswar, Fortune",
    "  Park Sishmo, Mayfair Lagoon, and Sandy's Tower.",
    "• Campus transit shuttle available from Patia & station."
]
draw_text_lines(c, acc_lines, PANEL_WIDTH * 2 + 22, PAGE_HEIGHT - 370, font="Helvetica", size=6.8, leading=9.5, fill=colors.HexColor("#166534"), align="left", width=PANEL_WIDTH-44)

# Contact Us Box at bottom
c.setFillColor(colors.HexColor("#1e3a8a"))
c.roundRect(PANEL_WIDTH * 2 + 14, 15, PANEL_WIDTH - 28, 145, 6, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 11)
c.setFillColor(colors.HexColor("#fbbf24"))
c.drawCentredString(PANEL_WIDTH * 2.5, 142, "CONTACT US & VENUE")

contact_lines = [
    "School of Computer Engineering",
    "Kalinga Institute of Industrial Technology (KIIT)",
    "Deemed to be University, Patia, Bhubaneswar",
    "Odisha, India – 751024",
    "",
    "Sponsorship Coordinator: subhradebdas",
    "Phone: +91 1234567890",
    "Email: sponsorship@acieopen.com | contact@acieopen.com",
    "Conference Portal: https://acieopen.com/",
    "University Portal: https://kiit.ac.in/"
]
draw_text_lines(c, contact_lines, PANEL_WIDTH * 2 + 22, 125, font="Helvetica", size=7, leading=9.8, fill=colors.white, align="center", width=PANEL_WIDTH-44)

c.showPage()
c.save()

print(f"SUCCESS: Generated {output_pdf} with file size {os.path.getsize(output_pdf)} bytes.")

