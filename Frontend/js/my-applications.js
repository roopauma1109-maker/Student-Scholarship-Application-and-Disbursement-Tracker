const API = "http://127.0.0.1:8000";

const student = JSON.parse(localStorage.getItem("student"));

if (!student) {
    window.location.href = "student-login.html";
}

async function loadApplications() {

    try {

        const response = await fetch(
            `${API}/students/${student.id}/applications`
        );

        const applications = await response.json();

        const table = document.getElementById("applicationTable");

        table.innerHTML = "";

        if (applications.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="5">No applications found.</td>
                </tr>
            `;

            return;
        }

        applications.forEach(app => {

            table.innerHTML += `
                <tr>
                    <td>${app.id}</td>
                    <td>${app.scholarship.name}</td>
                    <td>₹${app.scholarship.amount}</td>
                    <td>${app.status}</td>
                    <td>${app.applied_date}</td>
                </tr>
            `;

        });

    }

    catch (error) {

        console.error(error);
        alert("Unable to load applications.");

    }

}

loadApplications();