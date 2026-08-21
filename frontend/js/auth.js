const API_URL = "http://127.0.0.1:8000";


const loginForm =
    document.getElementById("loginForm");

const registerForm =
    document.getElementById("registerForm");


if (registerForm) {

    registerForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const full_name =
                document.getElementById(
                    "full_name"
                ).value;


            const email =
                document.getElementById(
                    "email"
                ).value;


            const password =
                document.getElementById(
                    "password"
                ).value;


            const role =
                document.getElementById(
                    "role"
                ).value;


            const response = await fetch(
                `${API_URL}/auth/register`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        full_name,
                        email,
                        password,
                        role
                    })
                }
            );


            const data =
                await response.json();


            if (!response.ok) {

                document.getElementById(
                    "message"
                ).textContent =
                    data.detail ||
                    "Error en registro";

                return;
            }


            alert(
                "Usuario registrado correctamente"
            );


            window.location.href =
                "login.html";

        }
    );
}
if (loginForm) {

    loginForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const email =
                document.getElementById("email").value;

            const password =
                document.getElementById("password").value;


            try {

                const response = await fetch(
                    `${API_URL}/auth/login`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            email,
                            password
                        })
                    }
                );


                const data =
                    await response.json();


                if (!response.ok) {

                    document.getElementById(
                        "message"
                    ).textContent =
                        data.detail ||
                        "Error al iniciar sesión";

                    return;
                }


                localStorage.setItem(
                    "token",
                    data.access_token
                );


                window.location.href =
                    "dashboard.html";


            } catch (error) {

                document.getElementById(
                    "message"
                ).textContent =
                    "No se pudo conectar con el servidor";
            }

        }
    );
}