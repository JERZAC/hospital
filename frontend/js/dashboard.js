const API_URL =
    "http://127.0.0.1:8000";


const token =
    localStorage.getItem("token");


if (!token) {

    window.location.href =
        "login.html";
}


// =====================================
// USUARIO
// =====================================

async function loadUser() {

    const response = await fetch(
        `${API_URL}/auth/me`,
        {
            headers: {
                "Authorization":
                    `Bearer ${token}`
            }
        }
    );


    if (!response.ok) {

        logout();

        return;
    }


    const user =
        await response.json();


    document.getElementById(
        "userName"
    ).textContent =
        user.full_name;
}


// =====================================
// TICKETS
// =====================================

async function loadTickets() {

    const response = await fetch(
        `${API_URL}/tickets`,
        {
            headers: {
                "Authorization":
                    `Bearer ${token}`
            }
        }
    );


    if (!response.ok) {

        return;
    }


    const tickets =
        await response.json();


    renderTickets(tickets);
}


// =====================================
// MOSTRAR TICKETS
// =====================================

function renderTickets(tickets) {

    const container =
        document.getElementById(
            "ticketsContainer"
        );


    container.innerHTML = "";


    let critical = 0;

    let open = 0;


    tickets.forEach(ticket => {

        if (
            ticket.priority === "crítica"
        ) {

            critical++;
        }


        if (
            ticket.status === "abierto"
        ) {

            open++;
        }


        const div =
            document.createElement(
                "div"
            );


        div.className =
            "ticket";


        div.innerHTML = `

            <div>

                <strong>
                    #${ticket.id}
                    ${ticket.title}
                </strong>

                <p>
                    ${ticket.description}
                </p>

            </div>

            <div>

                <span>
                    ${ticket.category}
                </span>

                <span>
                    ${ticket.priority}
                </span>

                <span>
                    ${ticket.status}
                </span>

            </div>

            <p>
                🤖 ${ticket.recommendation}
            </p>

        `;


        container.appendChild(div);

    });


    document.getElementById(
        "totalTickets"
    ).textContent =
        tickets.length;


    document.getElementById(
        "openTickets"
    ).textContent =
        open;


    document.getElementById(
        "criticalTickets"
    ).textContent =
        critical;
}


// =====================================
// CREAR TICKET
// =====================================

const form =
    document.getElementById(
        "createTicketForm"
    );


if (form) {

    form.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const ticket = {

                title:
                    document.getElementById(
                        "title"
                    ).value,

                description:
                    document.getElementById(
                        "description"
                    ).value,

                department:
                    document.getElementById(
                        "department"
                    ).value,

                impact:
                    Number(
                        document.getElementById(
                            "impact"
                        ).value
                    ),

                urgency:
                    Number(
                        document.getElementById(
                            "urgency"
                        ).value
                    )
            };


            const response =
                await fetch(
                    `${API_URL}/tickets`,
                    {
                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json",

                            "Authorization":
                                `Bearer ${token}`
                        },

                        body:
                            JSON.stringify(ticket)
                    }
                );


            if (!response.ok) {

                alert(
                    "No se pudo crear el ticket"
                );

                return;
            }


            form.reset();


            document.getElementById(
                "ticketForm"
            ).classList.add(
                "hidden"
            );


            loadTickets();

        }
    );
}


// =====================================
// MOSTRAR FORMULARIO
// =====================================

function showTicketForm() {

    document.getElementById(
        "ticketForm"
    ).classList.remove(
        "hidden"
    );
}


// =====================================
// LOGOUT
// =====================================

function logout() {

    localStorage.removeItem(
        "token"
    );

    window.location.href =
        "login.html";
}


// =====================================
// INICIO
// =====================================

loadUser();

loadTickets();