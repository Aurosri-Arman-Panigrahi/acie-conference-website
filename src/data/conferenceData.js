export const CONFERENCE_INFO = {
  name: "ACIE 2027",
  fullName: "International Conference on Advances in Computing, Intelligence and Engineering",
  shortName: "ACIE",
  journalTitle: "ACIE: Advances in Computing, Intelligence and Engineering",
  journalUrl: "https://acieopen.com/",
  edition: "2027 Annual Edition",
  dates: "January 22–24, 2027",
  location: "Kalinga Institute of Industrial Technology (KIIT), Bhubaneswar, Odisha, India",
  venue: "Campus 6, Auditorium Complex, KIIT Deemed to be University, Patia, Bhubaneswar - 751024, Odisha, India",
  mode: "Hybrid Mode (In-Person & Virtual)",
  theme: "AI-Driven Cyber-Physical Systems, Intelligent Automation & Sustainable Engineering",
  sponsorshipCoordinator: {
    name: "subhradebdas",
    phone: "1234567890",
    email: "sponsorship@acieopen.com",
    role: "Lead Sponsorship & Industry Liaison Chair"
  },
  generalContacts: {
    email: "contact@acieopen.com",
    altEmail: "conference@kiit.ac.in",
    helpline: "+91-9437376421",
    portal: "https://acieopen.com/"
  }
};

export const IMPORTANT_DATES = [
  { event: "Paper Submission Portal Opens", date: "August 1, 2026", status: "completed" },
  { event: "Paper Submission Deadline", date: "November 15, 2026", status: "extended", note: "Extended Deadline" },
  { event: "Notification of Acceptance", date: "December 10, 2026", status: "upcoming" },
  { event: "Registration & Camera-Ready Opens", date: "December 15, 2026", status: "upcoming" },
  { event: "Camera-Ready Submission Deadline", date: "December 30, 2026", status: "urgent" },
  { event: "Last Date of Author Registration", date: "January 10, 2027", status: "urgent" },
  { event: "Conference Dates (Hybrid)", date: "January 22–24, 2027", status: "highlight" }
];

export const TRACKS = [
  {
    id: 1,
    title: "Track 1: Artificial Intelligence, Machine Learning, and Deep Learning",
    description: "Deep neural networks, generative AI, reinforcement learning, explainable AI, self-supervised learning, and neural architecture search for complex systems.",
    icon: "Brain",
    tags: ["Deep Learning", "Generative AI", "XAI", "LLMs"]
  },
  {
    id: 2,
    title: "Track 2: Internet of Things (IoT), Edge AI, and Cyber-Physical Systems",
    description: "Resource-constrained embedded platforms, micro-architectures, ARM Cortex optimizations, low-latency telemetry, and resilient sensor networks.",
    icon: "Cpu",
    tags: ["Embedded ML", "ARM Cortex-M4", "Edge TPU", "IoT Telemetry"]
  },
  {
    id: 3,
    title: "Track 3: Natural Language Processing, Computer Vision, and Multimodal AI",
    description: "Large language models, vision transformers, multimodal fusion, image segmentation, optical character recognition, and cross-lingual translation.",
    icon: "Eye",
    tags: ["ViTs", "Multimodal", "NLP", "Object Detection"]
  },
  {
    id: 4,
    title: "Track 4: AI in Healthcare and Biomedical Engineering",
    description: "Medical imaging, electronic health record analytics, computational genomics, disease diagnostics, bioinformatics, and robotic surgical assistants.",
    icon: "Activity",
    tags: ["Medical AI", "Genomics", "Biosensors", "Tele-Health"]
  },
  {
    id: 5,
    title: "Track 5: AI for Smart Electrical and Power Systems",
    description: "Smart microgrids, renewable energy forecasting, predictive maintenance, power converter control, fault diagnosis, and battery management systems.",
    icon: "Zap",
    tags: ["Smart Grid", "Renewable Energy", "EV Charging", "Power Electronics"]
  },
  {
    id: 6,
    title: "Track 6: AI-Driven Smart Manufacturing and Industry 4.0",
    description: "Industrial IoT, digital twins, robotic process automation, supply chain optimization, automated optical inspection, and zero-defect manufacturing.",
    icon: "Factory",
    tags: ["Digital Twins", "Industry 4.0", "SCADA", "Predictive QC"]
  },
  {
    id: 7,
    title: "Track 7: AI Applications in Aerospace Systems",
    description: "Autonomous unmanned aerial vehicles (UAVs), swarm drone coordination, satellite orbit telemetry, avionics flight control, and collision avoidance.",
    icon: "Plane",
    tags: ["Multi-UAV", "Flight Control", "Satellite Telemetry", "Swarm Robotics"]
  },
  {
    id: 8,
    title: "Track 8: AI in Mining Engineering and Resource Exploration",
    description: "Geological remote sensing, mineral deposit exploration, automated drilling systems, underground hazard detection, and ecological restoration monitoring.",
    icon: "Mountain",
    tags: ["Remote Sensing", "Geospatial AI", "Resource Mining", "Hazard Prevention"]
  },
  {
    id: 9,
    title: "Track 9: AI for Smart Governance and Digital Public Infrastructure",
    description: "Public service delivery, citizen biometric verification, automated fraud detection, transparent e-voting protocols, and civic data analytics.",
    icon: "Shield",
    tags: ["GovTech", "Digital Public Goods", "Civic AI", "Fraud Detection"]
  },
  {
    id: 10,
    title: "Track 10: Sustainable Development, Green AI, and Environmental Intelligence",
    description: "Energy-efficient model quantization, climate modeling, carbon footprint reduction, soil health monitoring (SoilPrint), precision agriculture, and circular economy.",
    icon: "Leaf",
    tags: ["Green AI", "SoilPrint", "Precision Agri", "Carbon Neutrality"]
  }
];

export const KEYNOTE_SPEAKERS = [
  {
    id: 1,
    name: "Prof. (Dr.) Keshab K. Parhi",
    title: "Erwin A. Kelen Chair in Electrical Engineering",
    affiliation: "University of Minnesota, Twin Cities, USA",
    specialty: "VLSI Digital Signal Processing & Neuromorphic Hardware",
    image: "/assets/images/scraped/keynoteSpaker1-z4l0bNR_.png",
    bio: "Fellow of IEEE, renowned for foundational contributions to VLSI digital signal processing architectures, biomedical hardware accelerators, and high-throughput embedded cryptography."
  },
  {
    id: 2,
    name: "Dr. Bhabendu Mohanta",
    title: "Research Scientist & Faculty Member",
    affiliation: "United Arab Emirates University (UAEU), Al Ain, UAE",
    specialty: "Blockchain Architecture & Distributed Ledger Systems",
    image: "/assets/images/scraped/keynoteSpeaker2-BtsNogkk.png",
    bio: "Expert in decentralized consensus algorithms, IoT security architectures, and zero-trust edge infrastructure for cyber-physical deployments."
  },
  {
    id: 3,
    name: "Prof. Ganapati Panda",
    title: "Research Advisor & Former Deputy Director",
    affiliation: "IIT Bhubaneswar & CGU Odisha, India",
    specialty: "Adaptive Signal Processing & Computational Intelligence",
    image: "/assets/images/scraped/keynoteSpeaker3-7pPvxVRK.png",
    bio: "Pioneering researcher in evolutionary computing, digital signal processing, and bio-inspired optimization frameworks with over 350 published scientific papers."
  },
  {
    id: 4,
    name: "Dr. Suman Sourav",
    title: "Senior Research Fellow in Energy Systems",
    affiliation: "Aalborg University, Aalborg, Denmark",
    specialty: "Smart Energy Grids & Power Electronics Control",
    image: "/assets/images/scraped/keynoteSpeaker4-C7JEQMXu.png",
    bio: "Specializes in high-efficiency DC-DC converters, green energy transition frameworks, and real-time controller-hardware-in-the-loop (CHIL) simulations."
  },
  {
    id: 5,
    name: "Sangita Satapathy",
    title: "Senior Cloud Platform & Infrastructure Engineer",
    affiliation: "Royal Sutton Coldfield, England, United Kingdom",
    specialty: "Hyperscale Cloud Architecture & DevOps Governance",
    image: "/assets/images/scraped/keynoteSpeaker5-CU3eZAKd.jpeg",
    bio: "Leads enterprise Kubernetes deployments, distributed microservice meshes, and resilient cloud transformations across European financial networks."
  },
  {
    id: 6,
    name: "Dr. Akshaya Kumar Moharana",
    title: "Senior Engineering Consultant & Grid Strategist",
    affiliation: "EEPlus, Inc., Irving, Texas, USA",
    specialty: "Transmission Grid Modernization & Transient Analysis",
    image: "/assets/images/scraped/newSpeaker-BsSODFWa.png",
    bio: "Advises North American electrical utilities on large-scale renewable interconnection, EMT electromagnetic transient modeling, and grid reliability standards."
  },
  {
    id: 7,
    name: "Ms. Padmaja Pulivarthy",
    title: "Enterprise Data Systems Architect",
    affiliation: "Samsung Semiconductor, San Jose, California, USA",
    specialty: "Semiconductor AI Yield Optimization & High-Density Memory",
    image: "/assets/images/scraped/newSpeaker2-DRXI_EuR.png",
    bio: "Architecting automated silicon wafer inspection pipelines, high-bandwidth memory (HBM) data workflows, and edge inference engines."
  },
  {
    id: 8,
    name: "Dr. Subhas Chinara",
    title: "Associate Professor, Dept. of Computer Science",
    affiliation: "National Institute of Technology (NIT), Rourkela, India",
    specialty: "Wireless Sensor Networks & Mobile Ad-Hoc Routing",
    image: "/assets/images/scraped/newSpeaker3-CZHDiFUn.png",
    bio: "Distinguished academician and researcher focusing on fault-tolerant ad-hoc wireless sensor topologies, intrusion detection systems, and opportunistic edge routing."
  },
  {
    id: 9,
    name: "Mr. Deepak Mathur",
    title: "Distinguished Engineering Leader & Former Vice President",
    affiliation: "IEEE Member and Geographic Activities (MGA), Global",
    specialty: "Global Engineering Leadership & Standardization",
    image: "/assets/images/scraped/keynoteSpeaker10-xQzNenqP.png",
    bio: "Past IEEE Vice President (MGA) and IEEE Region 10 Director, championing technological innovation, student professional activities, and STEM inclusion worldwide."
  },
  {
    id: 10,
    name: "Dr. Rasmita Samantaray",
    title: "Senior Autonomous Driving Systems Engineer",
    affiliation: "Hyundai Motor Europe Technical Centre, Rüsselsheim, Germany",
    specialty: "Automotive Sensor Fusion & Autonomous Vehicles",
    image: "/assets/images/scraped/newSpeaker4-Brg4EqWV.png",
    bio: "Directs next-generation automotive radar/LiDAR fusion, ISO 26262 functional safety, and real-time deep neural trajectory controllers for European EV fleets."
  }
];

export const REGISTRATION_FEES = [
  {
    category: "Student / Research Scholar",
    indiaMember: "₹7,000",
    indiaNonMember: "₹7,500",
    foreignMember: "$250",
    foreignNonMember: "$300",
    benefits: "Full access to all technical sessions, presentation certificate, conference kit, working lunch & banquet dinner."
  },
  {
    category: "Academic Faculty",
    indiaMember: "₹8,000",
    indiaNonMember: "₹9,000",
    foreignMember: "$300",
    foreignNonMember: "$350",
    benefits: "Author presentation slot, inclusion in ACIE proceedings, certificate of presentation, conference proceedings download."
  },
  {
    category: "Industry Delegates",
    indiaMember: "₹9,000",
    indiaNonMember: "₹10,000",
    foreignMember: "$350",
    foreignNonMember: "$400",
    benefits: "Corporate networking pass, exhibition access, B2B liaison sessions, delegate directory inclusion."
  },
  {
    category: "Attendees / Listeners (Non-Author)",
    indiaMember: "₹3,000",
    indiaNonMember: "₹3,500",
    foreignMember: "$150",
    foreignNonMember: "$200",
    benefits: "Full observer access to all keynote sessions, workshops, Q&A panels, working lunches, and attendance certificate."
  }
];

export const SPONSORSHIP_PACKAGES = [
  {
    tier: "Title Sponsor",
    amount: "₹2,00,000",
    usdAmount: "$2,500",
    color: "from-amber-500 to-yellow-600",
    badge: "Most Prestigious",
    freeDelegates: 8,
    booth: "Prime 6m × 3m Exhibition Stall",
    benefits: [
      "Prominent 'Powered by' co-branding on main stage backdrop & website banner",
      "Dedicated 15-minute Corporate Keynote Presentation slot in main plenary",
      "8 Complimentary Full Delegate registrations with banquet invitations",
      "Full-page color advertisement on the back cover of Conference Proceedings",
      "Insertion of company promotional brochures into all official delegate kits",
      "Prominent logo on all lanyards, delegate badges, and press releases"
    ]
  },
  {
    tier: "Diamond Sponsor",
    amount: "₹1,50,000",
    usdAmount: "$1,900",
    color: "from-blue-600 to-cyan-600",
    badge: "Executive",
    freeDelegates: 6,
    booth: "Premium 4m × 3m Exhibition Stall",
    benefits: [
      "Prominent logo placement on website, backdrop, and official banner stands",
      "Session Chair slot for designated corporate executive in technical track",
      "6 Complimentary Full Delegate passes including lunches and banquets",
      "Full-page advertisement inside front cover of Conference Proceedings",
      "Promotional item inclusion in delegate kit bags",
      "VIP networking dinner access with keynote dignitaries"
    ]
  },
  {
    tier: "Platinum Sponsor",
    amount: "₹1,00,000",
    usdAmount: "$1,250",
    color: "from-slate-700 to-slate-900",
    badge: "Popular",
    freeDelegates: 4,
    booth: "Standard 3m × 3m Exhibition Stall",
    benefits: [
      "Logo branding on conference website, brochure, and banner collaterals",
      "4 Complimentary Full Delegate passes",
      "Half-page color advertisement in Conference Proceedings",
      "Flyer insertion in delegate registration bags",
      "Recognition during opening and closing award ceremonies"
    ]
  },
  {
    tier: "Gold Sponsor",
    amount: "₹75,000",
    usdAmount: "$950",
    color: "from-amber-600 to-amber-700",
    badge: "Standard",
    freeDelegates: 3,
    booth: "Exhibition Space 3m × 2m",
    benefits: [
      "Logo branding on conference website and sponsorship roll",
      "3 Complimentary Delegate passes",
      "Quarter-page advertisement in proceedings booklet",
      "Display banner inside session rooms"
    ]
  },
  {
    tier: "Silver Sponsor",
    amount: "₹50,000",
    usdAmount: "$650",
    color: "from-slate-400 to-slate-600",
    badge: "Associate",
    freeDelegates: 2,
    booth: "Dedicated Standee in Exhibition Hall",
    benefits: [
      "Logo inclusion on official website and registration desk banner",
      "2 Complimentary Delegate passes",
      "Formal acknowledgment during Inaugural Session"
    ]
  },
  {
    tier: "Bronze Sponsor",
    amount: "₹25,000",
    usdAmount: "$350",
    color: "from-orange-700 to-amber-800",
    badge: "Supporter",
    freeDelegates: 1,
    booth: "Tabletop Literature Display",
    benefits: [
      "Logo placement on conference website partner gallery",
      "1 Complimentary Delegate pass",
      "Certificate of Corporate Appreciation"
    ]
  }
];

export const TOURISM_DESTINATIONS = [
  {
    id: 1,
    name: "Lingaraj Temple",
    distance: "25 KM",
    image: "/assets/images/scraped/lingaraj-CzRx05ve.jpg",
    history: "An 11th-century temple dedicated to Lord Shiva, a masterpiece of Kalinga architecture."
  },
  {
    id: 2,
    name: "Puri Jagannath",
    distance: "57 KM",
    image: "/assets/images/scraped/puri-siI7osXQ.jpg",
    history: "One of the Char Dham pilgrimage sites, famous for the annual Rath Yatra festival."
  },
  {
    id: 3,
    name: "Konark Sun Temple",
    distance: "63 KM",
    image: "/assets/images/scraped/konark-B97Vv_kx.jpg",
    history: "A 13th-century UNESCO World Heritage site shaped like a massive stone chariot."
  },
  {
    id: 4,
    name: "Dhauli Shanti Stupa",
    distance: "31 KM",
    image: "/assets/images/scraped/Dhauli-C0DD5BOJ.jpg",
    history: "A Buddhist peace pagoda marking Emperor Ashoka’s transformation after the Kalinga war."
  },
  {
    id: 5,
    name: "Nandankanan Zoo",
    distance: "35 KM",
    image: "/assets/images/scraped/zoo-B5RwaHE3.jpg",
    history: "A unique zoological park known for conservation and white tigers."
  },
  {
    id: 6,
    name: "Chilika Lake",
    distance: "112 KM",
    image: "/assets/images/scraped/chilika-C2Nze43z.jpg",
    history: "Asia’s largest brackish water lagoon, home to migratory birds and dolphins."
  },
  {
    id: 7,
    name: "Barabati Stadium",
    distance: "55 KM",
    image: "/assets/images/scraped/barabati-B4WPFbhS.jpg",
    history: "Barabati Stadium, hosts cricket, football, and cultural events since 1958."
  },
  {
    id: 8,
    name: "Rajarani Temple",
    distance: "4 KM",
    image: "/assets/images/scraped/rajarani-BRbc6iQ7.jpg",
    history: "Stunning 11th-century temple built with red and yellow sandstone."
  }
];

export const COMMITTEE = {
  chiefPatron: {
    name: "Prof. (Dr.) Achyuta Samanta",
    role: "Chief Patron",
    designation: "Founder, KIIT & KISS Deemed to be University, Bhubaneswar, India",
    affiliation: "Eminent Educationist, Social Reformer and Philanthropist"
  },
  patrons: [
    {
      name: "Prof. (Dr.) Saranjit Singh",
      role: "Patron",
      designation: "Vice Chancellor, KIIT Deemed to be University"
    },
    {
      name: "Prof. (Dr.) J. R. Mohanty",
      role: "Patron",
      designation: "Registrar, KIIT Deemed to be University"
    }
  ],
  generalChairs: [
    {
      name: "Prof. (Dr.) Bhabani Shankar Prasad Mishra",
      role: "General Chair",
      designation: "Dean, School of Computer Engineering, KIIT University"
    },
    {
      name: "Prof. (Dr.) Arindam Deb",
      role: "General Chair",
      designation: "Professor & Senior Researcher, School of Electrical Engineering, KIIT University"
    }
  ],
  organizingChairs: [
    {
      name: "Dr. Subhra Debdas",
      role: "Organizing Chair & Sponsorship Coordinator",
      designation: "School of Electrical Engineering, KIIT University",
      contact: "subhradebdas | Phone: 1234567890 | Email: sponsorship@acieopen.com"
    },
    {
      name: "Dr. Swastik Panda",
      role: "Organizing Secretary",
      designation: "School of Computer Science & Engineering, KIIT University"
    },
    {
      name: "Dr. Prabhu Krupa Biswal",
      role: "Organizing Co-Chair",
      designation: "School of Computer Science & Engineering, KIIT University"
    }
  ],
  technicalProgramChairs: [
    {
      name: "Dr. Aayush Saha",
      role: "Technical Program Chair",
      designation: "KIIT Deemed to be University, India"
    },
    {
      name: "Dr. Sucharita Pradhan",
      role: "Publication & Track Chair",
      designation: "KIIT Deemed to be University, India"
    },
    {
      name: "Dr. Samir Kumar Panigrahi",
      role: "TPC Co-Chair & Quantum Intelligence Lead",
      designation: "KIIT Deemed to be University, India"
    }
  ],
  advisoryBoard: [
    { name: "Prof. (Dr.) Keshab K. Parhi", institution: "University of Minnesota, USA" },
    { name: "Dr. Bhabendu Mohanta", institution: "United Arab Emirates University, UAE" },
    { name: "Prof. Ganapati Panda", institution: "CGU Odisha & Former Dy. Director IIT Bhubaneswar" },
    { name: "Dr. Suman Sourav", institution: "Aalborg University, Denmark" },
    { name: "Dr. Akshaya Kumar Moharana", institution: "EEPlus Inc., Texas, USA" },
    { name: "Ms. Padmaja Pulivarthy", institution: "Samsung Semiconductor, USA" },
    { name: "Dr. Subhas Chinara", institution: "NIT Rourkela, India" },
    { name: "Mr. Deepak Mathur", institution: "Former IEEE Vice President (MGA)" },
    { name: "Dr. Rasmita Samantaray", institution: "Hyundai Motor Europe Tech Centre, Germany" }
  ]
};

export const HERO_SLIDES = [
  {
    image: "/assets/images/kiit/kiit-library-front.jpg",
    headline: "ACIE 2027 International Conference",
    subtitle: "Hosted by KIIT Deemed to be University, Bhubaneswar, Odisha, India",
    date: "January 22–24, 2027"
  },
  {
    image: "/assets/images/kiit/kiit-convention-center.webp",
    headline: "Pioneering Computing, Intelligence & Engineering",
    subtitle: "Advances in Intelligent Systems, Cyber-Physical Telemetry & Sustainable Technology",
    date: "Hybrid Mode • In-Person & Global Virtual Tracks"
  },
  {
    image: "/assets/images/kiit/kiit-campus-arch.webp",
    headline: "Peer-Reviewed Indexed Publication",
    subtitle: "All Accepted & Presented Papers Published in ACIE Open Access Journal",
    date: "Submit Manuscripts via Submission Portal"
  },
  {
    image: "/assets/images/kiit/kiit-campus-aerial.webp",
    headline: "Institution of Eminence & World-Class Venue",
    subtitle: "Spread Across 25 Campuses in the Temple City of Bhubaneswar",
    date: "Campus 6 Auditorium Complex • KIIT Bhubaneswar"
  }
];

export const SUBPAGE_CAROUSEL_IMAGES = [
  "/assets/images/kiit/kiit-library-front.jpg",
  "/assets/images/kiit/kiit-convention-center.webp",
  "/assets/images/kiit/kiit-campus-arch.webp",
  "/assets/images/kiit/kiit-academics-1.webp",
  "/assets/images/kiit/kiit-academics-2.webp",
  "/assets/images/kiit/kiit-academics-3.webp",
  "/assets/images/kiit/kiit-campus-aerial.webp",
  "/assets/images/kiit/kiit-campus-building-6.webp"
];

export const LOGO_OPTIONS = [
  {
    id: 1,
    name: "Modernist Geometric Lettermark",
    concept: "Pure 4 letters (A-C-I-E) with high-precision geometric cuts and emerald focal dot.",
    symbolism: "Minimalist Computational Intelligence",
    svgPath: "/assets/images/logos/acie-minimal-1.svg",
    colors: ["#0F172A", "#1E3A8A", "#2563EB", "#059669"]
  },
  {
    id: 2,
    name: "Architectural Cut Lettermark",
    concept: "Bespoke geometric vector paths forming the 4 letters with precision underline beam.",
    symbolism: "Architectural Rigor & Engineering Precision",
    svgPath: "/assets/images/logos/acie-minimal-2.svg",
    colors: ["#0F172A", "#1E40AF", "#2563EB", "#0284C7"]
  },
  {
    id: 3,
    name: "Swiss Typographic Wordmark",
    concept: "Pure minimalist wide-tracking typographic letterforms with square accent dot.",
    symbolism: "International Journal Authority & Clean Modernism",
    svgPath: "/assets/images/logos/acie-minimal-3.svg",
    colors: ["#0F172A", "#475569", "#10B981", "#CBD5E1"]
  },
  {
    id: 4,
    name: "Monospace Tech Grid",
    concept: "Raw monospace computing letterforms with subtle terminal status pulse node.",
    symbolism: "Algorithmic Precision & Computer Science",
    svgPath: "/assets/images/logos/acie-minimal-4.svg",
    colors: ["#0F172A", "#1E3A8A", "#2563EB", "#059669"]
  }
];

