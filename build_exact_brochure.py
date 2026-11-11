import os
import fitz  # PyMuPDF
from PIL import Image

def build_brochure():
    source_pdf = "sample brochure/AISIGH-SD-2026-Broucher.pdf"
    target_pdf = "public/assets/brochure/ACIE-2027-Brochure.pdf"
    dist_pdf = "dist/assets/brochure/ACIE-2027-Brochure.pdf"
    
    assert os.path.exists(source_pdf), f"Source PDF {source_pdf} not found!"
    doc = fitz.open(source_pdf)
    
    # -------------------------------------------------------------
    # PAGE 1
    # -------------------------------------------------------------
    p1 = doc[0]
    
    # Redact without ANY white box fill (fill=False removes text and leaves underlying background)
    p1_redactions = [
        fitz.Rect(4.0, 45.0, 238.0, 59.0),    # Paper submission URL
        fitz.Rect(4.0, 252.0, 238.0, 269.0),  # Registration / payment URL
        fitz.Rect(585.0, 218.0, 810.0, 248.0), # Dates: 28-30 Dec 2026
        fitz.Rect(570.0, 252.0, 835.0, 286.0), # Venue: CUTM
        fitz.Rect(575.0, 425.0, 835.0, 488.0), # Organized by: CUTM
        fitz.Rect(688.0, 547.0, 808.0, 605.0)  # Old CUTM Logo
    ]
    for r in p1_redactions:
        p1.add_redact_annot(r, fill=False)
    p1.apply_redactions()
    
    # Insert Page 1 text with clean invisible bounding boxes & proper alignment
    # 1. Submission URL
    p1.insert_textbox(
        fitz.Rect(4.0, 47.0, 238.0, 58.0),
        "https://cmt3.research.microsoft.com/ACIE2027",
        fontname="times-roman",
        fontsize=6.8,
        color=(0.1, 0.1, 0.1),
        align=1
    )
    
    # 2. Payment / Registration URL
    p1.insert_textbox(
        fitz.Rect(4.0, 253.5, 238.0, 267.5),
        "https://forms.gle/m2pqtU4VQpujxFMU8",
        fontname="times-roman",
        fontsize=7.0,
        color=(0.1, 0.1, 0.1),
        align=1
    )
    
    # 3. Dates on Cover: 22nd - 24th January 2027 (navy tone matching original palette)
    res_date = p1.insert_textbox(
        fitz.Rect(560.0, 216.0, 846.0, 252.0),
        "22nd - 24th January 2027",
        fontname="times-bold",
        fontsize=14.0,
        color=(0.0, 0.21, 0.33),
        align=1
    )
    assert res_date >= 0, f"res_date failed: {res_date}"
    
    # 4. Venue on Cover
    venue_text = "Venue : Kalinga Institute of Industrial Technology,\nBhubaneswar, Odisha, India"
    res_venue = p1.insert_textbox(
        fitz.Rect(560.0, 252.0, 846.0, 288.0),
        venue_text,
        fontname="times-bold",
        fontsize=9.8,
        color=(0.05, 0.05, 0.05),
        align=1
    )
    assert res_venue >= 0, f"res_venue failed: {res_venue}"
    
    # 5. Organized By on Cover
    org_text = "School of Computer Engineering\nKalinga Institute of Industrial Technology,\nBhubaneswar, Odisha, India"
    res_org = p1.insert_textbox(
        fitz.Rect(560.0, 426.0, 846.0, 488.0),
        org_text,
        fontname="times-bold",
        fontsize=10.0,
        color=(0.05, 0.05, 0.05),
        align=1
    )
    assert res_org >= 0, f"res_org failed: {res_org}"
    
    # 6. KIIT Logo at bottom right
    kiit_logo_path = "public/assets/images/logos/kiit-official-logo.png"
    if os.path.exists(kiit_logo_path):
        logo_rect = fitz.Rect(700.0, 548.0, 796.0, 602.0)
        p1.insert_image(logo_rect, filename=kiit_logo_path, keep_proportion=True)

    # -------------------------------------------------------------
    # PAGE 2
    # -------------------------------------------------------------
    p2 = doc[1]
    
    # Redact areas with fill=False so NO white boxes exist
    p2_redactions = [
        fitz.Rect(16.0, 22.0, 268.0, 235.0),   # About University
        fitz.Rect(16.0, 255.0, 268.0, 406.0),  # About School
        fitz.Rect(16.0, 428.0, 268.0, 608.0),  # About Conference
        fitz.Rect(310.0, 328.0, 570.0, 590.0), # Committee / Speakers
        fitz.Rect(709.0, 436.0, 831.0, 452.0), # Date of Conference (28/12/2026)
        fitz.Rect(595.0, 508.0, 825.0, 590.0)  # Contact Us
    ]
    for r in p2_redactions:
        p2.add_redact_annot(r, fill=False)
    p2.apply_redactions()
    
    # 1. About KIIT University
    about_kiit = (
        "Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, "
        "Bhubaneswar, is globally recognized as an Institution of Eminence by the "
        "Ministry of Education, Govt. of India. Founded by visionary educationist "
        "Prof. Achyuta Samanta, KIIT has emerged as a premier multidisciplinary university "
        "accredited with NAAC 'A++' Grade and ranked among top global institutions by "
        "Times Higher Education (THE) and QS World University Rankings. Spanning 25 "
        "world-class campuses, KIIT provides cutting-edge laboratories, world-class "
        "sports facilities, and an inspiring academic ecosystem to over 40,000 students "
        "from 65+ nations."
    )
    p2.insert_textbox(
        fitz.Rect(17.0, 25.0, 266.0, 232.0),
        about_kiit,
        fontname="times-roman",
        fontsize=8.0,
        color=(0.1, 0.1, 0.1),
        align=3
    )
    
    # 2. About School of Computer Engineering
    about_school = (
        "The School of Computer Engineering at KIIT is dedicated to excellence in "
        "technical education, research, and innovation. The School offers high-quality "
        "undergraduate, postgraduate, and doctoral programs with state-of-the-art "
        "computing facilities and industry-aligned curricula in AI, Data Science, and "
        "Software Engineering. It maintains strong industry collaborations, active IEEE "
        "student branches, and an environment fostering high-impact research, "
        "entrepreneurship, and experiential learning for real-world engineering solutions."
    )
    p2.insert_textbox(
        fitz.Rect(17.0, 258.0, 266.0, 404.0),
        about_school,
        fontname="times-roman",
        fontsize=8.0,
        color=(0.1, 0.1, 0.1),
        align=3
    )
    
    # 3. About the Conference
    about_conf = (
        "The AI-Enabled Smart Solutions for Industry, Governance, Healthcare, and "
        "Sustainable Development (ACIE-2027) conference, organized in technical "
        "collaboration with the IEEE Bhubaneswar Section and ACIE Open Access Journal, "
        "provides a premier international forum for researchers, academicians, and "
        "industry leaders to deliberate on modern advances in artificial intelligence. "
        "Focusing on foundational AI, IoT, multimodal perception, smart governance, and "
        "healthcare systems, ACIE-2027 bridges theory and practice for sustainable societal impact."
    )
    p2.insert_textbox(
        fitz.Rect(17.0, 430.0, 266.0, 606.0),
        about_conf,
        fontname="times-roman",
        fontsize=8.0,
        color=(0.1, 0.1, 0.1),
        align=3
    )
    
    # 4. Committee & Speakers (Prof. Dr. Subhas Chinara, NIT Rourkela; sponsorship coordinator subhradebdas)
    committee_entries = [
        ("Honorary Chairs:", True),
        ("Prof. Ganapati Panda, Ex Director IIT Bhubaneswar", False),
        ("Prof. Ashutosh Dutta, Johns Hopkins University, USA", False),
        ("Prof. Subhransu Sekhar Samantray, IIT Bhubaneswar", False),
        ("Prof. Sukumar Mishra, Director, IIT Dhanbad, India", False),
        ("General Chairs:", True),
        ("Prof. Saranjit Singh, Vice-Chancellor, KIIT", False),
        ("Prof. Jnyana Ranjan Mohanty, Registrar, KIIT", False),
        ("Organising Chairs:", True),
        ("Prof. Ashok Kumar Tripathy, IEEE, Bhubaneswar Section", False),
        ("Shri Hare Krishna Ratha, Former Director, DRDO", False),
        ("Prof. Bansidhar Majhi, CGU, Bhubaneswar", False),
        ("Prof. Pradipta Kumar Nanda, SoA, Bhubaneswar", False),
        ("Prof. Debi Prosad Dogra, IIT, Bhubaneswar", False),
        ("Prof. Dr. Subhas Chinara, NIT Rourkela, India", False),
        ("Conference Secretaries & Sponsorship:", True),
        ("Prof. Sudhansu Kumar Samal, KIIT, Bhubaneswar", False),
        ("subhradebdas (Phone: 1234567890 | sponsorship@acieopen.com)", False)
    ]
    
    y_start = 332.0
    for title, is_header in committee_entries:
        font = "times-bold" if is_header else "times-roman"
        color = (0.867, 0.169, 0.110) if is_header else (0.1, 0.1, 0.1) # exact original red accent for headers
        size = 8.5 if is_header else 7.5
        line_height = 11.0 if is_header else 10.0
        p2.insert_text(
            fitz.Point(312.0, y_start),
            title,
            fontname=font,
            fontsize=size,
            color=color
        )
        y_start += line_height
    
    # 5. Date of Conference in table
    p2.insert_textbox(
        fitz.Rect(709.0, 437.0, 831.0, 452.0),
        "22-24/01/2027",
        fontname="times-bold",
        fontsize=8.0,
        color=(0.1, 0.1, 0.1),
        align=1
    )
    
    # 6. Contact Us Box
    contact_text = (
        "School of Computer Engineering\n"
        "Kalinga Institute of Industrial Technology (KIIT)\n"
        "Patia, Bhubaneswar, Odisha - 751024\n"
        "Email : contact@acieopen.com\n"
        "Contact: +91 1234567890 (subhradebdas)\n"
        "Website: acieopen.com | kiit.ac.in"
    )
    p2.insert_textbox(
        fitz.Rect(592.0, 510.0, 828.0, 588.0),
        contact_text,
        fontname="times-roman",
        fontsize=8.0,
        color=(0.1, 0.1, 0.1),
        align=1
    )
    
    os.makedirs(os.path.dirname(target_pdf), exist_ok=True)
    doc.save(target_pdf, garbage=4, deflate=True)
    print(f"Saved {target_pdf}")
    
    if os.path.exists("dist"):
        os.makedirs(os.path.dirname(dist_pdf), exist_ok=True)
        doc.save(dist_pdf, garbage=4, deflate=True)
        print(f"Saved {dist_pdf}")

if __name__ == "__main__":
    build_brochure()
