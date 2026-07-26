const student = JSON.parse(localStorage.getItem("student"));

if (!student) {
    window.location.href = "student-login.html";
}

document.getElementById("welcome").innerHTML =
    `Welcome ${student.name}`;

document.getElementById("department").innerHTML =
    `Department : ${student.department}`;

document.getElementById("year").innerHTML =
    `Year : ${student.year}`;

function logout() {

    localStorage.removeItem("student");

    window.location.href = "student-login.html";

}