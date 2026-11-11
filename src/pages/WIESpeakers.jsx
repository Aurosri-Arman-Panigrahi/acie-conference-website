import React from 'react';
import PageBanner from '../components/PageBanner';
import { Award, Sparkles, BookOpen, ExternalLink, Heart } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function WIESpeakers() {
  const womenSpeakers = [
    {
      id: "sangita-satapathy",
      name: "Sangita Satapathy",
      title: "Senior Cloud Platform & Infrastructure Engineer",
      affiliation: "Royal Sutton Coldfield, England, United Kingdom",
      image: "/assets/images/scraped/keynoteSpeaker5-CU3eZAKd.jpeg",
      exactFocus: "Hyperscale Cloud Architecture, Distributed Kubernetes Meshes, Resilient Multi-Cloud Microservices & DevOps Governance",
      keynoteTitle: "Architecting Resilient Hyperscale Cloud Mesh Infrastructure for Mission-Critical Distributed Systems",
      abstract: "Focuses on high-availability container orchestration, distributed observability pipelines, zero-trust cloud network security, and automated CI/CD resilience frameworks across European financial cloud ecosystems."
    },
    {
      id: "padmaja-pulivarthy",
      name: "Ms. Padmaja Pulivarthy",
      title: "Enterprise Data Systems Architect",
      affiliation: "Samsung Semiconductor, San Jose, California, USA",
      image: "/assets/images/scraped/newSpeaker2-DRXI_EuR.png",
      exactFocus: "Semiconductor AI Yield Optimization, High-Bandwidth Memory (HBM3e/HBM4) Data Flow & Edge Inference Silicon",
      keynoteTitle: "Next-Generation High-Bandwidth Memory (HBM) and Silicon Wafer Defect Prediction via Deep Computer Vision",
      abstract: "Details real-time deep neural yield diagnostics for 3nm/2nm semiconductor fabrication, memory-centric heterogeneous compute, and silicon hardware accelerators for ultra-large language models."
    },
    {
      id: "celia-shahnaz",
      name: "Prof. (Dr.) Celia Shahnaz",
      title: "IEEE WIE Global Chair & Professor of Electrical & Computer Engineering",
      affiliation: "BUET, Fellow of IEEE, Distinguished Lecturer",
      image: "/assets/images/scraped/newSpeaker3-CZHDiFUn.png",
      exactFocus: "Deep Learning for Audio-Visual Signal Processing, Multimodal Biomedical Signal Analysis & Women in Engineering Empowerment",
      keynoteTitle: "Deep Neural Audio-Visual Signal Processing for Healthcare Telemetry & Fostering Global STEM Diversity",
      abstract: "Explores advanced machine learning architectures for non-invasive cardiovascular and neurological biomarker detection, combined with strategic roadmaps for accelerating women's participation in international academic and industry engineering leadership."
    },
    {
      id: "rasmita-samantaray",
      name: "Dr. Rasmita Samantaray",
      title: "Senior Autonomous Driving Systems Engineer",
      affiliation: "Hyundai Motor Europe Technical Centre, Rüsselsheim, Germany",
      image: "/assets/images/scraped/newSpeaker4-Brg4EqWV.png",
      exactFocus: "Automotive Sensor Fusion (LiDAR, Radar & Cameras), ISO 26262 Automotive Functional Safety & Deep Neural Trajectory Control",
      keynoteTitle: "Deep Multi-Modal Sensor Fusion and Fail-Operational Safety Architectures for Level 3/4 Autonomous Mobility",
      abstract: "Examines real-time spatial calibration between 4D imaging radar and solid-state LiDAR, stochastic motion forecasting under occluded urban conditions, and safety compliance across European EV commercial platforms."
    }
  ];

  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="WIE SPEAKER" 
        subtitle="Women in Engineering • Distinguished Keynote Luminaries & Their Research Focus"
      />

      <div className="w-full bg-[#E7ECFF] py-16 md:py-24">
        <div className="max-w-6xl mx-auto px-6 text-slate-700 space-y-12">
          
          {/* Section Introduction */}
          <div data-aos="fade-up" className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 md:p-10 text-center space-y-3">
            <span className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full bg-pink-100 text-pink-800 text-xs font-bold uppercase tracking-wider">
              <Sparkles className="w-3.5 h-3.5" />
              <span>IEEE &amp; ACIE Women in Engineering Symposium</span>
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 font-heading">
              Distinguished Women Keynote Speakers
            </h2>
            <p className="text-sm sm:text-base text-slate-600 max-w-3xl mx-auto leading-relaxed">
              Highlighting pioneering research contributions, technical innovations, and keynote addresses delivered exclusively by leading women scientists, academic professors, and enterprise systems architects.
            </p>
          </div>

          {/* Speakers Detailed Cards */}
          <div className="space-y-8">
            {womenSpeakers.map((speaker, idx) => (
              <div 
                key={speaker.id}
                data-aos="fade-up"
                data-aos-delay={idx * 100}
                className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 sm:p-8 hover:shadow-md transition-all duration-300 flex flex-col md:flex-row items-center md:items-start gap-6 lg:gap-8"
              >
                {/* Speaker Avatar */}
                <div className="shrink-0 flex flex-col items-center text-center">
                  <div className="w-32 h-32 sm:w-36 sm:h-36 rounded-full overflow-hidden border-4 border-pink-100 shadow-md">
                    <img 
                      src={speaker.image} 
                      alt={speaker.name}
                      className="w-full h-full object-cover object-top"
                    />
                  </div>
                  <span className="mt-3 px-3 py-1 rounded-full bg-pink-50 text-pink-700 text-xs font-bold uppercase tracking-wider border border-pink-200">
                    Keynote Speaker
                  </span>
                </div>

                {/* Speaker Info & Exact Focus */}
                <div className="flex-1 space-y-4 text-center md:text-left">
                  <div>
                    <h3 className="text-xl sm:text-2xl font-bold text-slate-900 font-heading">
                      {speaker.name}
                    </h3>
                    <p className="text-sm font-semibold text-blue-700 mt-0.5">
                      {speaker.title}
                    </p>
                    <p className="text-xs text-slate-500 font-medium">
                      {speaker.affiliation}
                    </p>
                  </div>

                  {/* Exact Focus Box */}
                  <div className="p-4 rounded-xl bg-gradient-to-r from-pink-50 to-purple-50 border border-pink-200/80 space-y-1.5">
                    <span className="text-xs font-bold uppercase tracking-wider text-pink-900 block flex items-center justify-center md:justify-start gap-1.5">
                      <Award className="w-4 h-4 text-pink-600" />
                      Exact Research Focus:
                    </span>
                    <p className="text-xs sm:text-sm font-semibold text-slate-800 leading-relaxed">
                      {speaker.exactFocus}
                    </p>
                  </div>

                  {/* Keynote Presentation Title & Abstract */}
                  <div className="space-y-1">
                    <h4 className="text-sm font-bold text-slate-900">
                      Keynote Title: <span className="text-blue-900 italic font-semibold">"{speaker.keynoteTitle}"</span>
                    </h4>
                    <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                      {speaker.abstract}
                    </p>
                  </div>
                </div>

              </div>
            ))}
          </div>

          {/* All Women Award Promotion Card */}
          <div data-aos="fade-up" className="bg-gradient-to-r from-pink-100 via-purple-100 to-blue-100 border border-pink-300 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-sm">
            <div className="space-y-1 text-center md:text-left">
              <h4 className="font-bold text-slate-900 text-lg flex items-center justify-center md:justify-start gap-2">
                <Heart className="w-5 h-5 text-pink-600 fill-pink-600" />
                <span>Best All-Women Authored Paper Award</span>
              </h4>
              <p className="text-xs sm:text-sm text-slate-700">
                Manuscripts authored exclusively by female researchers and engineers are automatically eligible for commendation trophies, certificates, and recognition at the ACIE 2027 Valedictory Ceremony.
              </p>
            </div>
            <Link
              to="/all-women"
              className="inline-flex items-center justify-center px-6 py-2.5 bg-pink-600 hover:bg-pink-700 text-white text-xs font-bold rounded-xl shadow-md transition-all whitespace-nowrap"
            >
              View Award Criteria
            </Link>
          </div>

        </div>
      </div>
    </main>
  );
}
