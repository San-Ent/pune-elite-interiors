const faqQuestions = document.querySelectorAll(".faq-question");

faqQuestions.forEach(function (question) {

    question.addEventListener("click", function () {

        const answer = question.nextElementSibling;
        const icon = question.querySelector(".faq-icon");

        if (answer.style.display === "block") {

            answer.style.display = "none";
            icon.textContent = "+";

        } else {

            answer.style.display = "block";
            icon.textContent = "−";

        }

    });

});



const contactForm = document.querySelector("#contact-form");

if (contactForm) {
    const formStatus = document.querySelector("#form-status");
    const submitButton = contactForm.querySelector(
        'button[type="submit"]'
    );

    contactForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        formStatus.textContent = "Sending your enquiry...";
        formStatus.className = "";
        submitButton.disabled = true;

        try {
            const response = await fetch(contactForm.action, {
                method: "POST",
                body: new FormData(contactForm),
                headers: {
                    Accept: "application/json"
                }
            });

            const result = await response.json();

            if (!response.ok) {
                const errorMessage = result.errors
                    ?.map(error => error.message)
                    .join(" ");

                throw new Error(
                    errorMessage || "Unable to submit your enquiry."
                );
            }

            formStatus.textContent =
                "Thank you! Your enquiry has been received. " +
                "We'll get back to you soon.";

            formStatus.className = "success";
            contactForm.reset();

        } catch (error) {
            formStatus.textContent =
                "We couldn't confirm your submission. " +
                "Please try again or contact us by phone or WhatsApp.";

            formStatus.className = "error";
            console.error("Form submission error:", error);

        } finally {
            submitButton.disabled = false;
        }
    });
}




