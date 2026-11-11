import React from 'react';
import PageBanner from '../components/PageBanner';

export default function AboutKIIT() {
  return (
    <div className="w-full">
      <PageBanner 
        title="ABOUT KIIT UNIVERSITY" 
        subtitle="Shaping lives, empowering communities, and building a sustainable future"
      />

      <div className="bg-[#E7ECFF] text-gray-800">
        
        {/* Section 1: About the University */}
        <section className="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-2 gap-10 items-center">
          <div data-aos="fade-right" className="relative group overflow-hidden rounded-xl shadow-lg bg-white">
            <img 
              src="/assets/images/kiit/kiit-library-front.jpg" 
              alt="KIIT University Campus" 
              className="w-full h-[320px] object-cover transition-transform duration-700 ease-out group-hover:scale-110"
            />
            <div className="absolute inset-0 bg-blue-900/20 opacity-0 transition duration-700 group-hover:opacity-100" />
          </div>

          <div data-aos="fade-left">
            <h2 className="text-2xl font-bold text-blue-900 mb-4 font-heading">
              About the University
            </h2>
            <p className="text-base sm:text-lg leading-relaxed text-gray-700">
              Kalinga Institute of Industrial Technology (KIIT) Deemed to be University, Bhubaneswar, is recognized by the Ministry of Education, Government of India as an <strong>Institution of Eminence</strong>. Founded in 1992 by visionary educationist and social reformer <strong>Prof. (Dr.) Achyuta Samanta</strong>, KIIT has evolved into a premier multi-disciplinary institution with 25 specialized campuses housing over 40,000 students from all Indian states and more than 65 countries.
            </p>
          </div>
        </section>

        {/* Section 2: Vision & Mission (Alternating Order) */}
        <section className="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-2 gap-10 items-center">
          <div data-aos="fade-right" className="order-2 md:order-1">
            <h2 className="text-2xl font-bold text-blue-900 mb-4 font-heading">
              Vision &amp; Mission
            </h2>
            <p className="text-base sm:text-lg leading-relaxed text-gray-700">
              The vision of KIIT is to create an advanced academic environment that fosters knowledge dissemination, intellectual inquiry, and technological innovation. Its mission focuses on high-impact scientific research, interdisciplinary engineering excellence, and societal transformation through inclusive education and sustainable community development.
            </p>
          </div>

          <div data-aos="fade-left" className="order-1 md:order-2 relative group overflow-hidden rounded-xl shadow-lg bg-white">
            <img 
              src="/assets/images/kiit/kiit-convention-center.webp" 
              alt="KIIT Convention Center and Auditorium" 
              className="w-full h-[320px] object-cover transition-transform duration-700 ease-out group-hover:scale-110"
            />
            <div className="absolute inset-0 bg-blue-900/20 opacity-0 transition duration-700 group-hover:opacity-100" />
          </div>
        </section>

        {/* Section 3: Research, Innovation & Global Impact */}
        <section className="max-w-6xl mx-auto px-6 py-16 grid md:grid-cols-2 gap-10 items-center">
          <div data-aos="fade-right" className="relative group overflow-hidden rounded-xl shadow-lg bg-white">
            <img 
              src="/assets/images/kiit/kiit-campus-arch.webp" 
              alt="KIIT Research and Innovation" 
              className="w-full h-[320px] object-cover transition-transform duration-700 ease-out group-hover:scale-110"
            />
            <div className="absolute inset-0 bg-blue-900/20 opacity-0 transition duration-700 group-hover:opacity-100" />
          </div>

          <div data-aos="fade-left">
            <h2 className="text-2xl font-bold text-blue-900 mb-4 font-heading">
              Research, Innovation &amp; Global Impact
            </h2>
            <p className="text-base sm:text-lg leading-relaxed text-gray-700">
              Ranked <strong>#16 in India (NIRF)</strong>, KIIT actively promotes high-level academic research, patenting, and international collaboration. With state-of-the-art supercomputing labs, AI innovation centers, and strong industry linkages across the globe, KIIT researchers lead breakthroughs in cyber-physical systems, renewable energy, and biomedical engineering.
            </p>
          </div>
        </section>

      </div>
    </div>
  );
}
