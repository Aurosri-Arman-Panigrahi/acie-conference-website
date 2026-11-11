import React from 'react';
import PageBanner from '../components/PageBanner';
import { KEYNOTE_SPEAKERS } from '../data/conferenceData';

const gradients = [
  "from-blue-600 via-indigo-600 to-purple-600",
  "from-emerald-500 via-teal-600 to-cyan-600",
  "from-amber-500 via-orange-500 to-red-500",
  "from-fuchsia-600 via-pink-600 to-rose-500",
  "from-violet-600 via-purple-600 to-indigo-600",
];

export default function KeynoteSpeakers() {
  return (
    <div className="w-full bg-[#E7ECFF] min-h-screen py-10 md:py-16">
      <div className="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        
        {/* Subpage Banner */}
        <PageBanner 
          title="KEYNOTE SPEAKERS" 
          subtitle="Distinguished Global Academicians, Industry Pioneers & Keynote Lecturers"
        />

        {/* Speakers Grid matching aisigh-sd.co.in */}
        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 sm:gap-8">
          {KEYNOTE_SPEAKERS.map((speaker, index) => {
            const grad = gradients[index % gradients.length];
            return (
              <div 
                key={speaker.id}
                data-aos="fade-up"
                data-aos-delay={(index % 5) * 100}
                className="group relative flex flex-col items-center text-center bg-white/90 backdrop-blur-md border border-slate-200/80 rounded-3xl p-6 transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-2xl hover:border-blue-300"
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
                    <h2 className="text-base sm:text-lg font-extrabold text-slate-800 tracking-tight leading-snug group-hover:text-blue-900 transition-colors duration-300">
                      {speaker.name}
                    </h2>
                    <p className="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed px-1 mt-2 line-clamp-3">
                      {speaker.title}
                    </p>
                    <p className="text-[11px] text-blue-700 font-semibold mt-1">
                      {speaker.affiliation}
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
