import React from 'react';
import PageBanner from '../components/PageBanner';

export default function BestPaper() {
  return (
    <div className="w-full">
      <PageBanner 
        title="BEST PAPER AWARD" 
        subtitle="Recognizing excellence in research quality, presentation, and scholarly impact"
      />

      <div className="bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-left space-y-6 hover:shadow-2xl transition-all duration-300">
            
            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">🏆</span>
              <p className="text-lg leading-relaxed text-gray-800">
                All papers selected for <strong>oral presentations</strong> will automatically be nominated for the <strong>ACIE 2027 Best Paper Award</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">📑</span>
              <p className="text-lg leading-relaxed text-gray-800">
                In each <strong>Technical Session</strong>, one paper will be chosen for the Best Paper Award based on the <strong>quality of research</strong>, <strong>presentation skills</strong>, and <strong>performance during the question-and-answer session</strong>.
              </p>
            </div>

            <div className="flex items-start gap-4">
              <span className="text-blue-600 text-2xl font-bold">🎤</span>
              <p className="text-lg leading-relaxed text-gray-800">
                The winners of the Best Paper Award from each technical session will be <strong>announced during the Valedictory Session</strong> of ACIE 2027 on January 24, 2027.
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
