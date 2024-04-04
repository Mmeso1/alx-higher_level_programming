//I am using this url instead cause the one provided is not getting any response and when i pass the provided url value to the browser, the url changes to this instead
$(document).ready(function () {
	$("#btn_translate").click(function () {
		const lang = $("#language_code").val();
		$.get(
			"https://hellosalut.stefanbohacek.dev/?lang=" + lang,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	});
});
