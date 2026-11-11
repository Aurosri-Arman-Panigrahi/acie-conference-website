import React, { useEffect } from 'react';
import PageBanner from '../components/PageBanner';
import AOS from 'aos';

export default function CameraReadySubmission() {
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
        title="CAMERA READY PAPER SUBMISSION" 
      />

      <div className="w-full bg-[#E7ECFF] py-20">
        <div data-aos="fade-up" className="max-w-6xl mx-auto px-6 py-10 text-slate-700 leading-relaxed">
          <p>
            The authors will have to submit a camera-ready version as per the following guidelines on or before 30th November 2026.
          </p>

          <ol className="list-decimal list-inside mt-4 space-y-2">
            <li>
              The similarity index of your paper must be less than 25%, including references. Please ensure that the overall similarity index is below 25% (with references), as verified using standard plagiarism detection tools (e.g., Turnitin). AI-generated content must be less than 20%. Papers exceeding these limits will not be included in the IEEE Xplore proceedings, and registration fees will not be refunded under any circumstances.
            </li>
            <li>
              The paper must be thoroughly revised, with all typographical, spelling, and grammatical errors corrected before submitting the final camera-ready version.
            </li>
            <li>
              Paper must be as per the IEEE template (
              <a 
                href="https://www.ieee.org/conferences/publishing/templates.html" 
                className="text-orange-600 no-underline hover:underline" 
                target="_blank" 
                rel="noopener noreferrer"
              >
                https://www.ieee.org/conferences/publishing/templates.html
              </a>
              ).
            </li>
            <li>
              Please include the copyright notice on the left of the footer section of the first page (not all pages) of your manuscript as mentioned below.
              <ul className="list-disc list-inside ml-6 mt-2 space-y-1">
                <li>For papers in which all authors are employed by the US government, the copyright notice is: U.S. Government work not protected by U.S. copyright</li>
                <li>For papers in which all authors are employed by a Crown government (UK, Canada, and Australia), the copyright notice is: 979-8-3315-7088-0/26/$31.00 ©2026 Crown</li>
                <li>For papers in which all authors are employed by the European Union, the copyright notice is: 979-8-3315-7088-0/26/$31.00 ©2026 European Union</li>
                <li>For all other papers the copyright notice is: 979-8-3315-7088-0/26/$31.00 ©2026 IEEE</li>
              </ul>
            </li>
            <li>
              After implementing all corrections and putting copyright number in the first page of your manuscript, follow the following process to prepare Camera Ready submission through IEEE pdf-express:
              <ul className="list-disc list-inside ml-6 mt-2 space-y-1">
                <li>
                  Log in to the IEEE PDF eXpress TM site (
                  <a 
                    href="https://ieee-pdf-express.org/account/Login" 
                    className="text-orange-600 no-underline hover:underline" 
                    target="_blank" 
                    rel="noopener noreferrer"
                  >
                    https://ieee-pdf-express.org/account/Login
                  </a>
                  )
                </li>
                <li>
                  First-time users should do the following:
                  <ol className="list-[lower-roman] list-inside ml-6 mt-2 space-y-1">
                    <li>Click on “Create account”.</li>
                    <li>Enter the following:</li>
                    <li>70672X for the Conference ID</li>
                    <li>your email address</li>
                    <li>a password</li>
                  </ol>
                </li>
                <li>Click on “SUBMIT” Button: (An email helpdesk-ieee will be sent to your email)</li>
                <li>Account Activation: Go to your email and please click on URL “Click for account activation”. (Email Addressed will be verified)</li>
                <li>Login to your New IEEE PDF Express Account using login credentials</li>
                <li>Fill the IEEE PDF eXpress User profile: Personal information and Submit; Click ok</li>
                <li>Go to the “Dashboard” and click on “CREATE NEW TITLE” and continue to enter information as prompted.</li>
                <li>If Error in converting file, then please correct the paper according to the IEEE Conference paper template and resubmit for the PDF eXpress until “File has been converted successfully” without error.</li>
                <li>After “File has been converted successfully”, download the Pdf from the “Action” Tab in the Dashboard.</li>
              </ul>
            </li>
            <li>
              Download the pdf file of your paper from PDF eXpressPlus website (Don’t rename it) and upload it via the CMT Portal for Camera Ready Paper Submission of ACIE-2027 at
              <br />
              <a 
                href="https://cmt3.research.microsoft.com/ACIE2027" 
                className="text-orange-600 no-underline hover:underline" 
                target="_blank" 
                rel="noopener noreferrer"
              >
                https://cmt3.research.microsoft.com/ACIE2027
              </a>
            </li>
          </ol>

          <h2 className="mt-12 mb-4 text-3xl font-extrabold text-slate-900">
            Electronic Copyright form submission:
          </h2>
          <p className="mb-6 text-base">
            Procedure for IEEE Copyright Form eCF submission:
            <br />
            To enable your paper to appear in IEEE eXplorer, it is mandatory to transfer the Copyright to IEEE. The corresponding/submitting author of each paper must transfer IEEE eCF. The steps to transfer the Copyright to IEEE are also given below:
          </p>
          <ol className="text-base list-decimal list-inside space-y-2 ml-6 mt-2">
            <li>Login to your CMT Paper Submission Portal and click on the IEEE copyright link. You will be redirected to IEEE Copyright Form Submission page.</li>
            <li>Click on “Click here to redirect to the IEEE copyright website” to transfer eCF and you will be redirected to IEEE copyright portal.</li>
            <li>Follow the steps (Step 1 to Step 5) and provided instructions to complete the IEEE Copyright Transfer process.</li>
            <li>At the end of Step 5, download the completed Copyright Form and save it as .pdf (Make sure to download a copy of the completed form.)</li>
            <li>Login to your CMT Paper Submission Portal and upload this pdf file of Copyright Transfer Form.</li>
          </ol>
          <p className="text-base mt-6">
            It completes the Copyright Transfer of your paper to IEEE. Please note that separate copyright transfer is required for each paper.
          </p>
        </div>
      </div>
    </main>
  );
}
