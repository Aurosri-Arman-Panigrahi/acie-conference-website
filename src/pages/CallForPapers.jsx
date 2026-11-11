import React from 'react';
import PageBanner from '../components/PageBanner';

export default function CallForPapers() {
  const tracks = [
    "Artificial Intelligence, Machine Learning and Deep Learning",
    "Internet of Things (IoT), Edge AI, and Cyber-Physical Systems",
    "Natural Language Processing, Computer Vision, and Multimodal AI",
    "AI in Healthcare and Biomedical Engineering",
    "AI for Smart Electrical and Power Systems",
    "AI-Driven Smart Manufacturing and Industry 4.0",
    "AI Applications in Aerospace Systems",
    "AI in Mining Engineering and Resource Exploration",
    "AI for Smart Governance and Digital Public Infrastructure",
    "Sustainable Development, Green AI, and Environmental Intelligence"
  ];

  return (
    <div className="w-full">
      <PageBanner 
        title="CALL FOR PAPERS" 
        subtitle="Call for original, high-quality, and unpublished research papers across computing and engineering"
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div className="max-w-5xl mx-auto px-6 text-slate-700 space-y-8">
          
          <div data-aos="fade-up">
            <p className="mb-6 text-lg leading-relaxed text-slate-800">
              The conference seeks original research papers in all aspects of Computing, Intelligence, and Electrical/Computer Engineering. Specifically, it covers (but is not limited to) the following tracks:
            </p>

            <ol className="list-decimal list-inside space-y-2.5 text-base font-medium text-slate-800 bg-white/80 p-8 rounded-2xl border border-blue-200/50 shadow-md hover:shadow-lg transition-all duration-300">
              {tracks.map((track, idx) => (
                <li key={idx} className="hover:text-blue-700 hover:translate-x-1 transition-all duration-200">
                  {track}
                </li>
              ))}
            </ol>
          </div>

          <div data-aos="fade-up" data-aos-delay="100">
            <h2 className="mb-4 text-3xl font-extrabold text-slate-900 font-heading">
              Submission Guidelines:
            </h2>
            <ol className="list-decimal list-inside space-y-3.5 text-base text-slate-700 leading-relaxed bg-white/80 p-8 rounded-2xl border border-blue-200/50 shadow-md hover:shadow-lg transition-all duration-300">
              <li>
                Authors are required to submit their manuscripts using Microsoft CMT by following the provided link:
                <br />
                <a 
                  href="https://cmt3.research.microsoft.com/" 
                  target="_blank" 
                  rel="noreferrer" 
                  className="text-orange-600 hover:underline break-all font-mono font-medium ml-4 inline-block mt-1"
                >
                  https://cmt3.research.microsoft.com/ACIE2027
                </a>
              </li>
              <li>
                Please ensure that your manuscript adheres to the specified length requirement of 4–6 pages, following standard 2-column format guidelines.
                <br />
                <span className="ml-4 inline-block mt-1">
                  Templates:{' '}
                  <a 
                    href="https://acieopen.com/" 
                    target="_blank" 
                    rel="noreferrer" 
                    className="text-orange-600 hover:underline break-all"
                  >
                    https://acieopen.com/templates
                  </a>
                </span>
              </li>
              <li>
                The submission of manuscripts should be done in <strong>PDF format only</strong>.
              </li>
              <li>
                All submitted papers will undergo a rigorous double-blind peer-review process. Acceptance decisions will be made based on criteria including quality, originality, technical content, and relevance to the conference theme.
              </li>
              <li>
                Every paper submitted will undergo plagiarism detection using anti-plagiarism software prior to review. Papers found to not meet the plagiarism policy (&lt;20% similarity) may be desk-rejected without further review.
              </li>
              <li>
                Only registered and presented papers will be forwarded for publication in the peer-reviewed open access journal <strong>ACIE</strong> (<a href="https://acieopen.com/" target="_blank" rel="noreferrer" className="text-blue-600 underline">https://acieopen.com/</a>). The ‘No Show’ policy will be enforced, whereby papers that are not presented at the conference will not be eligible for indexation.
              </li>
              <li>
                ACIE 2027 strictly prohibits authors from altering their author details or sequence once a manuscript has been submitted.
              </li>
            </ol>
          </div>

          <div data-aos="fade-up" data-aos-delay="200">
            <h2 className="mb-4 text-3xl font-extrabold text-slate-900 font-heading">
              Publication:
            </h2>
            <p className="mb-6 text-lg leading-relaxed text-slate-700 bg-white/80 p-8 rounded-2xl border border-blue-200/50 shadow-md hover:shadow-lg transition-all duration-300">
              All accepted and presented papers will be published in conference e-proceedings and considered for publication in <strong>ACIE: Advances in Computing, Intelligence and Engineering</strong> (ISSN Open Access | <a href="https://acieopen.com/" target="_blank" rel="noreferrer" className="text-blue-600 underline">https://acieopen.com/</a>), indexed across Google Scholar, CrossRef DOI, and major indexing databases within 30 days of the conference.
            </p>
          </div>

          <div data-aos="fade-up" data-aos-delay="300">
            <h3 className="mb-4 text-2xl font-extrabold text-slate-900 font-heading">
              CMT ACKNOWLEDGMENT:
            </h3>
            <p className="text-base text-slate-600 leading-relaxed bg-white/80 p-8 rounded-2xl border border-blue-200/50 shadow-md">
              The Microsoft CMT service was used for managing the peer-reviewing process for this conference. This service was provided for free by Microsoft and they bore all expenses, including costs for Azure cloud services as well as for software development and support.
            </p>
          </div>

        </div>
      </div>
    </div>
  );
}
