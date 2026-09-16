
const loginForm = document.getElementById("loginForm");
const errorMessage = document.getElementById("errorMessage");
const loginButton = document.getElementById("loginButton");

const API_URL = "http://127.0.0.1:8000";


loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    errorMessage.textContent = "";

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;


    loginButton.disabled = true;
    loginButton.textContent = "Verifying...";


    try {

        const response = await fetch(
            `${API_URL}/verify_credentials`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );


        const result = await response.json();


        if (response.ok && result.success === true) {

            window.location.href = "dashboard.html";

            return;
        }


        errorMessage.textContent = "Email or password is incorrect.";

    }

    catch (error) {

        console.error("Login error:", error);

        errorMessage.textContent =
            "Unable to connect to the server. Please try again.";
    }

    finally {

        loginButton.disabled = false;
        loginButton.textContent = "Login";
    }

});

