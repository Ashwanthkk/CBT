const API = "http://127.0.0.1:8000";




const storedAccount =
    sessionStorage.getItem("pendingAccount");


// If user directly opens otp.html
// without going through registration

if (!storedAccount) {

    window.location.href = "register.html";

}


// Convert stored JSON back into object

const accountData =
    JSON.parse(storedAccount);



const emailElement =
    document.getElementById("email");

const otpInput =
    document.getElementById("otp");

const otpForm =
    document.getElementById("otpForm");

const verifyButton =
    document.getElementById("verifyButton");

const resendButton =
    document.getElementById("resendButton");

const timer =
    document.getElementById("timer");

const message =
    document.getElementById("message");



emailElement.textContent =
    accountData.email;



// Allow only numbers in OTP


otpInput.addEventListener(
    "input",
    function () {

        this.value =
            this.value
                .replace(/\D/g, "")
                .slice(0, 6);

    }
);



// VERIFY OTP


otpForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const otp =
            otpInput.value;


        // Validate OTP length

        if (otp.length !== 6) {

            message.textContent =
                "Please enter the 6-digit OTP.";

            return;

        }


        // Disable button while request is running

        verifyButton.disabled = true;

        message.textContent =
            "Verifying OTP...";


        try {

            const response =
                await fetch(
                    `${API}/verify-otp`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            email:
                                accountData.email,

                            user_otp:
                                otp

                        })
                    }
                );


            const result =
                await response.json();


    
            // OTP verification failed

            if (
                !response.ok ||
                !result.result
            ) {

                message.textContent =
                    result.message ||
                    "Invalid OTP.";

                verifyButton.disabled =
                    false;

                return;

            }


            // OTP successfully verified
           

            message.textContent =
                "Email verified. Creating account...";


            // Prevent multiple account requests

            verifyButton.disabled = true;


            
            // CREATE ACCOUNT
           

            const accountResponse =
                await fetch(
                    `${API}/create-account`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify(
                            accountData
                        )
                    }
                );


            const accountResult =
                await accountResponse.json();


            
            // Account creation failed
            

            if (!accountResponse.ok) {

                message.textContent =
                    accountResult.detail ||
                    "Failed to create account.";

                verifyButton.disabled =
                    false;

                return;

            }


            
            // Account creation Suceess

            sessionStorage.removeItem(
                "pendingAccount"
            );


            showSuccessPopup();

        }

        catch (error) {

            console.error(
                "Request error:",
                error
            );


            message.textContent =
                "Unable to connect to the server.";


            verifyButton.disabled =
                false;

        }

    }
);




resendButton.addEventListener(
    "click",
    async function () {

        /*
         * Disable immediately.
         *
         * This prevents the user from
         * repeatedly clicking the button.
         */

        resendButton.disabled = true;


        message.textContent =
            "Sending new OTP...";


        try {

            const response =
                await fetch(
                    `${API}/resend-otp`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            email:
                                accountData.email

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
                    "Failed to resend OTP.";

                resendButton.disabled =
                    false;

                return;

            }


           

            message.textContent =
                "A new OTP has been sent.";

            startCooldown();

        }

        catch (error) {

            console.error(
                "Resend error:",
                error
            );


            message.textContent =
                "Unable to connect to the server.";


            resendButton.disabled =
                false;

        }

    }
);



function startCooldown() {

    let seconds = 30;


    timer.textContent =
        `Resend available in ${seconds}s`;


    const interval =
        setInterval(
            function () {

                seconds--;


                if (seconds <= 0) {

                    clearInterval(interval);

                    timer.textContent = "";

                    resendButton.disabled =
                        false;

                    return;

                }


                timer.textContent =
                    `Resend available in ${seconds}s`;

            },
            1000
        );

}



function showSuccessPopup() {


    const overlay =
        document.createElement("div");


    overlay.className =
        "success-overlay";


    // Create popup

    overlay.innerHTML = `

        <div class="success-popup">

            <div class="success-icon">
                ✓
            </div>

            <h2>
                Account Created
            </h2>

            <p>
                Your professor account has been
                created successfully.
            </p>

            <button
                id="continueButton"
                type="button"
            >
                Continue
            </button>

        </div>

    `;



    document.body.appendChild(
        overlay
    );



    document
        .getElementById("continueButton")
        .addEventListener(
            "click",
            function () {

                window.location.href =
                    "login.html";

            }
        );

}