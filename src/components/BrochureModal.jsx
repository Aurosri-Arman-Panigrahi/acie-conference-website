import React from 'react';
import { X, Download, FileText, CheckCircle2, Calendar, MapPin, ExternalLink, ShieldCheck } from 'lucide-react';
import { CONFERENCE_INFO, IMPORTANT_DATES } from '../data/conferenceData';

export default function BrochureModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm animate-in fade-in duration-200">
      <div 
        className="bg-white rounded-2xl shadow-2xl border border-slate-200 max-w-2xl w-full max-h-[90vh] overflow-y-auto overflow-x-hidden relative"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-900 via-blue-800 to-indigo-900 text-white p-6 rounded-t-2xl relative">
          <button 
            onClick={onClose}
            className="absolute top-4 right-4 p-1.5 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
          
          <div className="flex items-center gap-3 mb-2">
            <span className="px-2.5 py-0.5 rounded-full bg-amber-400 text-slate-900 text-xs font-bold uppercase tracking-wider">
              Official Brochure
            </span>
            <span className="text-xs text-blue-200 font-medium">January 22–24, 2027</span>
          </div>

          <h2 className="text-xl sm:text-2xl font-extrabold font-heading tracking-tight">
            ACIE 2027 Conference Information Packet
          </h2>
          <p className="text-xs sm:text-sm text-blue-100 mt-1">
            Advances in Computing, Intelligence and Engineering • KIIT Bhubaneswar, India
          </p>
        </div>

        {/* Body */}
        <div className="p-6 space-y-6 text-slate-700 text-sm">
          
          {/* Quick Summary Highlights */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="p-3.5 rounded-xl bg-blue-50 border border-blue-200/70 flex items-start gap-3">
              <Calendar className="w-5 h-5 text-blue-600 shrink-0 mt-0.5" />
              <div>
                <strong className="block text-slate-900 text-xs uppercase tracking-wider">Dates</strong>
                <span className="text-slate-700 text-sm font-medium">January 22–24, 2027</span>
              </div>
            </div>
            <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200/70 flex items-start gap-3">
              <MapPin className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />
              <div>
                <strong className="block text-slate-900 text-xs uppercase tracking-wider">Host &amp; Venue</strong>
                <span className="text-slate-700 text-sm font-medium">KIIT University, Bhubaneswar</span>
              </div>
            </div>
          </div>

          {/* Publication and Indexing */}
          <div className="border border-slate-200 rounded-xl p-4 bg-slate-50 space-y-2">
            <div className="flex items-center gap-2 font-bold text-slate-900">
              <ShieldCheck className="w-4 h-4 text-blue-600" />
              <span>Publication &amp; Indexing</span>
            </div>
            <p className="text-xs text-slate-600 leading-relaxed">
              All registered and presented papers will be considered for publication in <strong>ACIE: Advances in Computing, Intelligence and Engineering</strong> (An International Peer-Reviewed Open Access Journal | <a href="https://acieopen.com/" target="_blank" rel="noreferrer" className="text-blue-600 underline">https://acieopen.com/</a>).
            </p>
          </div>

          {/* Key Milestone Timeline */}
          <div>
            <h3 className="font-bold text-slate-900 text-sm uppercase tracking-wider mb-2.5">
              Important Milestones
            </h3>
            <div className="divide-y divide-slate-100 border border-slate-200 rounded-xl overflow-hidden">
              {IMPORTANT_DATES.map((item, idx) => (
                <div key={idx} className="flex items-center justify-between p-3 text-xs sm:text-sm hover:bg-slate-50">
                  <span className="font-medium text-slate-800 flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                    {item.event}
                  </span>
                  <span className="font-mono font-semibold text-blue-700 bg-blue-50 px-2 py-0.5 rounded">
                    {item.date}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Sponsorship Coordinator Contact Note */}
          <div className="p-4 rounded-xl bg-amber-50 border border-amber-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs">
            <div>
              <strong className="text-amber-900 block font-bold">For Sponsorship Inquiries:</strong>
              <span className="text-amber-800">
                Contact Coordinator: <strong>{CONFERENCE_INFO.sponsorshipCoordinator.name}</strong> • Phone: <a href="tel:1234567890" className="underline font-mono font-bold">1234567890</a>
              </span>
            </div>
            <a 
              href="mailto:sponsorship@acieopen.com"
              className="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-700 text-white font-semibold transition-colors shrink-0"
            >
              Email Coordinator
            </a>
          </div>

        </div>

        {/* Footer Actions */}
        <div className="p-5 bg-slate-50 border-t border-slate-200 rounded-b-2xl flex flex-col sm:flex-row items-center justify-between gap-3">
          <span className="text-xs text-slate-500 text-center sm:text-left">
            Complete details are published on <a href="https://acieopen.com/" target="_blank" rel="noreferrer" className="text-blue-600 underline">acieopen.com</a>
          </span>
          <div className="flex items-center gap-2.5 w-full sm:w-auto">
            <button
              onClick={onClose}
              className="flex-1 sm:flex-initial px-4 py-2 text-xs font-semibold text-slate-700 bg-white hover:bg-slate-100 rounded-xl border border-slate-300 transition-colors"
            >
              Close
            </button>
            <a
              href="/assets/brochure/ACIE-2027-Brochure.pdf"
              target="_blank"
              rel="noopener noreferrer"
              className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-4 py-2 text-xs font-bold text-blue-700 bg-blue-50 hover:bg-blue-100 border border-blue-200 rounded-xl transition-colors"
            >
              <ExternalLink className="w-3.5 h-3.5" />
              <span>Open in New Tab</span>
            </a>
            <a
              href="/assets/brochure/ACIE-2027-Brochure.pdf"
              download="ACIE-2027-Brochure.pdf"
              className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-1.5 px-5 py-2 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 rounded-xl shadow-md transition-colors"
            >
              <Download className="w-4 h-4" />
              <span>Download PDF</span>
            </a>
          </div>
        </div>

      </div>
    </div>
  );
}

