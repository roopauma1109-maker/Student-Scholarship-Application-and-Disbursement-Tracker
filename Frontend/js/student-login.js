const API = "http://127.0.0.1:8000";

async function loginStudent() {

    const id = document.getElementById("studentId").value;

    if (!id) {
        alert("Enter Student ID");
        return;
    }

    try {

        const response = await fetch(`${API}/students`);

        const students = await response.json();

        const student = students.find(s => s.id == id);

        if (!student) {

            document.getElementById("message").innerHTML =
                "Student not found";

            return;
        }

        localStorage.setItem(
            "student",
            JSON.stringify(student)
        );

        window.location.href = "student-dashboard.html";

    } catch (err) {

        console.log(err);

        alert("Server Error");

    }

}