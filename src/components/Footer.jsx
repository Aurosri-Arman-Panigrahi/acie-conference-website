import React from 'react';
import { Link } from 'react-router-dom';
import { CONFERENCE_INFO } from '../data/conferenceData';

export default function Footer() {
  return (
    <>
      {/* Bottom Gradient Section matching exact aisigh-sd.co.in styling */}
      <section className="bg-gradient-to-r from-blue-200 via-indigo-200 to-blue-300 text-slate-900 py-6">
        <div className="max-w-5xl mx-auto px-4 grid grid-cols-1 md:grid-cols-2 mt-8 gap-14">
          
          {/* Card 1: CONTACT US */}
          <div className="bg-white/90 rounded-xl p-5 shadow-lg border border-blue-200" data-aos="fade-up">
            <h3 className="text-orange-600 text-lg font-semibold mb-3 tracking-wide font-heading">
              CONTACT US
            </h3>
            <div className="space-y-3 text-[13px] leading-snug">
              <p className="flex gap-2">
                <span className="text-orange-500 text-base">📍</span>
                <span>
                  <strong>School of Computer Engineering</strong><br />
                  Centurion University of Technology and Management (CUTM) &amp; KIIT University<br />
                  Bhubaneswar, Odisha – 751024, India
                </span>
              </p>
              <p>
                <strong>Email:</strong> <span className="text-blue-800"> contact@acieopen.com</span>
              </p>
              <p>
                <strong>Contact:</strong> <span className="text-blue-800 font-semibold">+91-9437376421</span>
              </p>
              <p>
                <strong>Website:</strong>{' '}
                <a href="https://acieopen.com" target="_blank" rel="noopener noreferrer" className="text-blue-800 hover:underline">
                  acieopen.com
                </a>{' '}
                |{' '}
                <a href="https://www.cutm.ac.in" target="_blank" rel="noopener noreferrer" className="text-blue-800 hover:underline">
                  cutm.ac.in
                </a>
              </p>
            </div>
          </div>

          {/* Card 2: TECHNICAL CO-SPONSORS */}
          <div className="bg-white/90 rounded-xl p-5 shadow-lg border border-blue-200" data-aos="fade-up" data-aos-delay="200">
            <h3 className="text-orange-600 text-lg font-semibold mb-3 tracking-wide font-heading">
              TECHNICAL CO-SPONSORS
            </h3>
            <ul className="space-y-3 text-[13px]">
              <li className="flex items-center gap-2">
                <span className="text-orange-500 text-sm">✔</span>
                ACIE: Advances in Computing, Intelligence and Engineering
              </li>
              <li className="flex items-center gap-2">
                <span className="text-orange-500 text-sm">✔</span>
                IEEE Bhubaneswar Section
              </li>
              <li className="flex items-center gap-2">
                <span className="text-orange-500 text-sm">✔</span>
                IEEE COMPUTER SOCIETY CHAPTER (CH11163)
              </li>
              <li className="flex items-center gap-2">
                <span className="text-orange-500 text-sm">✔</span>
                Centurion University of Technology and Management
              </li>
            </ul>
          </div>

        </div>
      </section>

      {/* Bottom Copyright Strip matching exact aisigh-sd.co.in styling */}
      <footer className="border-t border-slate-200 bg-white">
        <div className="max-w-6xl mx-auto px-4 py-3 flex flex-col md:flex-row justify-between items-center text-sm" data-aos="fade-up" data-aos-delay="300">
          <span className="text-slate-400">© 2026–2027 ACIE / AISIGH-SD Conference. All rights reserved.</span>
          <div className="flex gap-6 mt-2 md:mt-0">
            <a href="https://acieopen.com/" target="_blank" rel="noopener noreferrer" className="text-slate-500 hover:text-slate-900 transition">
              Journal
            </a>
            <Link to="/patrons" className="text-slate-500 hover:text-slate-900 transition">
              Committee
            </Link>
            <Link to="/registration" className="text-slate-500 hover:text-slate-900 transition">
              Registration
            </Link>
            <Link to="/accomodation" className="text-slate-500 hover:text-slate-900 transition">
              Accomodation
            </Link>
          </div>
        </div>
      </footer>
    </>
  );
}
