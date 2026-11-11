import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import { 
  Calendar, 
  MapPin, 
  Globe, 
  CheckCircle2, 
  ArrowRight, 
  Users, 
  Sparkles,
  ChevronRight,
  ExternalLink
} from 'lucide-react';
import { 
  CONFERENCE_INFO, 
  IMPORTANT_DATES, 
  TRACKS, 
  KEYNOTE_SPEAKERS, 
  TOURISM_DESTINATIONS,
  HERO_SLIDES 
} from '../data/conferenceData';

export default function Home({ onOpenBrochure }) {
  const [currentSlide, setCurrentSlide] = useState(0);
  const touchStartX = useRef(0);
  const touchEndX = useRef(0);

  // Auto-advance hero carousel every 5 seconds
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % HERO_SLIDES.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  const handleNextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % HERO_SLIDES.length);
  };

  const handlePrevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + HERO_SLIDES.length) % HERO_SLIDES.length);
  };

  const handleTouchStart = (e) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchMove = (e) => {
    touchEndX.current = e.touches[0].clientX;
  };

  const handleTouchEnd = () => {
    const diff = touchStartX.current - touchEndX.current;
    if (diff > 50) handleNextSlide();
    if (diff < -50) handlePrevSlide();
  };

  return (
    <main className="relative w-full overflow-x-hidden">

      {/* ======================= HERO SECTION (Matching aisigh-sd.co.in & media_1794361814835_5a750b31) ======================= */}
      <div 
        className="relative w-full h-screen overflow-hidden"
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
      >
        {/* Carousel Background Images with smooth translateX transition */}
        <div className="absolute inset-0 z-0">
          <div 
            className="flex h-full transition-transform duration-700 ease-in-out"
            style={{ transform: `translateX(-${currentSlide * 100}%)` }}
          >
            {[
              "/assets/images/kiit/kiit-campus-aerial.webp",
              "/assets/images/kiit/kiit-convention-center.webp",
              "/assets/images/kiit/kiit-campus-building-6.webp",
              "/assets/images/kiit/kiit-library-front.jpg"
            ].map((imgSrc, index) => (
              <div key={index} className="w-full h-full flex-shrink-0 relative">
                <img 
                  src={imgSrc} 
                  alt={`Campus slide ${index + 1}`} 
                  className="absolute inset-0 w-full h-full object-cover"
                  loading={index === 0 ? "eager" : "lazy"}
                  fetchPriority={index === 0 ? "high" : "auto"}
                  decoding="async"
                />
              </div>
            ))}
          </div>
        </div>

        {/* Transparent container - no white background overlay so only text and slides remain */}
        <div className="absolute inset-0 z-10 pointer-events-none bg-transparent" />

        {/* Hero Content with exact AOS animations & hover transforms */}
        <section className="relative z-20 h-full flex items-center">
          <div className="pl-6 sm:pl-10 lg:pl-16 max-w-5xl">
            
            {/* Metadata Pills matching media_1794361814835_5a750b31 & Home-7Lgsr6xV.js */}
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span 
                data-aos="fade-up"
                className="inline-block py-1 px-4 rounded-full bg-blue-100 text-blue-900 text-sm font-semibold mb-4 hover:bg-blue-200 transition-colors duration-300 cursor-pointer"
              >
                📍 KIIT, BBSR • January 22–24, 2027
              </span>

              <span 
                data-aos="fade-up"
                data-aos-delay="100"
                className="inline-block py-1 px-4 rounded-full bg-blue-100 text-blue-900 text-sm font-semibold mb-4 hover:bg-blue-200 transition-colors duration-300 cursor-pointer"
              >
                <a 
                  href="https://conferences.ieee.org/conferences_events/conferences/conferencedetails/70672" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="text-blue-900 hover:text-blue-600"
                >
                  Conference ID : 70672
                </a>
              </span>
            </div>

            {/* Main Headline with exact design colors, typography, hover transitions & animations from aisigh-sd.co.in */}
            <h1 
              data-aos="fade-right"
              className="text-xl sm:text-2xl md:text-3xl lg:text-[36px] xl:text-[38px] font-bold leading-tight text-blue-900 hover:text-blue-600 hover:scale-105 transition-all duration-300 cursor-pointer"
              style={{ textShadow: "0 1px 4px rgba(255,255,255,0.95), 0 2px 8px rgba(255,255,255,0.85)" }}
            >
              AI-Enabled Smart Solutions <br />
              for Industry, Governance, Healthcare <br />
              and Sustainable Development (ACIE-2027)
            </h1>

            {/* Host Institution with hover effect */}
            <p 
              data-aos="fade-left"
              className="mt-6 font-semibold text-base sm:text-lg text-slate-800 hover:text-blue-900 hover:no-underline transition duration-300 cursor-pointer"
              style={{ textShadow: "0 1px 3px rgba(255,255,255,0.95), 0 2px 6px rgba(255,255,255,0.85)" }}
            >
              Kalinga Institute of Industrial Technology, Bhubaneswar
            </p>

            <span 
              data-aos="fade-up"
              className="inline-block py-1 px-4 rounded-full bg-blue-100 text-blue-900 text-sm font-semibold mt-4 mb-4 hover:bg-blue-200 transition-colors duration-300 cursor-pointer"
            >
              🌐 Hybrid Mode
            </span>

          </div>
        </section>

        {/* Carousel Pagination Dots matching Home-7Lgsr6xV.js & media_1794361814835_5a750b31 */}
        <div className="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2 z-20">
          {[0, 1, 2, 3].map((idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => setCurrentSlide(idx)}
              aria-label={`Show slide ${idx + 1}`}
              aria-current={currentSlide === idx ? 'true' : undefined}
              className={`h-3 w-3 rounded-full cursor-pointer transition-all duration-300 ${
                currentSlide === idx ? 'bg-blue-600' : 'bg-white/60 hover:bg-white'
              }`}
            />
          ))}
        </div>
      </div>


      {/* ======================= PARTNERS & LOGOS STRIP (Matching aisigh-sd.co.in) ======================= */}
      <section className="bg-[#E7ECFF] px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto pt-16 pb-12">
        <div className="text-center mb-8">
          <span className="text-xs font-bold uppercase tracking-widest text-blue-900 block">
            Academic Association &amp; Technical Co-Sponsors
          </span>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-8 border-t border-blue-200 pt-10 text-center">
          <div className="flex justify-center items-center" data-aos="fade-up" data-aos-delay="100">
            <div className="h-40 w-48 p-4 bg-white border-2 border-blue-300 rounded-2xl shadow-md hover:scale-110 transition-transform duration-300 flex items-center justify-center">
              <img 
                src="/assets/images/logos/acie-official-logo-transparent.png" 
                alt="ACIE Official Logo" 
                className="max-h-20 max-w-full object-contain" 
              />
            </div>
          </div>
          <div className="flex justify-center items-center" data-aos="fade-up" data-aos-delay="200">
            <div className="h-40 w-48 p-4 bg-white border-2 border-blue-300 rounded-2xl shadow-md hover:scale-110 transition-transform duration-300 flex items-center justify-center">
              <img 
                src="/assets/images/logos/kiit-official-logo.webp" 
                alt="KIIT University Logo" 
                className="max-h-24 max-w-full object-contain" 
              />
            </div>
          </div>
          <div className="flex justify-center items-center col-span-2 md:col-span-1" data-aos="fade-up" data-aos-delay="300">
            <div className="h-40 w-48 p-4 bg-white border-2 border-blue-300 rounded-2xl shadow-md hover:scale-110 transition-transform duration-300 flex items-center justify-center">
              <img 
                src="/assets/images/logos/ieee-logo.svg" 
                alt="IEEE Technical Partner" 
                className="max-h-20 max-w-full object-contain" 
              />
            </div>
          </div>
        </div>
      </section>


      {/* ======================= ABOUT THE CONFERENCE (#aboutconference) ======================= */}
      <section id="aboutconference" className="w-full bg-[#E7ECFF] py-20 scroll-mt-20">
        <div className="max-w-6xl mx-auto px-6">
          
          <div className="text-center mb-16" data-aos="fade-up">
            <h2 className="text-3xl md:text-4xl font-extrabold tracking-wide text-blue-900 mb-6 font-heading">
              ABOUT THE CONFERENCE
            </h2>
            <p className="max-w-4xl mx-auto text-base sm:text-lg text-slate-700 leading-relaxed">
              The <strong>2027 International Conference on Advances in Computing, Intelligence and Engineering (ACIE 2027)</strong>, hosted and organized by <strong>Kalinga Institute of Industrial Technology (KIIT)</strong>, Bhubaneswar in association with the peer-reviewed open access journal <strong>ACIE</strong> (<a href="https://acieopen.com/" target="_blank" rel="noreferrer" className="text-blue-800 underline">acieopen.com</a>), is an international forum for researchers, academicians, and engineers. Covering disciplines from machine learning, edge transformers, post-quantum cryptography, and autonomous robotics to smart healthcare and sustainable green technologies, the conference promotes high-impact scientific exchange and global collaboration.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-10 items-stretch">
            
            {/* Conference Mission Card */}
            <div 
              data-aos="fade-right"
              className="relative p-8 rounded-2xl bg-gradient-to-r from-blue-50 to-green-50 shadow-md border border-blue-200/60 flex flex-col justify-between"
            >
              <div>
                <h3 className="text-2xl md:text-3xl font-bold text-slate-900 mb-6 text-center font-heading">
                  Conference Mission
                </h3>
                <ul className="space-y-4">
                  <li data-aos="fade-up" data-aos-delay="100" className="flex items-start gap-3">
                    <span className="text-green-600 mt-1 text-2xl shrink-0">🎯</span>
                    <span className="text-slate-700 text-sm sm:text-base leading-relaxed">
                      Provides an interdisciplinary international platform to showcase AI-enabled computing and engineering innovations addressing challenges in industry, governance, healthcare, and sustainable development.
                    </span>
                  </li>
                  <li data-aos="fade-up" data-aos-delay="200" className="flex items-start gap-3">
                    <span className="text-blue-600 mt-1 text-2xl shrink-0">🎯</span>
                    <span className="text-slate-700 text-sm sm:text-base leading-relaxed">
                      Focuses on advanced technologies including post-quantum embedded security, edge-quantized transformers, autonomous swarm robotics, smart cyber-physical telemetry, and green computing.
                    </span>
                  </li>
                  <li data-aos="fade-up" data-aos-delay="300" className="flex items-start gap-3">
                    <span className="text-purple-600 mt-1 text-2xl shrink-0">🎯</span>
                    <span className="text-slate-700 text-sm sm:text-base leading-relaxed">
                      Encourages global collaboration among researchers, industry leaders, and policymakers to enhance peer-reviewed technical rigor, real-world deployment, and open-access knowledge dissemination.
                    </span>
                  </li>
                </ul>
              </div>

              <div className="pt-6 mt-6 border-t border-slate-200 flex items-center justify-between">
                <Link to="/aboutkiit" className="text-xs font-bold text-blue-700 hover:text-blue-900 flex items-center gap-1">
                  <span>Explore KIIT Campus &amp; Infrastructure</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </Link>
              </div>
            </div>

            {/* Conference Vision Card with zoom effect and blur circle */}
            <div 
              data-aos="fade-left"
              className="group relative rounded-2xl overflow-hidden shadow-xl border border-slate-200 transition-all duration-500 hover:shadow-2xl hover:-translate-y-1 min-h-[380px] flex flex-col justify-end"
            >
              <img 
                src="/assets/images/kiit/kiit-convention-center.webp" 
                alt="Conference Vision Venue" 
                className="absolute inset-0 w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-110"
                loading="lazy"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/45 to-transparent" />
              <div className="absolute -bottom-16 -left-16 w-48 h-48 bg-[#E7ECFF] rounded-full blur-3xl opacity-40 pointer-events-none" />

              <div className="relative z-10 p-8 text-white space-y-3">
                <span className="px-3 py-1 rounded-full bg-blue-500/30 text-cyan-300 text-xs font-bold uppercase tracking-wider border border-blue-400/40 inline-block">
                  Vision &amp; Global Impact
                </span>
                <h3 className="text-2xl sm:text-3xl font-bold font-heading">
                  Conference Vision
                </h3>
                <p className="text-slate-200 text-sm sm:text-base leading-relaxed italic opacity-95 group-hover:opacity-100 transition-opacity duration-500">
                  "Advancing intelligent computational paradigms and resilient engineering architectures across industry, governance, healthcare, and sustainable societies through rigorous peer-reviewed scholarship and inclusive international partnership."
                </p>
              </div>
            </div>

          </div>

        </div>
      </section>


      {/* ======================= VENUE & CULTURE 3D FLIP CARDS ======================= */}
      <section 
        className="relative pt-12 pb-20 bg-cover bg-center"
        style={{ backgroundImage: `url('/assets/images/scraped/map-BfyYLnYn.jpg')` }}
      >
        <div className="absolute inset-0 bg-[#E7ECFF]/70 backdrop-blur-[2px]" />

        <div className="relative z-10 max-w-[1800px] mx-auto px-4 sm:px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-12 px-4" data-aos="fade-up">
            <h2 className="text-3xl md:text-4xl font-extrabold text-blue-900 tracking-wide font-heading">
              Venue &amp; Odisha Heritage
            </h2>
            <p className="mt-3 text-slate-700 text-base sm:text-lg">
              Hosted at <strong>KIIT Deemed to be University</strong>, Bhubaneswar — explore the ancient architectural wonders and serene natural sanctuaries of Odisha.
            </p>
          </div>

          <div className="flex flex-col lg:flex-row gap-8 w-full">
            
            {/* Conference Venue Card (1/3 width) */}
            <div className="lg:w-1/3 bg-white/90 backdrop-blur-md rounded-3xl p-8 shadow-xl border border-blue-200 flex flex-col justify-between" data-aos="fade-right">
              <div>
                <h3 className="text-2xl font-bold mb-6 text-slate-900 font-heading">
                  Conference Venue
                </h3>
                
                <div className="flex items-start gap-3 mb-6">
                  <span className="text-blue-700 text-2xl shrink-0 mt-1">📍</span>
                  <div>
                    <h4 className="font-bold text-slate-900 text-base">
                      Kalinga Institute of Industrial Technology (KIIT)
                    </h4>
                    <p className="text-slate-600 text-sm mt-1">
                      Auditorium Complex, Campus 6, Patia, Bhubaneswar, Odisha – 751024, India
                    </p>
                  </div>
                </div>

                <div className="space-y-3 p-4 rounded-2xl bg-blue-50/80 border border-blue-200/60 text-xs sm:text-sm text-slate-700 mb-6">
                  <p><strong>✈️ Airport:</strong> Biju Patnaik International Airport (~14 km)</p>
                  <p><strong>🚆 Rail:</strong> Bhubaneswar Railway Station (~12 km)</p>
                  <p><strong>🌐 Mode:</strong> Hybrid (In-Person &amp; Virtual Plenary Stream)</p>
                </div>
              </div>

              <div>
                <a
                  href="https://maps.google.com/?q=KIIT+University+Bhubaneswar"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full inline-flex items-center justify-center gap-2 border-2 border-blue-900 text-blue-900 font-bold px-6 py-3 rounded-xl hover:bg-blue-900 hover:text-white transition-all duration-300 shadow-sm"
                >
                  <span>➜ Get Directions on Google Maps</span>
                </a>
              </div>
            </div>

            {/* 3D Flip Cards Showcase (2/3 width) */}
            <div className="lg:w-2/3 rounded-3xl p-6 sm:p-8 bg-white/80 backdrop-blur-md shadow-xl border border-blue-200" data-aos="fade-left">
              <h3 className="text-2xl font-bold mb-6 text-slate-900 font-heading">
                Experience the Culture &amp; Heritage (Tap or Hover to Flip)
              </h3>

              {/* Responsive 3D Flip Card Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {TOURISM_DESTINATIONS.map((item) => (
                  <div 
                    key={item.id} 
                    className="relative w-full aspect-[6/5] cursor-pointer perspective-1000 group"
                  >
                    <div 
                      className="relative w-full h-full transition-transform duration-700 transform-style-preserve-3d"
                      onMouseEnter={(e) => { e.currentTarget.style.transform = "rotateY(180deg) scale(1.05)"; }}
                      onMouseLeave={(e) => { e.currentTarget.style.transform = "rotateY(0deg) scale(1)"; }}
                      onClick={(e) => {
                        const cur = e.currentTarget.style.transform;
                        e.currentTarget.style.transform = cur.includes("180deg") ? "rotateY(0deg) scale(1)" : "rotateY(180deg) scale(1.05)";
                      }}
                    >
                      {/* Front Card Face */}
                      <div 
                        className="absolute inset-0 rounded-2xl overflow-hidden shadow-lg backface-hidden"
                        style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden" }}
                      >
                        <img 
                          src={item.image} 
                          alt={item.name} 
                          className="absolute inset-0 w-full h-full object-cover" 
                          loading="lazy"
                          decoding="async"
                        />
                        <div className="absolute inset-0 bg-black/30" />
                        <div className="absolute bottom-3 sm:bottom-4 left-3 sm:left-4 right-3 sm:right-4 text-white">
                          <h4 className="font-semibold text-base sm:text-lg leading-snug drop-shadow">{item.name}</h4>
                          <p className="text-xs sm:text-sm drop-shadow opacity-90">{item.distance}</p>
                        </div>
                      </div>

                      {/* Back Card Face (Revealed on 3D Flip matching original aisigh-sd.co.in) */}
                      <div 
                        className="absolute inset-0 rounded-2xl bg-blue-900 text-white p-3.5 sm:p-5 flex items-center justify-center text-center shadow-lg backface-hidden"
                        style={{
                          backfaceVisibility: "hidden",
                          WebkitBackfaceVisibility: "hidden",
                          transform: "rotateY(180deg)"
                        }}
                      >
                        <p className="text-xs sm:text-[13px] md:text-sm font-normal leading-relaxed max-h-full overflow-hidden select-none">
                          {item.history}
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

            </div>

          </div>

        </div>
      </section>


      {/* ======================= SCHEDULE & MARQUEE ANNOUNCEMENT (#schedule) ======================= */}
      <section id="schedule" className="py-16 bg-[#E7ECFF] border-t border-blue-200 overflow-x-hidden scroll-mt-20">
        <div className="max-w-4xl mx-auto px-4" data-aos="fade-up">
          
          <div className="text-center mb-12">
            <h2 className="text-2xl sm:text-3xl font-bold text-slate-900 font-heading">
              Important Dates
            </h2>
            <p className="text-slate-600 mt-2 text-sm sm:text-base">
              Paper submission &amp; acceptance milestones
            </p>
          </div>

          {/* Marquee Announcement Ticker matching aisigh-sd.co.in */}
          <div className="flex w-max flex-nowrap animate-deadline-marquee motion-reduce:animate-none">
            <span className="shrink-0 px-8 tracking-widest whitespace-nowrap text-white font-bold bg-blue-600 py-1.5" aria-hidden="true">
              📢 Early Bird Registration for the conference has already begun.
            </span>
            <span className="shrink-0 px-8 tracking-widest whitespace-nowrap text-white font-bold bg-blue-600 py-1.5" aria-hidden="true">
              📢 Early Bird Registration for the conference has already begun.
            </span>
            <span className="shrink-0 px-8 tracking-widest whitespace-nowrap text-white font-bold bg-blue-600 py-1.5" aria-hidden="true">
              📢 Early Bird Registration for the conference has already begun.
            </span>
            <span className="shrink-0 px-8 tracking-widest whitespace-nowrap text-white font-bold bg-blue-600 py-1.5" aria-hidden="true">
              📢 Early Bird Registration for the conference has already begun.
            </span>
          </div>

          {/* Timeline Table Box matching original styling exactly from Home-7Lgsr6xV.js */}
          <div className="flex items-center justify-center p-4 mt-8">
            <div className="w-full max-w-xl bg-gradient-to-b from-gray-200 to-gray-300 rounded-xl shadow-lg border border-gray-400 overflow-hidden">
              
              {/* Header with decorative dividers in exact orange-600 and orange-800 */}
              <div className="pt-8 pb-4 text-center">
                <h2 className="text-3xl font-bold text-orange-600 uppercase tracking-tight font-heading">
                  Keynote Speakers
                </h2>
                <div className="flex items-center justify-center my-2">
                  <div className="h-0.5 w-16 bg-orange-800" />
                  <div className="h-2 w-8 bg-orange-800 mx-1" />
                  <div className="h-0.5 w-16 bg-orange-800" />
                </div>
                <h3 className="text-4xl font-bold text-orange-600 mt-4 italic font-heading">
                  Time Line
                </h3>
                <div className="flex items-center justify-center mt-2 mb-6">
                  <div className="h-0.5 w-16 bg-orange-800" />
                  <div className="h-2 w-8 bg-orange-800 mx-1" />
                  <div className="h-0.5 w-16 bg-orange-800" />
                </div>
              </div>

              {/* Table with border-gray-500 matching original */}
              <div className="px-6 pb-12">
                <div className="border border-gray-500 overflow-hidden bg-transparent">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-transparent">
                        <th className="py-3 px-4 text-xl font-bold text-slate-800 border-r border-b border-gray-500">
                          Event
                        </th>
                        <th className="py-3 px-4 text-xl font-bold text-slate-800 border-b border-gray-500">
                          Date
                        </th>
                      </tr>
                    </thead>
                    <tbody className="text-slate-700 font-medium text-xs sm:text-sm">
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Paper Submission Begins
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono">
                          10/02/2026
                        </td>
                      </tr>
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Paper Submission Deadline
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono">
                          <strike className="text-gray-500 mr-2">15/09/2026</strike>
                          <strike className="text-gray-500 mr-2">30/09/2026</strike>
                          <b>10/10/2026</b>
                        </td>
                      </tr>
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Notification of Acceptance
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono">
                          15/08/2026 - 25/11/2026
                        </td>
                      </tr>
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Registration &amp; Camera Ready Copy Submission Begins
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono">
                          25/10/2026
                        </td>
                      </tr>
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Camera-Ready Submission Deadline
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono font-bold text-slate-900">
                          30/11/2026
                        </td>
                      </tr>
                      <tr>
                        <td className="py-3.5 px-4 border-r border-b border-gray-500">
                          Last Date of Registration
                        </td>
                        <td className="py-2 px-4 border-b border-gray-500 font-mono font-bold text-slate-900">
                          10/12/2026
                        </td>
                      </tr>
                      <tr>
                        <td className="py-4 px-4 border-r border-gray-500 font-bold text-slate-900">
                          Date of Conference
                        </td>
                        <td className="py-4 px-4 font-mono font-bold text-blue-900">
                          22/01/2027 - 24/01/2027
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

            </div>
          </div>

        </div>
      </section>


      {/* ======================= 10 THEMATIC TRACKS PREVIEW ======================= */}
      <section className="py-20 bg-slate-50 border-t border-slate-200">
        <div className="container mx-auto px-4 sm:px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-14" data-aos="fade-up">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-bold uppercase tracking-wider mb-3">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Call For Papers</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-900 font-heading tracking-tight">
              10 Thematic Conference Tracks
            </h2>
            <p className="text-slate-600 text-sm sm:text-base mt-2">
              Submissions are invited across state-of-the-art computational domains, intelligent cybernetics, and engineering solutions.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {TRACKS.slice(0, 6).map((track, idx) => (
              <div 
                key={track.id} 
                data-aos="fade-up"
                data-aos-delay={(idx % 3) * 100}
                className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl border border-slate-200 hover:border-blue-300 transition-all duration-300 flex flex-col justify-between group"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <span className="w-10 h-10 rounded-xl bg-blue-50 group-hover:bg-blue-600 text-blue-600 group-hover:text-white flex items-center justify-center font-bold text-sm transition-colors duration-200">
                      T{track.id}
                    </span>
                    <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">ACIE 2027</span>
                  </div>

                  <h3 className="font-bold text-slate-900 text-base mb-2 group-hover:text-blue-600 transition-colors">
                    {track.title.split(': ')[1]}
                  </h3>

                  <p className="text-xs text-slate-600 leading-relaxed mb-4">
                    {track.description}
                  </p>
                </div>

                <div className="flex flex-wrap gap-1.5 pt-3 border-t border-slate-100">
                  {track.tags.map((tag, i) => (
                    <span key={i} className="text-[10px] font-medium bg-slate-100 text-slate-600 px-2 py-0.5 rounded">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-10" data-aos="fade-up">
            <Link
              to="/callForPapers"
              className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm shadow-md hover:shadow-lg transition-all"
            >
              <span>View All 10 Tracks &amp; Author Guidelines</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

        </div>
      </section>


      {/* ======================= KEYNOTE SPEAKERS SHOWCASE ======================= */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 sm:px-6">
          
          <div className="text-center max-w-3xl mx-auto mb-14" data-aos="fade-up">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-50 border border-purple-200 text-purple-700 text-xs font-bold uppercase tracking-wider mb-3">
              <Users className="w-3.5 h-3.5" />
              <span>Distinguished Global Faculty</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-900 font-heading tracking-tight">
              Featured Keynote Luminaries
            </h2>
            <p className="text-slate-600 text-sm sm:text-base mt-2">
              Learn from pioneering researchers shaping next-generation artificial intelligence, post-quantum cybersecurity, and autonomous mobility.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {KEYNOTE_SPEAKERS.slice(0, 4).map((speaker, idx) => (
              <div 
                key={speaker.id} 
                data-aos="fade-up"
                data-aos-delay={idx * 100}
                className="bg-white rounded-2xl overflow-hidden shadow-lg border border-slate-200 hover:shadow-2xl transition-all duration-300 group flex flex-col hover:-translate-y-1.5"
              >
                <div className="relative h-64 overflow-hidden bg-slate-100">
                  <img 
                    src={speaker.image} 
                    alt={speaker.name} 
                    className="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500" 
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent" />
                  <div className="absolute bottom-3 left-3 right-3 text-white">
                    <span className="text-[11px] font-semibold text-cyan-300 uppercase tracking-wider block">Keynote Address</span>
                    <h3 className="font-bold text-base font-heading">{speaker.name}</h3>
                  </div>
                </div>

                <div className="p-4 flex-1 flex flex-col justify-between space-y-3 bg-white">
                  <div>
                    <p className="text-xs font-semibold text-blue-700 mb-1">{speaker.title}</p>
                    <p className="text-xs text-slate-500 font-medium">{speaker.affiliation}</p>
                  </div>
                  <div className="pt-2 border-t border-slate-100 text-[11px] text-slate-600 line-clamp-3">
                    {speaker.bio}
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-10" data-aos="fade-up">
            <Link
              to="/keynote-speakers"
              className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm shadow-md hover:shadow-lg transition-all"
            >
              <span>Explore All 10 Keynote Speakers</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

        </div>
      </section>

    </main>
  );
}
