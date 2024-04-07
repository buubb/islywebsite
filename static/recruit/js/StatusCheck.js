// StatusCheck.js

document.getElementById("studentID-box").style.display = "none";

function validatePhoneNumber() {
    var phone_number = document.getElementById("phone_number").value;

    // 전화번호 유효성 검사
    if (/^010\d{8}$/.test(phone_number)) {
        // Admin에 전화번호가 존재하는지 확인
        checkAdminPhoneNumber(phone_number);
    } else {
        document.getElementById("feedback-1").style.display = "block";
    }

    event.preventDefault();
    return false;
}

function checkAdminPhoneNumber(phone_number) {
    fetch(`/recruit/check_phone_number/?phone_number=${phone_number}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error("Network response was not ok.");
        })
        .then(data => {
            if (data.exists) {
                document.getElementById("phoneNumber-box").style.display = "none";
                document.getElementById("studentID-box").style.display = "block";
                document.getElementById("format").style.display = "none";
                document.getElementById("entered-number").innerHTML = phone_number;
            } else {
                alert("Phone Number not found.");
            }
        })
        .catch(error => {
            console.error("There has been a problem with your fetch operation:", error);
        });
}





function validateStudentID() {
    var student_id = document.getElementById("student_id").value;

    // 학번 유효성 검사
    if (/^\d{8}$/.test(student_id)) {
        // Admin에 학번이 존재하는지 확인
        checkAdminStudentID(student_id);
    } else {
        document.getElementById("feedback-2").style.display = "block";
    }

    event.preventDefault();
    return false;
}

function checkAdminStudentID(student_id) {
    var phone_number = document.getElementById("phone_number").value;

    fetch(`/recruit/check_student_id/?student_id=${student_id}&phone_number=${phone_number}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error("Network response was not ok.");
        })
        .then(data => {
            if (data.exists) {
                // 학번과 전화번호에 해당하는 applicant의 합격 여부 확인
                if (data.is_passed) {
                    renderPassPage(student_id, phone_number);
                } else {
                    renderFailPage(student_id, phone_number);
                }
            } else {
                alert("Student ID not found.");
            }
        })
        .catch(error => {
            console.error("There has been a problem with your fetch operation:", error);
        });
}





function renderPassPage(student_id, phone_number) {
    fetch(`/recruit/pass/?student_id=${student_id}&phone_number=${phone_number}`)
        .then(response => response.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => console.error("Error rendering pass page:", error));
}

function renderFailPage(student_id, phone_number) {
    fetch(`/recruit/fail/?student_id=${student_id}&phone_number=${phone_number}`)
        .then(response => response.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => console.error("Error rendering fail page:", error));
}
