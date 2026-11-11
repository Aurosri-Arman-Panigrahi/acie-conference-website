import React from 'react';
import { SUBPAGE_CAROUSEL_IMAGES } from '../data/conferenceData';

export default function PageBanner({ title, subtitle, badge }) {
  // Duplicate array for seamless infinite carousel illusion
  const images = [...SUBPAGE_CAROUSEL_IMAGES, ...SUBPAGE_CAROUSEL_IMAGES];

  return (
    <div className="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8 pt-4">
      <section className="relative w-full h-[220px] sm:h-[240px] overflow-hidden rounded-2xl shadow-xl bg-slate-900">
        
        {/* Animated Background Carousel Strip */}
        <div className="absolute inset-0 z-0 opacity-55 flex items-center overflow-hidden">
          <div className="flex w-max gap-4 animate-carousel">
            {images.map((src, idx) => (
              <div key={idx} className="h-[170px] w-[260px] rounded-2xl overflow-hidden shadow-xl shrink-0">
                <img 
                  src={src} 
                  alt="" 
                  className="w-full h-full object-cover" 
                  loading="lazy" 
                />
              </div>
            ))}
          </div>
        </div>

        {/* Gradient Overlay matching original academic theme */}
        <div className="absolute inset-0 z-10 bg-gradient-to-r from-blue-900/85 via-blue-700/75 to-blue-900/85" />

        {/* Content Overlay */}
        <div className="relative z-20 h-full flex flex-col items-center justify-center text-center px-4 sm:px-8 gap-3">
          {/* Optional Badge matching Featured Experts badge from aisigh-sd.co.in */}
          {badge && (
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-pink-500/20 via-purple-500/20 to-blue-500/20 border border-white/20 shadow-inner animate-pulse">
              <span className="w-2 h-2 rounded-full bg-pink-400 animate-ping" />
              <span className="text-xs font-bold uppercase tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-pink-300 via-yellow-200 to-cyan-300">
                {badge}
              </span>
            </div>
          )}

          {/* Title with Exact Academic Gradient & Drop Shadow from aisigh-sd.co.in */}
          <h1 
            className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-pink-400 via-yellow-300 to-blue-400 uppercase font-heading tracking-wide px-2"
            style={{ textShadow: "2px 2px 0 rgba(0,0,0,0.5), 4px 4px 0 rgba(0,0,0,0.4)" }}
          >
            {title}
          </h1>

          {/* Subtitle */}
          {subtitle && (
            <p className="text-xs sm:text-sm md:text-base text-blue-100 max-w-3xl opacity-90 font-medium px-2 leading-relaxed">
              {subtitle}
            </p>
          )}
        </div>
      </section>
    </div>
  );
}
