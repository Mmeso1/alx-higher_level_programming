$(document).ready(function () {
	$("#btn_translate").click(translate);

	// Trigger translation on Enter key press in #language_code input
	$("#language_code").keypress(function (e) {
		if (e.which === 13) {
			translate();
		}
	});

	function translate() {
		const lang = $("#language_code").val();
		$.get(
			"https://hellosalut.stefanbohacek.dev/?lang=" + lang,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	}
});
