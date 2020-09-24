function openAddDeadlineForm() {
    closeAnyEventForm();

    let deadlineFormDOM = document.getElementById("deadline-form");

    let formTitleDOM = deadlineFormDOM.getElementsByClassName("form-title")[0];
    formTitleDOM.innerHTML = "Add Deadline!";

    let buttonDOM = deadlineFormDOM.getElementsByClassName("btn")[0];
    buttonDOM.innerHTML = "Add Deadline";

    let formDOM = deadlineFormDOM.getElementsByClassName("form-container")[0];
    formDOM.setAttribute("action", "/add_deadline/");

    document.getElementById("deadline-form").style.display = "block";
}


function openEditDeadlineForm(id, date, endTime, project, title, description) {
  closeAnyEventForm();

  let deadlineFormDOM = document.getElementById("deadline-form");

  let formTitleDOM = deadlineFormDOM.getElementsByClassName("form-title")[0];
  formTitleDOM.innerHTML = "Edit Deadline!";

  let buttonDOM = deadlineFormDOM.getElementsByClassName("btn")[0];
  buttonDOM.innerHTML = "Edit Deadline";

  let formDOM = deadlineFormDOM.getElementsByClassName("form-container")[0];
  formDOM.setAttribute("action", `deadlines/${id}/edit/`);

  let formContainer = deadlineFormDOM.getElementsByClassName("form-container")[0];

  let dateDOM = formContainer.getElementsByClassName("date")[0];
  dateDOM.setAttribute("value", date);

  let endTimeDOM = formContainer.getElementsByClassName("endTime")[0];
  endTimeDOM.setAttribute("value", endTime);

  let projectDOM = formContainer.getElementsByClassName("project")[0];
  projectDOM.setAttribute("value", project);

  let titleDOM = formContainer.getElementsByClassName("title")[0];
  titleDOM.setAttribute("value", title);

  let descriptionDOM = formContainer.getElementsByClassName("description")[0];
  descriptionDOM.setAttribute("value", description);

  document.getElementById("deadline-form").style.display = "block";
}

function closeAnyDeadlineForm() {
  document.getElementById("deadline-form").style.display = "none";
}