import React, { useEffect } from 'react';
import PageBanner from '../components/PageBanner';
import AOS from 'aos';

export default function Sponsorship() {
  useEffect(() => {
    AOS.init({
      duration: 1000,
      once: true,
      offset: 100
    });
  }, []);

  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="SPONSORSHIP" 
        subtitle="Partner with us to showcase your brand and drive meaningful impact through sponsorship."
      />

      <div className="px-6 py-10 md:px-8 lg:px-15 bg-[#E7ECFF]">
        <div data-aos="fade-up" className="rounded-2xl overflow-hidden border border-gray-300 shadow-lg bg-white">
          <div className="overflow-x-auto">
            <table className="min-w-full text-center border-collapse">
              <thead>
                <tr className="bg-blue-50 text-blue-900 font-semibold">
                  <th className="border border-gray-300 px-4 py-4"></th>
                  <th className="border border-gray-300 px-4 py-4">₹2 Lakh*</th>
                  <th className="border border-gray-300 px-4 py-4">₹1.5 Lakh*</th>
                  <th className="border border-gray-300 px-4 py-4">₹1 Lakh*</th>
                  <th className="border border-gray-300 px-4 py-4">₹0.75 Lakh*</th>
                  <th className="border border-gray-300 px-4 py-4">₹0.5 Lakh*</th>
                  <th className="border border-gray-300 px-4 py-4">₹0.25 Lakh*</th>
                </tr>
                <tr className="bg-gray-100 text-gray-800 font-semibold">
                  <th className="border border-gray-300 px-4 py-4">Particulars</th>
                  <th className="border border-gray-300 px-4 py-4">Title Sponsor</th>
                  <th className="border border-gray-300 px-4 py-4">Diamond</th>
                  <th className="border border-gray-300 px-4 py-4">Platinum</th>
                  <th className="border border-gray-300 px-4 py-4">Gold</th>
                  <th className="border border-gray-300 px-4 py-4">Silver</th>
                  <th className="border border-gray-300 px-4 py-4">Bronze</th>
                </tr>
              </thead>
              <tbody className="text-gray-700">
                <tr className="bg-gray-50">
                  <td className="border border-gray-300 px-4 py-4 font-medium text-left">Number of free attendee registrations</td>
                  <td className="border border-gray-300 px-4 py-4">6</td>
                  <td className="border border-gray-300 px-4 py-4">5</td>
                  <td className="border border-gray-300 px-4 py-4">4</td>
                  <td className="border border-gray-300 px-4 py-4">3</td>
                  <td className="border border-gray-300 px-4 py-4">2</td>
                  <td className="border border-gray-300 px-4 py-4">1</td>
                </tr>
                <tr>
                  <td className="border border-gray-300 px-4 py-4 font-medium text-left">Invitation to expert talk</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                </tr>
                <tr className="bg-gray-50">
                  <td className="border border-gray-300 px-4 py-4 font-medium text-left">Space for sponsor logos (website, posters, flyers, banners, etc.)</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                </tr>
                <tr>
                  <td className="border border-gray-300 px-4 py-4 font-medium text-left">Exhibition Booth details</td>
                  <td className="border border-gray-300 px-4 py-4">6m × 6m</td>
                  <td className="border border-gray-300 px-4 py-4">6m × 3m</td>
                  <td className="border border-gray-300 px-4 py-4">3m × 3m</td>
                  <td className="border border-gray-300 px-4 py-4">3m × 3m</td>
                  <td className="border border-gray-300 px-4 py-4">2m × 3m</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                </tr>
                <tr className="bg-gray-50">
                  <td className="border border-gray-300 px-4 py-4 font-medium text-left">Sponsor brochure/flyer in conference kit</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✔</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                  <td className="border border-gray-300 px-4 py-4">✖</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <p className="mt-4 text-sm text-gray-600">
          * GST exclusive rates
        </p>
      </div>

      <div className="mt-0 pb-16 px-6 md:px-10 lg:px-20 bg-[#E7ECFF]" data-aos="fade-up">
        <h2 className="text-xl font-semibold text-slate-800 mb-4">
          For Sponsorship, contact Sponsorship Chairs:
        </h2>
        <ul className="space-y-2 text-slate-700 text-sm md:text-base">
          <li>
            <span className="font-medium">Prof. Raj Kumar Mohanta</span> –{' '}
          </li>
          <li>
            <span className="font-medium">Assitant Professor, HOD of Computer Science and Engineering</span>
          </li>
          <li>
            <a href="mailto:rajkumar.mohanta@cutm.ac.in" className="text-blue-600 hover:underline">
              rajkumar.mohanta@cutm.ac.in
            </a>
          </li>
          <li>
            <span className="font-medium text-slate-900">Dr. Subhra Debdas</span> – Sponsorship Coordinator (Phone: +91-9437376421 | Email: contact@acieopen.com)
          </li>
        </ul>
      </div>
    </main>
  );
}
