import React, { useState, useEffect, useRef } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { ChevronDown } from 'lucide-react';

export default function Navbar({ onOpenBrochure }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState(null);
  const [mobileExpanded, setMobileExpanded] = useState({});
  const location = useLocation();
  const navigate = useNavigate();
  const dropdownRef = useRef(null);

  // Close dropdown on click outside
  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setActiveDropdown(null);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Handle smooth scroll for anchor links
  const handleAnchorClick = (anchorId) => {
    setActiveDropdown(null);
    setMobileMenuOpen(false);
    if (location.pathname === '/') {
      const el = document.getElementById(anchorId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    } else {
      navigate('/');
      setTimeout(() => {
        const el = document.getElementById(anchorId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
        }
      }, 150);
    }
  };

  const toggleMobileSubmenu = (menu) => {
    setMobileExpanded(prev => ({ ...prev, [menu]: !prev[menu] }));
  };

  return (
    <nav className="fixed top-0 left-0 w-full h-20 z-50 bg-[#E7ECFF] border-b border-blue-200 shadow-xs" ref={dropdownRef}>
      <div className="max-w-7xl mx-auto px-2 sm:px-4 lg:px-2.5 xl:px-6 2xl:px-8 h-full">
        <div className="flex justify-between items-center h-full gap-1.5 xl:gap-2">
          
          {/* Logo Brand (Official ACIE Logo from acie logo folder) */}
          <Link to="/" className="flex items-center gap-2 shrink-0 py-1 group">
            <img 
              src="/assets/images/logos/acie-official-logo-transparent.png" 
              alt="ACIE 2027 Logo" 
              className="h-8 sm:h-9 xl:h-10 w-auto object-contain transition-transform duration-200 group-hover:scale-105" 
            />
          </Link>

          {/* Desktop Navigation Links & Action Buttons (One Single Exact Row matching aisigh-sd.co.in) */}
          <div className="hidden lg:flex items-center space-x-0.5 xl:space-x-1.5 2xl:space-x-2 flex-nowrap shrink-0">
            
            {/* HOME */}
            <Link 
              to="/" 
              className="nav-link whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
            >
              HOME
            </Link>

            {/* ABOUT */}
            <div 
              className="relative group"
              onMouseEnter={() => setActiveDropdown('about')}
              onMouseLeave={() => setActiveDropdown(null)}
            >
              <button 
                onClick={() => setActiveDropdown(activeDropdown === 'about' ? null : 'about')}
                className="nav-link cursor-pointer flex items-center gap-0.5 whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
              >
                <span>ABOUT</span>
                <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${activeDropdown === 'about' ? 'rotate-180' : ''}`} />
              </button>

              <div className={`absolute left-0 top-full pt-1.5 w-56 bg-[#E7ECFF] rounded-md shadow-lg border border-blue-200/80 transition-all duration-200 z-50 ${
                activeDropdown === 'about' ? 'opacity-100 visible' : 'opacity-0 invisible'
              }`}>
                <div className="py-1">
                  <button
                    onClick={() => handleAnchorClick('aboutconference')}
                    className="dropdown-link w-full text-left"
                  >
                    About Conference
                  </button>
                  <Link
                    to="/aboutkiit"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    About KIIT
                  </Link>
                </div>
              </div>
            </div>

            {/* AUTHORS */}
            <div 
              className="relative group"
              onMouseEnter={() => setActiveDropdown('authors')}
              onMouseLeave={() => setActiveDropdown(null)}
            >
              <button 
                onClick={() => setActiveDropdown(activeDropdown === 'authors' ? null : 'authors')}
                className="nav-link cursor-pointer flex items-center gap-0.5 whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
              >
                <span>AUTHORS</span>
                <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${activeDropdown === 'authors' ? 'rotate-180' : ''}`} />
              </button>

              <div className={`absolute left-0 top-full pt-1.5 w-64 bg-[#E7ECFF] rounded-md shadow-lg border border-blue-200/80 transition-all duration-200 z-50 ${
                activeDropdown === 'authors' ? 'opacity-100 visible' : 'opacity-0 invisible'
              }`}>
                <div className="py-1">
                  <Link
                    to="/callForPapers"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Call for Papers
                  </Link>
                  <Link
                    to="/camera-ready-paper-submission"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Camera Ready Paper Submission
                  </Link>
                  <Link
                    to="/publication-and-templates"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Publication and Templates
                  </Link>
                </div>
              </div>
            </div>

            {/* SPEAKERS */}
            <div 
              className="relative group"
              onMouseEnter={() => setActiveDropdown('speakers')}
              onMouseLeave={() => setActiveDropdown(null)}
            >
              <button 
                onClick={() => setActiveDropdown(activeDropdown === 'speakers' ? null : 'speakers')}
                className="nav-link cursor-pointer flex items-center gap-0.5 whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
              >
                <span>SPEAKERS</span>
                <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${activeDropdown === 'speakers' ? 'rotate-180' : ''}`} />
              </button>

              <div className={`absolute left-0 top-full pt-1.5 w-56 bg-[#E7ECFF] rounded-md shadow-lg border border-blue-200/80 transition-all duration-200 z-50 ${
                activeDropdown === 'speakers' ? 'opacity-100 visible' : 'opacity-0 invisible'
              }`}>
                <div className="py-1">
                  <Link
                    to="/keynote-speakers"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Keynote Speakers
                  </Link>
                  <Link
                    to="/wie-speakers"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    WIE Speakers
                  </Link>
                  <Link
                    to="/penalties"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Penalties
                  </Link>
                </div>
              </div>
            </div>

            {/* COMMITTEE */}
            <Link 
              to="/patrons" 
              className="nav-link whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
            >
              COMMITTEE
            </Link>

            {/* AWARDS */}
            <div 
              className="relative group"
              onMouseEnter={() => setActiveDropdown('awards')}
              onMouseLeave={() => setActiveDropdown(null)}
            >
              <button 
                onClick={() => setActiveDropdown(activeDropdown === 'awards' ? null : 'awards')}
                className="nav-link cursor-pointer flex items-center gap-0.5 whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
              >
                <span>AWARDS</span>
                <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${activeDropdown === 'awards' ? 'rotate-180' : ''}`} />
              </button>

              <div className={`absolute left-0 top-full pt-1.5 w-64 bg-[#E7ECFF] rounded-md shadow-lg border border-blue-200/80 transition-all duration-200 z-50 ${
                activeDropdown === 'awards' ? 'opacity-100 visible' : 'opacity-0 invisible'
              }`}>
                <div className="py-1">
                  <Link
                    to="/best-paper"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Best Paper Award
                  </Link>
                  <Link
                    to="/best-poster"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    Best Poster Award
                  </Link>
                  <Link
                    to="/all-women"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    All Women Authored Paper Award
                  </Link>
                  <Link
                    to="/all-industry"
                    onClick={() => setActiveDropdown(null)}
                    className="dropdown-link"
                  >
                    All Industry Authored Paper Award
                  </Link>
                </div>
              </div>
            </div>

            {/* ACCOMODATION */}
            <Link 
              to="/accomodation" 
              className="nav-link whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
            >
              ACCOMODATION
            </Link>

            {/* SCHEDULE */}
            <button 
              onClick={() => handleAnchorClick('schedule')}
              className="nav-link cursor-pointer whitespace-nowrap uppercase !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
            >
              SCHEDULE
            </button>

            {/* SPONSORSHIP */}
            <Link 
              to="/sponsership" 
              className="nav-link whitespace-nowrap !text-[10.5px] xl:!text-[12px] 2xl:!text-[13px] font-semibold px-0.5 xl:px-1 py-1"
            >
              SPONSORSHIP
            </Link>

            {/* REGISTRATION SOLID BLUE PILL */}
            <Link to="/registration" className="shrink-0">
              <button className="bg-blue-600 text-white px-2.5 xl:px-4 2xl:px-5 py-1.5 xl:py-2 rounded-full text-[11px] xl:text-[12px] 2xl:text-[13px] font-semibold hover:bg-blue-900 transition whitespace-nowrap shadow-xs cursor-pointer">
                REGISTRATION
              </button>
            </Link>

            {/* BROCHURE SOLID BLUE PILL (Opens PDF in new tab and triggers modal) */}
            <a 
              href="/assets/brochure/ACIE-2027-Brochure.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="shrink-0"
              onClick={(e) => {
                if (onOpenBrochure) onOpenBrochure();
              }}
            >
              <button 
                type="button"
                className="bg-blue-600 text-white px-2.5 xl:px-4 2xl:px-5 py-1.5 xl:py-2 rounded-full text-[11px] xl:text-[12px] 2xl:text-[13px] font-semibold hover:bg-blue-900 transition whitespace-nowrap shadow-xs cursor-pointer"
              >
                BROCHURE
              </button>
            </a>

          </div>

          {/* Mobile Hamburger Button */}
          <button 
            className="lg:hidden text-slate-800 text-2xl p-2 focus:outline-none"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle Navigation Menu"
          >
            {mobileMenuOpen ? '✕' : '☰'}
          </button>

        </div>
      </div>

      {/* Mobile Menu Dropdown matching aisigh-sd.co.in */}
      {mobileMenuOpen && (
        <div className="lg:hidden absolute top-full left-0 w-full bg-white shadow-xl border-b border-slate-200 z-50 animate-in fade-in slide-in-from-top-2 duration-200 max-h-[80vh] overflow-y-auto">
          <div className="flex flex-col px-6 py-5 space-y-3.5">
            <Link
              to="/"
              onClick={() => setMobileMenuOpen(false)}
              className="nav-link"
            >
              HOME
            </Link>

            {/* About Mobile */}
            <div>
              <button
                onClick={() => toggleMobileSubmenu('about')}
                className="nav-link flex justify-between items-center w-full"
              >
                <span>ABOUT</span>
                <span>{mobileExpanded['about'] ? '▲' : '▼'}</span>
              </button>
              {mobileExpanded['about'] && (
                <div className="ml-4 mt-2 rounded-md bg-[#E7ECFF] shadow-sm flex flex-col p-2 space-y-1">
                  <button
                    onClick={() => handleAnchorClick('aboutconference')}
                    className="dropdown-link text-left"
                  >
                    About Conference
                  </button>
                  <Link
                    to="/aboutkiit"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    About KIIT
                  </Link>
                </div>
              )}
            </div>

            {/* Authors Mobile */}
            <div>
              <button
                onClick={() => toggleMobileSubmenu('authors')}
                className="nav-link flex justify-between items-center w-full"
              >
                <span>AUTHORS</span>
                <span>{mobileExpanded['authors'] ? '▲' : '▼'}</span>
              </button>
              {mobileExpanded['authors'] && (
                <div className="ml-4 mt-2 rounded-md bg-[#E7ECFF] shadow-sm flex flex-col p-2 space-y-1">
                  <Link
                    to="/callForPapers"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Call for Papers
                  </Link>
                  <Link
                    to="/camera-ready-paper-submission"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Camera Ready Paper Submission
                  </Link>
                  <Link
                    to="/publication-and-templates"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Publication and Templates
                  </Link>
                </div>
              )}
            </div>

            {/* Speakers Mobile */}
            <div>
              <button
                onClick={() => toggleMobileSubmenu('speakers')}
                className="nav-link flex justify-between items-center w-full"
              >
                <span>SPEAKERS</span>
                <span>{mobileExpanded['speakers'] ? '▲' : '▼'}</span>
              </button>
              {mobileExpanded['speakers'] && (
                <div className="ml-4 mt-2 rounded-md bg-[#E7ECFF] shadow-sm flex flex-col p-2 space-y-1">
                  <Link
                    to="/keynote-speakers"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Keynote Speakers
                  </Link>
                  <Link
                    to="/wie-speakers"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    WIE Speakers
                  </Link>
                  <Link
                    to="/penalties"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Penalties
                  </Link>
                </div>
              )}
            </div>

            {/* Committee Mobile */}
            <Link
              to="/patrons"
              onClick={() => setMobileMenuOpen(false)}
              className="nav-link"
            >
              COMMITTEE
            </Link>

            {/* Awards Mobile */}
            <div>
              <button
                onClick={() => toggleMobileSubmenu('awards')}
                className="nav-link flex justify-between items-center w-full"
              >
                <span>AWARDS</span>
                <span>{mobileExpanded['awards'] ? '▲' : '▼'}</span>
              </button>
              {mobileExpanded['awards'] && (
                <div className="ml-4 mt-2 rounded-md bg-[#E7ECFF] shadow-sm flex flex-col p-2 space-y-1">
                  <Link
                    to="/best-paper"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Best Paper Award
                  </Link>
                  <Link
                    to="/best-poster"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    Best Poster Award
                  </Link>
                  <Link
                    to="/all-women"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    All Women Authored Paper Award
                  </Link>
                  <Link
                    to="/all-industry"
                    onClick={() => setMobileMenuOpen(false)}
                    className="dropdown-link"
                  >
                    All Industry Authored Paper Award
                  </Link>
                </div>
              )}
            </div>

            {/* Accommodation Mobile */}
            <Link
              to="/accomodation"
              onClick={() => setMobileMenuOpen(false)}
              className="nav-link"
            >
              ACCOMODATION
            </Link>

            {/* Schedule Mobile */}
            <button
              onClick={() => handleAnchorClick('schedule')}
              className="nav-link text-left"
            >
              SCHEDULE
            </button>

            {/* Sponsorship Mobile */}
            <Link
              to="/sponsership"
              onClick={() => setMobileMenuOpen(false)}
              className="nav-link"
            >
              SPONSORSHIP
            </Link>

            {/* Mobile Actions */}
            <div className="pt-2 flex flex-col sm:flex-row gap-3">
              <Link 
                to="/registration" 
                onClick={() => setMobileMenuOpen(false)}
                className="w-full text-center bg-blue-600 text-white px-5 py-2.5 rounded-full font-semibold hover:bg-blue-900 transition"
              >
                REGISTRATION
              </Link>

              <a
                href="/assets/brochure/ACIE-2027-Brochure.pdf"
                target="_blank"
                rel="noopener noreferrer"
                onClick={() => {
                  setMobileMenuOpen(false);
                  if (onOpenBrochure) onOpenBrochure();
                }}
                className="w-full text-center bg-blue-600 text-white px-5 py-2.5 rounded-full font-semibold hover:bg-blue-900 transition"
              >
                BROCHURE
              </a>
            </div>

          </div>
        </div>
      )}
    </nav>
  );
}
