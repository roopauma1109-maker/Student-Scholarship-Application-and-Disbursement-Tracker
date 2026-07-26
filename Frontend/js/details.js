const API = "http://127.0.0.1:8000";

const params = new URLSearchParams(window.location.search);

const id = params.get("id");

async function loadDetails() {

    const response = await fetch(`${API}/applications/${id}`);

    const app = await response.json();

    const applied = new Date(app.applied_date);

    const today = new Date();

    const days =
        Math.floor((today - applied) / (1000 * 60 * 60 * 24));

    document.getElementById("details").innerHTML = `

    <h2>${app.student.name}</h2>

    <p><b>Department:</b> ${app.student.department}</p>

    <p><b>Year:</b> ${app.student.year}</p>

    <p><b>Scholarship:</b> ${app.scholarship.name}</p>

    <p><b>Amount:</b> ₹${app.scholarship.amount}</p>

    <p><b>Status:</b> ${app.status}</p>

    <p><b>Applied Date:</b> ${app.applied_date}</p>

    <h3>Days Since Applied : ${days}</h3>

    `;

    // Fetch application history
    const historyResponse = await fetch(`${API}/applications/${id}/history`);
    const history = await historyResponse.json();

    let historyHtml = "<h3>Status History</h3><ul>";

    history.forEach(item => {
        historyHtml += `<li>${item.status} - ${item.updated_date}</li>`;
    });

    historyHtml += "</ul>";

    document.getElementById("details").innerHTML += historyHtml;

}

loadDetails();