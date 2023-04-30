function showOfficeFields() {
    var hasOffice = document.getElementById("has-office").value;
    if (hasOffice === "yes") {
      document.getElementById("office-fields").style.display = "block";
    } else {
      document.getElementById("office-fields").style.display = "none";
    }
  }