import React from 'react';
import PageBanner from '../components/PageBanner';

export default function Accomodation() {
  const nearbyHotels = [
    {
      name: "Ginger Hotel Bhubaneswar",
      distance: "3.2 km from KIIT Campus",
      address: "Jayadev Vihar, Near Fortune Tower, Bhubaneswar",
      contact: "+91-674-6663333"
    },
    {
      name: "Fortune Park Sishmo",
      distance: "7.5 km from KIIT Campus",
      address: "Bapuji Nagar, Near Janpath, Bhubaneswar",
      contact: "+91-674-3988444"
    },
    {
      name: "Vivanta Bhubaneswar DN Square",
      distance: "8.5 km from KIIT Campus",
      address: "DN Regalia Mall Complex, Patrapada, Bhubaneswar",
      contact: "+91-674-6622222"
    },
    {
      name: "Sandy's Tower",
      distance: "4.8 km from KIIT Campus",
      address: "P1 & P1/A, Jayadev Vihar, Bhubaneswar",
      contact: "+91-674-6666555"
    }
  ];

  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="ACCOMODATION" 
        subtitle="Hostel and Guest House Accommodation for Registered Participants"
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div data-aos="fade-up" className="max-w-6xl mx-auto px-6 md:px-12 py-16 bg-[#E7ECFF] text-gray-700">
          
          <h2 className="text-3xl font-bold text-gray-900 mb-6 font-heading">
            Hostel Accommodation for Registered Student Participants
          </h2>

          <p className="text-lg leading-relaxed mb-8">
            Registered student participants may opt for shared accommodation in the hostel on a payment basis. Those interested are required to fill out the Google Form provided below. Hostel seats will be allocated on a <span className="font-semibold text-gray-900">first-come, first-served basis</span>. The <span className="font-semibold text-gray-900">last date</span> to submit interest for hostel accommodation is <span className="font-semibold text-blue-900">10th January 2027</span>; requests received after this date will not be considered.
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mb-2 font-heading">
            Form Link
          </h3>
          <p className="mb-8 text-blue-700 font-medium">
            <a 
              href="https://forms.gle/m2pqtU4VQpujxFMU8" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-orange-600 hover:underline"
            >
              Click here to submit Hostel &amp; Guest House Accommodation Request
            </a>
          </p>

          <h3 className="text-2xl font-semibold text-gray-900 mb-4 font-heading">
            Important Notes
          </h3>
          <ul className="list-disc list-inside space-y-3 text-lg mb-10 text-gray-800">
            <li>
              Family members or acquaintances who are not registered for the conference will not be permitted to stay in the hostel.
            </li>
            <li>
              The accommodation charges are <span className="font-semibold text-gray-900">INR 400/- per night</span>, payable in advance for the entire duration of the stay at the time of arrival.
            </li>
            <li>
              Working lunch will be hosted by the organizers for all registered participants during the conference (<span className="font-semibold text-blue-900">22–24 January 2027</span>).
            </li>
            <li>
              Registered participants must strictly adhere to the KIIT hostel norms during their stay.
            </li>
          </ul>

          <h3 className="text-2xl font-semibold text-gray-900 mb-4 font-heading">
            Nearby Hotels in Bhubaneswar (Patia Area)
          </h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
            {nearbyHotels.map((hotel, idx) => (
              <div key={idx} className="bg-white/80 p-5 rounded-2xl border border-blue-200 shadow-sm space-y-1.5 text-sm">
                <h4 className="font-bold text-slate-900">{hotel.name}</h4>
                <p className="text-xs text-blue-700 font-semibold">{hotel.distance}</p>
                <p className="text-xs text-slate-600">{hotel.address}</p>
                <p className="text-xs text-slate-700 font-mono pt-1">{hotel.contact}</p>
              </div>
            ))}
          </div>

        </div>
      </div>
    </main>
  );
}
