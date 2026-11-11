import React from 'react';
import { SUBPAGE_CAROUSEL_IMAGES } from '../data/conferenceData';

export default function PageBanner({ title, subtitle }) {
  // Duplicate array for seamless infinite carousel illusion
  const images = [...SUBPAGE_CAROUSEL_IMAGES, ...SUBPAGE_CAROUSEL_IMAGES];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8 pt-4">
      <div className="relative w-full h-[220px] overflow-hidden rounded-2xl shadow-xl bg-slate-900">
        
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
        <div className="relative z-20 h-full flex flex-col items-center justify-center text-center px-6 gap-3">
          {/* Title with Academic Drop Shadow */}
          <h1 className="text-2xl sm:text-3xl md:text-5xl font-extrabold text-white tracking-wide uppercase drop-shadow-md font-heading">
            {title}
          </h1>

          {/* Subtitle */}
          {subtitle && (
            <p className="text-sm sm:text-base md:text-lg text-blue-100 max-w-3xl opacity-90 font-medium">
              {subtitle}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
