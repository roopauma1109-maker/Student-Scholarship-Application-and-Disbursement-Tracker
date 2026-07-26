const API = "http://127.0.0.1:8000";

const role = document.getElementById("role");

role.addEventListener("change", () => {

    const label = document.getElementById("userLabel");
    const input = document.getElementById("username");

    if(role.value === "student"){
        label.textContent = "Student ID";
        input.placeholder = "Enter Student ID";
    }else{
        label.textContent = "Username";
        input.placeholder = "Enter Username";
    }

});

async function login(){

    const selectedRole = role.value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if(selectedRole === "admin"){

        if(username === "admin" && password === "admin123"){

            localStorage.setItem("adminLoggedIn","true");
            window.location.href = "index.html";

        }else{

            document.getElementById("message").textContent =
            "Invalid Admin Credentials";

        }

    }else{

        const response = await fetch(`${API}/students`);
        const students = await response.json();

        const student = students.find(s => s.id == username);

        if(student){

            localStorage.setItem("student",JSON.stringify(student));
            window.location.href="student-dashboard.html";

        }else{

            document.getElementById("message").textContent =
            "Student not found";

        }

    }

}