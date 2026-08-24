const API = "http://127.0.0.1:8000";


const registerForm =
    document.getElementById("registerForm");

const submitButton =
    document.getElementById("submitButton");

const message =
    document.getElementById("message");


registerForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const account = {

            profile_id:
                document.getElementById("profile_id").value.trim(),

            name:
                document.getElementById("name").value.trim(),

            email:
                document.getElementById("email").value.trim(),

            password:
                document.getElementById("password").value,

            phone_number:
                document.getElementById("phone_number").value.trim(),

            university_id:
                getNumberValue("university_id"),

            department_id:
                getNumberValue("department_id"),

            designation:
                document.getElementById("designation").value.trim(),

            employee_id:
                document.getElementById("employee_id").value.trim()

        };



        if (!account.email) {

            message.textContent =
                "Please enter your email.";

            return;
        }


        if (!account.password) {

            message.textContent =
                "Please enter a password.";

            return;
        }


        submitButton.disabled = true;

        message.textContent =
            "Sending verification code...";


        try {

            const response =
                await fetch(
                    `${API}/send-otp`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            email: account.email
                        })
                    }
                );


            const result =
                await response.json();


            if (
                !response.ok ||
                !result.result
            ) {

                message.textContent =
                    result.detail ||
                    "Failed to send OTP.";

                submitButton.disabled = false;

                return;
            }


            /*
             * Store the account temporarily.
             *
             * It has NOT been inserted into MySQL yet.
             */

            sessionStorage.setItem(
                "pendingAccount",
                JSON.stringify(account)
            );


            // Go to OTP page

            window.location.href = "otp.html";

        }

        catch (error) {

            console.error(error);

            message.textContent =
                "Unable to connect to the server.";

            submitButton.disabled = false;

        }

    }
);


function getNumberValue(id) {

    const value =
        document.getElementById(id).value.trim();

    if (value === "") {
        return null;
    }

    return Number(value);
}