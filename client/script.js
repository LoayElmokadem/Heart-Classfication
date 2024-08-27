function check() {
    const inputs = document.querySelectorAll('input, select');
    let isValid = true;

    inputs.forEach(input => {
        if (input.value === "") {
            isValid = false;
            console.log(`Empty input found: ${input.name}`);
        }
    });

    if (isValid) {
        console.log("Form is invalid, showing toast...");
        const toastLiveExample = document.getElementById('liveToast');
        const toast = new bootstrap.Toast(toastLiveExample);
        toast.show();
    } else {
        console.log("Form is valid, proceeding with submission...");
        enter_ML_model();
    }   
}

function enter_ML_model(){
    var age = parseFloat(document.getElementById('age').value);
    var sex = document.getElementById('sex').value;
    var cp = document.getElementById('cp').value;
    var trestbps = parseFloat(document.getElementById('trestbps').value);
    var chol = parseFloat(document.getElementById('chol').value);
    var fbs = document.getElementById('fbs').value;
    var restecg = document.getElementById('restecg').value;
    var thalach = parseFloat(document.getElementById('thalach').value);
    var exang = document.getElementById('exang').value;
    var oldpeak = parseFloat(document.getElementById('oldpeak').value);
    var slope = document.getElementById('slope').value;
    var ca = parseFloat(document.getElementById('ca').value);
    var thal = document.getElementById('thal').value;

    document.getElementById('done').innerHTML = "<p>added to ML model successfully</p>";
    document.getElementById('download').innerHTML = "<button onclick='down_pdf()' class='btn btn-primary mt-3'>Download Your Results As PDF</button>";

    if (prediction == 1) {
        window.location.href = "diseased.html";
    } else {
        window.location.href = "not_diseased.html";
    }
    
}

function down_pdf(){

}