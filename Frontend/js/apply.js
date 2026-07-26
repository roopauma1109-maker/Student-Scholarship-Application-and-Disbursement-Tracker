const API = "http://127.0.0.1:8000";

const student = JSON.parse(localStorage.getItem("student"));

if (!student) {
    window.location.href = "student-login.html";
}

document.getElementById("studentName").textContent = student.name;

async function applyScholarship() {

    const scholarshipId = document.getElementById("scholarship").value;

    if (!scholarshipId) {
        alert("Please select a scholarship");
        return;
    }

    const today = new Date().toISOString().split("T")[0];

    const application = {
        student_id: student.id,
        scholarship_id: parseInt(scholarshipId),
        status: "Submitted",
        applied_date: today
    };

    try {

        const response = await fetch(`${API}/applications`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(application)
        });

        const data = await response.json();

        if (!response.ok) {
            console.log(data);
            throw new Error("Application failed");
        }

        document.getElementById("message").textContent =
            "Application submitted successfully!";

    } catch (error) {

        console.error(error);

        document.getElementById("message").textContent =
            "Failed to submit application.";

    }
}