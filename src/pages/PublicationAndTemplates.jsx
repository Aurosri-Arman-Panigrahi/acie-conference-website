import React from 'react';
import PageBanner from '../components/PageBanner';

export default function PublicationAndTemplates() {
  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="PUBLICATION AND TEMPLATE" 
        subtitle="ACIE Conference Proceedings, Journal Indexing & Official Manuscript Templates"
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-slate-700">
          
          {/* Publication Card matching aisigh-sd.co.in */}
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-sm p-8 mb-12 border border-slate-200">
            <h2 className="text-2xl font-bold text-slate-900 mb-4 font-heading">
              Publication
            </h2>
            <p className="text-lg leading-relaxed text-slate-700">
              All accepted and presented papers will be published in <span className="font-semibold text-slate-900">e-proceedings</span> and considered for publication in <span className="font-semibold text-slate-900">ACIE: Advances in Computing, Intelligence and Engineering</span> (<a href="https://acieopen.com/" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">https://acieopen.com/</a>), indexed by <span className="font-semibold text-slate-900">Scopus</span> and <span className="font-semibold text-slate-900">Google Scholar</span>.
            </p>
          </div>

          {/* Templates Card matching aisigh-sd.co.in */}
          <div data-aos="fade-up" data-aos-delay="100" className="bg-white rounded-2xl shadow-sm p-8 border border-slate-200">
            <h2 className="text-2xl font-bold text-slate-900 mb-6 font-heading">
              Templates
            </h2>
            <div className="space-y-4 text-lg text-slate-700">
              <p>
                <span className="font-semibold text-slate-900">Paper Submission Template:</span>{' '}
                <a 
                  href="https://www.ieee.org/conferences/publishing/templates" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="text-blue-600 hover:text-blue-700 hover:underline break-all"
                >
                  https://www.ieee.org/conferences/publishing/templates
                </a>
              </p>
              <p>
                <span className="font-semibold text-slate-900">PPT Template:</span>{' '}
                <span className="text-slate-500">(Will be updated soon)</span>
              </p>
              <p>
                <span className="font-semibold text-slate-900">A0 Size Poster Template:</span>{' '}
                <span className="text-slate-500">(Will be updated soon)</span>
              </p>
            </div>
          </div>

        </div>
      </div>
    </main>
  );
}
