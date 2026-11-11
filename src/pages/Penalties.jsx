import React from 'react';
import PageBanner from '../components/PageBanner';
import { AlertTriangle, ShieldAlert, XCircle, FileWarning, Ban, DollarSign } from 'lucide-react';

export default function Penalties() {
  const penalties = [
    {
      id: "plagiarism",
      icon: <ShieldAlert className="w-8 h-8 text-rose-600" />,
      title: "1. Plagiarism & Generative AI Similarity Penalty",
      subtitle: "Desk Rejection & Complete Forfeiture of Registration Fees",
      severity: "Strict Disqualification",
      rules: [
        "The overall similarity index of the submitted manuscript must be strictly below 20%, including references, verified via standard plagiarism detection tools (Turnitin / iThenticate).",
        "AI-generated text or unverified synthetic outputs must be strictly below 20% of the manuscript.",
        "Paraphrasing or copying text, algorithms, figures, or data from published sources without explicit attribution constitutes scientific misconduct."
      ],
      application: "How it will be applied: Any manuscript exceeding the similarity threshold will be immediately desk-rejected without peer review. If plagiarism or synthetic fabrication is discovered after acceptance or payment, the paper's acceptance is revoked instantly, the paper is excluded from publication and indexing, and the registration fee will NOT be refunded under any circumstances."
    },
    {
      id: "no-show",
      icon: <Ban className="w-8 h-8 text-orange-600" />,
      title: "2. 'No-Show' Non-Presentation Penalty",
      subtitle: "Exclusion from Conference Proceedings & IEEE / ACIE Indexing",
      severity: "Indexing Barred",
      rules: [
        "At least one registered author of each accepted paper must attend and present the paper during their scheduled technical oral or poster session (in-person or virtual).",
        "Proxy presentations by non-authors are strictly prohibited without prior formal written approval from the General Chairs."
      ],
      application: "How it will be applied: Papers that are not presented during their designated session will be officially designated as 'No-Show'. In strict enforcement of IEEE and ACIE policy, 'No-Show' manuscripts will NOT be published in the conference proceedings, will NOT be submitted for indexing in IEEE Xplore or ACIE Open Access Journal, and no presentation certificates will be issued. No refund of registration fees will be granted."
    },
    {
      id: "author-alteration",
      icon: <FileWarning className="w-8 h-8 text-amber-600" />,
      title: "3. Post-Submission Author Modification Penalty",
      subtitle: "Strict Prohibition Against Altering Author Order or Identity",
      severity: "Immediate Paper Revocation",
      rules: [
        "ACIE 2027 strictly prohibits authors from altering, adding, or removing author names, corresponding author designation, or rearranging the author sequence after the final manuscript submission deadline.",
        "The author list and affiliations on the final Camera-Ready paper must match the original Microsoft CMT submission exactly."
      ],
      application: "How it will be applied: Any discrepancy between the author list in the final manuscript and the original submission will result in an immediate administrative block. If unauthorized changes are detected, the paper will be removed from the publication pipeline and disqualified from inclusion in conference proceedings."
    },
    {
      id: "overlength",
      icon: <DollarSign className="w-8 h-8 text-purple-600" />,
      title: "4. Over-Length Page Charge & Excess Page Penalty",
      subtitle: "Mandatory Additional Fee & Hard 8-Page Ceiling",
      severity: "Financial Penalty & Automatic Cutoff",
      rules: [
        "The standard allowable paper length is 4 to 6 pages, formatted strictly according to the two-column conference template.",
        "Authors may submit up to two (2) additional pages (pages 7 and 8), subject to mandatory over-length page charges.",
        "Under no circumstances will any paper exceed the absolute maximum ceiling of eight (8) pages."
      ],
      application: "How it will be applied: For Indian authors, the 7th page incurs a charge of ₹1,000 and the 8th page incurs ₹2,000. For international authors, the 7th page incurs USD 50 and the 8th page incurs USD 100. Any manuscript exceeding 8 pages will be rejected automatically by the submission system and will not be forwarded for review."
    },
    {
      id: "cancellation",
      icon: <XCircle className="w-8 h-8 text-red-600" />,
      title: "5. Strict Non-Refund & Cancellation Policy",
      subtitle: "Zero Refund Under Any Circumstances",
      severity: "Zero Refund",
      rules: [
        "Conference registration fees cover peer review management, electronic proceedings publication, indexing charges, kit preparation, and conference infrastructure.",
        "Personal travel difficulties, visa delays, or paper withdrawal requests post-acceptance do not qualify for fee reimbursement."
      ],
      application: "How it will be applied: Once payment has been completed and registered, the registration fee is 100% non-refundable and non-transferable under all circumstances. Authors requesting paper withdrawal after payment will have their paper retracted, but all fees remain fully forfeited."
    }
  ];

  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="PENALTIES" 
        subtitle="Conference Ethical Guidelines, Violation Penalties & Policy Enforcement Protocols"
      />

      <div className="w-full bg-[#E7ECFF] py-16 md:py-24">
        <div className="max-w-5xl mx-auto px-6 text-slate-700 space-y-10">
          
          {/* Header Introduction Card */}
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 md:p-10 text-center space-y-3">
            <span className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-rose-50 text-rose-700 text-xs font-bold uppercase tracking-wider border border-rose-200">
              <AlertTriangle className="w-4 h-4" />
              <span>Official Conference Policy</span>
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 font-heading">
              Conference Penalties &amp; Enforcement Regulations
            </h2>
            <p className="text-sm sm:text-base text-slate-600 max-w-3xl mx-auto leading-relaxed">
              To preserve the highest standards of scientific integrity, peer-reviewed rigor, and fairness for all delegates, the ACIE 2027 Organizing Committee enforces strict penalties for ethics violations, non-presentation, and unauthorized modifications.
            </p>
          </div>

          {/* Penalties List */}
          <div className="space-y-8">
            {penalties.map((item, idx) => (
              <div 
                key={item.id}
                data-aos="fade-up"
                data-aos-delay={idx * 100}
                className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 sm:p-8 hover:shadow-md transition-all duration-300 space-y-5"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100">
                  <div className="flex items-center gap-4">
                    <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 shrink-0">
                      {item.icon}
                    </div>
                    <div>
                      <h3 className="text-lg sm:text-xl font-bold text-slate-900 font-heading">
                        {item.title}
                      </h3>
                      <p className="text-xs sm:text-sm text-slate-500 font-medium">
                        {item.subtitle}
                      </p>
                    </div>
                  </div>
                  <span className="self-start sm:self-center px-3 py-1 rounded-full bg-rose-100 text-rose-800 text-xs font-bold whitespace-nowrap">
                    {item.severity}
                  </span>
                </div>

                {/* Rules List */}
                <div className="space-y-2">
                  <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
                    Violation Criteria:
                  </h4>
                  <ul className="list-disc list-inside space-y-1.5 text-xs sm:text-sm text-slate-700 leading-relaxed pl-1">
                    {item.rules.map((rule, rIdx) => (
                      <li key={rIdx}>{rule}</li>
                    ))}
                  </ul>
                </div>

                {/* Application Section */}
                <div className="p-4 rounded-xl bg-rose-50/70 border border-rose-200/60 text-xs sm:text-sm text-rose-950 font-medium leading-relaxed">
                  <strong>{item.application.split(':')[0]}:</strong>
                  <span>{item.application.split(':')[1]}</span>
                </div>

              </div>
            ))}
          </div>

        </div>
      </div>
    </main>
  );
}
