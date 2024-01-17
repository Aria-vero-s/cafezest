document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $(".navbar-toggler").click(function () {
            $(".transparent-navbar").toggleClass("background-visible");
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var openModalBtn = document.getElementById("openModalBtn");
    var closeModalBtn = document.getElementById("closeModalBtn");
    var newsletterModal = document.getElementById("newsletterModal");
    var newsletterForm = document.getElementById("newsletterForm");
    var thankYouMessage = document.getElementById("thankYouMessage");

    // Trigger the modal to open when the page loads
    newsletterModal.style.display = "block";

    closeModalBtn.addEventListener("click", function() {
        newsletterModal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === newsletterModal) {
            newsletterModal.style.display = "none";
        }
    });

    newsletterForm.addEventListener("submit", function(event) {
        event.preventDefault();
        // Add your code here to handle form submission (e.g., sending the email to the server).
        
        // Display the thank you message for 2 seconds and then close the modal
        thankYouMessage.style.display = "block";
        setTimeout(function() {
            thankYouMessage.style.display = "none";
            newsletterModal.style.display = "none"; // Close the modal
        }, 2000); // 2 seconds
    });
});

// menu


// This JavaScript code will change the text color to red
document.addEventListener("DOMContentLoaded", function() {
    var demo = document.getElementById("demo");
    demo.style.color = "red";
});

