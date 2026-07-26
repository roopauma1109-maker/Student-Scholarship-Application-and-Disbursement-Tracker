const API = "http://127.0.0.1:8000";

let applications = [];

async function loadApplications() {
    try {

        const response = await fetch(`${API}/applications`);

        if (!response.ok) {
            throw new Error("Failed to fetch data");
        }

        applications = await response.json();

        document.getElementById("total").textContent =
            applications.length;

        document.getElementById("approved").textContent =
            applications.filter(a => a.status === "Approved").length;

        document.getElementById("verified").textContent =
            applications.filter(a => a.status === "Verified").length;

        document.getElementById("submitted").textContent =
            applications.filter(a => a.status === "Submitted").length;

        displayData(applications);

    } catch (error) {

        console.error(error);
        alert("Unable to connect to the backend.");

    }
}

function displayData(data) {

    const table = document.getElementById("tableBody");
    table.innerHTML = "";

    // Empty state
    if (data.length === 0) {

        table.innerHTML = `
        <tr>
            <td colspan="8" style="text-align:center;">
                No applications found
            </td>
        </tr>
        `;

        document.getElementById("count").textContent =
            "Showing 0 record(s)";

        return;
    }

    data.forEach(app => {

        table.innerHTML += `
        <tr>
            <td>${app.id}</td>
            <td>${app.student.name}</td>
            <td>${app.student.department}</td>
            <td>${app.scholarship.name}</td>
            <td>₹${app.scholarship.amount}</td>
            <td>
                <span class="status ${app.status.toLowerCase()}">
                    ${app.status}
                </span>
            </td>
            <td>${app.applied_date}</td>
            <td>
                <button onclick="viewDetails(${app.id})">
                    View
                </button>
            </td>
        </tr>
        `;

    });

    document.getElementById("count").textContent =
        `Showing ${data.length} record(s)`;
}

document.getElementById("search").addEventListener("input", filterData);
document.getElementById("statusFilter").addEventListener("change", filterData);

function filterData() {

    const search = document.getElementById("search").value.toLowerCase();
    const status = document.getElementById("statusFilter").value;

    const filtered = applications.filter(app => {

        const matchSearch =
            app.student.name.toLowerCase().includes(search) ||
            app.student.department.toLowerCase().includes(search) ||
            app.scholarship.name.toLowerCase().includes(search);

        const matchStatus =
            status === "" || app.status === status;

        return matchSearch && matchStatus;

    });

    displayData(filtered);
}

loadApplications();

async function askAssistant() {

    const question =
        document.getElementById("question").value;

    if (question === "") {
        alert("Enter a question");
        return;
    }

    const response = await fetch(`${API}/assistant`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question
        })

    });

    const data = await response.json();

    document.getElementById("answer").innerHTML =
        data.answer;
}

function viewDetails(id) {
    window.location.href = `details.html?id=${id}`;
}