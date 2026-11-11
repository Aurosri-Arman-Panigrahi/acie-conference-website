import React from 'react';
import PageBanner from '../components/PageBanner';

export default function AllWomenAward() {
  return (
    <div className="w-full">
      <PageBanner 
        title="ALL WOMEN AUTHORED PAPER AWARD" 
        subtitle="Celebrating excellence and leadership by women in research and innovation"
      />

      <div className="bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-left space-y-6 hover:shadow-2xl transition-all duration-300">
            
            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">👩‍🔬</span>
              <p className="text-lg leading-relaxed text-gray-800">
                From all accepted papers, <strong>one exceptional paper authored entirely by women</strong> will be selected for the <strong>All-Women Authored Paper Award</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">📄</span>
              <p className="text-lg leading-relaxed text-gray-800">
                Eligibility requires that <strong>all contributing authors are women</strong>, highlighting collaborative excellence and inclusive research leadership.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">⭐</span>
              <p className="text-lg leading-relaxed text-gray-800">
                The selection will be based on the <strong>technical quality of the work</strong>, the <strong>clarity and effectiveness of the presentation</strong>, and the <strong>engagement demonstrated during the question-and-answer session</strong>.
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
