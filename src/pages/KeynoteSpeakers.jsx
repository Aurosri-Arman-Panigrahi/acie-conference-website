import React from 'react';
import PageBanner from '../components/PageBanner';
import { KEYNOTE_SPEAKERS } from '../data/conferenceData';

export default function KeynoteSpeakers() {
  return (
    <div className="w-full bg-[#E7ECFF] min-h-screen py-10 md:py-16">
      <div className="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        
        {/* Subpage Banner matching exact aisigh-sd.co.in */}
        <PageBanner 
          badge="Featured Experts"
          title="KEYNOTE SPEAKERS" 
          subtitle="Recognizing impactful research driven by industry expertise, visionary leadership, and cutting-edge innovation."
        />

        {/* Speakers Grid matching aisigh-sd.co.in KeynoteSpeakers-CabTs-nx.js */}
        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 sm:gap-8">
          {KEYNOTE_SPEAKERS.map((speaker, index) => {
            const grad = speaker.gradient || "from-blue-600 via-indigo-600 to-purple-600";
            const glow = speaker.glow || "group-hover:shadow-blue-500/30";
            const borderGlow = speaker.borderGlow || "group-hover:border-blue-400";

            return (
              <div 
                key={speaker.id}
                data-aos="fade-up"
                data-aos-delay={(index % 5) * 100}
                style={{ animationDelay: `${index * 150}ms` }}
                className={`group relative flex flex-col items-center text-center bg-white/80 backdrop-blur-md border border-slate-200/80 rounded-3xl p-6 transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-2xl ${glow} ${borderGlow}`}
              >
                {/* Subtle Hover Gradient */}
                <div className={`absolute inset-0 rounded-3xl bg-gradient-to-br ${grad} opacity-0 group-hover:opacity-5 transition-opacity duration-500 pointer-events-none`} />

                {/* Avatar with Circular Gradient Ring */}
                <div className="relative mb-5 flex-shrink-0">
                  <div className={`p-1 rounded-full bg-gradient-to-tr ${grad} shadow-md group-hover:shadow-lg transition-all duration-500 group-hover:scale-105`}>
                    <div className="w-32 h-32 sm:w-36 sm:h-36 rounded-full overflow-hidden bg-slate-100 border-2 border-white">
                      <img 
                        src={speaker.image} 
                        alt={speaker.name} 
                        className="w-full h-full object-cover object-center transition-transform duration-700 ease-out group-hover:scale-110" 
                        onError={(e) => {
                          e.target.src = 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80';
                        }}
                      />
                    </div>
                  </div>
                </div>

                {/* Info */}
                <div className="flex flex-col flex-1 justify-between space-y-3 mt-2 w-full">
                  <div>
                    <h2 className="text-base sm:text-lg font-extrabold text-slate-800 tracking-tight leading-snug group-hover:text-indigo-900 transition-colors duration-300">
                      {speaker.name}
                    </h2>
                    <p className="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed px-1 mt-2 line-clamp-4">
                      {speaker.title}
                    </p>
                  </div>

                  <div className="pt-2 w-full flex justify-center">
                    <span className={`h-1 w-12 rounded-full bg-gradient-to-r ${grad} opacity-40 group-hover:w-24 group-hover:opacity-100 transition-all duration-500`} />
                  </div>
                </div>
              </div>
            );
          })}
        </section>

      </div>
    </div>
  );
}
