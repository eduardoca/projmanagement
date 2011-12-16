
$(document).ready(function () {
	
	$('#feedback').ajaxError(function () {
	    $(this).text("Server Error - Save Attempt Failed");
	});
	
	$('#save_button').click(function () {
		// Remove any error messages that may be present from previous attempts
		$('#project_form ul.errorlist').remove();

		// Let the user know that the system is working
		$('#feedback').text('Saving...');

		// Make the attempt to save
		$.post('{% url update_project %}', $('#project_form').serialize(), function (data) {
			if (data[0]) {
				var date = new Date();
				$('#feedback').text('Project saved ' + date.toLocaleString());
			}
			else {
				// Set the feedback string
				$('#feedback').text('Project not saved');
				// Put in the error messages
				$.each(data, function(key, value) {
					// The edit was unsuccessful, put in the error messages.
					var UL = $('#project_form input[name=' + key + ']').closest('td')
					.prepend('<ul class="errorlist"></ul>')
					.find('ul');
					$.each(value, function() {
						UL.append("<li>" + this + "</li>");
					});
				});
			}
		}, "json");
	}); 
});