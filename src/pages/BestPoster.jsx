import React from 'react';
import PageBanner from '../components/PageBanner';

export default function BestPoster() {
  return (
    <div className="w-full">
      <PageBanner 
        title="BEST POSTER AWARD" 
        subtitle="Celebrating excellence in poster research and scholarly communication"
      />

      <div className="bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-left space-y-6 hover:shadow-2xl transition-all duration-300">
            
            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">🖼️</span>
              <p className="text-lg leading-relaxed text-gray-800">
                All accepted papers scheduled for <strong>poster presentations</strong> will be considered for the <strong>ACIE 2027 Best Poster Award</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">📊</span>
              <p className="text-lg leading-relaxed text-gray-800">
                In each poster session, one poster will be selected based on the <strong>originality and quality of the research</strong>, the <strong>clarity and visual effectiveness</strong> of the poster, and the <strong>level of engagement during the discussion</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">🏅</span>
              <p className="text-lg leading-relaxed text-gray-800">
                The recipients of the Best Poster Award will be <strong>announced during the Valedictory Session</strong> of ACIE 2027 on January 24, 2027.
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
