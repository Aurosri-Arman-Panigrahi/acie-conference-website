import React, { useState, useEffect } from 'react';
import { HashRouter, Routes, Route, useLocation } from 'react-router-dom';
import AOS from 'aos';

// Layout Components
import MarqueeTicker from './components/MarqueeTicker';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import BrochureModal from './components/BrochureModal';

// Pages
import Home from './pages/Home';
import CallForPapers from './pages/CallForPapers';
import CameraReadySubmission from './pages/CameraReadySubmission';
import PublicationAndTemplates from './pages/PublicationAndTemplates';
import KeynoteSpeakers from './pages/KeynoteSpeakers';
import WIESpeakers from './pages/WIESpeakers';
import Penalties from './pages/Penalties';
import Patrons from './pages/Patrons';
import BestPaper from './pages/BestPaper';
import BestPoster from './pages/BestPoster';
import AllWomenAward from './pages/AllWomenAward';
import AllIndustryAward from './pages/AllIndustryAward';
import Accomodation from './pages/Accomodation';
import Sponsorship from './pages/Sponsorship';
import Registration from './pages/Registration';
import AboutKIIT from './pages/AboutKIIT';

// Scroll to top on route change & refresh AOS
function RouteScrollAndAOSHandler() {
  const { pathname, hash } = useLocation();

  useEffect(() => {
    if (!hash) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      const id = hash.replace('#', '');
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
    // Refresh AOS triggers whenever location changes
    setTimeout(() => {
      AOS.refresh();
    }, 100);
  }, [pathname, hash]);

  return null;
}

export default function App() {
  const [brochureOpen, setBrochureOpen] = useState(false);
  const [isPageLoading, setIsPageLoading] = useState(true);

  // Initialize AOS once on app mount
  useEffect(() => {
    AOS.init({
      duration: 1000,
      once: true,
      offset: 100,
      easing: 'ease-out-cubic',
    });

    const timer = setTimeout(() => {
      setIsPageLoading(false);
    }, 450);

    return () => clearTimeout(timer);
  }, []);

  return (
    <HashRouter>
      <RouteScrollAndAOSHandler />
      
      {/* Top Loading Progress Bar */}
      {isPageLoading && (
        <div className="fixed top-0 left-0 right-0 z-50 h-1 bg-gradient-to-r from-blue-600 via-cyan-400 to-indigo-600 shimmer-loader animate-pulse" />
      )}

      <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans relative">
        
        {/* Fixed Header Navigation (fixed top-0) */}
        <Navbar onOpenBrochure={() => setBrochureOpen(true)} />

        {/* Top Notification Announcement Ticker (mt-20) */}
        <MarqueeTicker />

        {/* Dynamic Main Routes */}
        <main className="flex-1 animate-fadeIn">
          <Routes>
            <Route path="/" element={<Home onOpenBrochure={() => setBrochureOpen(true)} />} />
            
            {/* Authors Dropdown Routes */}
            <Route path="/callForPapers" element={<CallForPapers />} />
            <Route path="/camera-ready-paper-submission" element={<CameraReadySubmission />} />
            <Route path="/publication-and-templates" element={<PublicationAndTemplates />} />
            
            {/* Speakers Dropdown Routes */}
            <Route path="/keynote-speakers" element={<KeynoteSpeakers />} />
            <Route path="/wie-speakers" element={<WIESpeakers />} />
            <Route path="/penalties" element={<Penalties />} />
            
            {/* Committee Route */}
            <Route path="/patrons" element={<Patrons />} />
            
            {/* Awards Dropdown Routes */}
            <Route path="/best-paper" element={<BestPaper />} />
            <Route path="/best-poster" element={<BestPoster />} />
            <Route path="/all-women" element={<AllWomenAward />} />
            <Route path="/all-industry" element={<AllIndustryAward />} />
            
            {/* Accommodation Route */}
            <Route path="/accomodation" element={<Accomodation />} />
            
            {/* Sponsorship Route */}
            <Route path="/sponsership" element={<Sponsorship />} />
            
            {/* Registration Route */}
            <Route path="/registration" element={<Registration />} />
            
            {/* About Institution Routes (both original /aboutcutm and branded /aboutkiit) */}
            <Route path="/aboutcutm" element={<AboutKIIT />} />
            <Route path="/aboutkiit" element={<AboutKIIT />} />
            
            {/* Fallback to Home */}
            <Route path="*" element={<Home onOpenBrochure={() => setBrochureOpen(true)} />} />
          </Routes>
        </main>

        {/* Global Footer */}
        <Footer />

        {/* Brochure Download & View Modal */}
        <BrochureModal 
          isOpen={brochureOpen} 
          onClose={() => setBrochureOpen(false)} 
        />

      </div>
    </HashRouter>
  );
}
