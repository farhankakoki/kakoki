// Initialize EmailJS with your public key
(function () {
  emailjs.init("cRCZbdyMRRzyoyIyz");
})();

const contactForm = document.getElementById("contact-form");
const successPopup = document.getElementById("success-popup");
const popupOverlay = document.getElementById("popup-overlay");
const closePopupBtn = document.getElementById("close-popup");

if (contactForm) {
  const submitBtn = contactForm.querySelector("button[type='submit']");

  function showFormError(message) {
    let errEl = document.getElementById("form-error-msg");
    if (!errEl) {
      errEl = document.createElement("p");
      errEl.id = "form-error-msg";
      errEl.style.cssText =
        "color:#c0392b;font-size:0.75rem;font-weight:600;margin:12px 0 0;text-align:center;line-height:1.4;text-transform:uppercase;letter-spacing:0.05em;";
      contactForm.appendChild(errEl);
    }
    errEl.textContent = message;
  }

  function clearFormError() {
    const errEl = document.getElementById("form-error-msg");
    if (errEl) errEl.textContent = "";
  }

  function showPopup() {
    if (successPopup && popupOverlay) {
        // Remove hidden and set display
        successPopup.classList.remove("hidden");
        popupOverlay.classList.remove("hidden");
        
        // Use timeout to allow transition
        setTimeout(() => {
          popupOverlay.classList.remove("opacity-0");
          successPopup.style.opacity = "1";
          successPopup.style.transform = "translate(-50%, -50%) scale(1)";
        }, 10);
    }
  }

  function hidePopup() {
    if (successPopup && popupOverlay) {
        popupOverlay.classList.add("opacity-0");
        successPopup.style.opacity = "0";
        successPopup.style.transform = "translate(-50%, -50%) scale(0.95)";
        
        setTimeout(() => {
          successPopup.classList.add("hidden");
          popupOverlay.classList.add("hidden");
          if (typeof closeContactModal === "function") {
            closeContactModal();
          }
        }, 300);
    }
  }

  if (closePopupBtn) closePopupBtn.addEventListener("click", hidePopup);
  if (popupOverlay) popupOverlay.addEventListener("click", hidePopup);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && successPopup && successPopup.style.display === "block") {
      hidePopup();
    }
  });

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    clearFormError();

    const name = contactForm.querySelector("#user_name").value.trim();
    const phone = contactForm.querySelector("#user_phone").value.trim();
    const email = contactForm.querySelector("#user_email").value.trim();
    const projectType = contactForm.querySelector("#project_type").value.trim();
    const message = contactForm.querySelector("#message").value.trim();
    const serviceAreaEl = contactForm.querySelector('input[name="service_area"]');
    const serviceArea = serviceAreaEl ? serviceAreaEl.value.trim() : "Default";
    const leadSourceEl = contactForm.querySelector('input[name="lead_source"]');
    const leadSource = leadSourceEl ? leadSourceEl.value.trim() : "Main Form";
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneDigits = phone.replace(/\D/g, "");

    if (!name || !phone || !email || !projectType || !message) {
      showFormError("Please fill in all fields before submitting.");
      return;
    }

    if (phoneDigits.length < 10) {
      showFormError("Please enter a valid phone number.");
      return;
    }

    if (!emailRegex.test(email)) {
      showFormError("Please enter a valid email address.");
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Sending...";

    const formattedMessage = [
      `Name: ${name}`,
      `Phone: ${phone}`,
      `Email: ${email}`,
      `Project Type: ${projectType}`,
      `Service Area: ${serviceArea}`,
      `Lead Source: ${leadSource}`,
      "",
      "Project Details:",
      message,
    ].join("\n");

    const templateParams = {
      name,
      from_name: name,
      user_name: name,
      phone,
      user_phone: phone,
      email,
      user_email: email,
      reply_to: email,
      project_type: projectType,
      service_area: serviceArea,
      lead_source: leadSource,
      subject: `New ${projectType} inquiry from ${name}`,
      title: `New ${projectType} inquiry`,
      message: formattedMessage,
    };

    emailjs
      .send("service_ppfo81u", "template_1xcw28x", templateParams)
      .then(() => {
        showPopup();
        contactForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Send inquiry <i class="fa-solid fa-paper-plane ml-2"></i>';
      })
      .catch((err) => {
        console.error("EmailJS Error:", err);
        showFormError(
          "Oops! Something went wrong. Please try again or email us directly at kakokicreativeco@gmail.com"
        );
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Send inquiry <i class="fa-solid fa-paper-plane ml-2"></i>';
      });
  });
}

// Mini lead form submission logic for Homepage Popup
const miniForm = document.getElementById("miniLeadForm");
if (miniForm) {
  miniForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const btn = this.querySelector("button");
    const originalText = "SEND INQUIRY";
    btn.innerText = "SENDING...";
    btn.disabled = true;

    const nameInput = this.querySelector('input[name="user_name"]');
    const phoneInput = this.querySelector('input[name="user_phone"]');
    const name = nameInput ? nameInput.value.trim() : "Anonymous";
    const phone = phoneInput ? phoneInput.value.trim() : "N/A";

    const templateParams = {
      name,
      from_name: name,
      user_name: name,
      phone,
      user_phone: phone,
      reply_to: 'Inquiry via Mini-Form',
      project_type: 'Quick Lead',
      service_area: 'Mini-Popup Hub',
      lead_source: 'Homepage Mini-Popup',
      subject: `Quick Lead Inquiry from ${name}`,
      message: `Quick Inquiry from Mini-Popup\nName: ${name}\nPhone: ${phone}`
    };

    emailjs
      .send("service_ppfo81u", "template_1xcw28x", templateParams)
      .then(() => {
        btn.innerText = "SUCCESS!";
        btn.style.backgroundColor = "#4ade80";
        setTimeout(() => {
          const miniPopup = document.getElementById("miniContactPopup");
          if (miniPopup) {
            miniPopup.style.transform = "translateY(150%)";
            miniPopup.style.opacity = "0";
          }
          this.reset();
          btn.innerText = originalText;
          btn.style.backgroundColor = "";
          btn.disabled = false;
        }, 2000);
      })
      .catch((err) => {
        console.error("EmailJS Error:", err);
        // Show actual error message if possible to help user
        const errorMsg = err.text || err.message || "Failed to send";
        btn.innerText = "RETRY";
        btn.disabled = false;
        alert("Enquiry Error: " + errorMsg);
      });
  });
}
