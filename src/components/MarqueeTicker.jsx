import React from 'react';

export default function MarqueeTicker() {
  return (
    <div 
      className="mt-20 overflow-hidden bg-blue-700 py-2 text-xs sm:text-sm font-semibold text-white shadow-xs relative z-40"
      role="status" 
      aria-label="Deadline announcement"
    >
      <div className="flex w-max flex-nowrap animate-deadline-marquee motion-reduce:animate-none">
        <span className="shrink-0 px-8 tracking-wider whitespace-nowrap">
          📢 Important: ACIE 2027 Paper Submission Portal is Open! All accepted and presented papers will be considered for publication in ACIE (https://acieopen.com/). Early registrations begin soon.
        </span>
        <span className="shrink-0 px-8 tracking-wider whitespace-nowrap" aria-hidden="true">
          📢 Important: ACIE 2027 Paper Submission Portal is Open! All accepted and presented papers will be considered for publication in ACIE (https://acieopen.com/). Early registrations begin soon.
        </span>
      </div>
    </div>
  );
}
