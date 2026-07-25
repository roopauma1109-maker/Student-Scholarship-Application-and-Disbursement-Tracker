const API = "http://127.0.0.1:8000";

let applications = [];

async function loadApplications() {

    const response = await fetch(`${API}/applications`);

    applications = await response.json();

    displayData(applications);
}

function displayData(data){

    const table = document.getElementById("tableBody");

    table.innerHTML = "";

    data.forEach(app=>{

        table.innerHTML += `
        <tr>
            <td>${app.id}</td>
            <td>${app.student_id}</td>
            <td>${app.scholarship_id}</td>
            <td>${app.status}</td>
            <td>${app.applied_date}</td>
        </tr>
        `;

    });

    document.getElementById("count").innerHTML =
        `Showing ${data.length} record(s)`;
}

document.getElementById("search").addEventListener("input", filterData);

document.getElementById("statusFilter").addEventListener("change", filterData);

function filterData(){

    const search =
        document.getElementById("search").value.toLowerCase();

    const status =
        document.getElementById("statusFilter").value;

    const filtered = applications.filter(app=>{

        const matchSearch =
            app.student_id.toString().includes(search);

        const matchStatus =
            status==="" || app.status===status;

        return matchSearch && matchStatus;

    });

    displayData(filtered);
}

loadApplications();