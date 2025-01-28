function submitForm(formId) {
    var form = document.getElementById(formId);
    var formData = new FormData(form);

    fetch("{% url 'upload_menu' %}", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
        },
    })
    .then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error en la respuesta del servidor: " + response.status);
        }
    })
    .then((data) => {
        console.log("Respuesta del servidor:", data);
        if (data.status === "success") {
            alert("Formulario " + formId + " enviado exitosamente");
        } else {
            alert("Error al enviar el formulario " + formId);
            console.log(data.errors);
        }
    })
    .catch((error) => {
        console.error("Error en el envío:", error);
        alert("Error en el envío del formulario " + formId);
    });
}


