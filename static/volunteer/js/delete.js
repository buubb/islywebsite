// delete.js

function confirmDelete() {
    // 경고창을 표시하고 사용자의 응답을 확인
    if (confirm("Are you sure you want to delete?")) {
        // 확인 버튼을 클릭한 경우 포스트를 삭제하기 위해 form을 제출
        document.getElementById("delete").submit();
    }
}