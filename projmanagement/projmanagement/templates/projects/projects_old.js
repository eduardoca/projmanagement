

$(document).ready(function () {
    /* Setup */
    /* $.blockUI.defaults.applyPlatformOpacityRules = false; */
    $.ajaxSetup({traditional: true});
    
    /* All jQuery and AJAX go below this comment */
    $('#save_button').click(function () {
        $('#feedback').text("Saving...");
        $('#project_form').load('{% url update_project %}', $('#project_form').serializeArray());
    });
    /* All jQuery and AJAX go above this comment */
});