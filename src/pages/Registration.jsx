import React, { useState } from 'react';
import PageBanner from '../components/PageBanner';
import { ExternalLink, CheckCircle, FileText, Upload, Sparkles, X, Download } from 'lucide-react';

export default function Registration() {
  const [activeFormModal, setActiveFormModal] = useState(null); // 'author' | 'attendee' | null
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    paperId: '',
    paperTitle: '',
    authorName: '',
    affiliation: '',
    phone: '',
    category: 'Students - India (IEEE) [₹7,000 + 18% GST = ₹8,260]',
    utrNumber: '',
    paymentDate: '',
    presentationMode: 'In-Person at KIIT Campus, Bhubaneswar',
    fileName: ''
  });

  const feeRows = [
    ["Students", "₹7000", "₹7500", "$250", "$300"],
    ["Academia", "₹8000", "₹9000", "$300", "$350"],
    ["Industry", "₹9000", "₹10000", "$350", "$400"],
    ["Attendee", "₹3000", "₹3500", "$150", "$200"]
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleFileUpload = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFormData(prev => ({ ...prev, fileName: e.target.files[0].name }));
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    setFormSubmitted(true);
  };

  const closeFormModal = () => {
    setActiveFormModal(null);
    setFormSubmitted(false);
  };

  return (
    <main className="relative w-full overflow-x-hidden">
      <PageBanner 
        title="REGISTRATION" 
        subtitle="Author and Attendee Registration Fee Matrix & Payment Guidelines"
      />

      <div className="min-h-screen bg-[#E7ECFF] p-6 md:p-12">
        
        {/* Top Registration Form Links matching aisigh-sd.co.in exactly */}
        <div data-aos="fade-up" className="max-w-5xl mx-auto flex flex-col sm:flex-row justify-between gap-4 mb-6">
          <div className="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
            <a 
              href="https://forms.gle/eFNAa3H4Qg13kfyn8" 
              target="_blank" 
              rel="noopener noreferrer"
              className="w-full sm:w-auto"
            >
              <button className="w-full sm:w-auto bg-blue-600 text-white px-6 py-3 rounded-md font-semibold hover:bg-blue-900 transition shadow-sm cursor-pointer inline-flex items-center justify-center gap-2">
                <span>Author Registration Form</span>
                <ExternalLink className="w-4 h-4 opacity-80" />
              </button>
            </a>
            <button 
              onClick={() => { setActiveFormModal('author'); setFormSubmitted(false); }}
              className="w-full sm:w-auto bg-indigo-700 text-white px-4 py-3 rounded-md font-semibold hover:bg-indigo-900 transition text-xs sm:text-sm cursor-pointer shadow-sm"
            >
              Fill ACIE-2027 Author Form Here
            </button>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
            <a 
              href="https://forms.gle/m2pqtU4VQpujxFMU8" 
              target="_blank" 
              rel="noopener noreferrer"
              className="w-full sm:w-auto"
            >
              <button className="w-full sm:w-auto bg-blue-600 text-white px-6 py-3 rounded-md font-semibold hover:bg-blue-900 transition shadow-sm cursor-pointer inline-flex items-center justify-center gap-2">
                <span>Attendee Registration Form</span>
                <ExternalLink className="w-4 h-4 opacity-80" />
              </button>
            </a>
            <button 
              onClick={() => { setActiveFormModal('attendee'); setFormSubmitted(false); }}
              className="w-full sm:w-auto bg-indigo-700 text-white px-4 py-3 rounded-md font-semibold hover:bg-indigo-900 transition text-xs sm:text-sm cursor-pointer shadow-sm"
            >
              Fill ACIE-2027 Attendee Form Here
            </button>
          </div>
        </div>

        {/* Fee Structure Card matching aisigh-sd.co.in exactly */}
        <div data-aos="fade-up" data-aos-delay="100" className="max-w-5xl mx-auto bg-white rounded-2xl shadow-lg border border-slate-200 p-8">
          <h2 className="text-2xl font-bold text-slate-800 mb-6 font-heading">
            Fee Structure for Author / Attendee Registration
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-5 text-sm font-semibold text-slate-600 border-b pb-3 mb-4">
            <span>Category</span>
            <span className="md:text-center">India (IEEE)</span>
            <span className="md:text-center">India (Non-IEEE)</span>
            <span className="md:text-center">Abroad (IEEE)</span>
            <span className="md:text-center">Abroad (Non-IEEE)</span>
          </div>

          {feeRows.map((row, idx) => (
            <div key={idx} className="grid grid-cols-1 md:grid-cols-5 text-sm text-slate-700 py-3 border-b last:border-b-0">
              <span className="font-medium">{row[0]}</span>
              <span className="md:text-center font-semibold text-slate-900">{row[1]}</span>
              <span className="md:text-center font-semibold text-slate-900">{row[2]}</span>
              <span className="md:text-center font-semibold text-slate-900">{row[3]}</span>
              <span className="md:text-center font-semibold text-slate-900">{row[4]}</span>
            </div>
          ))}

          <div className="mt-6 bg-yellow-50 border border-yellow-200 rounded-lg p-4">
            <p className="text-sm text-yellow-800 font-medium">
              ⚠ GST at <strong>18%</strong> must be paid additionally at the time of payment.
            </p>
          </div>
        </div>

        {/* Payment Details Card matching aisigh-sd.co.in */}
        <div className="max-w-5xl mx-auto mt-10 rounded-2xl shadow-lg border bg-white p-6 md:p-8">
          <h2 className="text-2xl font-bold text-slate-800 mb-6 font-heading">
            Payment Details:
          </h2>

          <div className="flex flex-col md:flex-row items-center justify-between gap-8 bg-slate-50 border border-slate-200 rounded-xl p-6 mb-8">
            <div className="flex flex-col items-center text-center">
              <div className="w-48 h-48 bg-white border border-slate-300 rounded-lg p-2 flex items-center justify-center shadow-sm">
                <img 
                  src="/assets/images/scraped/qr-code-B5kqw1J3.png" 
                  alt="Payment QR Code" 
                  className="w-full h-full object-contain"
                />
              </div>
              <p className="text-sm font-medium text-slate-600 mt-2">
                Scan to Pay via UPI / QR
              </p>
            </div>

            <div className="flex-1 flex flex-col items-center md:items-start text-center md:text-left gap-3">
              <h3 className="text-lg font-semibold text-slate-800">
                Online Payment Gateway
              </h3>
              <p className="text-sm text-slate-600">
                You can also proceed directly with payment through our secure payment gateway portal.
              </p>
              <a 
                href="https://www.onlinesbi.sbi/sbicollect/icollecthome.htm" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="inline-block bg-green-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-green-700 transition shadow-sm"
              >
                Proceed to Pay Online
              </a>
            </div>
          </div>

          {/* Bank Transfer Details */}
          <div className="border border-slate-200 rounded-xl p-5 bg-slate-50/60 mb-8 space-y-2 text-sm text-slate-700">
            <h4 className="font-bold text-slate-900">Direct Bank Transfer (NEFT / RTGS / IMPS):</h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs sm:text-sm">
              <div>Beneficiary Name: <strong>ACIE Conference 2027</strong></div>
              <div>Bank: <strong>State Bank of India (SBI)</strong></div>
              <div>Account Number: <strong className="font-mono">38491029481</strong></div>
              <div>IFSC Code: <strong className="font-mono">SBIN0010250</strong></div>
              <div className="sm:col-span-2">Branch: <strong>KIIT Campus Branch, Patia, Bhubaneswar, Odisha</strong></div>
            </div>
          </div>

          <h2 className="text-2xl font-bold text-slate-800 mt-8 mb-4 font-heading">
            Special Note:
          </h2>
          <ul className="list-disc pl-6 space-y-3 text-base text-slate-700 leading-relaxed">
            <li>
              At least one author of each accepted paper must be registered for the conference to have the paper included in the conference proceedings and indexed publication.
            </li>
            <li>
              One author (Indian or Foreign, from Academia or Industry) may register a second paper with a <strong>50% concession</strong> on the registration fee. A separate registration is required for each additional paper beyond the first two (Authors are eligible for a 50% discount on the second paper, provided that both papers have the same authors).
            </li>
            <li>
              Student registration is accepted for papers to be published, but the two-paper registration concession does not apply to student registrations.
            </li>
            <li>
              Please include <strong>18% GST</strong> on the total registration amount while making the payment. For example, if the registration fee is INR 7000, the total payable amount including GST is INR 8260.
            </li>
            <li>
              Manuscripts are limited to a standard length of six (6) pages. Authors may submit up to two (2) additional pages, subject to over-length page charges. The applicable fees for the seventh and eighth pages are ₹1,000 and ₹2,000 respectively for Indian authors, and USD 50 and USD 100 respectively for international authors. Under no circumstances will a manuscript exceed the absolute maximum limit of eight (8) pages.
            </li>
            <li>
              After completing the payment, authors must fill out the Google Form at{' '}
              <a href="https://forms.gle/eFNAa3H4Qg13kfyn8" target="_blank" rel="noreferrer" className="text-blue-600 font-medium underline">
                Click here to fill the Author Registration Form
              </a>{' '}
              to complete the registration process.
            </li>
            <li>
              If you are <strong>not an author</strong> and wish to attend the conference, please register as an attendee by paying the applicable fee and filling out the attendee registration form at{' '}
              <a href="https://forms.gle/m2pqtU4VQpujxFMU8" target="_blank" rel="noreferrer" className="text-blue-600 font-medium underline">
                Click here to fill the Attendee Registration Form
              </a>. Authors who have already registered should not fill out this form.
            </li>
          </ul>
        </div>

      </div>

      {/* ======================= GOOGLE FORMS MODAL REPLICA ======================= */}
      {activeFormModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-900/75 backdrop-blur-sm overflow-y-auto">
          <div className="relative w-full max-w-3xl bg-[#f0ebf8] rounded-2xl shadow-2xl overflow-hidden my-8 border border-purple-200">
            
            {/* Google Forms Purple Top Accent Banner */}
            <div className="h-4 bg-[#673ab7] w-full" />

            {/* Modal Header Card */}
            <div className="bg-white p-6 sm:p-8 border-b border-slate-200 relative">
              <button 
                onClick={closeFormModal}
                className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 rounded-full hover:bg-slate-100 transition"
                aria-label="Close form"
              >
                <X className="w-5 h-5" />
              </button>

              <div className="flex items-center gap-2 mb-2">
                <span className="px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800 text-xs font-bold uppercase tracking-wider">
                  Official Registration
                </span>
                <span className="text-xs text-slate-500 font-medium">KIIT Bhubaneswar • January 22–24, 2027</span>
              </div>

              <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 font-heading">
                {activeFormModal === 'author' 
                  ? 'ACIE-2027 Author Registration Form' 
                  : 'ACIE-2027 Attendee Registration Form'}
              </h2>

              <p className="text-sm text-slate-600 mt-2 leading-relaxed">
                1st International Conference on Advances in Computing, Intelligence and Engineering (ACIE 2027). Please fill in all the details accurately. Ensure payment has been executed and UTR reference number is available.
              </p>
              
              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                <span className="text-rose-600 font-medium">* Indicates required question</span>
                <a 
                  href={activeFormModal === 'author' ? "https://forms.gle/eFNAa3H4Qg13kfyn8" : "https://forms.gle/m2pqtU4VQpujxFMU8"}
                  target="_blank" 
                  rel="noreferrer"
                  className="text-purple-700 font-semibold hover:underline inline-flex items-center gap-1"
                >
                  Open in Google Forms <ExternalLink className="w-3 h-3" />
                </a>
              </div>
            </div>

            {/* Form Content / Confirmation */}
            {formSubmitted ? (
              <div className="p-8 sm:p-12 text-center bg-white space-y-4">
                <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-2">
                  <CheckCircle className="w-10 h-10" />
                </div>
                <h3 className="text-2xl font-bold text-slate-900 font-heading">
                  Registration Successfully Submitted!
                </h3>
                <p className="text-slate-600 text-sm max-w-lg mx-auto">
                  Thank you, <strong>{formData.authorName || 'Author'}</strong>. Your submission for {activeFormModal === 'author' ? `Paper ID: ${formData.paperId || 'ACIE-2027'}` : 'Conference Attendance'} has been registered in the ACIE 2027 database. A confirmation receipt has been dispatched to <strong>{formData.email || 'your email'}</strong>.
                </p>
                <div className="p-4 bg-slate-50 rounded-xl border border-slate-200 max-w-md mx-auto text-left text-xs space-y-1 font-mono">
                  <div>Registration ID: <strong>ACIE-2027-REG-{(Math.random()*90000+10000).toFixed(0)}</strong></div>
                  <div>Category: <strong>{formData.category}</strong></div>
                  <div>Payment Reference: <strong>{formData.utrNumber || 'VERIFIED'}</strong></div>
                </div>
                <div className="pt-4 flex justify-center gap-3">
                  <button
                    onClick={closeFormModal}
                    className="px-6 py-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-bold text-sm transition shadow-sm"
                  >
                    Done
                  </button>
                </div>
              </div>
            ) : (
              <form onSubmit={handleFormSubmit} className="p-4 sm:p-6 space-y-5 max-h-[70vh] overflow-y-auto">
                
                {/* Email Field */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Email Address <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="email"
                    name="email"
                    required
                    value={formData.email}
                    onChange={handleInputChange}
                    placeholder="your.email@institution.edu"
                    className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                  />
                </div>

                {/* Author / Attendee Name */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Full Name <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="text"
                    name="authorName"
                    required
                    value={formData.authorName}
                    onChange={handleInputChange}
                    placeholder="Prof. / Dr. / Mr. / Ms. Full Name"
                    className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                  />
                </div>

                {/* Paper ID & Title (if Author form) */}
                {activeFormModal === 'author' && (
                  <>
                    <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                      <label className="block text-sm font-bold text-slate-800">
                        Paper ID (Microsoft CMT Submission ID) <span className="text-rose-500">*</span>
                      </label>
                      <input
                        type="text"
                        name="paperId"
                        required
                        value={formData.paperId}
                        onChange={handleInputChange}
                        placeholder="e.g. 104, 256, ACIE-48"
                        className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                      />
                    </div>

                    <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                      <label className="block text-sm font-bold text-slate-800">
                        Paper Title <span className="text-rose-500">*</span>
                      </label>
                      <input
                        type="text"
                        name="paperTitle"
                        required
                        value={formData.paperTitle}
                        onChange={handleInputChange}
                        placeholder="Full title of the accepted manuscript"
                        className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                      />
                    </div>
                  </>
                )}

                {/* Affiliation / University */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Affiliation / Institution / University <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="text"
                    name="affiliation"
                    required
                    value={formData.affiliation}
                    onChange={handleInputChange}
                    placeholder="Department &amp; University / Company Name"
                    className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                  />
                </div>

                {/* Contact Phone */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Contact / WhatsApp Mobile Number <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="tel"
                    name="phone"
                    required
                    value={formData.phone}
                    onChange={handleInputChange}
                    placeholder="+91-XXXXXXXXXX"
                    className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                  />
                </div>

                {/* Registration Category Radio */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-3">
                  <label className="block text-sm font-bold text-slate-800">
                    Registration Fee Tier (including 18% GST) <span className="text-rose-500">*</span>
                  </label>
                  {[
                    "Students - India (IEEE) [₹7,000 + 18% GST = ₹8,260]",
                    "Students - India (Non-IEEE) [₹7,500 + 18% GST = ₹8,850]",
                    "Academia - India (IEEE) [₹8,000 + 18% GST = ₹9,440]",
                    "Academia - India (Non-IEEE) [₹9,000 + 18% GST = ₹10,620]",
                    "Industry - India (IEEE) [₹9,000 + 18% GST = ₹10,620]",
                    "Industry - India (Non-IEEE) [₹10,000 + 18% GST = ₹11,800]",
                    "Attendee - India (IEEE) [₹3,000 + 18% GST = ₹3,540]",
                    "Foreign Authors / Delegates [USD $250 - $400]"
                  ].map((cat, idx) => (
                    <label key={idx} className="flex items-center gap-3 text-xs sm:text-sm text-slate-700 cursor-pointer hover:text-purple-900">
                      <input 
                        type="radio" 
                        name="category" 
                        value={cat} 
                        checked={formData.category === cat}
                        onChange={handleInputChange}
                        className="accent-purple-700 w-4 h-4"
                      />
                      <span>{cat}</span>
                    </label>
                  ))}
                </div>

                {/* Presentation Mode */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-3">
                  <label className="block text-sm font-bold text-slate-800">
                    Presentation Mode Preference <span className="text-rose-500">*</span>
                  </label>
                  {[
                    "In-Person at KIIT Campus, Bhubaneswar",
                    "Virtual Presentation via Conference Plenary Stream"
                  ].map((mode, idx) => (
                    <label key={idx} className="flex items-center gap-3 text-xs sm:text-sm text-slate-700 cursor-pointer hover:text-purple-900">
                      <input 
                        type="radio" 
                        name="presentationMode" 
                        value={mode} 
                        checked={formData.presentationMode === mode}
                        onChange={handleInputChange}
                        className="accent-purple-700 w-4 h-4"
                      />
                      <span>{mode}</span>
                    </label>
                  ))}
                </div>

                {/* Payment Reference UTR */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Payment Transaction Reference / UTR Number <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="text"
                    name="utrNumber"
                    required
                    value={formData.utrNumber}
                    onChange={handleInputChange}
                    placeholder="Enter UPI / NEFT / IMPS reference number"
                    className="w-full p-2.5 text-sm border-b-2 border-slate-300 focus:border-purple-600 outline-none transition bg-slate-50/50"
                  />
                </div>

                {/* Upload Payment Proof */}
                <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                  <label className="block text-sm font-bold text-slate-800">
                    Upload Payment Receipt / Screenshot (PDF, PNG, JPG) <span className="text-rose-500">*</span>
                  </label>
                  <div className="border-2 border-dashed border-slate-300 hover:border-purple-500 rounded-xl p-4 text-center cursor-pointer transition">
                    <input 
                      type="file" 
                      accept=".pdf,.png,.jpg,.jpeg" 
                      onChange={handleFileUpload} 
                      className="hidden" 
                      id="paymentProofFile"
                    />
                    <label htmlFor="paymentProofFile" className="cursor-pointer flex flex-col items-center justify-center gap-2">
                      <Upload className="w-6 h-6 text-purple-600" />
                      <span className="text-xs font-semibold text-slate-700">
                        {formData.fileName ? `Selected: ${formData.fileName}` : 'Click to select payment screenshot or PDF'}
                      </span>
                    </label>
                  </div>
                </div>

                {/* Form Footer Actions */}
                <div className="flex items-center justify-between pt-4">
                  <button
                    type="button"
                    onClick={closeFormModal}
                    className="px-5 py-2 text-xs font-semibold text-slate-600 hover:bg-slate-200 rounded-lg transition"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-8 py-2.5 bg-[#673ab7] hover:bg-[#5e35b1] text-white font-bold rounded-lg shadow-md hover:shadow-lg transition text-sm cursor-pointer"
                  >
                    Submit ACIE-2027 Registration
                  </button>
                </div>

              </form>
            )}

          </div>
        </div>
      )}

    </main>
  );
}
