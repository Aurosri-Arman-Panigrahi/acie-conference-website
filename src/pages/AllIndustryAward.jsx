import React from 'react';
import PageBanner from '../components/PageBanner';

export default function AllIndustryAward() {
  return (
    <div className="w-full">
      <PageBanner 
        title="ALL INDUSTRY AUTHORED PAPER AWARD" 
        subtitle="Recognizing impactful research driven by industry expertise and innovation"
      />

      <div className="bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-left space-y-6 hover:shadow-2xl transition-all duration-300">
            
            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">🏭</span>
              <p className="text-lg leading-relaxed text-gray-800">
                From all accepted submissions, <strong>one outstanding paper authored entirely by industry-affiliated contributors</strong> will be selected for the <strong>All-Industry Authored Paper Award</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">📌</span>
              <p className="text-lg leading-relaxed text-gray-800">
                Eligibility requires that <strong>all authors are affiliated with industry</strong>, highlighting real-world problem-solving and applied research excellence.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">⭐</span>
              <p className="text-lg leading-relaxed text-gray-800">
                The selection will be based on the <strong>quality and originality of the work</strong>, the <strong>effectiveness of the presentation</strong>, and the <strong>practical impact of the findings in commercial or industrial engineering applications</strong>.
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
