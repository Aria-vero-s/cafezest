document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $(".navbar-toggler").click(function () {
            $(".transparent-navbar").toggleClass("background-visible");
        });
    });
});