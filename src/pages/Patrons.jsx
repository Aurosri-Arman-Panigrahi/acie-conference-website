import React from 'react';
import PageBanner from '../components/PageBanner';
import { CONFERENCE_INFO } from '../data/conferenceData';

export default function Patrons() {
  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="COMMITTEE" 
        subtitle="Acknowledging the invaluable contributions of our committee in fostering knowledge, collaboration"
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div data-aos="fade-up" className="max-w-5xl mx-auto px-6 text-slate-700">
          
          {/* Chief Patron */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Chief Patron:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Prof. (Dr.) Achyuta Samanta, Founder, KIIT &amp; KISS Deemed to be University, Bhubaneswar, India</li>
            </ul>
          </div>

          {/* Patron */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Patron:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Prof. (Dr.) Saranjit Singh, Vice-Chancellor, KIIT Deemed to be University, Odisha, India</li>
              <li>Prof. (Dr.) J. R. Mohanty, Registrar, KIIT Deemed to be University, Odisha, India</li>
              <li>Prof. (Dr.) Bhabani Shankar Prasad Mishra, Dean, School of Computer Engineering, KIIT University</li>
            </ul>
          </div>

          {/* Honorary Chairs */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Honorary Chairs:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Prof. Ganapati Panda, Ex Director, IIT Bhubaneswar, India</li>
              <li>Prof. Ashutosh Dutta, Johns Hopkins University, Maryland, United States</li>
              <li>Prof. S. R. Samantaray, IIT Bhubaneswar, India</li>
              <li>Prof. Sukumar Mishra, Director, IIT Dhanbad, India</li>
              <li>Prof. Ashok Kumar Tripathy, Former Chair, IEEE Bhubaneswar Section, India</li>
              <li>Shri Hare Krishna Ratha, Former Director, DRDO, India</li>
              <li>Prof. Bansidhar Majhi, Vice Chancellor, VSSUT &amp; CGU, Bhubaneswar, India</li>
              <li>Prof. Pradipta Kumar Nanda, Vice Chancellor, SOA University, Bhubaneswar, India</li>
              <li>Prof. Debi Prosad Dogra, IIT Bhubaneswar, India</li>
              <li>Prof. Renu Sharma, IEEE WIE India Council, SOA, Bhubaneswar, India</li>
            </ul>
          </div>

          {/* General Chairs */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              General Chairs:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Prof. (Dr.) Arindam Deb, Senior Researcher, KIIT University, Bhubaneswar, India</li>
              <li>Prof. Tapan Kumar Gandhi, IIT Delhi, India</li>
            </ul>
          </div>

          {/* Organizing Chairs & Sponsorship */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Organizing Chairs &amp; Sponsorship:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>
                <strong>Dr. Subhra Debdas</strong>, Organizing Chair &amp; Sponsorship Coordinator, School of Electrical Engineering, KIIT University
                <br />
                <span className="text-sm text-blue-700 ml-5 font-mono">
                  (Phone: {CONFERENCE_INFO.sponsorshipCoordinator.phone} | Email: {CONFERENCE_INFO.sponsorshipCoordinator.email})
                </span>
              </li>
              <li>Dr. Swastik Panda, Organizing Secretary, School of Computer Science &amp; Engineering, KIIT University</li>
              <li>Dr. Prabhu Krupa Biswal, Organizing Co-Chair, KIIT University, Bhubaneswar, India</li>
            </ul>
          </div>

          {/* Technical Program Chairs */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Technical Program Chairs:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Dr. Aayush Saha, KIIT Deemed to be University, Bhubaneswar, India</li>
              <li>Dr. Sucharita Pradhan, KIIT Deemed to be University, Bhubaneswar, India</li>
              <li>Dr. Samir Kumar Panigrahi, KIIT Deemed to be University, Bhubaneswar, India</li>
            </ul>
          </div>

          {/* Technical Program Committee */}
          <div className="mb-8">
            <h3 className="text-2xl font-bold text-slate-900 mb-2 font-heading">
              Technical Program Committee &amp; Advisory Board:
            </h3>
            <ul className="list-disc list-inside space-y-1 text-base text-slate-800">
              <li>Prof. B. K. Panigrahi, IIT Delhi, India</li>
              <li>Prof. Dipayan Guha, MNNIT Allahabad, India</li>
              <li>Prof. Abhishek Dey, NIT Rourkela, India</li>
              <li>Prof. Chinmoy Kumar Panigrahi, KIIT University, Bhubaneswar, India</li>
              <li>Prof. Chandrasekhar Perumalla, IIT Bhubaneswar, India</li>
              <li>Prof. Manohar Mishra, SOA University, Bhubaneswar, India</li>
              <li>Prof. Satyajit Das, VIT Vellore, India</li>
              <li>Prof. Trilochan Penthia, NIT Patna, India</li>
              <li>Dr. Bhabendu Mohanta, United Arab Emirates University, UAE</li>
              <li>Dr. Suman Sourav, Aalborg University, Denmark</li>
              <li>Dr. Akshaya Kumar Moharana, EEPlus Inc., Texas, USA</li>
              <li>Ms. Padmaja Pulivarthy, Samsung Semiconductor, USA</li>
              <li>Dr. Subhas Chinara, NIT Rourkela, India</li>
              <li>Mr. Deepak Mathur, Former IEEE Vice President (MGA)</li>
              <li>Dr. Rasmita Samantaray, Hyundai Motor Europe Technical Centre, Germany</li>
            </ul>
          </div>

        </div>
      </div>
    </main>
  );
}
