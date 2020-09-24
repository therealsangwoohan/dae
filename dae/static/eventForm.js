function openAddEventForm() {
    closeAnyDeadlineForm();

    let eventFormDOM = document.getElementById("event-form");

    let formTitleDOM = eventFormDOM.getElementsByClassName("form-title")[0];
    formTitleDOM.innerHTML = "Add Event!";

    let buttonDOM = eventFormDOM.getElementsByClassName("btn")[0];
    buttonDOM.innerHTML = "Add Event";

    let formDOM = eventFormDOM.getElementsByClassName("form-container")[0];
    formDOM.setAttribute("action", "/add_event/");

    document.getElementById("event-form").style.display = "block";
}


function openEditEventForm(id, date, startTime, endTime, project, title, description) {
  closeAnyDeadlineForm();

  let eventFormDOM = document.getElementById("event-form");

  let formTitleDOM = eventFormDOM.getElementsByClassName("form-title")[0];
  formTitleDOM.innerHTML = "Edit Event!";

  let buttonDOM = eventFormDOM.getElementsByClassName("btn")[0];
  buttonDOM.innerHTML = "Edit Event";

  let formDOM = eventFormDOM.getElementsByClassName("form-container")[0];
  formDOM.setAttribute("action", `events/${id}/edit/`);

  let formContainer = eventFormDOM.getElementsByClassName("form-container")[0];

  let dateDOM = formContainer.getElementsByClassName("date")[0];
  dateDOM.setAttribute("value", date);

  let startTimeDOM = formContainer.getElementsByClassName("startTime")[0];
  startTimeDOM.setAttribute("value", startTime);

  let endTimeDOM = formContainer.getElementsByClassName("endTime")[0];
  endTimeDOM.setAttribute("value", endTime);

  let projectDOM = formContainer.getElementsByClassName("project")[0];
  projectDOM.setAttribute("value", project);

  let titleDOM = formContainer.getElementsByClassName("title")[0];
  titleDOM.setAttribute("value", title);

  let descriptionDOM = formContainer.getElementsByClassName("description")[0];
  descriptionDOM.setAttribute("value", description);

  document.getElementById("event-form").style.display = "block";
}

function closeAnyEventForm() {
  document.getElementById("event-form").style.display = "none";
}