document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {
        form.addEventListener("submit", function (e) {
            const email = form.querySelector("input[name='email']");
            const password = form.querySelector("input[name='password']");

            if (!email.value.includes("@")) {
                alert("Please enter a valid email.");
                e.preventDefault();
                return;
            }

            if (password.value.length < 6) {
                alert("Password must be at least 6 characters.");
                e.preventDefault();
                return;
            }
        });
    });
});
