import React, { useEffect } from 'react';
import PageBanner from '../components/PageBanner';
import AOS from 'aos';

export default function Accomodation() {
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
        title="ACCOMODATION" 
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div data-aos="fade-up" className="max-w-6xl mx-auto px-6 md:px-12 py-16 bg-[#E7ECFF] text-gray-700">
          <h2 className="text-3xl font-bold text-gray-900 mb-6">
            Hostel Accommodation for Registered Student Participants
          </h2>

          <p className="text-lg leading-relaxed mb-8">
            Registered student participants may opt for shared accommodation in the hostel on a payment basis. Those interested are required to fill out the Google Form provided below. Hostel seats will be allocated on a{' '}
            <span className="font-semibold">first-come, first-served basis</span>. The{' '}
            <span className="font-semibold">last date</span> to submit interest for hostel accommodation is{' '}
            <span className="font-semibold">15th January 2027</span>; requests received after this date will not be considered.
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mb-2">
            Form Link
          </h3>
          <p className="mb-8 text-gray-500">
            To be updated
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mb-4">
            Important Notes
          </h3>
          <ul className="list-disc list-inside space-y-3 text-lg mb-10">
            <li>
              Family members or acquaintances who are not registered for the conference will not be permitted to stay in the hostel.
            </li>
            <li>
              The accommodation charges are{' '}
              <span className="font-semibold">INR 400/- per night</span>, payable in advance for the entire duration of the stay at the time of arrival.
            </li>
            <li>
              Working lunch will be hosted by the organizers for all registered participants during the conference ({' '}
              <span className="font-semibold">22–24 January 2027</span>).
            </li>
            <li>
              Registered participants must strictly adhere to the KIIT hostel norms during their stay.
            </li>
          </ul>

          <h3 className="text-2xl font-semibold text-gray-900 mb-2">
            Nearby Hotels
          </h3>
          <p className="text-lg text-gray-500">
            To be updated soon
          </p>
        </div>
      </div>
    </main>
  );
}
